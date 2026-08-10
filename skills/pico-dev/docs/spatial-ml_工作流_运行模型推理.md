一旦你有了一个[准备好的输入张量](workflows-prepare-image-data)，[runModelInference](reference-operators-run-model-inference) 就会在管线内部执行一个端上模型。你把张量绑定到模型的输入和输出节点名称上，管线提交时运行时就会运行该模型。
## 三个必要组成部分
运行一个模型需要：

1. 存放在 [SharedMemory](reference-core-api#sharedmemory) 中的**模型字节数据**——通常从一个 asset 加载。
2. 一个用于选择加速器/格式的**推理类型**（[Pipeline.ModelInferenceType](reference-tensor-types-and-enums#pipeline-modelinferencetype)）。
3. 把模型节点名称映射到张量的**输入与输出编码**（[Pipeline.ModelNodeEncoding](reference-core-api#pipeline-modelnodeencoding)）。

## 加载模型
把 asset 读取到 `SharedMemory` 中。示例使用了一个小型辅助函数，它打开一个 asset、把它映射到内存，再把 `SharedMemory` 交给回调函数：
```text
loadAssetToSharedMemory(appContext, "real_esrgan_x4v3.tflite") { modelMem ->
    runModelInference(
        modelName = "real_esrgan_x4v3",
        modelType = Pipeline.ModelInferenceType.LITE_RT_NPU,
        modelBinary = modelMem,
        inputs  = arrayOf(Pipeline.ModelNodeEncoding("image", affinedFloat)),
        outputs = arrayOf(Pipeline.ModelNodeEncoding("upscaled_image", zoomedResult)),
    )
}
```

供参考的辅助函数（来自示例）：
```kotlin
fun loadAssetToSharedMemory(appContext: Context, assetName: String, loader: (SharedMemory) -> Unit) {
    appContext.assets.open(assetName).use { input ->
        val size = input.available()
        SharedMemory.create("model_$assetName", size).use { mem ->
            val buffer = mem.mapReadWrite()
            Channels.newChannel(input).use { ch -> while (ch.read(buffer) > 0) {} }
            buffer.rewind(); SharedMemory.unmap(buffer)
            loader(mem)
        }
    }
}
```

## 按节点名称绑定输入与输出
每个 [ModelNodeEncoding](reference-core-api#pipeline-modelnodeencoding) 都把一个**模型节点名称**与一个**张量**配对。节点名称必须与模型内部的名称完全一致。
```text
inputs  = arrayOf(Pipeline.ModelNodeEncoding("image", affinedFloat)),
outputs = arrayOf(Pipeline.ModelNodeEncoding("upscaled_image", zoomedResult)),
```


* 输入张量（`affinedFloat`）必须满足模型的输入约定——形状、类型、范围和数据排布（参见[准备图像数据](workflows-prepare-image-data)）。
* 输出张量（`zoomedResult`）必须预先按模型的输出形状和类型分配好。

## 选择推理类型
[Pipeline.ModelInferenceType](reference-tensor-types-and-enums#pipeline-modelinferencetype)用于选择模型的运行方式。在最新的 SDK 中，模型二进制文件始终是 TensorFlow Lite FlatBuffer（`.tflite`）；这个类型只用于选择由哪个加速器来运行它：
| 取值 | 运行位置 |
| --- | --- |
| `LITE_RT_CPU` | 在 CPU 上运行 LiteRT |
| `LITE_RT_GPU` | 在 GPU 上运行 LiteRT |
| `LITE_RT_NPU` | 在 NPU 上运行 LiteRT（示例使用的选项） |
请选择适合你延迟/质量预算的加速器。示例中的 `real_esrgan_x4v3` 是一个运行在 NPU 上的 `.tflite` 模型，所以它使用 `LITE_RT_NPU`。
## 对输出做后处理
模型的输出也只是另一个张量；可以继续在图中处理它。示例把模型 `[0, 1]` 范围的 RGB 输出缩放回 `[0, 255]`，将其转换为无符号字节，然后扩展到 RGBA 显示贴图：
```text
arithmetic(zoomedResult) { zoomedResult * 255.0 }
copy(zoomedResult, zoomedResultU8)
convertColor(Pipeline.ColorConversion.RGB_TO_RGBA, zoomedResultU8, dynamicTexture)
```

常见的后处理算子：分类任务用 [argmax](reference-operators-argmax)，检测框用 [nonMaximumSuppression](reference-operators-non-maximum-suppression)，缩放用 [arithmetic](reference-operators-arithmetic)。
## 约束条件

* 在调用 `runModelInference` **之前**，先把模型字节数据加载进 `SharedMemory`。
* 输入/输出名称必须是模型实际的节点名称。
* 输出张量必须预先按模型的输出约定分配好。
* 模型二进制文件必须是 TensorFlow Lite FlatBuffer（`.tflite`）；`modelType` 用于选择加速器（CPU/GPU/NPU）。

## 延伸阅读

* [runModelInference](reference-operators-run-model-inference)[ 算子卡片](reference-operators-run-model-inference)
* [为模型准备图像数据](workflows-prepare-image-data)
* [驱动场景图输出](workflows-drive-scene-graph-output) / [将数据回读到应用](workflows-read-back-results)——对结果做进一步处理。

