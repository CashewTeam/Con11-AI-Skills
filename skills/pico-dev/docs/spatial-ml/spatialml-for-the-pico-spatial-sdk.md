PICO Spatial SDK · 空间模式运行时
SpatialML 是 PICO Spatial SDK 中受保护的、基于图的机器学习运行时。使用它可以为**空间模式**应用构建由相机和机器学习驱动的体验，同时将透视影像、相机帧、模型输入以及受控回读数据始终保留在受保护的运行时边界内。
[开始上手](getting-started-prerequisites)
[构建第一个场景](getting-started-first-spatialml-scene)
[浏览算子](reference-operator-catalog)
**最快路径：加载管线包**
要发布一项功能，你并不需要自己编写算子。来自 [Pipeline Zoo](https://huggingface.co/picoxr) 的 **管线包**——人脸检测等等——本身就是一个完整的 SpatialML 图，只需一次调用即可加载并提交。可以从 [使用管线包](workflows-use-pipeline-packages) 和 [SuperResolutionApp 演练](samples-super-resolution) 开始；只有在没有合适的包可用时，才需要手动搭建图。
## 什么是 SpatialML？
SpatialML 是面向运行在**空间模式**下的 Kotlin 应用的 PICO Spatial SDK 功能——这类应用通过 `SpatialLaunchActivity` 启动，并由 PICO SpatialEngine 渲染。你以张量（**tensors**）上的算子构成的 **管线（pipeline）**来描述机器学习和计算机视觉任务，将其提交给运行时，然后驱动场景图输出或将结果回读到应用中。
该编程模型围绕四个核心概念展开：[SpatialMLInstance](reference-core-api#spatialmlinstance)、[SpatialMLSession](reference-core-api#spatialmlsession)、[Pipeline](reference-core-api#pipeline)，以及[张量](concepts-tensors-and-shapes)。算子是**`Pipeline` 上的方法**（例如 `pipeline.rectifiedVSTAccess(...)`、`pipeline.runModelInference(...)`、`pipeline.updateSceneGraphProperty(...)`），而不是需要你实例化的独立类。
**聚焦空间模式**
本文档描述的是用 Kotlin Spatial SDK 构建的**空间模式**应用中的 SpatialML。运行时会自动获取透视帧并通过 SpatialEngine 渲染结果；不需要应用自行搭建单独的渲染路径。

* **隐私优先设计**
   在[安全模式（Secure Mode）](concepts-secure-and-readback-modes)下，源自相机的数据始终保留在运行时内部。你的应用只描述要执行的工作并驱动场景，永远不会接收到原始透视帧。
* **基于图的运行时**
   由张量和算子调用构建一个 [Pipeline](reference-core-api#pipeline)，再通过管线依赖（`waitFor`）和条件来控制执行顺序。
* **端侧机器学习**
   在 SpatialML 中运行 TensorFlow Lite（`.tflite`）模型，使用明确的输入/输出张量契约，并通过 [ModelInferenceType](reference-tensor-types-and-enums#pipeline-modelinferencetype)（LiteRT CPU/GPU/NPU）选择加速器。
* **SpatialEngine 输出**
   通过[场景图算子](workflows-drive-scene-graph-output)，直接从图驱动 SpatialEngine 实体：更新材质、变换、文本和可见性。
* **Portal 输出（用于被追踪内容）**
   当相机锚定的内容需要在常规体积边界之外保持可见时，为立体 SpatialML 容器添加一个[传送门（Portal）](concepts-containers-and-portals)。

## 开始构建

* **1. 准备项目**
   添加 Spatial SDK BOM 以及 `securemr`/`readback` 相关制品，设置清单文件标志位，并确认可以部署到 PICO 设备上。
   [前置条件](getting-started-prerequisites)
* **2. 构建第一个场景**
   创建一个最小可用的 SpatialML 图，并确认 实例、会话、管线、张量与输出之间的连接都是正确的。
   [第一个 SpatialML 场景](getting-started-first-spatialml-scene)
* **3. 选择一个工作流**
   添加相机访问、图像预处理、模型推理、回读，或场景图输出。
   [访问 VST 相机图像](workflows-access-camera-vst)
* **4. 查找算子**
   从你希望某个管线阶段完成的任务出发，再深入到具体的算子卡片。
   [算子目录](reference-operator-catalog)
* **捷径——加载一个包**
   跳过编写：加载一个现成的 [Pipeline Zoo](https://huggingface.co/picoxr) 包并提交即可。
   [使用管线包](workflows-use-pipeline-packages)

## 运行时概览

**刚接触 SpatialML？**
先阅读[前置条件](getting-started-prerequisites)，构建[第一个 SpatialML 场景](getting-started-first-spatialml-scene)，再用[运行时模型](concepts-mental-model)来理解 实例、会话、管线、张量和算子之间的配合方式。当你准备好动手写真实代码时，可以跟着 [SuperResolutionApp 演练](samples-super-resolution)一步步来。
## 学习路径

1. [前置条件](getting-started-prerequisites)
2. [第一个 SpatialML 场景](getting-started-first-spatialml-scene)
3. [运行时模型](concepts-mental-model)
4. [空间模式](concepts-spatial-mode)
5. [安全模式与回读模式](concepts-secure-and-readback-modes)
6. [容器与传送门](concepts-containers-and-portals)
7. [张量与形状](concepts-tensors-and-shapes)
8. [执行模型](concepts-execution-model)
9. [算子目录](reference-operator-catalog)

## 文档地图
| 板块 | 用途 | 关键页面 |
| --- | --- | --- |
| 快速上手 | 首次完成设置并搭建好图 | [前置条件](getting-started-prerequisites)、[第一个 SpatialML 场景](getting-started-first-spatialml-scene) |
| Pipeline Zoo | 基于预构建的包发布功能 | [使用管线包](workflows-use-pipeline-packages)、[管线包格式](reference-pipeline-packages) |
| 核心概念 | 运行时模型与设计规则 | [运行时模型](concepts-mental-model)、[空间模式](concepts-spatial-mode)、[安全模式与回读模式](concepts-secure-and-readback-modes)、[容器与传送门](concepts-containers-and-portals)、[执行模型](concepts-execution-model) |
| 工作流 | 面向任务的实现指南 | [访问 VST 相机图像](workflows-access-camera-vst)、[运行模型推理](workflows-run-model-inference)、[将数据回读到应用](workflows-read-back-results)、[驱动场景图输出](workflows-drive-scene-graph-output) |
| 示例 | 仓库示例展示的内容 | [SuperResolutionApp](samples-super-resolution) |
| 算子与参考 | API 与算子查询 | [算子目录](reference-operator-catalog)、[核心 API](reference-core-api)、[张量类型与枚举](reference-tensor-types-and-enums) |
| 疑难排查 | 故障特征与具体排查方法 | [疑难排查](troubleshooting) |
## 范围
本文档聚焦于 SpatialML 作为 PICO Spatial SDK 中**空间模式**功能的这一部分，以及让 SpatialML 在设备上可靠运行所需的最基本设置。文档会链接到更完整的 [PICO Spatial SDK 文档](https://developer.picoxr.com/document/spatial-sdk/)，而不是取代它。

