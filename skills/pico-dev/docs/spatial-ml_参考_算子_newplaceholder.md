创建一个 [PipelineTensorPlaceholder](zh-reference-core-api#pipelinetensor-%E4%B8%8E-pipelinetensorplaceholder)——[GlobalTensor](zh-reference-core-api#tensor-%E4%B8%8E-globaltensor) 的占位符，会在[提交（submit）时](zh-concepts-execution-model#%E5%8D%A0%E4%BD%8D%E7%AC%A6%E4%B8%8E%E7%BB%91%E5%AE%9A)绑定到具体的张量。占位符使同一条管线能够在不同的运行中操作不同的全局张量。
## 签名
```text
Pipeline.newPlaceholder(config: Tensor.InitInfo): PipelineTensorPlaceholder
```

## 参数
| 参数 | 说明 |
| --- | --- |
| `config` | 描述该占位符所代表张量的 [init-info](zh-reference-tensor-types-and-enums#%E5%BC%A0%E9%87%8F%E5%88%9D%E5%A7%8B%E5%8C%96%E4%BF%A1%E6%81%AF-init-info)（初始化信息）。 |
## 示例
```kotlin
val placeholderMap = mutableMapOf<PipelineTensorPlaceholder, GlobalTensor>()

val input = newPlaceholder(
    MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(512, 512), channel = 3)
)
placeholderMap[input] = someGlobalTensor

// bind at submit
submit(placeholderMap, null, null)
```

## 空间模式说明

* 通过传给 [submit](zh-reference-operators-submit) 的 `parameters` 映射来绑定占位符；在多次提交之间更新该映射即可重新绑定。
* 当计算图需要接受外部传入的全局张量时使用占位符；纯内部使用的值请使用 [newLocalTensor](zh-reference-operators-new-local-tensor)。

## 相关算子

* [newPlaceholderLike](zh-reference-operators-new-placeholder-like) —— 匹配现有张量配置的占位符。
* [submit](zh-reference-operators-submit) —— 将占位符绑定到全局张量。
* [执行模型](zh-concepts-execution-model#%E5%8D%A0%E4%BD%8D%E7%AC%A6%E4%B8%8E%E7%BB%91%E5%AE%9A)

