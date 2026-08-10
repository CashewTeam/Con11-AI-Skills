通过将张量绑定到模型的输入和输出节点名称，在管线内运行一个端侧模型。该模型会在管线被[提交](zh-reference-operators-submit)时执行。
## 签名
```kotlin
Pipeline.runModelInference(
    modelName: String,
    modelType: Pipeline.ModelInferenceType,
    modelBinary: SharedMemory,
    inputs: Array<Pipeline.ModelNodeEncoding>,
    outputs: Array<Pipeline.ModelNodeEncoding>,
)

// each binding pairs a model node name with a tensor
Pipeline.ModelNodeEncoding(val nodeName: String, val tensor: Tensor)
```

## 参数
| 参数 | 说明 |
| --- | --- |
| `modelName` | 由你为模型选择的标识符。 |
| `modelType` | 后端/格式——参见 [ModelInferenceType](zh-reference-tensor-types-and-enums#pipeline-modelinferencetype)。 |
| `modelBinary` | 已加载到 [SharedMemory](zh-reference-core-api#sharedmemory) 中的模型字节数据。 |
| `inputs` | 每个模型输入节点名称对应一个 `ModelNodeEncoding` → 输入张量。 |
| `outputs` | 每个模型输出节点名称对应一个 `ModelNodeEncoding` → 预先分配好的输出张量。 |
## 示例
来自 SuperResolutionApp：
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

## 空间模式说明

* 在调用此算子**之前**，需先将模型字节数据加载到 `SharedMemory` 中。
* `nodeName` 的取值必须与模型实际的输入/输出节点名称一致。
* 输出张量必须预先按模型的输出形状和类型完成分配。
* 输入张量必须满足模型的约定——形状、类型、取值范围和布局（参见[准备图像数据](zh-workflows-prepare-image-data)）。
* 模型二进制文件必须是 TensorFlow Lite FlatBuffer（`.tflite`）；`modelType` 用于选择加速器（示例运行在 NPU 上，因此使用 `LITE_RT_NPU`）。

## 相关算子

* [arithmetic](zh-reference-operators-arithmetic) —— 前/后处理缩放。
* [argmax](zh-reference-operators-argmax) / [nonMaximumSuppression](zh-reference-operators-non-maximum-suppression) —— 对输出做后处理。
* [运行模型推理](zh-workflows-run-model-inference)

