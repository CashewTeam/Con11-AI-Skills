本文介绍 Spatial Editor 中的音频组件。
音频组件可以被添加到实体或从实体中删除。在 .usda 文件中，音频组件的类型为 `SpatialComponent`。这是一种由 Spatial Editor 定义的、非 USD 原生的组件类型。
在一个场景中最多同时播放 39 个音频文件。

## Channel Audio

声道音频源，没有空间效果，例如普通背景音乐。
| **参数** |  | **说明** |
| --- | --- | --- |
| Volume |  | 音量大小，取值范围为 0 到 1，支持小数。0 表示静音，1 表示最大音量。 |
| Preview | Audio Resource | 音源。你可以： ;; * 单击下拉菜单，选择一个音源文件节点作为音源。 ;  * 单击右侧按钮从场景中选择一个音频文件作为音源。 ;; **Preview** 参数关联的 **Audio Resource** 仅用于预览，音频文件并没有实际关联到 Channel Audio 组件。你必须通过 PICO Spatial SDK 把音频文件关联到 Channel Audio 组件。 ;   |
## Ambient Audio

环境音频源是一种有方向但没有具体位置的音频，例如风声。
| **参数** |  | **说明** |
| --- | --- | --- |
| Volume |  | 音量大小，取值范围为 0 到 1，支持小数。0 表示静音，1 表示最大音量。 |
| Preview | Audio Resource | 音源。你可以： ;; * 单击下拉菜单，选择一个音源文件节点作为音源。 ;  * 单击右侧按钮从场景中选择一个音频文件作为音源。 ;; **Preview** 参数关联的 **Audio Resource** 仅用于预览，音频文件并没有实际关联到 Ambient Audio 组件。你必须通过 PICO Spatial SDK 把音频文件关联到 Ambient Audio 组件。 ;   |
## Object Audio

这种音频源在空间中既有具体位置，也有明确方向，例如一个虚拟收音机。
| **参数** |  | **说明** |
| --- | --- | --- |
| Volume |  | 音量大小，取值范围为 0 到 1，支持小数。0 表示静音，1 表示最大音量。 |
| Sound Radius |  | 声源半径（米）。默认为 0.1。 |
| Distance Attenuation Mode |  | 设置声音随距离变化的衰减方式。 ;; * **Fixed**：在 **Sound Radius** 参数定义的范围内，音量保持恒定，不会随距离衰减。 ;  * **Inverse Square**：（默认）模拟真实世界的声音衰减效果，音量会随着与声源距离的增加而自然减弱。 ; |
| Directivity |  | 设置声源指向。声源指向主要由两个参数控制：**Pattern** 和 **Sharpness**。通过合理设置这两个参数，可以在虚拟环境中模拟不同声源的发声特性，例如麦克风拾音模式、扬声器辐射方向或环境中乐器的空间感，使声音的空间表现更加真实和自然。 ;  你可以： ;; * 单击右侧图标选择一个预设的声源指向。 ;; * 通过设置 **Pattern** 和 **Sharpness** 自定义声源指向。关于 **Pattern** 和 **Sharpness** 的设置方法，详情参阅 [使用 ObjectAudioComponent](./spatial-sdk_音频_使用-objectaudiocomponent.md)。 |
| Preview | Audio Resource | 音源。你可以： ;; * 单击下拉菜单，选择一个音源文件节点作为音源。 ;  * 单击右侧按钮从场景中选择一个音频文件作为音源。 ;; **Preview** 参数关联的 **Audio Resource** 仅用于预览，音频文件并没有实际关联到 Object Audio 组件。你必须通过 PICO Spatial SDK 把音频文件关联到 Object Audio 组件。 ;   |
## Audio Mix Groups

Audio Mix Groups 组件包括通过 Audio Mixer 创建的音频混合组。你可以使用音频混合组对音频文件的播放属性进行分组管理。详情参阅 [什么是 Audio Mixer](./spatial-toolkit_pico-spatial-editor_音频_audio-mixer_什么是-audio-mixer.md)。
## Audio Resource Library

Audio Resource Library 组件可以包括一个或多个音源文件节点。你可以单击加号添加当前项目中的音源文件节点。
Audio Resource Library 组件有以下主要用途：

* 场景被加载到 PICO Spatial SDK 后，你可以获取实体的 `AudioResourceLibraryComponent`，然后播放 Audio Resource Library 组件中的音频资源。
* 为 Timelines 动画效果器中的 **Play Audio** 动作提供音频资源。详情参阅 [Play Audio](/editor/timeline-built-in-animation-model)。

## Audio Resource

音频资源。每个 Audio Resource 组件可关联一个音频文件。
添加到 Spatial Editor 项目的音源会自带 Audio Resource 组件。
Audio Resource 组件无法通过 **Inspector** 窗口底部的 **Add Component** 按钮添加。你可以通过点击 **Hierarchy** 窗口的 + 按钮，然后在下拉菜单中选择 **Audio Asset** > **Audio Resource** 添加一个自带 Audio Resource 组件的音源文件节点。

| **参数** | **说明** |
| --- | --- |
| Source File | 关联的音频文件。单击右侧按钮从场景中选择一个音频文件。 |
| Ambisonics Type | 设置 Ambisonics（高保真度立体声响复制）的空间音频处理方式。 ;; * **None**：不进行 Ambisonics 处理。 ;  * **ACN_SN3D_1**：采用 ACN 排序与 SN3D 归一化，适用于一阶 Ambisonics 音频。 ;  * **ACN_SN3D_2**：采用 ACN 排序与 SN3D 归一化，适用于二阶 Ambisonics 音频。 |
| Audio Mixer Group | 音频混合组。你可以使用音频混合组对音频文件的播放属性进行分组管理。详情参阅 [什么是 Audio Mixer](./spatial-toolkit_pico-spatial-editor_音频_audio-mixer_什么是-audio-mixer.md)。 |
| Loop | 是否循环播放。 |
| Random Start | 每次播放时，从音频总长度中随机抽取一个时间点作为起点。 |
## Audio Group Resource

音频组资源。音频组资源是一个音频播放列表。每个 Audio Group Resource 组件可关联一个或多个音频文件。你可以点击 **+** 添加音频文件。
Audio Group Resource 组件无法通过 **Inspector** 窗口底部的 **Add Component** 按钮添加。你可以通过点击 **Hierarchy** 窗口的 + 按钮，然后在下拉菜单中选择 **Audio Asset** > **Audio Group Resource** 添加一个自带 Audio Group Resource 组件的音源文件节点。被添加的音频文件会成为这个音源文件节点的子节点。

| **参数** |  | **说明** |
| --- | --- | --- |
| Play Mode |  | 音频组的播放模式。 ;; * **Random**：随机播放。 ;  * **Forward：**按顺序正向播放。 ;  * **Backward**：按顺序反向播放。 |

