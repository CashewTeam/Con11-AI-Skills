让用户通过滑动 Scroll Indicator 来查看超出 View 视图的内容。帮助用户感知内容长度及当前位置，提升导航效率与用户体验。它的功能点总结如下:

* 可随滚动实时更新
* 适配横向/纵向滚动场景
* 在 XR 场景下，因滑动长内容对用户产生的消耗较大，应提供快速定位的能力

Scroll Indicator 只有在滑动页面时才会显示，因此建议在视觉上表示页面可滚动，引导用户去查看更多内容。例如：在视图边缘显示部分内容，表示该方向有更多内容。
## 位置
Scroll Indicator 固定在 Scroll View 的中间，且尺寸偏小，有助于用户无需大幅度移动即可高效滚动。

## 交互行为
Scroll Indicator 提供当前位置和总长度的反馈。直接与 Scroll Indicator 交互时，拖动速度达到某个阈值后，可加快翻页速度。

1. Normal 态
2. Hover 态
3. Pinch 态：显示速度线

虽然指示符的总体尺寸较小，但它比其他系统的要稍微粗一些。如果内容与试图边距过于紧凑，请考虑增加外边距以防止 Scroll Indicator 与内容重叠。如果 Scroll Indicator 与内容重叠，优先响应 Scroll Indicator 的交互。
