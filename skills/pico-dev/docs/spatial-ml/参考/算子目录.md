在 Kotlin SDK 中，**算子是** [Pipeline](reference-core-api#pipeline) **上的一个方法**。你不需要实例化算子对象——只需调用 `pipeline.rectifiedVSTAccess(...)`、`pipeline.runModelInference(...)` 等方法，每次调用都会向图中添加一个阶段。当你知道想让某个阶段完成什么工作、但不确定方法名时，可以使用本目录查找。每个算子都链接到一张事实卡片，包含其签名、参数、输出、示例、约束条件以及相关页面。
**先查目录**
各个算子卡片被有意排除在侧边栏之外，以便导航始终聚焦于任务。请从这里开始，再逐步深入。
**不需要自己编写图？**
如果某个 [Pipeline Zoo](https://huggingface.co/picoxr) 包已经覆盖了你的使用场景，你可以[直接加载并提交它](workflows-use-pipeline-packages)，无需编写任何算子代码。只有在你要自行构建或扩展图时，才需要查阅本目录。
## 按任务选择
| 如果你想…… | 从这里开始 | 常见的后续步骤 |
| --- | --- | --- |
| 将实时相机 / 深度数据拉取到图中 | [rectifiedVSTAccess](reference-operators-rectified-vst-access)、[getDepthMap](reference-operators-get-depth-map) | [getAffine](reference-operators-get-affine)、[applyAffine](reference-operators-apply-affine)、[runModelInference](reference-operators-run-model-inference) |
| 裁剪、缩放、归一化或重塑图像张量 | [getAffine](reference-operators-get-affine)、[applyAffine](reference-operators-apply-affine)、[normalize](reference-operators-normalize) | [convertColor](reference-operators-convert-color)、[switchCHWAndHWC](reference-operators-switch-chw-and-hwc)、[copy](reference-operators-copy) |
| 运行一个 ML 模型 | [runModelInference](reference-operators-run-model-inference) | [argmax](reference-operators-argmax)、[nonMaximumSuppression](reference-operators-non-maximum-suppression)、[arithmetic](reference-operators-arithmetic) |
| 把 2D 检测结果转换为 3D 放置信息 | [uvTo3DInCameraSpace](reference-operators-uv-to-3d-in-camera-space) | [solvePnP](reference-operators-solve-pnp)、[makeTransform](reference-operators-make-transform) |
| 在 Spatial 场景中展示结果 | [updateSceneGraphProperty](reference-operators-update-scene-graph-property)、[switchSceneVisibility](reference-operators-switch-scene-visibility) | [newSceneFromGLTF](reference-operators-new-scene-from-gltf)、文本相关算子 |
| 在图中采集或播放音频 | [captureMicrophone](reference-operators-capture-microphone)、[outputSounds](reference-operators-output-sounds) | 音频预处理、模型管线 |
| 比较、归约、排序或组合张量 | [arithmetic](reference-operators-arithmetic)、比较类算子、[bytewiseAll](reference-operators-bytewise-all)、[bytewiseAny](reference-operators-bytewise-any) | [elementwiseMin](reference-operators-elementwise-min)、[elementwiseMax](reference-operators-elementwise-max)、[sortVec](reference-operators-sort-vec) |
| 运行脚本定义的图逻辑 | [runJavaScript](reference-operators-run-java-script) | [into](reference-operators-run-java-script)[ / ](reference-operators-run-java-script)[outFrom](reference-operators-run-java-script)[ 辅助函数](reference-operators-run-java-script) |
| 执行图 | [submit](reference-operators-submit) | [执行模型](concepts-execution-model) |
## 管线位置图

## 传感器与相机访问
| 算子 | 使用场景 |
| --- | --- |
| [rectifiedVSTAccess](reference-operators-rectified-vst-access) | 管线需要经过校正的 VST 图像、时间戳或相机矩阵。 |
| [getDepthMap](reference-operators-get-depth-map) | 管线需要深度图，用于深度感知的放置或过滤。 |
| [captureMicrophone](reference-operators-capture-microphone) | 管线需要麦克风 PCM 数据。 |
| [uvTo3DInCameraSpace](reference-operators-uv-to-3d-in-camera-space) | 需要把 UV/图像坐标转换为相机空间中的 3D 点。 |
## 模型推理
| 算子 | 使用场景 |
| --- | --- |
| [runModelInference](reference-operators-run-model-inference) | 图需要执行一个端上模型。 |
## 张量创建与搬移
| 算子 | 使用场景 |
| --- | --- |
| [newLocalTensor](reference-operators-new-local-tensor) | 你需要在管线内部创建一个中间张量。 |
| [newPlaceholder](reference-operators-new-placeholder) | 图需要接收一个在提交时绑定的全局张量。 |
| [newPlaceholderLike](reference-operators-new-placeholder-like) | 你需要一个与现有张量配置相匹配的占位符。 |
| [copy](reference-operators-copy) | 在张量之间搬移/转换数据（包括类型转换）。 |
| [get](reference-operators-get) | 提取张量的一个切片/区域。 |
| [switchCHWAndHWC](reference-operators-switch-chw-and-hwc) | 在图像风格的 HWC 布局与模型风格的 CHW 布局之间切换。 |
## 算术与数学运算
| 算子 | 使用场景 |
| --- | --- |
| [arithmetic](reference-operators-arithmetic) | 闭包风格的标量/张量组合运算（例如 `{ t / 255.0 }`）。 |
| [elementwiseMultiply](reference-operators-elementwise-multiply) | 逐元素相乘。 |
| [elementwiseMax](reference-operators-elementwise-max) | 逐元素取最大值。 |
| [elementwiseMin](reference-operators-elementwise-min) | 逐元素取最小值。 |
| [inversion](reference-operators-inversion) | 矩阵求逆。 |
| [norm](reference-operators-norm) | 向量/矩阵范数。 |
| [normalize](reference-operators-normalize) | 与模型兼容的归一化处理。 |
| [argmax](reference-operators-argmax) | 最大值所在的索引。 |
| [sortVec](reference-operators-sort-vec) | 对向量排序。 |
| [sortMatrix](reference-operators-sort-matrix) | 对矩阵排序。 |
| [singularValueDecomposition](reference-operators-singular-value-decomposition) | 矩阵的奇异值分解（SVD）。 |
## 比较与逻辑运算
| 算子 | 使用场景 |
| --- | --- |
| [equal](reference-operators-equal) / [notEqual](reference-operators-not-equal) | 逐元素判断相等/不相等。 |
| [largerThan](reference-operators-larger-than) / [largerEqual](reference-operators-larger-equal) | 逐元素的大于类比较。 |
| [smallerThan](reference-operators-smaller-than) / [smallerEqual](reference-operators-smaller-equal) | 逐元素的小于类比较。 |
| [bitwiseAnd](reference-operators-bitwise-and) / [bitwiseOr](reference-operators-bitwise-or) | 张量间的按位逻辑运算。 |
| [bytewiseAll](reference-operators-bytewise-all) / [bytewiseAny](reference-operators-bytewise-any) | 归约运算：判断是否所有/任一字节满足某条件。 |
## 几何与视觉数学运算
| 算子 | 使用场景 |
| --- | --- |
| [getAffine](reference-operators-get-affine) | 根据点对应关系计算一个 2×3 仿射矩阵。 |
| [applyAffine](reference-operators-apply-affine) | 通过仿射矩阵对图像做重采样。 |
| [applyAffinePoint](reference-operators-apply-affine-point) | 变换点坐标（而非像素）。 |
| [makeTransform](reference-operators-make-transform) | 由各分量构建一个变换矩阵。 |
| [solvePnP](reference-operators-solve-pnp) | 根据 2D/3D 对应关系估计位姿。 |
| [convertColor](reference-operators-convert-color) | 转换图像的色彩排布/通道数。 |
| [nonMaximumSuppression](reference-operators-non-maximum-suppression) | 抑制重叠的检测框。 |
## 场景图输出（Spatial）
| 算子 | 使用场景 |
| --- | --- |
| [newSceneFromGLTF](reference-operators-new-scene-from-gltf) | 将 glTF 场景作为张量加载到图中。 |
| [updateSceneGraphProperty](reference-operators-update-scene-graph-property) | 更新实体属性（变换、材质、贴图）。 |
| [switchSceneVisibility](reference-operators-switch-scene-visibility) | 显示或隐藏一个场景/实体。 |
| [updateSceneGraphTextContent](reference-operators-update-scene-graph-text-content) | 设置文本实体的字符串内容。 |
| [updateSceneGraphTextHorizontalAlignment](reference-operators-update-scene-graph-text-horizontal-alignment) | 设置文本水平对齐方式。 |
| [updateSceneGraphTextVerticalAlignment](reference-operators-update-scene-graph-text-vertical-alignment) | 设置文本垂直对齐方式。 |
## 音频输出
| 算子 | 使用场景 |
| --- | --- |
| [outputSounds](reference-operators-output-sounds) | 播放图中生成/处理过的 PCM 音频。 |
## 脚本
| 算子 | 使用场景 |
| --- | --- |
| [runJavaScript](reference-operators-run-java-script) | 用脚本表达图侧逻辑会更清晰；配合使用 `into`/`outFrom` I/O 辅助函数。 |
## 管线执行
| 算子 | 使用场景 |
| --- | --- |
| [submit](reference-operators-submit) | 将图排入队列执行一次。 |
## 延伸阅读

* [核心 API](reference-core-api)
* [张量类型与枚举](reference-tensor-types-and-enums)
* [运行时模型](concepts-mental-model)
* [运行模型推理](workflows-run-model-inference)

