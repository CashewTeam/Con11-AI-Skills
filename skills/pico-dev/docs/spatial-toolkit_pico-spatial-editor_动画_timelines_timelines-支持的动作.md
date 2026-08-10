本文介绍 Timelines 支持的动作和每个动作可配置的参数。
## Transform By
对实体应用增量变换。基于实体当前的状态（位置、旋转、大小）叠加新的变化量。
你可以根据使用场景选择 **Transform To** 或 **Transform By**。

* **Transform To** 适合用于归位、复原或移动到特定地点（如“回到起点”）。
* **Transform By** 适合用于连续动作（如“向前走一步”、“向左转”）。

### 参数说明
你选中 **Transform By** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒）。默认为 1 |
| Timing Function | 缓动函数。控制动画过程中的速度变化曲线： ;  • **Linear:** （默认）线性。全程匀速。 ;  • **EaseIn:** 缓入。启动慢，逐渐加速。 ;  • **EaseOut:**  缓出。启动快，逐渐减速。 ;  • **EaseInOut:** 缓入缓出。两头慢，中间快（最自然）。 |
| Position | 位移增量。在当前坐标上累加的距离。例如 (0, 10, 0) 表示向 Y 轴正方向移动 10 米。 |
| Rotation | 旋转增量。在当前角度上叠加的旋转值。例如 (0, 90, 0) 表示向右转 90 度。 |
| Scale | 缩放系数。基于当前尺寸的乘数。默认为 (1, 1, 1)。 |
## Transform To
将实体从当前状态平滑过渡到指定的世界坐标目标状态。
你可以根据使用场景选择 **Transform To** 或 **Transform By**。

* **Transform To** 适合用于归位、复原或移动到特定地点（如“回到起点”）。
* **Transform By** 适合用于连续动作（如“向前走一步”、“向左转”）。

### 参数说明
你选中 **Transform To** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒）。默认为 1 |
| Timing Function | 缓动函数。控制动画过程中的速度变化曲线： ;  • **Linear:** （默认）线性。全程匀速。 ;  • **EaseIn:** 缓入。启动慢，逐渐加速。 ;  • **EaseOut:**  缓出。启动快，逐渐减速。 ;  • **EaseInOut:** 缓入缓出。两头慢，中间快（最自然）。 |
| Transform Mode | 空间坐标类型。 ;; * **Global**：（默认）世界坐标系。 ;  * **Local**：本地坐标系。 |
| Position | 实体移动终点的世界坐标 (x, y, z)。 |
| Rotation | 实体旋转终点的欧拉角 (x, y, z)。 |
| Scale | 实体的最终缩放比例。默认为 (1, 1, 1) 即原始大小。 |
## Spin
旋转实体。
### 参数说明
你选中 **Spin** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒）。默认为 1 |
| Revolutions | 实体旋转的圈数，默认值为 1。该值可以是正数、负数或小数： ;; * **正数**：沿 **Spin Direction** 参数指定的方向旋转。 ;  * **负数**：沿 **Spin Direction** 参数指定的相反方向旋转。 ;  * **小数**：表示旋转不足一整圈。例如，0.5 代表旋转半圈。 |
| Timing Function | 缓动函数。控制动画过程中的速度变化曲线： ;  • **Linear:** （默认）线性。全程匀速。 ;  • **EaseIn:** 缓入。启动慢，逐渐加速。 ;  • **EaseOut:**  缓出。启动快，逐渐减速。 ;  • **EaseInOut:** 缓入缓出。两头慢，中间快（最自然）。 |
| Axis | 旋转轴向量。默认为 (0, 1, 0)。 |
| Spin Direction | 旋转方向。 ;; * **Clockwise**：（默认）顺时针旋转。; * **Counter Clockwise**：逆时针旋转。 |
## Hide Entity
隐藏实体。该动画本质上是把实体的 Opacity Controller 组件的 Opacity 参数值设置为 0。
如果实体没有关联 Opacity Controller 组件，你把 **Hide Entity** 动作拖拽到轨道上时，Spatial Editor 会提示你先为实体添加该组件。你需要在提示信息中单击 **Add**，Spatial Editor 会为该实体添加 Opacity Controller 组件。

### 参数说明
你选中 **Hide Entity** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒）。默认为 1 |
| Timing Function | 缓动函数。控制动画过程中的速度变化曲线： ;  • **Linear:** （默认）线性。全程匀速。 ;  • **EaseIn:** 缓入。启动慢，逐渐加速。 ;  • **EaseOut:**  缓出。启动快，逐渐减速。 ;  • **EaseInOut:** 缓入缓出。两头慢，中间快（最自然）。 |
## Show Entity
显示实体。该动画本质上是把实体的 Opacity Controller 组件的 Opacity 参数值设置为 1。
如果实体没有关联 Opacity Controller 组件，你把 **Show Entity** 动作拖拽到轨道上时，Spatial Editor 会提示你先为实体添加该组件。你需要在提示信息中单击 **Add**，Spatial Editor 会为该实体添加 Opacity Controller 组件。
### 参数说明
你选中 **Show Entity** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒）。默认为 1 |
| Timing Function | 缓动函数。控制动画过程中的速度变化曲线： ;  • **Linear:** （默认）线性。全程匀速。 ;  • **EaseIn:** 缓入。启动慢，逐渐加速。 ;  • **EaseOut:**  缓出。启动快，逐渐减速。 ;  • **EaseInOut:** 缓入缓出。两头慢，中间快（最自然）。 |
## Disable Entity
禁用实体。禁用后，该实体无法被渲染，也无法与物理系统交互。
### 参数说明
你选中 **Disable Entity** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
## Enable Entity
启用实体。禁用后，该实体可以被渲染，也可以与物理系统交互。
### 参数说明
你选中 **Enable Entity** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
## Play Audio
播放 Audio Resource Library 组件中的音频文件。详情参阅 [Audio Resource Library](/editor/audio-components)。
如果实体没有关联 Audio Resource Library 组件，你把 **Play Audio** 动作拖拽到轨道上时，Spatial Editor 会提示你先为实体添加该组件。你需要在提示信息中单击 **Add**，Spatial Editor 会为该实体添加 Audio Resource Library 组件。

### 参数说明
你选中 **Play Audio** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Audio | 要播放的音频文件。你只能选择已添加到 Audio Resource Library 组件的音频文件。关于如何把音频文件添加到 Audio Resource Library 组件，详情参阅 [把音频文件添加到实体关联的 Audio Resource Library 组件](/editor/timeline-built-in-animation-model)。 |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒），默认与音频文件的时长相同。 |
| Volume | 音量大小，取值范围为 0 到 1，支持小数。0 表示静音，1 表示最大音量。 |
| Repeat Count | 音频的重复播放次数。默认为 0，表示仅播放一次，不会重复。 |
| Repeat Forever | 勾选该选项后，音频将无限循环播放，不勾选则按 **Repeat Count** 设置的次数播放。  |
### 把音频文件添加到实体关联的 Audio Resource Library 组件
参考以下步骤把音频文件添加到实体关联的 Audio Resource Library 组件。

1. 选中添加了 **Play Audio** 动作的实体。在右侧的 **Inspector** 窗口找到 **Audio Resource Library** 组件。

2. 单击 **+** 按钮。弹出的下拉菜单会显示 **Hierarchy** 窗口中所有的音频文件。你可以选择要添加的音频文件，也可以单击 **Choose...** 从当前项目的资源中选择要添加的音频文件。

3. 音频文件被添加到 Audio Resource Library 组件后，你就可以在 **Play Audio** 动作的 Audio 参数中选择该音频文件。

## Play Animation
播放 Animation Resource Library 组件中的动画。详情参阅 [Animation Resource Library](/editor/animation-component)。
目前 Animation Resource Library 组件仅支持骨骼动画。
你把 **Play Animation** 动作拖拽到轨道上时：

* 如果添加到 Timeline 的实体类型是 SkelRoot，Spatial Editor 会自动为该实体添加一个 Animation Resource Library 组件。实体下的骨骼动画会自动被添加到 Animation Resource Library 组件。
* 如果添加到 Timeline 的实体类型不是 SkelRoot，Spatial Editor 会遍历其子实体，直到找到 SkelRoot 类型的实体。Spatial Editor 会自动为该实体添加一个 Animation Resource Library 组件。实体下的骨骼动画会自动被添加到 Animation Resource Library 组件。

### 参数说明
你选中 **Play Animation** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Animation | 要播放的动画。你只能选择已添加到 Animation Resource Library 组件的动画或通过 Animation Resource Library 组件剪辑的动画片段。详情参阅： ;; * [使用 Animation Resource Library 组件添加动画](/editor/timeline-built-in-animation-model) ;  *  [使用 Animation Resource Library 组件剪辑动画](/editor/timeline-built-in-animation-model) |
| Repeat Count | 动画的重复播放次数。默认为 0，表示仅播放一次，不会重复。 |
| Repeat Forever | 勾选该选项后，动画将无限循环播放，不勾选则按 **Repeat Count** 设置的次数播放。  |
### 使用 Animation Resource Library 组件添加动画
参考以下步骤使用 Animation Resource Library 组件添加动画。

1. 选中被添加了 Animation Resource Library 组件的实体。在右侧的 **Inspector** 窗口找到 **Audio Resource Library** 组件。

2. 单击组件下方的 **+** 按钮，从当前项目的资源中选择要添加的动画（仅支持 .usdz 格式）。Animation Resource Library 中默认包括 **default_animation**，即未剪辑的原始动画。

### 使用 Animation Resource Library 组件剪辑动画
参考以下步骤使用 Animation Resource Library 组件剪辑动画。

1. 选中添加了 **Play Animation** 动作的实体。在右侧的 **Inspector** 窗口找到 **Audio Resource Library** 组件。

2. 找到需要剪辑的动画，单击动画右侧的 **+** 按钮以创建一个或多个副本。

3. 调整副本的开始和结束时间，以剪辑出所需的动画片段。

## Play Particle
播放 Particle 组件中的粒子效果。详情参阅 [Particle](/editor/general-components)。
你把 **Play Particle** 动作拖拽到轨道上时：

* 如果添加到 Timeline 的实体有 Particle 组件，该组件的粒子效果将会在 **Play Particle** 动作中播放。
* 如果添加到 Timeline 的实体没有 Particle 组件，Spatial Editor 会提示你该实体缺少 Particle 组件。你可以单击 **Add** 添加一个 Particle 组件。

### 参数说明
你选中 **Play Particle** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒）。 |
| Repeat Count | 粒子效果的重复播放次数。默认为 0，表示仅播放一次，不会重复。 |
| Repeat Forever | 勾选该选项后，粒子效果将无限循环播放，不勾选则按 **Repeat Count** 设置的次数播放。  |
## Notification
添加消息通知。
Timeline 动画播放到 **Notification** 动作对应的时间点时，会向场景中所有监听消息通知的  [Behavior Trigger](/editor/general-components) 组件发送消息通知，从而触发 Behavior Trigger 组件所关联的 Timeline 动画的播放。
### 参数说明
你选中 **Notification** 动作后，可以在 **Inspector** 窗口设置以下参数：

| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Identifier | 消息通知的 ID。 |
### 通过 Notification 动作触发 Timeline 动画
假设你在 Spatial Editor 中分别为场景中的两个实体添加 Timeline 动画：

Toy_Biplane_Anime 实体对应 Timeline_plane 动画。Timeline_plane 动画包括 **Play Animation** 动作和 **Notification** 动作。

同时，Notification 动作的 **Identifier** 是 `start_celestial_globe`。

Celestial_Globe_Anime 实体对应 Timeline_globe 动画。Timeline_globe 动画包括 **Play Animation** 动作。

同时，Celestial_Globe_Anime 实体添加了 Behavior Trigger 组件，且该组件 **On Notification** 模块的 **Identifier** 是 `start_celestial_globe`，Action 是 `Timeline_globe`。

如果 Toy_Biplane_Anime 实体对应 Timeline_plane 动画首先被播放，那么在动画播放到 Notification 动作对应的时间点时，Celestial_Globe_Anime 实体对应的 Timeline_globe 动画就会被触发播放。

## Shader Graph
修改实体的 Shader Graph 材质属性。
如果同一时刻对应多个轨道中的 Shader Graph 动作，最下方轨道中的 Shader Graph 动作生效。

### 参数说明
| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒）。 |
| Timing Function | 缓动函数。控制动画过程中的速度变化曲线： ;  • **Linear:** （默认）线性。全程匀速。 ;  • **EaseIn:** 缓入。启动慢，逐渐加速。 ;  • **EaseOut:**  缓出。启动快，逐渐减速。 ;  • **EaseInOut:** 缓入缓出。两头慢，中间快（最自然）。 |
| Material | 实体需要修改的 Shader Graph 材质。 |
| Input Node | Shader Graph 的输入节点。 |
| Input Value | Shader Graph 的输入节点的值。 |
### 通过 Shader Graph 动作实现渐变动画
假设你创建了一个 Cube 且为其设置了 Shader Graph 材质。材质包含一个输入节点 **DiffuseColor**。**DiffuseColor** 的初始值为黑色。

你为该 Cube 创建了一个 Timeline 动画，向轨道中添加了 **Shader Graph** 动作，且把 **Input Node** 设置为 `DiffuseColor`，把 **Input Value** 设置为绿色。

这样你就可以实现材质颜色的渐变动画。

## Light
控制实体关联的 Directional、Point 及 Spot 灯光组件的颜色与强度。

### 参数说明
| 参数 | 说明 |
| --- | --- |
| Start Time | 动作在时间轴上的开始时间，单位为秒。你也可以在时间轴上手动拖拽动作来调整该参数的值。 |
| Duration | 动作时长（秒）。 |
| Color | 灯光组件的灯光颜色。 |
| Intensity | 灯光组件的灯光强度。 |
下面的动图展示了关联 Spotlight 灯光组件的实体如何在 Timeline 动画中通过 Light 动作改变 Spotlight 灯光的强度和颜色。

