本文介绍如何使用 Timelines 为实体添加动画效果。
你可以在一个场景中创建多个 Timeline 动画。在一个 Timeline 动画中，你可以为单个或多个实体设置动画，而每个实体又可以包含一条或多条动画轨道。Timelines 提供了多种预置的动作（即动画模板）。你只需将这些动作拖拽到轨道上，即可为实体应用相应的动画效果。

## 如何在空间应用中播放 Timeline 动画
在空间应用中，Timeline 动画可以通过 Behavior Trigger 组件触发，也可以通过 PICO Spatial SDK 的 `entity.playTimeline()` 函数播放。

* 你可以通过向实体添加 Behavior Trigger 组件触发 Timeline 动画。详情参阅 [Behavior Trigger](/editor/general-components)。
* Timeline 会作为 SpatialTimeline 类型的组件被保存在场景的 .usda 文件中。由于 Timeline 动画的数据结构与传统类型的动画不同，场景被加载到 PICO Spatial SDK 后，你可以使用 `entity.playTimeline()` 播放场景中的 Timeline 动画。详情参阅 [Timeline 动画](./spatial-sdk_动画_timeline-动画.md)。
   `entity.playAnimation(animationResource)` 函数不能用于播放 Timeline 动画。

## 操作步骤
参考以下步骤为场景中的 3D 模型添加动画效果。
### 步骤一：创建 Timeline 动画
在 Spatial Editor 的最下方，单击  **Timelines-Beta** 标签。

* 如果场景下没有 Timeline 动画，**Timelines-Beta** 标签页会提示你创建一个 Timeline。单击 **Create Timeline**。

* 如果场景下已经有了 Timeline 动画，你可在 **Timelines-Beta** 标签页左侧的 **Timelines** 栏单击加号按钮创建一个 Timeline。

建议为每个 Timeline 动画设置一个有意义且唯一的名称。因为当你使用 PICO Spatial SDK 播放动画时，需要通过同名的 `Entity` 对象来调用 `entity.playTimeline()` 函数。
Timeline 的名称只能包含字母、数字和下划线，且不能以数字开头。

如需重命名 Timeline 动画，在 **Timelines** 栏中双击该动画的名称并输入新名称即可。

### 步骤二：把实体添加到 Timeline
在 **Animated Object** 栏，单击 **Choose**。Spatial Editor 会弹出窗口提示你选择一个实体作为动画的作用对象。此时，你需要在 **Hierarchy** 窗口单击选中一个实体。选中后，单击提示窗口中的 **Done**。实体就会被添加到 **Animated Object** 栏。
另外，你也可以直接从 **Hierarchy** 窗口把实体拖拽到 **Animated Object** 栏。
只有绑定了 Transform 组件的实体才能被添加到 Timeline。

### 步骤三：为实体创建轨道
在 **Animated Object** 栏，单击实体右侧的添加轨道图标就可以添加一条轨道。你可以创建一条或多条轨道。

你可以通过拖拽调整轨道的上下顺序。

你也可以单击轨道左侧的按钮隐藏或锁定轨道。

* 被隐藏后，轨道中的动作不再生效。
* 被锁定后，轨道中的动作不再接受更改。

要删除一条轨道，可以先选中该轨道，然后按 Backspace 键（Windows）或 Delete 键（macOS）。
### 步骤四：向轨道添加动作
在轨道右侧的 **Action** 区域，把需要添加的动作拖拽到一条轨道上。你可以通过拖拽调整动作在轨道上的位置。
关于每个动作的配置方式，详情参阅 [Timelines 支持的动作](./spatial-toolkit_pico-spatial-editor_动画_timelines_timelines-支持的动作.md)。

你可以右击动作，在下拉菜单选择剪切、拷贝、复制、粘贴、删除、禁用及锁定操作。

你还可以通过拖动动作的左右边界来调整其在轨道上的时间长度。该操作本质上是调整动作的 **Duration** 参数。在下图中，注意动作的长度被调整时，右上角 **Duration** 参数值的变化。
**Play Audio** 和 **Play Animation** 动作的左右边界不能被调整，也没有 **Duration** 参数，因为音频和骨骼动画的长度是固定的。但你可以通过 **Repeat Count** 参数设置其播放的重复次数，或者勾选 **Repeat Forever** 使其永久循环播放。

如果不同轨道上的动作在时间轴上重合，那不同动作的动画效果会叠加。下图从左到右分别展示了：

* **Transform By** 与 **Play Animation** 的叠加效果。**Spin** 被隐藏。
* **Transform By**、**Play Animation** 与 **Spin** 叠加的效果。

<strong>Transform By 与 Play Animation 叠加</strong>

<strong>Transform By、Play Animation 与 Spin 叠加</strong>

你可以拖拽右侧的滑块来放大或缩小时间轴。

### 步骤五：预览动画效果
单击时间轴移动播放标尺，设定动画的播放起点。设定好播放起点后，单击播放按钮即可播放动画。

## 其他操作
### 嵌套 Timeline 动画
你可以把一个 Timeline 动画嵌套到另一个 Timeline 动画。
在下面的示例中，你把 Timeline_Plane 嵌套到了 Timeline_Bird 中。你可以右击 Timeline_Plane，在下拉菜单中选择 **Insert into Timeline**，也可以直接把 Timeline_Plane 拖拽到 Timeline_Bird 的轨道中。
* 嵌套后的 Timeline 动画长度无法修改。
* Timeline 动画不支持循环嵌套。例如，不能将 Timeline_Bird 嵌套进已嵌套了 Timeline_Bird 的 Timeline_Plane 中。

两个 Timeline 动画的嵌套播放效果与单个 Timeline 动画播放效果的对比如下：

