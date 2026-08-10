# 开始之前
在《[第一阶段：从平面窗口和 2D 内容开始](./spatial-tutorial_从模板开始搭建空间应用_第一阶段：从平面窗口和-2d-内容开始.md)》教程中，你已经学会了如何创建 2D 平面窗口（**Planar Window Container**）并在窗口间导航。现在，是时候让你的应用真正“立体”起来了。
## 你将实现什么
在本阶段教程中，你将学习如何创建一个具有可控深度的 **Volumetric Window Container**，并在其中放置和操控你的第一个 3D 对象。
完成本阶段教程后，你将实现以下功能：

* 打开和关闭一个 Volumetric Window Container。
* 在窗口内放置一个 3D 立方体，并使用控制面板改变其绕 Y 轴（竖直轴）的旋转。
* 通过拖拽手势，在空间中移动立方体的位置。
* 当拖拽开始时，立方体会变为半透明浅灰色以提供视觉反馈；拖拽结束时，它会恢复原色。

## 你将学习什么

* Volumetric Window Container 与 Planar Window Container 的本质区别。
* 如何声明一个 Volumetric WindowContainer 的属性和内容（包含默认与非默认）。
* 什么是 `Entity`（实体），如何通过代码创建基础几何模型并返回一个 `ModelEntity`。
* 如何创建和修改 `Entity` 的 `TransformComponent` 来控制其位置、旋转和缩放。
* 如何修改 `ModelComponent` 来改变 3D 物体的网格和材质（如颜色）。
* 如何实现简单的空间交互，例如拖拽 3D 物体在空间中的位置。

## 你将需要什么

* 完成《[第一阶段：从平面窗口和 2D 内容开始](./spatial-tutorial_从模板开始搭建空间应用_第一阶段：从平面窗口和-2d-内容开始.md)》教程的所有步骤。
* **预计耗时**：约 25 分钟

---

# 第 1 步：理解 Planar 与 Volumetric
**目标：**理解“Volumetric 窗口仍然是窗口，但开始具备体积和朝向”，并通过现成模板快速感受 Volumetric 窗口与 Planar 窗口的差异。
在动手改造代码前，先通过对比模板项目，建立对 Volumetric 窗口的直观认知。
## 操作步骤

1. **对比窗口声明**
   基于 Volumetric Window Container 模板新建一个空间应用，并打开其中的 `app/src/main/AndroidManifest.xml` 与 `app/src/main/java/.../Main.kt` 文件。将其与《[第一阶段：从平面窗口和 2D 内容开始](./spatial-tutorial_从模板开始搭建空间应用_第一阶段：从平面窗口和-2d-内容开始.md)》教程中 Planar Window Container 模板的配置进行对比，你会发现：
   * 在 `AndroidManifest.xml` 中，`Volumetric` 窗口的 `style` 被设为 `2`（对应 `Form.Volumetric`），`defaultsize` 包含三个维度，并可额外配置 `volumealignment` 和 `volumebasepanel` 等特有属性。
   * 在 `Main.kt` 中，`Volumetric` 版本的 `windowConstraints` 修饰符额外增加了一个 `depth` 参数。
   这些属性是赋予窗口“体积感”的关键。
2. **观察 Volumetric 内容组织**
   打开 `app/src/main/java/.../content/HomeVolume.kt` 文件。你会看到，Volumetric Window Container 同样使用 `SpatialView` 来承载 3D 场景。但与 Planar Window Container 不同，Volumetric Window Container 通过 `AttachmentPanel` 将 2D 文本面板“附着”在 3D 空间中的特定位置，而不是进行平面堆叠。
   ```Kotlin
   @Composable
   fun HomeVolume(modifier: Modifier) {
       SpatialView(
           modifier = modifier,
           // 1. 初始化 3D 场景内容
           initial = { content, attachments ->
               // 加载 3D 模型资源
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-asset.bundle")
               }
               val model = Entity.loadSuspend(modelName = "MyScene", bundle = bundle)
               bundle.close() // 加载完成后关闭 bundle
               
               // 调整模型位置与缩放并添加到场景
               model.apply {
                   components[TransformComponent::class.java]?.apply {...}
                   content.addEntity(this)
               }
   
               // 调整 Attachment (2D UI 面板) 在 3D 空间中的位置并添加到场景
               val bodyTextAttachment = attachments.entity(id = "homepage_body")
               bodyTextAttachment?.apply {...}
               
               val titleTextAttachment = attachments.entity(id = "homepage_title")
               titleTextAttachment?.apply {...}
           },
           // 2. 定义 2D UI 内容 (Attachments)
           attachments = {
               AttachmentPanel(id = "homepage_body") {
                   // 使用 Spatial UI 构建界面
                   Box(...) {
                       Text(text = stringResource(R.string.homepage_body))
                   }
               }
   
               AttachmentPanel(id = "homepage_title") {
                   Box(...) {
                       Text(text = stringResource(R.string.homepage_title))
                   }
               }
           }
       )
   }
   ```

3. **运行模板并感受差异**

运行 Volumetric Window Container 的模板项目，并与之前的 Planar Window Container 模板对比，你会发现以下不同：

* **Volumetric 窗口**：像一个可以放置在空间任意位置的“透明盒子”，让你可以从不同角度观察内部的 3D 内容。它有几个独特的表现：
   * 当你的视线焦点或手柄射线悬停在窗口底部时，会出现一个毛玻璃效果的半透明底板（basepanel）。
   * 底部的 Caption Bar（也就是窗口底部的图标按钮）会自动跟随你的视角移动到窗口侧面，方便你随时进行移动、最小化和关闭等操作。

* **Planar 窗口**：像一块内容厚度有限的“屏幕”。除非你通过拖拽底部的 Caption Bar 来调整，否则它会始终保持其初始的位置和朝向。

## 预期结果
完成此步骤后，你应该已经了解 Volumetric 窗口的两个本质特性：

* **拥有体积和感知能力**：Volumetric 窗口与 Planar 窗口都属于 Window Container，但 Volumetric 窗口拥有了真实的深度，并能感知你的视角。
* **支持更立体的内容**：更大的内部空间，让你可以添加和组合更灵活的 2D 与 3D 内容。

接下来，你将亲手创建一个 Volumetric 窗口。

---

# 第 2 步：创建并打开 Volumetric 窗口
**目标：**在《[第一阶段：从平面窗口和 2D 内容开始](./spatial-tutorial_从模板开始搭建空间应用_第一阶段：从平面窗口和-2d-内容开始.md)》教程中创建的 Spatial 项目的基础上，创建一个新的 Volumetric 窗口，并能从主窗口打开它。
上一步在查看 Volumetric Window Container 的模板项目时，你学习了如何声明默认 Volumetric 窗口的属性和内容，方式基本和声明默认 Planar 窗口类似，只是部分属性的 meta-data 不同。这里，你需要通过 DSL 声明一个非默认 Volumetric 窗口的属性和内容。
## 操作步骤

1. **使用 DSL 声明一个新的 Volumetric 窗口**
   打开 `app/src/main/java/.../Main.kt`，在 `mainApp` 中添加一个新的 `WindowContainer`，并设置和 `Volumetric` 类型相关的参数。
   以下代码通过设置多个参数，将窗口配置为 `Volumetric` 类型：
      * `form = Form.Volumetric`: 将窗口指定为 `Volumetric` 类型。
      * `defaultSize`: 设置窗口打开时的三维尺寸，包括宽度、高度和深度。
      * `volumeAlignment`: 控制窗口的对齐方式。设置为 `VolumeAlignment.Tilted` 后，当你的头部有俯仰（如低头或抬头）时，窗口会自动倾斜以正对你的视线焦点或手柄射线。
      * `defaultVolumeBasePanelType`: 定义窗口底板的行为。设置为 `VolumeBasePanelType.Default` 时，只要交互焦点悬停在窗口底部，系统就会默认显示底板。
      * `enableMaterialBackground = false`: 禁用默认的毛玻璃背景，使窗口呈现为一个完全透明的“空盒子”。
   此外，由于 Volumetric 窗口始终按等比例缩放，因此 `ContainerResizeRestriction` 设置对其无效。
   ```Kotlin
   // ... 原有 import 语句
   
   // [新增] import 语句
   import androidx.compose.foundation.layout.Box
   import com.pico.spatial.ui.foundation.dsl.VolumeAlignment
   import com.pico.spatial.ui.platform.resize.VolumeBasePanelType
   
   fun mainApp(scope: SpatialAppScope) = with(scope) {
       // ... 原有 DefaultWindowContainer 和 SecondaryWindow 的声明
   
       // [新增]声明 Volumetric 窗口
       WindowContainer(
           id = "VolumetricWindow",
           form = Form.Volumetric,
           defaultSize = WindowContainerSize(width = 1000.dp, height = 1000.dp, depth = 1000.dp),
           resizeType = ContainerResizeType.ContentSize,
           volumeAlignment = VolumeAlignment.Tilted,
           defaultVolumeBasePanelType = VolumeBasePanelType.Default,
           enableMaterialBackground = false
       ) {
           PicoTheme {
               // 新 Volumetric 窗口的内容，临时使用 Box，之后进行替换
               Box {}
           }
       }
   }
   ```

2. **从主窗口添加 Volumetric 窗口的入口**
   现在，你需要在主窗口中添加一个按钮，打开新的 Volumetric 窗口。
   回到 `HomePage.kt`，在 `Column` 布局中再添加一个打开 Volumetric 窗口的按钮。
   下面的代码在原有基础上，在最外围 `Column` 布局的底部，添加了一个 `Row` 布局，用于包裹住所有的 `Button`，让它们能够水平排列。然后把原来控制 Planar 窗口打开的 `Button` 移入，并添加了一个用于控制 Volumetric 窗口打开的新 `Button`。
   ```Kotlin
   // ... 原 import 语句
   
   @Composable
   fun HomePage(modifier: Modifier) {
       val navigator = LocalSpatialNavigator.current
       Column(
           modifier = modifier.padding(horizontal = 32.dp),
       ) {
           // ... 原有 Text 和 Row 布局
           Spacer(modifier = Modifier.weight(1f))
           
           // [新增]用 Row 布局组织打开容器的按钮
           Row(
               modifier = Modifier.fillMaxWidth(),
               horizontalArrangement = Arrangement.spacedBy(32.dp)
           ) {
               // [变更] 把原有打开新 Planar 窗口的按钮移动到新增的 Row 布局
               Button(
                   modifier = Modifier.padding(bottom = 32.dp),
                   onClick = {
                       navigator.openWindowContainer("SecondaryWindow")
                   }
               ) {
                   Text("Open A New Planar Window Container")
               }
               // [新增] 打开 Volumetric 窗口的按钮
               Button(
                   modifier = Modifier.padding(bottom = 32.dp),
                   onClick = {
                       navigator.openWindowContainer("VolumetricWindow")
                   }
               ) {
                   Text("Open A Volumetric Window")
               }
           }
       }
   }
   ```


## 预期结果
运行应用后，主窗口将显示两个按钮，分别用于打开 Planar 和 Volumetric 窗口。
点击右侧的 **Open A Volumetric Window** 按钮，即可打开一个空的、透明的“盒子”—— 这就是你刚刚创建的 Volumetric 窗口。你可以抓取并移动它，当视线焦点或手柄射线悬停在其底部时，还会出现一个毛玻璃底板。
虽然窗口内目前没有内容，但它已经清晰地展示了三维容器的形态。

---

# 第 3 步：创建 3D 模型并控制其旋转
**目标：**为 Volumetric 窗口添加内容，在其中创建一个简单的立方体，并添加 UI 来控制它的旋转。
## 操作步骤

1. **使用** **`ModelEntity` 创建立方体实体**
   在 `content` 包下创建一个新文件 `VolumeContent.kt`，粘贴以下代码：
   ```Kotlin
   package com.pico.spatial.sample.myapplication.content
   
   import androidx.compose.runtime.Composable
   import com.pico.spatial.core.ecs.ModelEntity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.resource.BlendingMode
   import com.pico.spatial.core.ecs.resource.MeshResource
   import com.pico.spatial.core.ecs.resource.PhysicallyBasedMaterial
   import com.pico.spatial.core.math.Color4
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.foundation.content.SpatialView
   
   @Composable
   fun VolumeContent() {
       SpatialView(
           // initial: 在 SpatialView 初始化时执行一次，用于创建和设置 3D 实体
           initial = { content, attachments ->
               // 创建一个立方体实体 (ModelEntity)
               val cube = ModelEntity(
                   // 创建网格资源：一个边长为 0.3 的立方体，圆角半径为 0.06
                   mesh = MeshResource.createBox(size = Vector3(0.3f), cornerRadius = 0.06f),
                   // 创建材质资源：基于物理的材质 (PBR)，混合模式为透明
                   material = PhysicallyBasedMaterial.create(BlendingMode.TRANSPARENT).apply {
                       // 设置基础颜色 (RGBA)，这里是一种浅灰色
                       setBaseColor(Color4(0.88f, 0.88f, 0.85f, 1f))
                       // 设置金属度，0 表示非金属
                       setMetallic(0f)
                       // 设置粗糙度，0.2 表示比较光滑
                       setRoughness(0.2f)
                   }
               )
               // 调整立方体的初始 Transform
               cube.components[TransformComponent::class.java]?.apply {
                   // 设置初始位置
                   setPosition(Vector3(0.0f, -0.15f, 0f))
               }
               // 为立方体设置名称，方便后续在 update 中查找
               cube.setName("cube")
               // 将立方体添加到场景内容中
               content.addEntity(cube)
           }
       )
   }
   ```

   完成后，记得在 `Main.kt` 文件中，将占位的 `Box{}` 替换为 `VolumeContent()` 并添加对应的 import 语句。
   ```Kotlin
   // ... 原有 import 语句
   
   // [新增] import 语句
   import com.pico.spatial.sample.myapplication.content.VolumeContent
   
   fun mainApp(scope: SpatialAppScope) = with(scope) {
       // ... 
       
       WindowContainer(
           id = "VolumetricWindow",
           form = Form.Volumetric,
           defaultSize = WindowContainerSize(width = 1000.dp, height = 1000.dp, depth = 1000.dp),
           resizeType = ContainerResizeType.ContentSize,
           volumeAlignment = VolumeAlignment.Tilted,
           defaultVolumeBasePanelType = VolumeBasePanelType.Default,
           enableMaterialBackground = false
       ) {
           PicoTheme {
               // 把 Box {} 替换为 VolumeContent()
               VolumeContent()
           }
       }
   }
   ```

   上面的代码使用 `ModelEntity` 创建了一个立方体模型。一个最基础的模型实体由两部分组成：
   * **网格 (mesh)**：定义模型的几何形状。代码中通过 `MeshResource.createBox()` 创建了一个带圆角的立方体。
   * **材质 (material)**：定义模型表面的外观。代码中通过 `PhysicallyBasedMaterial.create()` 创建了一种类似大理石的材质。
   最后，代码调整了立方体实体的位置，并将其添加到了场景中。
   PICO Spatial SDK 采用定制化的的实体-组件-系统（Entity-Component-System，ECS）架构。

   * `Entity` 表示一个对象的实体，本质上是若干 `Component` 的容器。
   * `Component` 表示与 `Entity` 相关的、具有特定格式的数据。在 PICO Spatial SDK 中，内置的 `Component` 包括 3D 模型组件、空间变换组件、渲染组件、物理组件、动画组件等。

2. **添加 Slider 组件，控制立方体绕 Y 轴的旋转**
   接下来，在 `VolumeContent.kt` 中实现一个控制面板，通过拖动滑动条控制立方体绕 Y 轴（竖直轴）的旋转。
   ```Kotlin
   // ... 原 import 语句
   
   // [新增] import 语句
   import androidx.compose.foundation.layout.Arrangement
   import androidx.compose.foundation.layout.Column
   import androidx.compose.foundation.layout.Row
   import androidx.compose.foundation.layout.padding
   import androidx.compose.foundation.layout.size
   import androidx.compose.foundation.layout.width
   import androidx.compose.foundation.shape.RoundedCornerShape
   import androidx.compose.runtime.getValue
   import androidx.compose.runtime.mutableFloatStateOf
   import androidx.compose.runtime.remember
   import androidx.compose.runtime.setValue
   import androidx.compose.ui.Alignment
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.draw.clip
   import androidx.compose.ui.text.font.FontWeight
   import androidx.compose.ui.unit.dp
   import androidx.compose.ui.unit.sp
   import com.pico.spatial.core.math.EulerAngles
   import com.pico.spatial.ui.design.Slider
   import com.pico.spatial.ui.design.Text
   import com.pico.spatial.ui.foundation.material.backgroundMaterial
   
   @Composable
   fun VolumeContent() {
       // [新增]使用 remember 保存立方体的 Y 轴旋转角度状态，初始值为 0 度
       var rotationY by remember { mutableFloatStateOf(0f) }
   
       SpatialView(
           // initial: 在 SpatialView 初始化时执行一次，用于创建和设置 3D 实体
           initial = { content, attachments ->
               // 原有创建立方体实体的代码
               val cube = ModelEntity(...)
               
               // 调整立方体的初始 Transform
               cube.components[TransformComponent::class.java]?.apply {
                   setPosition(Vector3(0.0f, -0.15f, 0f))
                   // [新增]设置初始旋转角度
                   setEulerAngles(EulerAngles(0f, rotationY, 0f))
               }
               cube.setName("cube")
               content.addEntity(cube)
   
               // [新增]获取名为 "control_panel" 的 AttachmentPanel 并设置其在 3D 空间中的位置
               val controlPanel = attachments.entity(id = "control_panel")
               controlPanel?.apply {
                   components[TransformComponent::class.java]?.apply {
                       setPosition(Vector3(0.2f, 0.1f, 0f))
                   }
                   content.addEntity(this)
               }
           },
           // [新增] update: 当 Composable 的状态 (如 rotationY) 发生变化时执行
           update = { content, _ ->
               // 根据名称查找立方体实体
               val cube = content.entities.find { it.getName() == "cube" }
   
               // 更新立方体的 Transform
               cube?.components?.get(TransformComponent::class.java)?.apply {
                   setEulerAngles(EulerAngles(0f, rotationY, 0f))
               }
           },
           // [新增] attachments: 定义关联的 2D UI 面板
           attachments = {
               // 定义 ID 为 "control_panel" 的面板内容
               AttachmentPanel(id = "control_panel") {
                   // 使用 CubeControlPanel Composable 显示 UI
                   // 并将状态 (rotationY) 和事件处理 (onRotationChange) 传递给它
                   CubeControlPanel(
                       rotationY = rotationY,
                       onRotationChange = { rotationY = it }
                   )
               }
           }
       )
   }
   
   /**
    * [新增]
    * CubeControlPanel 是一个纯 UI Composable，用于显示控制面板。
    * 它遵循状态提升 (State Hoisting) 模式，不直接持有状态，而是通过参数接收状态和回调。
    *
    * @param rotationY 当前的 Y 轴旋转角度
    * @param onRotationChange 当滑块值变化时的回调函数
    * @param modifier 修饰符
    */
   @Composable
   fun CubeControlPanel(
       rotationY: Float,
       onRotationChange: (Float) -> Unit,
       modifier: Modifier = Modifier
   ) {
       Column(
           modifier = modifier
               .size(width = 450.dp, height = 150.dp)
               .backgroundMaterial() // 应用空间材质背景
               .clip(RoundedCornerShape(12.dp))
               .padding(32.dp),
           verticalArrangement = Arrangement.spacedBy(16.dp)
       ) {
           // 标题文本
           Text(
               text = "Cube Control Panel",
               fontSize = 24.sp,
               fontWeight = FontWeight.Medium,
           )
   
           // 包含标签、滑动条和数值显示的行
           Row(
               verticalAlignment = Alignment.CenterVertically,
           ) {
               Text(
                   text = "Rotation Y: ",
                   fontSize = 18.sp,
                   fontWeight = FontWeight.Medium,
               )
               // 控制旋转的滑动条
               Slider(
                   modifier = Modifier.width(240.dp),
                   value = rotationY,
                   valueRange = 0f..360f, // 旋转范围 0 到 360 度
                   onValueChange = onRotationChange,
               )
               // 显示当前角度值
               Text(
                   text = " ${rotationY.toInt()}º",
                   fontSize = 18.sp,
                   fontWeight = FontWeight.Medium,
               )
           }
       }
   }
   ```

   上述代码的核心逻辑可以分解为以下三个部分：
   * **创建数据源**：使用 `remember { mutableFloatStateOf(0f) }` 创建了一个名为 `rotationY` 的可变状态。这个状态是整个逻辑的核心，它作为统一的数据源，同时控制着 UI 滑动条的显示和 3D 立方体的实际旋转角度。
   * **初始化场景 (`initial` 块)**：在 `SpatialView` 的 `initial` 块中，不仅创建了 3D 立方体，还添加了一个 `AttachmentPanel` 来作为 UI 控制面板。
      * **为何使用** **`AttachmentPanel`**：虽然你可以直接在 Volumetric 窗口中添加 2D UI，但使用 `AttachmentPanel` 可以将 UI 包装成一个实体（Entity），从而能更灵活地控制其在 3D 空间中的位置和朝向。另外，如果不使用 `AttachmentPanel`，在没有额外 Z **** 轴偏移量的情况下，UI 会直接显示在 Volumetric 窗口的背板上；而通过 `AttachmentPanel`，可以让 UI 作为独立的空间元素悬浮在立方体旁边，从而获得更自然的空间布局效果。在代码中，`AttachmentPanel` 被设置为悬浮在立方体旁边。
      * **面板内容**：该面板的具体内容是 `CubeControlPanel`。它负责显示当前的 `rotationY` 值，并在你拖动滑动条时通过 `onValueChange` 回调来更新这个值。
   * **响应状态更新 (`update` 块)**：`SpatialView` 的 `update` 块会在其依赖的 Compose 状态（即 `rotationY`）发生变化时自动执行。在 `update` 块内部，通过 `content.entities.find { it.getName() == "cube" }` 找到之前创建的立方体实体，获取其 `TransformComponent`，并调用 `setEulerAngles(EulerAngles(0f, rotationY, 0f))` 方法，根据最新的 `rotationY` 值来更新立方体的旋转角度。

## 预期结果
重新运行应用，打开 Volumetric 窗口，你会看到一个白色的立方体置于窗口中央，它的右上方悬浮着一个控制面板。拖动控制面板上的滑动条，立方体会随着绕 Y 轴旋转。你已经成功地创建并操控了你的第一个 3D 实体！

---

# 第 4 步：添加空间交互 - 空间拖拽
**目标：**为立方体添加空间拖拽交互，让它能响应你的交互输入。
用 UI 面板来控制 3D 物体还不够直观，现在让我们来给物体添加一些空间交互特性。
## 操作步骤

1. **定义状态**
   打开 `VolumeContent.kt`，在 Composable 中定义驱动 UI 和 3D 实体变化的“单一数据源”：
   * `dragOffset (Offset3D)`：记录用户拖拽产生的累积像素偏移量。使用 `Offset3D.Zero` 初始化
   * `initialPosition (Vector3)`：记录立方体在世界坐标系中的初始物理位置，单位为米
   * `isDragging (Boolean)`：记录当前是否处于拖拽状态，用于触发变色
   ```Kotlin
   // ... 原 import 语句
   
   // [新增] import 语句
   import androidx.compose.runtime.mutableStateOf
   import com.pico.spatial.ui.geometry.Offset3D
   
   @Composable
   fun VolumeContent() {
       // ...
       // [新增]添加状态定义
       val initialPosition = remember { Vector3(0.0f, -0.15f, 0f) } // 保存初始位置
       var dragOffset by remember { mutableStateOf(Offset3D.Zero) } // 保存拖拽产生的像素偏移
       var isDragging by remember { mutableStateOf(false) } // 保存是否正在拖拽的状态
       
       SpatialView(...)
   }
   ```

2. **处理交互输入**
   在 `VolumeContent.kt` 中，为 `SpatialView` 添加 `Modifier.pointerInput`，使用 `detectSpatialDragGesture` 监听用户的拖拽行为，并对拖拽对应的像素偏移量进行累加。在 `onDrag` 回调中，只做像素值的累加，不进行任何复杂的逻辑或坐标转换，保持输入处理的纯粹性。
   ```Kotlin
   // ... 原 import 语句
   
   // [新增] import 语句
   import androidx.compose.ui.input.pointer.pointerInput
   import androidx.compose.ui.platform.LocalContext
   import com.pico.spatial.ui.foundation.gesture.TargetEntity
   import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
   
   @Composable
   fun VolumeContent() {
       // ...
       
       // [新增]获取 Local Context
       val context = LocalContext.current
       
       SpatialView(
           // [新增]处理交互输入
           modifier = Modifier.pointerInput(Unit) {
               detectSpatialDragGesture(
                   context = context,
                   targetedToEntity = TargetEntity.any { it.getName() == "cube" }, // 仅拖拽名为 "cube" 的 Entity
                   onDragStart = { isDragging = true }, // 更新状态：开始拖拽
                   onDragEnd = { isDragging = false }, // 更新状态：结束拖拽
                   onDragCancel = { isDragging = false }, // 更新状态：取消拖拽
                   onDrag = { spatialDragValue ->
                       // 更新数据：仅累加像素增量
                       dragOffset += spatialDragValue.dragAmount
                   }
               )
           },
           // initial: 在 SpatialView 初始化时执行一次，用于创建和设置 3D 实体
           initial = {...},
           // update: 当 Composable 的状态发生变化时执行
           update = {...},
           // attachments: 定义关联的 2D UI 面板
           attachments = {...},
       )
   }
   ```

3. **为立方体添加交互和碰撞组件**
   打开 `VolumeContent.kt`，为立方体添加 `InteractableComponent` 和 `CollisionComponent`。
   为了让立方体响应手势或手柄射线的交互，你需要为其添加 `InteractableComponent`，使其能够接收交互事件。此外，还需添加 `CollisionComponent` 来定义一个可供交互的物理形状。这个物理形状由 `collisionShape` 属性定义。出于性能优化或特殊设计的考虑，它通常可以设置为与模型实际的视觉形状不同。但在本阶段教程中，由于立方体模型较为简单，我们将其碰撞形状设置为与视觉形状一致，以确保交互的准确性：
   ```Kotlin
   // ... 原有 import 语句
   
   // [新增]import 语句
   import com.pico.spatial.core.ecs.CollisionComponent
   import com.pico.spatial.core.ecs.InteractableComponent
   import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
   import com.pico.spatial.core.ecs.resource.ShapeResource
   
   @Composable
   fun VolumeContent() {
       // ...
       
       SpatialView(
           // 处理交互输入
           modifier = Modifier.pointerInput(Unit) {...},
           // initial: 在 SpatialView 初始化时执行一次，用于创建和设置 3D 实体
           initial = { content, attachments ->
               // ...
               // 调整立方体的初始 Transform
               cube.components[TransformComponent::class.java]?.apply {
                   // 设置初始位置
                   setPosition(Vector3(0.0f, -0.15f, 0f))
                   // 设置初始旋转角度
                   setEulerAngles(EulerAngles(0f, rotationY, 0f))
               }
                           
               // [新增]添加交互组件，使其可接收交互事件
               cube.components.set(InteractableComponent())
               // [新增]添加碰撞组件，定义可用于交互的物理形状
               cube.components.set(
                   CollisionComponent(
                       collisionShape = listOf(ShapeResource.createBox(Vector3(0.3f))),
                       physicsMaterial = PhysicsMaterialResource()
                   )
               )
               // 为立方体设置名称，方便后续在 update 中查找
               cube.setName("cube")
               // 将立方体添加到场景内容中
               content.addEntity(cube)
               
               // ...
           },
           // update: 当 Composable 的状态发生变化时执行
           update = {...},
           // attachments: 定义关联的 2D UI 面板
           attachments = {...},
       )
   }
   ```

4. **设置立方体的初始 Transform 时，换用状态变量**
   在 `VolumeContent.kt` 的 `SpatialView` `initial` 块中，改用你在步骤 1 中定义的状态变量来设置立方体的初始 `Transform`：
   ```Kotlin
   // [更新]调整立方体的初始 Transform
   cube.components[TransformComponent::class.java]?.apply {
       // 设置初始位置
       setPosition(initialPosition)
       // 设置初始旋转角度
       setEulerAngles(EulerAngles(0f, rotationY, 0f))
   }
   ```

5. **渲染更新**
   打开 `VolumeContent.kt`，在 `SpatialView` 的 `update` 块中，根据步骤 1 中定义的状态来更新立方体的属性，包括：
   * 拖拽时的位置更新：将 `dragOffset` 进行坐标空间转换，并叠加到 `initialPosition`
   * 拖拽状态下的材质改变效果：根据 `isDragging` 切换材质颜色
   ```Kotlin
   // ... 其他 import 语句
   
   // [新增]import 语句
   import androidx.compose.ui.platform.LocalDensity
   import androidx.compose.ui.unit.Density
   import com.pico.spatial.core.ecs.ModelComponent
   import com.pico.spatial.ui.platform.LengthUnit
   import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
   import com.pico.spatial.ui.platform.PhysicalLengthConverter
   
   @Composable
   fun VolumeContent() {
       // ...
       
       // [新增] 获取当前屏幕密度与物理长度转换器，用于将像素位移转换为 3D 空间中的米制单位
       val density = LocalDensity.current
       val converter = LocalPhysicalLengthConverter.current
       
       SpatialView(
           // 处理交互输入
           modifier = Modifier.pointerInput(Unit) {...},
           // initial: 在 SpatialView 初始化时执行一次，用于创建和设置 3D 实体
           initial = {...},
           // update: 当 Composable 的状态发生变化时执行
           update = { content, _ ->
               val cube = content.entities.find { it.getName() == "cube" }
           
               // [更新]位置计算与更新 
               cube?.components?.get(TransformComponent::class.java)?.apply {
                   setEulerAngles(EulerAngles(0f, rotationY, 0f))
                   // 将累计的像素偏移进行坐标空间转换，并加上初始位置
                   // 核心转换逻辑：像素 -> 米，且修正 Y 轴方向
                   val position = initialPosition + Vector3(
                       x = convertPxToMeter(dragOffset.x, density, converter),
                       y = convertPxToMeter(-dragOffset.y, density, converter), // Y 轴取反
                       z = convertPxToMeter(dragOffset.z, density, converter)
                   )
                   setPosition(position)
               }
           
               // [新增]材质变色效果
               val material =
                   cube?.components?.get(ModelComponent::class.java)?.materials?.get(0) as? PhysicallyBasedMaterial
               material?.apply {
                   if (isDragging) {
                       // 拖拽时显示半透明浅灰色
                       setBaseColor(Color4(0.85f, 0.85f, 0.8f, 0.5f))
                   } else {
                       // 正常显示
                       setBaseColor(Color4(0.88f, 0.88f, 0.85f, 1f))
                   }
               }
           },
           // attachments: 定义关联的 2D UI 面板
           attachments = {...}
       )
   }
   // [新增] 定义 convertPxToMeter 函数
   private fun convertPxToMeter(
       px: Float,
       density: Density,
       converter: PhysicalLengthConverter,
   ): Float {
       return with(density) { converter.dpToLength(px.toDp(), LengthUnit.Meters) }
   }
   ```


你可能会疑惑，为什么在实现拖拽立方体的逻辑时，示例代码没有使用复杂的 `convertPosition` 接口进行完整的坐标空间转换，而只是简单地将像素单位转换为米，并翻转了 Y 轴？
答案在于我们处理的是**相对位移**，而非**绝对坐标**。
`dragAmount` 是一个向量，它只描述“移动的方向和距离”（即位移增量），不关心物体的起点或终点在哪里。因为是相对移动，所以我们无需考虑 UI 坐标系和 3D 世界坐标系原点的不同，从而大大简化了计算。
尽管如此，为了让拖拽符合直觉，代码中仍需进行两项关键调整：

* **单位转换**：手势操作发生在 UI 坐标系中，单位是像素；而物体移动在 3D 世界坐标系中，单位是米。你必须进行单位换算，才能保证拖拽的距离感真实可信。
* **轴向修正**：在 UI 坐标系中，Y 轴向下为正；但在 3D 世界坐标系中，Y 轴向上为正。因此，你需要对 Y 轴的位移量取反（`-dragOffset.y`），这样当你向上拖动手势时，物体才会向上移动。

**那什么时候需要完整的坐标转换呢？**
当你的需求超出简单的“跟随拖拽”时，就需要使用 `convertPosition` 或 `convertRotation` 等接口进行完整的坐标转换。这通常发生在以下场景：

* **绝对位置映射**：例如，你希望通过单次点击（如使用 `detectSpatialTapGesture`）将物体精确放置在手势射线与一个平面相交的位置。在这种情况下，系统必须计算出 UI 中的一个点对应到 3D 世界中的确切坐标，这需要考虑两个坐标系原点的偏移。
* **旋转与朝向**：例如，你想让一个物体的正面始终朝向用户。这需要实时计算并转换两个坐标系之间的旋转关系，确保朝向正确。

## 预期结果
再次运行应用。现在，当你保持捏合（Pinch）手势或按住手柄的 Trigger 键并拖拽立方体时，它会跟随你的手势在空间中移动。在拖拽过程中，立方体会变为半透明的浅灰色，以提供清晰的视觉反馈。如果立方体移出 Volumetric 窗口，其超出边界的部分将被裁剪。
现在你已经能灵活地控制 3D 物体了！

# **总结**
恭喜你顺利完成本阶段教程！你成功地为 3D 内容赋予了更大的展示空间和更灵活的展现方式。
通过本教程，你已经掌握了：

* Volumetric Window Container 和 Planar Window Container 的核心区别，以及如何通过 DSL 创建 Volumetric 窗口并声明其属性与内容。
* 如何通过代码创建基础几何模型，理解 ECS 组件化的基本思想，以及如何通过修改不同组件来控制实体。
* 如何使用 `SpatialView` 的 `AttachmentPanel` 将 2D UI 与 3D 场景结合，并实现 UI 交互控制。
* 如何使用 `detectSpatialDragGesture` 监听 3D 交互事件，并为物体添加交互效果。

# **接下来**
`Volumetric` 窗口虽然提供了更大的三维空间，但它本质上仍是一个“有边界的盒子”，会裁剪掉超出其范围的内容。
如果你想构建一个无边界、不受裁剪的沉浸式世界，那么下一节教程不容错过。你将打破窗口的束缚，学习一种全新的应用形态——`Stage`，从而释放应用的全部空间潜力。详情参阅《[第三步：扩展到沉浸式场景并实现动画效果](./spatial-tutorial_从模板开始搭建空间应用_第三阶段：扩展到沉浸式场景.md)》。
## **延伸阅读**
如果你想更深入地探索本章涉及的概念，可以阅读以下文档：

* 《[了解空间容器 & 空间状态](./spatial-sdk_空间容器_了解空间容器-&-空间状态.md)》：通过阅读“WindowContainer”小节，理解 Planar 与 Volumetric 窗口在概念和使用场景上的区别。
* 《[声明 WindowContainer](./spatial-sdk_空间容器_管理-windowcontainer_声明-windowcontainer.md)》：了解如何为默认和非默认的 Volumetric 窗口声明属性与内容。
* 《[模型](./spatial-sdk_资源管理_模型.md)》、《[网格](./spatial-sdk_资源管理_网格.md)》与《[材质](./spatial-sdk_资源管理_材质.md)》：了解如何加载和创建 3D 模型，及其网格与材质资源的构成。
* 《[Spatial UI](/document/spatial-ui/)》与《[Slider](./spatial-ui_slider.md)》：了解 Spatial UI 支持的主题和组件库，学习如何丰富应用的 2D 内容。
* 《[了解 ECS 架构](./spatial-sdk_实体-组件-系统（ecs）_了解-ecs-架构.md)》与《[内置组件](./spatial-sdk_实体-组件-系统（ecs）_内置组件.md)》：了解 PICO Spatial SDK 的 ECS 架构思想，以及支持的内置组件。
* 《[添加 3D 内容](./spatial-sdk_内容布局与呈现_在-spatialmodelview-和-spatialview-中添加-3d-内容.md)》：学习如何使用 `SpatialView` 添加 3D 内容，以及如何通过 `AttachmentPanel` 将 2D UI 融入 3D 空间。
* 《[空间手势](./spatial-sdk_交互_空间手势.md)》与《[与 entity 交互](./spatial-sdk_交互_与实体交互.md)》：了解 PICO Spatial SDK 支持的空间手势，学习如何让 View 和 3D 实体响应交互事件。
* 《[坐标空间转换](./spatial-sdk_空间数学_坐标空间转换.md)》与《[长度单位转换](./spatial-sdk_空间数学_长度单位转换.md)》：了解 PICO Spatial SDK 的坐标系、长度单位及其转换方法。
* 《[PICO 设计指南](/document/spatial-design/)》：在 “基础” 章节中，阅读《[窗口](./spatial-design_基础_窗口.md)》与《[输入与交互](./spatial-design_输入与交互_概览.md)》部分，了解官方推荐的应用窗口与交互体验设计。
