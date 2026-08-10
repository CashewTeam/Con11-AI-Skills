**管线包**是一个应用资源目录，以 JSON 加二进制文件的形式描述一个完整的 SpatialML 功能——包括它的管线、张量、模型以及任何 glTF 场景。[loadPipelinePackageFromAssets](zh-reference-core-api#spatialmlsession) 会解析该目录、构建管线、实体化共享张量，并返回一个可供提交的 [PipelinePackageBundle](zh-reference-core-api#pipelinepackagebundle)。本页介绍的是磁盘上的 schema；关于加载并提交的流程，请参阅[使用管线包](zh-workflows-use-pipeline-packages)。
**通常无需手写这些文件**
预置的包来自 [Pipeline Zoo](https://huggingface.co/picoxr)。本参考页面适用于理解你已加载的包、改造某个包，或自行构建一个包。
## 目录结构
所有路径都相对于你传给加载器的 `assetRoot`。一个典型的包看起来就像示例中附带的 `face-mediapipe-pipeline` 包：
```text
face-mediapipe-pipeline/
├── manifest.json                     # entry point — always at assetRoot
├── model/
│   ├── model.json                    # model metadata
│   └── face_detector.tflite          # TensorFlow Lite model binary
├── pipeline/
│   ├── face_detection_pipeline.json  # one pipeline per file
│   └── face_display_pipeline.json
└── gltf/
    └── frame.gltf                     # scenes referenced by tensors
```

**路径会被校验**
JSON 内部的每个路径都按**相对于包的路径**来解析。开头的斜杠和 `..` 路径段都会被拒绝——一个包只能引用位于自己 `assetRoot` 内部的文件。
## manifest.json
manifest 是加载器唯一按文件名查找的文件。它列出了各个管线、（可选的）共享模型，以及该包支持的运行时模式。
```json
{
  "format_version": 1,
  "pipelines": [
    { "id": "detection", "path": "pipeline/face_detection_pipeline.json" },
    { "id": "display",   "path": "pipeline/face_display_pipeline.json" }
  ],
  "model": {
    "bin_path": "model/face_detector.tflite",
    "json_path": "model/model.json"
  },
  "runtime": {
    "supported_modes": ["spatial"]
  }
}
```

| 键 | 是否必填 | 含义 |
| --- | --- | --- |
| `format_version` | 是 | 包格式版本，必须为 `1`。对应 [PipelinePackageManifest.formatVersion](zh-reference-core-api#pipelinepackagemanifest)。 |
| `pipelines` | 是 | 非空的 `{ "id", "path" }` 数组。id 必须唯一；加载器会**按数组顺序**构建它们，并以 `id` 为键存入 `bundle.pipelines`。 |
| `model` | 否 | 该包推理算子所使用的共享模型——参见[模型块](#%E6%A8%A1%E5%9E%8B%E5%9D%97)。 |
| `runtime` | 是 | 运行时元数据——参见[运行时与模式](#%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B8%8E%E6%A8%A1%E5%BC%8F)。 |
**被忽略的键**
如果存在顶层的 `id` 和 `schema_version`，加载器会忽略它们；它们只是编写时的元数据。只有上面列出的键会影响加载过程。
### 运行时与模式
```text
"runtime": {
  "supported_modes": ["spatial"],
  "detection_tensor": "post_det"
}
```

| 键 | 是否必填 | 含义 |
| --- | --- | --- |
| `supported_modes` | 是 | 模式字符串数组。每一项必须是 `"xr"` 或 `"spatial"`。**必须包含** **`"spatial"`**，否则加载器会以 `supported_modes must include spatial` 拒绝该包。 |
| `detection_tensor` | 否 | 承载该包检测输出结果的张量名称。对应 [bundle.detectionTensor](zh-reference-core-api#pipelinepackagebundle) 与 `manifest.detectionTensor`。 |
本文档只覆盖 [空间模式](zh-concepts-spatial-mode)。一个包也可以同时声明支持 `"xr"`，但这里使用的加载器要求必须包含 `"spatial"`；仅支持 XR 的包无法在空间模式应用中加载。
### 模型块
```text
"model": {
  "bin_path": "model/face_detector.tflite",
  "json_path": "model/model.json"
}
```

| 键 | 是否必填 | 含义 |
| --- | --- | --- |
| `bin_path` | 是 | TensorFlow Lite（`.tflite`）FlatBuffer 文件的路径。 |
| `json_path` | 否 | 模型元数据 JSON 的路径——参见 [model.json](#model-json)。 |
| `extra_json_path` | 否 | 如果模型还需要额外的元数据 JSON，则填写其路径。 |
## Pipeline JSON
`manifest.pipelines` 中的每一项都指向一个 Pipeline JSON 文件。它声明了该管线的张量、按顺序排列的算子，以及哪些张量名称是它的输入和输出。
```json
{
  "metadata": { "version": 1 },
  "tensors": {
    "model_input": { "dimensions": [256, 256], "channels": 3, "data_type": 6, "usage": 6 },
    "vst_left_image": { "dimensions": [326, 580], "channels": 3, "data_type": 1, "is_placeholder": true, "usage": 6 }
  },
  "operators": [
    { "type": "XR_SECURE_MR_OPERATOR_TYPE_RECTIFIED_VST_ACCESS_PICO",
      "inputs": [], "outputs": ["vst_right_image", "vst_left_image", "vst_timestamp", "vst_camera_matrix"] }
  ],
  "inputs": ["post_det"],
  "outputs": ["frame_pose", "frame_gltf"]
}
```

| 键 | 是否必填 | 含义 |
| --- | --- | --- |
| `metadata.version` | 是 | 管线 schema 版本，必须为 `1`。 |
| `tensors` | 是 | 张量名称 → [张量描述符](#%E5%BC%A0%E9%87%8F%E6%8F%8F%E8%BF%B0%E7%AC%A6)的映射。 |
| `operators` | 是 | 按顺序排列的[算子条目](#%E7%AE%97%E5%AD%90%E6%9D%A1%E7%9B%AE)数组，顺序即执行顺序。 |
| `inputs` | 是 | 该管线从外部消费的张量名称（在提交时绑定的占位符）。 |
| `outputs` | 是 | 该管线为其他管线或应用产生的张量名称。 |
`inputs`/`outputs` 中命名的占位符张量会成为该管线的 [submitBindings](zh-reference-core-api#pipelinepackagepipeline)：加载器会实体化一个与之匹配的[全局张量](zh-concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F)（该包各管线间共享，以键的形式存放在 `bundle.globalTensors` 中），并将其绑定到该占位符。
### 张量描述符
`tensors` 下的每个值都描述一个张量。大多数字段与 Kotlin 的 [初始化信息（init-info）](zh-reference-tensor-types-and-enums#%E5%BC%A0%E9%87%8F%E5%88%9D%E5%A7%8B%E5%8C%96%E4%BF%A1%E6%81%AF-init-info)一一对应。
| 字段 | 默认值 | 含义 |
| --- | --- | --- |
| `tensor_type` | `mat` | 形状族：`mat`（默认的矩阵/图像形式）、`point2`/`point3`（及其 `_array` 形式）、`scalar`、`timestamp`、`color`、`gltf`。 |
| `dimensions` | —— | `mat` 张量的形状，例如 `[256, 256]`。 |
| `channels` | `1` | `mat` 张量的通道数（RGB 为 `3`）。 |
| `data_type` | —— | 元素类型，可用整数或字符串表示——参见[数据类型代码](#%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%E4%BB%A3%E7%A0%81)。 |
| `usage` | `6`（MAT） | 张量用途——参见[用途代码](#%E7%94%A8%E9%80%94%E4%BB%A3%E7%A0%81)。 |
| `is_placeholder` | `false` | 对于在提交时绑定的张量（即包的输入/输出）应设为 `true`。 |
| `value` | —— | 常量初始化数组，用固定数据填充一个非占位符张量。 |
| `asset` | —— | 对于 `gltf` 张量，指要加载的 glTF/GLB 相对于包的路径。 |
| `size` | —— | point/color **array** 类型张量的元素个数。 |
**flag 会被忽略**
某些编写工具生成的 Pipeline JSON 会在每个张量上附带一个数字类型的 `flag`。Kotlin 加载器会**忽略**它，所需的全部信息都从 `data_type`、`usage`、`channels` 和 `tensor_type` 中推导得出。
#### 数据类型代码
`data_type` 可以接受一个整数代码，或等价的字符串（`uint8`、`int32`、`float32` 等）：
| 代码 | 类型 |
| --- | --- |
| `1` | `UINT8` |
| `2` | `INT8` |
| `3` | `UINT16` |
| `4` | `INT16` |
| `5` | `INT32` |
| `6` | `FLOAT32` |
| `7` | `FLOAT64` |
#### 用途代码
`usage` 用来告诉运行时该如何解释这个张量：
| 代码 | 用途 |
| --- | --- |
| `1` | 点（Point） |
| `2` | 标量（Scalar） |
| `4` | 颜色（RGBA） |
| `5` | 时间戳（Timestamp） |
| `6` | 矩阵/图像（`MAT`，默认值） |
| `7` | 场景图/glTF |
### 算子条目
每个算子条目都会指明自己的类型，并按名称连接张量。`inputs`/`outputs` 有两种写法，加载器两者都接受：

* **位置式（Positional）**——张量名称数组，与算子的参数顺序一一对应：
   ```json
   { "type": "XR_SECURE_MR_OPERATOR_TYPE_APPLY_AFFINE_PICO",
     "inputs": ["full_affine", "vst_left_image"], "outputs": ["warped_bgr"] }
   ```

* **命名式（Named）**——`{ "name", "tensor" }` 数组，用于某个阶段需要按节点名绑定的场景（例如[模型推理](zh-reference-operators-run-model-inference)的节点名，或 [JavaScript](zh-reference-operators-run-java-script) 变量名）：
   ```json
   { "type": "XR_SECURE_MR_OPERATOR_TYPE_RUN_MODEL_INFERENCE_PICO",
     "inputs":  [{ "name": "image", "tensor": "model_input" }],
     "outputs": [{ "name": "box_coords_1", "tensor": "box_coords_1" }],
     "model_name": "main", "model_type": "litert", "model_target": "npu" }
   ```


部分算子还会内联携带额外字段：[arithmeticCompose](zh-reference-operators-arithmetic) 用 `expression`，[runJavaScript](zh-reference-operators-run-java-script) 用 `script`，颜色转换方向等阶段变体用 `flag`，推理阶段则使用一组 `model_*` 字段（参见[模型选择](#%E6%A8%A1%E5%9E%8B%E9%80%89%E6%8B%A9)）。
#### 算子类型名称
`type` **既**可以接受完整的 XR 枚举名，**也**可以接受简短的别名。下面两种写法加载的是同一个阶段：
```json
{ "type": "XR_SECURE_MR_OPERATOR_TYPE_RECTIFIED_VST_ACCESS_PICO", ... }
{ "type": "camera_access", ... }
```

常见的别名包括 `camera_access`、`run_algorithm`（推理）、`nms` 和 `uv_to_3d`。这套别名映射到的是[算子目录](zh-reference-operator-catalog)中记录的同一批算子。
**部分算子在空间模式下是空操作**
为 XR 模式编写的包，可能会引用一些只在 XR 场景下才有意义的算子——例如 `load_texture`、`draw_text`、`render_gltf`、`update_gltf`、`scenegraph_visibility`、麦克风相关阶段等。在空间模式应用中，这些算子可以正常加载但不会产生任何效果；请改由你的应用来驱动场景（参见[驱动场景图输出](zh-workflows-drive-scene-graph-output)）。
## model.json
`model.json_path` 指向的模型元数据 JSON。face 包中的这个文件看起来像这样：
```json
{
  "model_name": "main",
  "engine_type": "litert",
  "model_target": "npu",
  "input":  [{ "name": "image", "shape": [1, 256, 256, 3], "encoding_type": "FP32" }],
  "output": [{ "name": "box_coords_1", "shape": [1, 512, 16], "encoding_type": "FP32" }]
}
```

加载器只从这个文件中读取 **`model_name`**（默认值为 `"main"`）；推理算子会用这个名称来引用模型。`input`/`output`/`encoding_type`/`path_to_zoo` 字段只是构建该包的工具留下的编写元数据，加载时并不会被使用——真正的输入/输出绑定来自[算子命名式的 ](#%E7%AE%97%E5%AD%90%E6%9D%A1%E7%9B%AE)[inputs](#%E7%AE%97%E5%AD%90%E6%9D%A1%E7%9B%AE)[/](#%E7%AE%97%E5%AD%90%E6%9D%A1%E7%9B%AE)[outputs](#%E7%AE%97%E5%AD%90%E6%9D%A1%E7%9B%AE)。
### 模型选择
Pipeline JSON 中的推理阶段决定了引擎和加速器的选择：
| 字段 | 可接受的值 | 结果 |
| --- | --- | --- |
| `model_type` | `litert`、`lite_rt`、`tflite`、`tensorflow_lite` 等 | LiteRT（TensorFlow Lite）。 |
| `model_target` | `gpu` | [LITE_RT_GPU](zh-reference-tensor-types-and-enums#pipeline-modelinferencetype) |
| `model_target` | `npu` | `LITE_RT_NPU` |
| `model_target` | 其他任意值/未填写 | `LITE_RT_CPU` |
## 外部全局张量与绑定顺序
加载时，你可以传入 `externalGlobals` 来提供那些包原本会自行创建的张量。对于包所需要的每一个占位符张量，加载器会按以下顺序解析：

1. **`externalGlobals[name]`**——由你的应用提供的全局张量。它的配置必须与包内张量的配置完全一致，否则加载器会抛出异常。
2. **已存在的共享全局张量**——已经以同名方式为该包实体化（配置必须匹配）。
3. **新建的全局张量**——根据张量描述符创建。`gltf` 张量会通过其 `asset` 字段使用 [newSceneFromGLTF](zh-reference-operators-new-scene-from-gltf) 加载；其他类型则是普通的 [newGlobalTensor](zh-reference-core-api#spatialmlsession)。

只有出现在某个管线的 `inputs`/`outputs`（或 manifest 的 `detection_tensor`）中的占位符张量才会被实体化并绑定。传递方式请参见[工作流](zh-workflows-use-pipeline-packages#4-%E9%9C%80%E8%A6%81%E6%97%B6%E4%BC%A0%E5%85%A5%E5%A4%96%E9%83%A8%E5%BC%A0%E9%87%8F)页面。
## 延伸阅读

* [使用管线包](zh-workflows-use-pipeline-packages)——在运行时加载并提交。
* [FaceDetection 示例](zh-samples-face-detection)——端到端走一遍某个包的完整流程。
* [核心 API](zh-reference-core-api#%E7%AE%A1%E7%BA%BF%E5%8C%85%E7%B1%BB%E5%9E%8B)——你会用到的 `PipelinePackage*` 类型。
* [算子目录](zh-reference-operator-catalog)——构成一个包各条管线的那些算子。

