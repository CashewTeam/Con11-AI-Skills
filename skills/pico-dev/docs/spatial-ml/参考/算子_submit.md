将管线的一次执行加入队列。所有算子调用只是在*描述*计算图；真正运行它的是 `submit`。它会将全局张量绑定到计算图的占位符上，可选地根据条件门控执行，并可以在前一次运行之后串联执行。
## 签名
```text
Pipeline.submit(
    parameters: Map<PipelineTensorPlaceholder, GlobalTensor>,
    condition: GlobalTensor?,
    waitFor: Pipeline.RunTask?,
): Pipeline.RunTask
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `parameters` | 输入 | 将每个 [newPlaceholder](zh-reference-operators-new-placeholder) 绑定到本次运行所使用的具体全局张量。 |
| `condition` | 输入 | 可选的门控条件——仅当该张量非零时才会执行（通常来自 [bytewiseAny](zh-reference-operators-bytewise-any)/[bytewiseAll](zh-reference-operators-bytewise-all)）。传入 `null` 表示始终执行。 |
| `waitFor` | 输入 | 可选的前一个 `RunTask`；本次运行会在它完成后才开始，用于强制管线之间的执行顺序。 |
| 返回值 | 结果 | 一个 `RunTask` 句柄，可用于 `waitFor` 或等待完成。 |
## 示例
来自 SuperResolutionApp 初始化管线——没有占位符、没有条件、没有依赖：
```text
submit(mapOf(), null, null)
```

将一个管线串联在另一个之后（来自异步执行器模式），把前一次运行作为 `waitFor` 传入：
```kotlin
val task = pipeline.submit(tensorMap, null, previousTask)
```

## 空间模式说明

* 只有**全局**张量才能作为 `parameters` 绑定——局部张量的生命周期仅限于单次运行内。
* 使用 `waitFor` 来约束存在依赖关系的管线的执行顺序（例如，在消费其矩阵结果的主管线之前先运行仿射更新管线）。参见 [异步管线模式](zh-workflows-async-pipeline-patterns)。
* 逐帧计算图会重复提交（示例中主管线以约 10 Hz 的频率驱动）；应只构建一次计算图，然后反复 re-submit，而不是每帧都重新构建。
* `condition` 张量可以在不重建计算图的情况下实现数据驱动的执行控制。

## 相关算子

* [newPlaceholder](zh-reference-operators-new-placeholder) —— 声明 `parameters` 所绑定的内容。
* [bytewiseAny](zh-reference-operators-bytewise-any) / [bytewiseAll](zh-reference-operators-bytewise-all) —— 用于生成 `condition`。
* [执行模型](zh-concepts-execution-model)

