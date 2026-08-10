# 开始之前
本阶段在《[第一阶段：让 3D 物体可以被交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第一阶段：让-3d-物体可以被交互.md)》完成后的项目上继续开发。你的 `HomeStage.kt` 应当处于第一阶段最后一节的最终状态：包含 `enableInteraction()` 扩展函数、地球模型加载逻辑以及单手拖拽交互。本阶段会替换原有场景为新的 8 大行星场景，并新增双手缩放等复合交互。
## **你要实现什么**
完成本教程后，你将在空间应用中看到太阳系的八大行星，并可以和它们进行互动：

* **单手捏合**：抓取并拖动任意行星。
* **双手捏合**：放大或缩小任意行星。

## **你将学习什么**

* 如何在应用中和多个物体进行交互。
* 如何让一个物体可以接受多个不同的交互操作。
* 如何使用 `detectSpatialScaleGesture()` 缩放物体。

## **你将需要什么**

* 完成《[第一阶段：让 3D 物体可以被交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第一阶段：让-3d-物体可以被交互.md)》中的全部内容。
* PICO 设备或 PICO Emulator。
* [PICO Spatial Editor](./spatial-toolkit_pico-spatial-editor_什么是-pico-spatial-editor.md)：用于搭建包含多个行星模型的场景。
* **预计耗时：**约 40 分钟。

# 第一步：交互准备工作
## 搭建场景
首先，你需要在 Spatial Editor 中搭建场景。

1. 使用 Android Studio 打开你在《[第一阶段：让 3D 物体可以被交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第一阶段：让-3d-物体可以被交互.md)》教程中创建的空间应用，选择 **File** > **New** > **New Module**。
2. 在 **Create New Module** 页面的 **Templates** 区域，选择 **Spatial Resource Library**，然后设置以下参数。
   | 参数 | 说明 |
   | --- | --- |
   | **New Spatial Editor Project** | 是否创建一个新的 Spatial Editor 项目。在教程中勾选该复选框。 |
   | **Module name** | 库模块名称。在教程中设置为 **editor-planets**。 |
   | **Package name** | 库模块的包名。在教程中设置为 **com.pico.spatial.tutorial.editor.planets**。 |
   | **Minimum OS version** | 最低 PICO OS 6 版本。在教程中设置为 **PICO OS 6 v0.13 preview**。 |

3. 点击 **Finish**。Spatial Editor 项目会作为一个类型为 **Spatial Resource Library** 的库模块被导入到 Spatial 项目。
4. 切换到 Project Files 视图，点击`editor-planets/src/main/res3d/SpatialPackContent/Sources/ModelView` 预览 Spatial Editor 项目中的场景，然后点击预览界面右上角的 **Open In Editor** 在 Spatial Editor 中打开场景。

5. 进入 Spatial Editor 后，点击上方标签右侧的 **+** 按钮新建一个名称为 **Planets** 的场景。

6. 在 Spatial Editor 右上角找到内置资源库，然后将 8 大行星拖拽到场景中。

7. 通过 **Transform** 面板将它们等间距排列，使 8 颗行星以场景原点 (0, 0, 0) 为中心，从左到右依次排开。
   | **星球名称** | **空间位置（X，Y，Z）** |
   | --- | --- |
   | Mercury | (-2.1, 0, 0)  |
   | Earth | (-0.9, 0, 0)  |
   | Jupiter | (0.3, 0, 0)  |
   | Uranus | (1.5, 0, 0)  |
   | Venus | (-1.5, 0, 0) |
   | Mars | (-0.3, 0, 0) |
   | Saturn | (0.9, 0, 0) |
   | Neptune | (2.1, 0, 0) |
8. 将 8 个行星分成两组，每组四个（Mercury、Venus、Earth、Mars 一组；Jupiter、Saturn、Uranus、Neptune 一组）。为此，你需要在场景根节点 `Root` 下创建两个空的 `Entity`，并将它们分别命名为 `Group1` 和 `Group2`。然后，将相应的行星拖入各自的分组内。具体操作参考以下视频：

最终搭建完成的场景如下图所示：

## 展示场景

1. 为了在空间应用中使用并加载这个新创建的场景，你首先需要修改 `app/build.gradle.kts` 文件，将 `editor-planets` 子模块添加为 `app` 主模块的依赖项。
   ```Kotlin
   ...
   
   dependencies {
       implementation(libs.androidx.core.ktx)
       implementation(platform(libs.bom))
       implementation(libs.core)
       implementation(libs.platform)
       implementation(libs.foundation)
       implementation(libs.design)
       implementation(libs.sense)
       implementation(libs.tracking)
       implementation(libs.androidx.ui.tooling)
       implementation(libs.androidx.annotation)
       implementation(libs.androidx.appcompat)
       implementation(project(":editor-asset"))
   
       // [Add] 添加 editor-planets 模块
       implementation(project(":editor-planets"))
   
       testImplementation(libs.junit)
       androidTestImplementation(libs.androidx.junit)
       androidTestImplementation(libs.androidx.espresso.core)
       debugImplementation(libs.androidx.ui.tooling.preview)
   }
   
   ...
   ```

   这样，你就可以在代码中直接访问新场景。在应用运行时，SDK 会将 `editor-planets` 模块打包成 `editor-planets.bundle` 文件并放入应用的 `assets/` 目录，因此你可以用与之前相同的方式来加载场景。
2. 使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.graphics.Color
   import androidx.compose.ui.input.pointer.pointerInput
   import androidx.compose.ui.platform.LocalContext
   import com.pico.spatial.core.ecs.DirectionalLightComponent
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.foundation.content.SpatialView
   import com.pico.spatial.ui.foundation.content.toColor4
   import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
   import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   
   @Composable
   fun HomeStage() {
       val context = LocalContext.current
       val converter = LocalPhysicalLengthConverter.current
   
       SpatialView(
           Modifier
               .pointerInput(Unit) {
                   detectSpatialDragGesture(context) { dragValue ->
                       // We will come back later to this part.
                   }
               },
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-planets.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "Planets", bundle = bundle)
                   .apply {
                       // Move the entire scene to a proper position with original scale
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(1f)
                           position = Vector3(0f, 1.5f, -1f)
                       }
                   }
   
               bundle.close()
   
               content.addEntity(entity)
   
               val lightEntity = Entity().apply {
                   components.set(DirectionalLightComponent(
                       Color(0xFFFFFFFF).toColor4(),
                       500f))
               }
   
               content.addEntity(lightEntity)
           },
       )
   }
   ```

   上述代码主要执行了以下操作：
   * 删除与旧场景相关的代码（光照部分除外）。
   * 初始化名为 `Planets` 的新场景，并将其添加到空间中。
   * 使用 `TransformComponent` 将整个场景放置在 `(0f, 1.5f, -1f)` 坐标处。
3. 运行应用。你会看到新的场景。

## 设置交互条件
在新场景中，你需要让每个行星都能被单独交互。为此，你要先在场景的根节点中找到每个行星的 `Entity`，然后为其添加碰撞体和可交互组件。为避免重复编码，你可以将组件设置逻辑提取出来，定义一个 `Entity` 的扩展函数 `enableInteraction()`。对所有行星使用一个与它们自身大小相同的球形作为碰撞体形状。然后，在场景初始化的时候，通过名称找到不同的行星，调用上面的函数来为它们添加必要的组件。

1. 使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.graphics.Color
   import androidx.compose.ui.input.pointer.pointerInput
   import androidx.compose.ui.platform.LocalContext
   import com.pico.spatial.core.ecs.DirectionalLightComponent
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.foundation.content.SpatialView
   import com.pico.spatial.ui.foundation.content.toColor4
   import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
   import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   import com.pico.spatial.core.ecs.CollisionComponent
   import com.pico.spatial.core.ecs.HoverEffectComponent
   import com.pico.spatial.core.ecs.InteractableComponent
   import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
   import com.pico.spatial.core.ecs.resource.ShapeResource
   
   private fun Entity.enableInteraction() {
       val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
   
       // Use a sphere as collision
       val collisionComponent = CollisionComponent(
           collisionShape = listOf(ShapeResource.createSphere(boundingBox.size.x / 2f)),
           physicsMaterial = PhysicsMaterialResource(),
       )
   
       components.set(collisionComponent)
   
       // Set interactable component
       components.set(InteractableComponent())
   
       // Set HoverEffect component
       components.set(HoverEffectComponent())
   }
   
   @Composable
   fun HomeStage() {
       val context = LocalContext.current
       val converter = LocalPhysicalLengthConverter.current
       val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
   
       SpatialView(
           Modifier
               .pointerInput(Unit) {
                   detectSpatialDragGesture(context) { dragValue ->
                       // We will come back later to this part.
                   }
               },
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-planets.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "Planets", bundle = bundle)
                   .apply {
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(1f)
                           position = Vector3(0f, 1.5f, -1.5f)
                       }
   
                       planets.forEach {
                           findEntity(it)?.enableInteraction()
                       }
   
                   }
   
               bundle.close()
   
               content.addEntity(entity)
   
               val lightEntity = Entity().apply {
                   components.set(DirectionalLightComponent(
                       Color(0xFFFFFFFF).toColor4(),
                       500f))
               }
   
               content.addEntity(lightEntity)
           },
       )
   }
   ```

2. 打开 PICO Emulator，在 **设置** 面板的 **调试** 页面勾选 **碰撞包围盒**。然后在 PICO Emulator 中运行空间应用，检查物体的碰撞组件和交互组件是否被正确设置。关于 **调试** 页面的详细用法，参考 [《UI 调试》](./spatial-toolkit_pico-emulator_ui-调试.md)。

   你会发现，设置的碰撞体与行星模型没有正确对齐，而是整体偏下。出现这个现象的原因是，Spatial Editor 中所有行星模型的原点都位于其底部。当你添加碰撞体时，系统会默认将碰撞体的中心与模型的原点对齐，因此造成了你看到的偏移。
3. 在 PICO Emulator **设置** 面板的 **调试** 页面勾选 **坐标轴**。

   你会发现，模型的原点位于其底部。为了修正这个问题，你需要更新代码，将碰撞体的位置移动到模型的中心点。

4. 使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
   更新后的 `enableInteraction()` 函数从`boundingBox.center`的获取模型的中心点位置，然后将用来创建碰撞体形状的球形移动到该位置。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.graphics.Color
   import androidx.compose.ui.input.pointer.pointerInput
   import androidx.compose.ui.platform.LocalContext
   import com.pico.spatial.core.ecs.DirectionalLightComponent
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.foundation.content.SpatialView
   import com.pico.spatial.ui.foundation.content.toColor4
   import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
   import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   import com.pico.spatial.core.ecs.CollisionComponent
   import com.pico.spatial.core.ecs.HoverEffectComponent
   import com.pico.spatial.core.ecs.InteractableComponent
   import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
   import com.pico.spatial.core.ecs.resource.ShapeResource
   
   private fun Entity.enableInteraction() {
       val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
       val centerOffset = boundingBox.center
   
       // Use a sphere as collision
       val collisionComponent = CollisionComponent(
           collisionShape = listOf(
               ShapeResource
                   .createSphere(boundingBox.size.x / 2f)
                   .offsetByTranslation(centerOffset)
           ),
           physicsMaterial = PhysicsMaterialResource(),
       )
   
       components.set(collisionComponent)
   
       // Set interactable component
       components.set(InteractableComponent())
   
       // Set HoverEffect component
       components.set(HoverEffectComponent())
   }
   
   @Composable
   fun HomeStage() {
       val context = LocalContext.current
       val converter = LocalPhysicalLengthConverter.current
       val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
   
       SpatialView(
           Modifier
               .pointerInput(Unit) {
                   detectSpatialDragGesture(context) { dragValue ->
                       // We will come back later to this part.
                   }
               },
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-planets.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "Planets", bundle = bundle)
                   .apply {
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(1f)
                           position = Vector3(0f, 1.5f, -1.5f)
                       }
   
                       planets.forEach {
                           findEntity(it)?.enableInteraction()
                       }
   
                   }
   
               bundle.close()
   
               content.addEntity(entity)
   
               val lightEntity = Entity().apply {
                   components.set(DirectionalLightComponent(
                       Color(0xFFFFFFFF).toColor4(),
                       500f))
               }
   
               content.addEntity(lightEntity)
           },
       )
   }
   ```

5. 再次在 PICO Emulator 中运行应用，你将看到模型的碰撞体已与模型本身的形状对齐。

# 第二步：实现复合交互
在第一阶段，你学习了如何与单个物体进行交互。第二阶段将在此基础上，介绍更加复杂的交互场景与技巧，即“复合交互”。
与单一物体的交互相比，复合交互主要包含两个方面：

* 与多个物体进行交互
* 对同一个物体应用多种交互方式

## 和多个物体进行交互
默认情况下，只要你为 `SpatialView` 中的物体设置了可交互条件，用户就可以通过 `detectSpatial` 系列接口与之交互。
回顾上一阶段的教程，你实现的 `detectSpatialDragGesture` 拖拽逻辑会根据 `dragValue.targetEntity` 确定用户正在拖拽的物体，并修改其 `Transform` 来实现移动。由于这套逻辑是通用的，它在当前的多行星场景中依然生效，因此你无需修改代码就能拖拽所有行星。

从与单个物体交互扩展到与多个物体交互，通常无需修改代码。但在实际场景中，你可能需要更精确地控制哪些物体可以响应交互。为此，所有以 `detectSpatial` 开头的接口都提供了一个 `targetedToEntity` 参数。它的默认值为 `null`，表示手势将作用于场景中所有可交互的物体。当你为该参数提供一个 `TargetEntity` 值后，就可以将交互范围限定在指定的物体上，从而实现更灵活的控制。
`TargetEntity` 的常见用法主要分为以下两种：

* 通过 `TargetEntity.hit()` 接口，开发者可以将交互限制在某个特定实体及其层级树下的所有子节点。例如，当前场景中，我们希望用户的拖拽手势仅对左侧四个行星生效，让接受交互事件的物体仅仅限制在`Group1`节点下的物体。我们并不需要改变`detectSpatialDragGesture`中的逻辑，只需通过`TargetEntity.hit()`来添加`targetedToEntity`指向的物体范围。
   你可以使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.graphics.Color
   import androidx.compose.ui.input.pointer.pointerInput
   import androidx.compose.ui.platform.LocalContext
   import androidx.compose.runtime.mutableStateOf
   import androidx.compose.runtime.remember
   import androidx.compose.runtime.getValue
   import androidx.compose.runtime.setValue
   import com.pico.spatial.core.ecs.DirectionalLightComponent
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.foundation.content.SpatialView
   import com.pico.spatial.ui.foundation.content.toColor4
   import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
   import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
   import com.pico.spatial.ui.foundation.gesture.TargetEntity
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   import com.pico.spatial.core.ecs.CollisionComponent
   import com.pico.spatial.core.ecs.HoverEffectComponent
   import com.pico.spatial.core.ecs.InteractableComponent
   import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
   import com.pico.spatial.core.ecs.resource.ShapeResource
   import com.pico.spatial.ui.platform.LengthUnit
   
   
   private fun Entity.enableInteraction() {
       val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
       val centerOffset = boundingBox.center
   
       // Use a sphere as collision
       val collisionComponent = CollisionComponent(
           collisionShape = listOf(
               ShapeResource
                   .createSphere(boundingBox.size.x / 2f)
                   .offsetByTranslation(centerOffset)
           ),
           physicsMaterial = PhysicsMaterialResource(),
       )
   
       components.set(collisionComponent)
   
       // Set interactable component
       components.set(InteractableComponent())
   
       // Set HoverEffect component
       components.set(HoverEffectComponent())
   }
   
   @Composable
   fun HomeStage() {
       val context = LocalContext.current
       val converter = LocalPhysicalLengthConverter.current
       val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
       var group1: Entity? by remember { mutableStateOf<Entity?>(null) }
   
       SpatialView(
           Modifier
               .pointerInput(Unit) {
                   detectSpatialDragGesture(
                       context,
                       targetedToEntity = group1?.let {  TargetEntity.hit(it) }
                   ) { dragValue ->
                       // Convert drag offset into Meters.
                       val offsetXInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.x.toDp(), LengthUnit.Meters)
                       }
                       val offsetYInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.y.toDp(), LengthUnit.Meters)
                       }
                       val offsetZInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.z.toDp(), LengthUnit.Meters)
                       }
   
                       // Update the position of the Earth by offset in meters.
                       dragValue.targetEntity?.apply {
                           components[TransformComponent::class.java]?.apply {
                               setPosition(
                                   Vector3(
                                       position.x + offsetXInMeter,
                                       position.y - offsetYInMeter,
                                       position.z + offsetZInMeter,
                                   )
                               )
                           }
                       }
                   }
               },
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-planets.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "Planets", bundle = bundle)
                   .apply {
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(1f)
                           position = Vector3(0f, 1.5f, -1.5f)
                       }
   
                       planets.forEach {
                           findEntity(it)?.enableInteraction()
                       }
   
                       group1 = findEntity("Group1")
   
                   }
   
               bundle.close()
   
               content.addEntity(entity)
   
               val lightEntity = Entity().apply {
                   components.set(DirectionalLightComponent(
                       Color(0xFFFFFFFF).toColor4(),
                       500f))
               }
   
               content.addEntity(lightEntity)
           },
       )
   }
   ```

     运行应用后可以看到，只有左边四个行星是可以被拖动的，而右边的四个不行。

* 如果你需要根据特定条件筛选可交互的物体，可以使用 `TargetEntity.any()`。这种方式非常灵活，允许你通过传入一个逻辑判断来批量指定交互目标。例如，要实现仅允许拖拽地球（Earth）和火星（Mars），你可以提供一个条件，使交互只对这两个特定名称的物体生效。
   你可以使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.graphics.Color
   import androidx.compose.ui.input.pointer.pointerInput
   import androidx.compose.ui.platform.LocalContext
   import androidx.compose.runtime.mutableStateOf
   import androidx.compose.runtime.remember
   import androidx.compose.runtime.getValue
   import androidx.compose.runtime.setValue
   import com.pico.spatial.core.ecs.DirectionalLightComponent
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.foundation.content.SpatialView
   import com.pico.spatial.ui.foundation.content.toColor4
   import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
   import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
   import com.pico.spatial.ui.foundation.gesture.TargetEntity
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   import com.pico.spatial.core.ecs.CollisionComponent
   import com.pico.spatial.core.ecs.HoverEffectComponent
   import com.pico.spatial.core.ecs.InteractableComponent
   import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
   import com.pico.spatial.core.ecs.resource.ShapeResource
   import com.pico.spatial.ui.platform.LengthUnit
   
   
   private fun Entity.enableInteraction() {
       val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
       val centerOffset = boundingBox.center
   
       // Use a sphere as collision
       val collisionComponent = CollisionComponent(
           collisionShape = listOf(
               ShapeResource
                   .createSphere(boundingBox.size.x / 2f)
                   .offsetByTranslation(centerOffset)
           ),
           physicsMaterial = PhysicsMaterialResource(),
       )
   
       components.set(collisionComponent)
   
       // Set interactable component
       components.set(InteractableComponent())
   
       // Set HoverEffect component
       components.set(HoverEffectComponent())
   }
   
   @Composable
   fun HomeStage() {
       val context = LocalContext.current
       val converter = LocalPhysicalLengthConverter.current
       val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
       var group1: Entity? by remember { mutableStateOf<Entity?>(null) }
   
       SpatialView(
           Modifier
               .pointerInput(Unit) {
                   detectSpatialDragGesture(
                       context,
                       targetedToEntity = TargetEntity.any {
                           it.getName() == "Earth" || it.getName() == "Mars"
                       }
                   ) { dragValue ->
                       // Convert drag offset into Meters.
                       val offsetXInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.x.toDp(), LengthUnit.Meters)
                       }
                       val offsetYInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.y.toDp(), LengthUnit.Meters)
                       }
                       val offsetZInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.z.toDp(), LengthUnit.Meters)
                       }
   
                       // Update the position of the Earth by offset in meters.
                       dragValue.targetEntity?.apply {
                           components[TransformComponent::class.java]?.apply {
                               setPosition(
                                   Vector3(
                                       position.x + offsetXInMeter,
                                       position.y - offsetYInMeter,
                                       position.z + offsetZInMeter,
                                   )
                               )
                           }
                       }
                   }
               },
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-planets.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "Planets", bundle = bundle)
                   .apply {
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(1f)
                           position = Vector3(0f, 1.5f, -1.5f)
                       }
   
                       planets.forEach {
                           findEntity(it)?.enableInteraction()
                       }
   
                       group1 = findEntity("Group1")
   
                   }
   
               bundle.close()
   
               content.addEntity(entity)
   
               val lightEntity = Entity().apply {
                   components.set(DirectionalLightComponent(
                       Color(0xFFFFFFFF).toColor4(),
                       500f))
               }
   
               content.addEntity(lightEntity)
           },
       )
   }
   ```

   运行应用，可以发现整个场景中只有地球（Earth）和火星（Mars）可以被拖动。

## 使用多种方式进行交互
在实际开发中，一个物体通常需要响应多种交互方式。例如，你可能希望让行星既可以被“单手拖拽”，又可以被“双手缩放”。
要实现这种复合交互，你必须为每种手势分别设置一个 `Modifier.pointerInput` 修饰符。
切勿在同一个 `pointerInput` 代码块中调用多个 `detectSpatial` 系列的函数。PICO Spatial SDK 的`detectSpatial`函数会相互阻塞，如果放在一起，将导致手势识别失效。

在接下来的教程中，你将移除之前添加的 `TargetEntity` 逻辑，让所有行星都可以被交互。然后，你会再添加一个 `pointerInput` 来响应缩放手势，它会根据用户手部的位移计算缩放比例，并更新到相应物体的 `TransformComponent` 上。
你可以使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
```Kotlin
package com.pico.spatial.tutorial.interaction.content

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import com.pico.spatial.core.ecs.DirectionalLightComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.toColor4
import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.HoverEffectComponent
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.ui.platform.LengthUnit
// [Add] 增加 import
import com.pico.spatial.ui.foundation.gesture.detectSpatialScaleGesture


private fun Entity.enableInteraction() {
    val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
    val centerOffset = boundingBox.center

    // Use a sphere as collision
    val collisionComponent = CollisionComponent(
        collisionShape = listOf(
            ShapeResource
                .createSphere(boundingBox.size.x / 2f)
                .offsetByTranslation(centerOffset)
        ),
        physicsMaterial = PhysicsMaterialResource(),
    )

    components.set(collisionComponent)

    // Set interactable component
    components.set(InteractableComponent())

    // Set HoverEffect component
    components.set(HoverEffectComponent())
}

@Composable
fun HomeStage() {
    val context = LocalContext.current
    val converter = LocalPhysicalLengthConverter.current
    val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    SpatialView(
        Modifier
            .pointerInput(Unit) {
                detectSpatialDragGesture(context) { dragValue ->
                    // Convert drag offset into Meters.
                    val offsetXInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.x.toDp(), LengthUnit.Meters)
                    }
                    val offsetYInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.y.toDp(), LengthUnit.Meters)
                    }
                    val offsetZInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.z.toDp(), LengthUnit.Meters)
                    }

                    // Update the position of the Earth by offset in meters.
                    dragValue.targetEntity?.apply {
                        components[TransformComponent::class.java]?.apply {
                            setPosition(
                                Vector3(
                                    position.x + offsetXInMeter,
                                    position.y - offsetYInMeter,
                                    position.z + offsetZInMeter,
                                )
                            )
                        }
                    }
                }
            }
            // [Add] 新增缩放手势的 pointerInput
            .pointerInput(Unit) {
            detectSpatialScaleGesture(context) { scaleValue ->
                // Update the scale of the Earth according to the scale value
                scaleValue.targetEntity?.apply {
                    components[TransformComponent::class.java]?.apply {
                        setScaleVector(scaleVector * scaleValue.scaleValue)
                    }
                }

            }
        },
        initial = { content, attachments ->
            val bundle = withContext(Dispatchers.IO) {
                AssetBundle.load("asset://editor-planets.bundle")
            }

            val entity = Entity.loadSuspend(
                modelName = "Planets", bundle = bundle)
                .apply {
                    components[TransformComponent::class.java]?.apply {
                        scaleVector = Vector3(1f)
                        position = Vector3(0f, 1.5f, -1.5f)
                    }

                    planets.forEach {
                        findEntity(it)?.enableInteraction()
                    }
                }

            bundle.close()

            content.addEntity(entity)

            val lightEntity = Entity().apply {
                components.set(DirectionalLightComponent(
                    Color(0xFFFFFFFF).toColor4(),
                    500f))
            }

            content.addEntity(lightEntity)
        },
    )
}
```

运行应用，你将看到如下效果：

PICO Emulator 也可以模拟双手操作模式。在双手模拟模式下，鼠标代表第一只手，第二只手的位置与第一只手以窗口中心为对称点。你可拖动鼠标控制二者的距离与方向来控制两只手的位置。 点击鼠标左键模拟两只手同时捏合，拖动鼠标模拟两只手的位置移动，释放鼠标左键则模拟两只手同时释放捏合。

* Windows系统：使用组合键 Ctrl + Shift 可以切换至双手模拟。
* macOS系统：使用组合键 Control + Shift 可以切换至双手模拟。

详情参阅《[用户界面指引](/document/spatial-toolkit/pico-emulator-ui/)》。

# 总结
恭喜你完成了本阶段的教程。
在本阶段的教程中，你已经学习了如何实现更复杂的交互场景，包括：

* 如何与场景中的多个物体进行交互。
* 如何对同一个物体实现多种不同的交互方式。

# 接下来
在下一阶段的教程中，你将学习如何实现更自然的交互：通过单手拨动使行星自然旋转，带来更真实的物理交互体验。详情参阅《[第三阶段：实现更自然的交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第三阶段：实现更自然的交互.md)》。

