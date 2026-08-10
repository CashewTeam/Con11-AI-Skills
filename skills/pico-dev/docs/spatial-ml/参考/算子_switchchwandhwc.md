在图像张量的 HWC（高-宽-通道，图像风格）布局与 CHW（通道-高-宽，模型风格）布局之间重新排列。
## 签名
```text
Pipeline.switchCHWAndHWC(source: Tensor, result: Tensor)
```

## 参数 / 结果
| 参数 | 说明 |
| --- | --- |
| `source` | 源图像张量，为其中一种布局。 |
| `result` | 结果张量，为另一种布局。 |
## 空间模式说明

* 许多模型期望输入为 CHW，而相机图像通常是 HWC。当模型所需布局与图像布局不同时，请在 [runModelInference](zh-reference-operators-run-model-inference) 之前插入该算子。
* 结果张量的形状必须反映重新排列后的布局。

## 相关算子

* [convertColor](zh-reference-operators-convert-color) —— 变更颜色布局 / 通道数。
* [copy](zh-reference-operators-copy) —— 类型转换。
* [为模型准备图像数据](zh-workflows-prepare-image-data)

