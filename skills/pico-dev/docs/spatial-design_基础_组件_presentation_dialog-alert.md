Dialog Alert 用于向用户传达需要立即处理的关键信息，常见于负向操作的警告提示。它以模态窗口的形式显示在应用内容之前，会打断用户当前任务，并在用户做出响应前禁用其他操作。因此应谨慎使用。

## 位置
Dialog Alert 与主 Window 居中对齐，并在 Z 轴上前移 64dp。Dialog Alert 出现时，其父级窗口会变暗，表明父级窗口不可交互，同时引导用户将注意力集中在 Dialog Alert 上。

## 布局
Dialog Alert 提供水平和垂直两种布局样式，如下图：

* 水平布局：多数场景下，推荐使用。
* 垂直布局：如果按钮文案过长，或按钮数量超过三个，导致下方操作区域过于拥挤，则采用垂直布局。

## 构成

1. 容器：容器高度根据其中的内容自适应，最大高度为主 Window - 64dp。Dialog Alert 内容不可为输入数据类，如：文本输入框。
2. 图标（可选）：放置在标题前面。
3. 标题（可选）：文案尽量清晰简洁。
4. 副文本（可选）：用来补充说明。
5. 动作：至少需要一个动作，因为用户需要与之交互来关闭 Dialog Alert。

## 交互行为
### Caption Bar
Dialog Alert 的出现不会影响 Caption Bar 的交互。拖动 Caption Bar 时，Dialog Alert 会保持与主 Window 的位置关系。
### Resize
对 Window 进行 Resize，不会放大/缩小 Dialog Alert 中的内容的尺寸，只可能影响 Dialog Alert 的高度。
Dialog Alert 的高度根据其中的内容自适应，其最大高度为 Window 高度减去 64dp。在用户缩小 Window 的过程中，可能会使 Dialog Alert 高度缩小，导致内容显示不全。有下面两种解决方案：

* 让用户滑动页面查看完整内容。滑动时，Dialog Alert 的标题和底部的操作区域固定，不跟随滑动。
* 设置 Window 的最小高度，使其比 Dialog Alert 的高度大 64dp。详见 [Window 尺寸规范](./spatial-design_基础_窗口.md)。

