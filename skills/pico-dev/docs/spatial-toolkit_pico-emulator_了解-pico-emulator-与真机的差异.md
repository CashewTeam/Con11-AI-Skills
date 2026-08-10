PICO Emulator 可在 PC 上模拟 PICO OS 6 运行环境，但与 PICO 真机在体验与功能上仍存在差异。本文详细介绍 PICO Emulator 与 PICO 真机的差异。
PICO Emulator 暂不支持 PICO 真机的部分新特性，但不影响开发测试流程。故本文不再详述。

## **交互能力差异**
### 手势追踪
手势追踪依赖 ToF (Time of Flight，飞行时间）摄像头 ，但 PC 上不支持 ToF 摄像头，因此 PICO Emulator 无法获取手部相关数据。PICO SDK 的手势追踪相关功能也无法在 PICO Emulator 中生效。
PICO Emulator 后续计划增加基于键鼠的手势交互模拟。
### 眼手交互模式下 Z 轴方向的移动
在眼手交互模式下，手模不支持 Z 轴方向的移动，你仅能通过移动摄像机的位置来实现 Z 轴方向的移动。
PICO Emulator 后续计划增加键盘模拟的手势交互。
## **渲染与显示差异**
### 模拟器清晰度
PICO Emulator 的画面分辨率为 2K，低于 PICO 真机的实际分辨率。
### FOV
PICO Emulator 的 FOV 小于 PICO 真机，因此可视范围也小于 PICO 真机。
### 视觉效果
PICO Emulator 的视觉效果与 PICO 真机存在差异，例如你可能会感觉到 PICO Emulator 面板的大小或距离与 PICO 真机不同。这主要由视觉误差、观察距离和硬件差异等因素导致。
### 注视点渲染
注视点渲染是一种结合眼动追踪的渲染优化技术，在用户视线焦点区域保持高清渲染，周边区域降低精度以节省性能。该功能在 PICO Emulator 中不可用。
## **SDK 功能支持差异**
受硬件与运行环境限制，PICO Emulator 对 PICO SDK 的部分功能暂不支持。下文分别介绍了 PICO Spatial SDK、PICO XR SDK 和 WebXR/WebSpatial 的功能支持差异。
### PICO Spatial SDK
PICO Emulator 不支持 PICO Spatial SDK 的以下功能：

* 追踪：
   * 手部追踪（手势追踪）。详情参阅 [手部追踪](./spatial-sdk_追踪_手部追踪.md)。
   * 全身动捕。详情参阅 [全身动捕](./spatial-sdk_追踪_全身动捕.md)。
   * 独立追踪。详情参阅 [独立追踪](./spatial-sdk_追踪_独立追踪.md)。
* Spatial ML。详情参阅 [SpatialML 概览](./spatial-sdk_spatialml_spatialml-概览.md)。
* 8K 及 HEVC 格式的视频。详情参阅 [视频文件](./spatial-sdk_资源管理_视频文件.md)。
* 开启高清 UI 渲染。详情参阅 [开启高清 UI 渲染](./spatial-sdk_性能与调试_开启高清-ui-渲染.md)。

### PICO XR SDK
PICO Emulator 不支持 PICO XR SDK（包含 Unity SDK、Unreal SDK 和 OpenXR SDK）的以下功能：

* 渲染
   * 静态注视点渲染。详情参阅各个 SDK 的文档。
   * 眼动追踪注视点渲染。详情参阅各个 SDK 的文档。
   * 设置屏幕刷新率。详情参阅各个 SDK 的文档。
   * 延迟锁定。详情参阅各个 SDK 的文档。
   * 缓冲区丢弃优化。详情参阅各个 SDK 的文档。
   * 渲染视口调节。详情参阅各个 SDK 的文档。
   * 自适应分辨率。详情参阅各个 SDK 的文档。
   * 超分辨率。详情参阅各个 SDK 的文档。
   * 锐化。详情参阅各个 SDK 的文档。
* 交互
   * 触觉反馈。详情参阅各个 SDK 的文档。
   * 面部追踪。详情参阅各个 SDK 的文档。
   * 手势追踪。详情参阅各个 SDK 的文档。
   * 全身动捕。详情参阅各个 SDK 的文档。
   * 体感追踪器。详情参阅各个 SDK 的文档。
* 混合现实
   * 视频透视。详情参阅各个 SDK 的文档。
   * SecureMR。详情参阅各个 SDK 的文档。
   * 混合现实捕捉。详情参阅各个 SDK 的文档。

### PICO WebXR/WebSpatial
PICO Emulator 支持 WebXR/WebSpatial 的全部功能。

