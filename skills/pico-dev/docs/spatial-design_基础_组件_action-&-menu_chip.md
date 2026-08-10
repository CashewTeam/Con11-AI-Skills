多个 Chip 成组出现，常用于触发操作、内容筛选或进行选择。它能帮助用户更快捷、更轻松地完成当前任务。
##  类型
Chip 有 Button Chip、Removable Chip 和 Toggle Chip 3种类型。

### Button Chip
Button Chip 与 Button 类似，两者都提供视觉提示，促使用户采取行动或进行选择。但 Chip 用来增强用户体验或鼓励行动，Button 用于推进交互流程或采取重要行动。在使用过程中，避免将 Chip 用在重要操作中。

### Removable Chip
Removable Chip 常见于“搜索历史”，如上图。用户可以自行决定 Removable Chip 的显示和隐藏。点击 Removable Chip 结尾的 “X” 即可删除它。
### Toggle Chip
相较于 Button Chip，Toggle Chip 额外拥有选中状态。常用于筛选信息列表，支持同时选中多个。

## 构成

* 前导元素：内容可以是 Icon 或者图片
* 文本
* 尾随图标

下表列举了三种 Chip 的构成：
| **Chip 类型** | **前导元素** | **文本** | **尾随图标** |
| --- | --- | --- | --- |
| Button Chip | 可选 | 必有 | 可选 |
| Removable Chip | 可选 | 必有 | 固定为 “X“，且 不可修改 |
| Toggle Chip | 可选 | 必有 | 可选 |

