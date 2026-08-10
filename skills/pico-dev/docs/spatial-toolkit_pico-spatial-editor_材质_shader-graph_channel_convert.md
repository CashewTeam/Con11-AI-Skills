将输入的数据流从一种数据类型转换为另一种数据类型。

### 参数说明

* **In**: 需要转换的输入数据流。

### 节点使用说明
**Convert** 节点按以下规则处理数据类型：

* 当将 **Float** 转换为 **Color** 或 **Vector** 时，节点会将该 **Float** 值复制到 **Color** 或 **Vector** 的所有通道。
* 当将 **Color 3** 转换为 **Color 4** 时，节点会将输出的 Alpha 通道设置为 1.0。
* 当将 **Color 4** 转换为 **Color 3** 时，节点会舍弃 Alpha 通道。
* 当将 **Bool** 或 **Integer** 转换为 **Float** 时，输出值为 1.0 或 0.0。
* 当将 **Vector 2** 转换为 **Vector 3**  或将 **Vector 3** 转换为 **Vector 4**  时，节点会用 1.0 填充新增的通道。
* 当将 **Vector 4** 转换为 **Vector 3** 或将 **Vector 3** 转换为 **Vector 2** 时，节点会舍弃最后一个通道。

