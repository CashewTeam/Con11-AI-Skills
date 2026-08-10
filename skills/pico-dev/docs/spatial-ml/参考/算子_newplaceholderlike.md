创建一个 [PipelineTensorPlaceholder](zh-reference-core-api#pipelinetensor-%E4%B8%8E-pipelinetensorplaceholder)，其配置与某个已有张量一致，从而保证绑定目标具有兼容的形状和类型。
## 签名
```text
Pipeline.newPlaceholderLike(tensor: Tensor): PipelineTensorPlaceholder
```

## 参数
| 参数 | 描述 |
| --- | --- |
| `tensor` | 新占位符应复制其配置的已有张量。 |
## 空间模式说明

* 当已经有一个配置合适的张量，并希望占位符与其完全匹配时，比使用 [newPlaceholder](zh-reference-operators-new-placeholder) 更为便捷。
* 所绑定的 [GlobalTensor](zh-reference-core-api#tensor-%E4%B8%8E-globaltensor) 必须与所复制的配置兼容。

## 相关算子

* [newPlaceholder](zh-reference-operators-new-placeholder) — 通过初始化信息创建占位符。
* [submit](zh-reference-operators-submit) — 将占位符绑定到全局张量。
* [执行模型](zh-concepts-execution-model#%E5%8D%A0%E4%BD%8D%E7%AC%A6%E4%B8%8E%E7%BB%91%E5%AE%9A)

