Segmented Controls 常用于选择选项和切换视图。避免使用 Segmented Controls 来提供操作，如添加、移除或编辑内容。

Segmented Controls 分段数量控制在 2 到 7 个，过多会增加用户的理解成本和导航时间。每个分段的尺寸是一致的，所以分段内的文本长度不要有太大差异。

## 构成

1. Container 容器：开发者根据上层容器自定义。
2. Item 分段：内容可以是Text 、Icon 或 Icon + Text。避免将仅含图标的标签与文本标签混合使用。

## 交互行为
Segmented Controls 的分段不可置灰（无 Disabled 态）。目前仅提供单选，选中后颜色高亮。

