# 开始之前
## **你要实现什么**
通过这一阶段的上手实践，你将在空间中展示一个地球模型，并且和它进行最基本的交互。

* 当视线或射线扫过地球时，它会亮起边缘光晕（高亮提示）。
* 单手捏合拖拽它，你可以将地球抓起，在空间中自由拖拽平移。

## **你将学习什么**

* 理解空间交互的三大前提：碰撞体（Collision）、可交互组件（Interactable）与视觉反馈。
* 为三维物体添加不同类型的碰撞体，并权衡包围盒（Bounding Box）与网格（Mesh）的优缺点。
* 使用 `detectSpatialDragGesture()` 处理空间拖拽手势。
* 进行空间坐标系的单位换算（像素转米）与轴向映射。

## **你将需要什么**

* 配置完成的 PICO Spatial SDK 开发环境，包括 Android Studio 2025.1.x 和 PICO 空间应用开发工具（PICO Spatial Plugin、PICO Spatial Editor 和 PICO Emulator）。详情参阅《[第一步：准备开发环境](/document/spatial-sdk/set-up-development-environment)》。
* PICO 设备或 PICO Emulator。
* **预计耗时：**约 45 分钟。

# 第一步：在空间内展示模型
为了完成我们本章节中要实现的场景，第一步我们需要将地球模型展示到空间应用中。
## 创建空间应用

1. 打开 Android Studio。你可以点击主界面上的 **New Spatial Project** 按钮，或从顶部菜单栏选择 **File** > **New** > **New Spatial Project...**。

2. 在**New Project** 窗口，选择 **Full Stage** 类型的模板，然后点击 **Next** 按钮。**Full Stage** 类型的模板可以让用户随心所欲地在整个空间中和模型进行交互。

3. 设置项目的名称、包名、存储位置、PICO OS 6 的最低版本，然后点击 **Finish** 按钮。
   教程使用以下项目名称和包名。
      * **Name:** `SpatialInteraction`
      * **Package name:** `com.pico.spatial.tutorial.interaction`

## 添加地球模型
首先，把地球模型工程文件放到 Spatial 项目中。

1. 在 Android 视图中，在 **app** 上点击右键弹出菜单，然后选择 **New** > **Directory**，创建`src/main/assets`目录。

2. 将下面的`editor-asset-earth-pack.bundle`文件移动到创建的目录中。
   <a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bbd7b4cfbfd8479d8dc1d2f1cbda18de~tplv-goo7wpa0wc-image.image" filename="editor-asset-earth-pack.bundle" download>editor-asset-earth-pack.bundle</a>

## 展示地球模型
`com/pico/spatial/tutorial/interaction/content/HomeStage.kt` 包含了你创建的 Stage 空间容器的展示逻辑。你需要通过编辑 `HomeStage.kt`来展示地球模型。

1. 使用下面的代码覆盖`HomeStage.kt`中的内容。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.ui.foundation.content.SpatialView
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   
   @Composable
   fun HomeStage() {
       SpatialView(
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-asset-earth-pack.bundle")
               }
               
               val entity = Entity.loadSuspend(
                   modelName = "earth_outline", bundle = bundle)
               
               bundle.close()
   
               content.addEntity(entity)
           },
       )
   }
   ```

   在上面的代码中：
   * 删除了 `HomeStage.kt` 中的模板内容，仅保留 `SpatialView`。
   * 使用 `AssetBundle` 接口将模型加载到内存中。最后，调用 `content.addEntity()` 方法，将 `entity` 添加到 `SpatialView` 的内容节点上，以将其在用户面前展示出来。
   * `editor-asset-earth-pack.bundle`文件是一个打包的 Spatial Editor 项目。在这个 Spatial Editor 项目中，地球的场景名为`earth_outline`。代码中使用`Entity.loadSuspend()`加载 `earth_outline`并将其赋值给`entity`对象，然后关闭`bundle`对象来释放内存空间。关于 Spatial Editor 项目的更多信息，参考《[管理 Spatial Editor 项目](/document/spatial-toolkit/spatial-editor-project-management/)》。
   及时释放不用的`AssetBundle`对象是空间应用开发中的良好习惯，具体细节可以参考《[AssetBundle](./spatial-sdk_资源管理_assetbundle.md)》。

2. 运行空间应用。
   你会发现地球模型没有出现在正前方，而是位于你的脚下。这并非代码错误。向下调整视角，即可看到地球。

   之所以模型会出现在你的脚下，是因为在 Full Space 模式中，`SpatialView` 的坐标原点位于你的头显正下方（靠近脚底），而非像共享空间模式那样位于组件的中心。

## 调整模型位置和尺寸
为了将模型调整至你的视野前方并设置合适的大小，你需要修改 `HomeStage.kt` 文件。在加载 `Entity` 后，你需要访问其 `TransformComponent`，将模型缩小为原始尺寸的 0.15 倍，并将其移动到视野中心的位置 `Vector3(0f, 1.5f, -2f)`。

1. 使用下面的代码覆盖`HomeStage.kt`中的内容。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.ui.foundation.content.SpatialView
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   // [Add] 添加 import
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.math.Vector3
   
   @Composable
   fun HomeStage() {
       SpatialView(
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-asset-earth-pack.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "earth_outline", bundle = bundle)
                   // [Add] 调整模型位置和尺寸
                   .apply {
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(0.15f)
                           position = Vector3(0f, 1.5f, -2f)
                       }
                   }
               bundle.close()
   
               content.addEntity(entity)
           },
       )
   }
   ```

2. 运行空间应用。现在，地球会清晰地呈现在你的视野前方。

## 调整光照
你选择的 Full Stage 模板默认在 Full Space 模式下运行。在 Full Space 模式下，所有光照都必须由应用自身提供。因此，模型可能会因缺少环境光而显得较暗。为了让模型更亮，你可以：

* 将 Stage Style 切换到 `Mixed` 模式。此模式允许真实环境光照亮虚拟物体，使其更自然地融入现实空间。
* 添加动态光照，弥补周围环境光亮度不足的情况。
1. 打开 `app/src/AndroidManifest.xml` 文件，找到 `pico.spatial.stage.style` 项，并将其值从 `3` 改为 `1`。
   ```XML
   <!--Update from 3 to 1-->
   <meta-data
       android:name="pico.spatial.stage.style"
       android:value="1" />
   ```

2. 使用下面的代码覆盖`HomeStage.kt`中的内容。
   下面的代码在场景中创建一个新的 `Entity`，并为其设置 `DirectionalLightComponent` 组件，以添加一道强度为 500 流明的白色平行光来照亮模型。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.ui.foundation.content.SpatialView
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.math.Vector3
   // [Add] 添加 import
   import com.pico.spatial.core.ecs.DirectionalLightComponent
   import androidx.compose.ui.graphics.Color
   import com.pico.spatial.ui.foundation.content.toColor4
   
   @Composable
   fun HomeStage() {
       SpatialView(
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-asset-earth-pack.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "earth_outline", bundle = bundle)
                   .apply {
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(0.15f)
                           position = Vector3(0f, 1.5f, -2f)
                       }
                   }
               bundle.close()
   
               content.addEntity(entity)
               // [Add] 添加动态光照
               val lightEntity = Entity().apply {
                   components.set(
                       DirectionalLightComponent(
                           Color(0xFFFFFFFF).toColor4(),
                           500f
                       )
                   )
               }
               content.addEntity(lightEntity)
           },
       )
   }
   ```

3. 再次运行应用，一个清晰明亮的地球模型就会呈现在你的眼前。

# 第二步：添加物体交互条件
在空间应用中，一个三维物体（`Entity`）并非天生就具备交互能力。为了兼顾用户体验和系统性能，一个物体必须同时满足以下两个条件，才能响应用户的操作：

* **添加碰撞体** (`CollisionComponent`)：默认情况下，三维物体仅是一个“可见但不可触碰”的视觉外壳。你必须为其添加 `CollisionComponent` 来定义其物理边界，这样用户的视线、射线或手部才能“接触”到它。
* **添加可交互组件** (`InteractableComponent`)：拥有碰撞体只意味着物体可以被“碰到”，但这不代表它能响应交互。你还必须为其添加 `InteractableComponent`。该组件就像一个开关，负责接收并处理手势、射线等交互事件。

当你将一个 `Entity` 添加到 `SpatialView` 后，它默认不包含这两个组件，你需要通过代码手动为它添加，才能实现完整的交互功能。
## 设置碰撞体组件
你需要通过 `CollisionComponent` 来定义物体的碰撞属性，它主要包含以下两个核心元素：

* **碰撞几何体** (`ShapeResource`)：定义了物体在物理空间中的实际边界，也就是可交互的触碰区域。创建碰撞几何体通常有两种方式：
   * **使用包围盒** (`BoundingBox`)：根据物体的大致边界（如球体或立方体）来创建碰撞体。这种方式计算开销极小，性能表现出色。但缺点是碰撞边界与模型精细的视觉外观可能不完全贴合，导致交互体验不够细腻。
   * **使用网格** (`Mesh`)：直接使用模型自身的几何网格作为碰撞体。这种方式能让用户精确地触碰到模型的每一个表面细节，交互体验非常真实自然。但由于模型网格通常由大量三角面构成，进行碰撞检测时会消耗更多计算资源，性能开销更高。
* **物理材质** (`PhysicsMaterialResource`)：决定了物体在物理引擎中的表现，例如摩擦力、弹力等。由于本教程的交互主要关注用户手势和射线的检测，而非复杂的物理模拟，因此物理材质的配置影响不大，使用默认值即可。

针对本教程中使用的地球模型，下图分别展示了上述两种方法设置的碰撞体。图中绿色线条圈出的区域即代表该物体实际生效的碰撞边界。

<strong>根据包围盒大小设置球形碰撞体</strong>

<strong>用地球模型的 Mesh 设置的碰撞体</strong>

对于地球模型这样的规则球体，使用 `BoundingBox` 创建碰撞体是更高效的选择。虽然使用 `Mesh` 也能创建碰撞体，但它会生成一个由多个多边形拼接而成的复杂形状，不必要地增加了系统开销。在本例中，两种方法在交互范围和视觉效果上几乎没有区别，因此我们选择性能更优的 `BoundingBox` 来创建球形碰撞体。
使用下面的代码覆盖`HomeStage.kt`中的内容。下面的代码使用 `BoundingBox` 为模型添加了碰撞体。
```Kotlin
package com.pico.spatial.tutorial.interaction.content

import androidx.compose.runtime.Composable
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.ui.foundation.content.SpatialView
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.core.ecs.DirectionalLightComponent
import androidx.compose.ui.graphics.Color
import com.pico.spatial.ui.foundation.content.toColor4
// [Add] 添加 import
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource

@Composable
fun HomeStage() {
    SpatialView(
        initial = { content, attachments ->
            val bundle = withContext(Dispatchers.IO) {
                AssetBundle.load("asset://editor-asset-earth-pack.bundle")
            }

            val entity = Entity.loadSuspend(
                modelName = "earth_outline", bundle = bundle)
                .apply {
                    components[TransformComponent::class.java]?.apply {
                        scaleVector = Vector3(0.15f)
                        position = Vector3(0f, 1.5f, -2f)
                    }
                    // [Add] 使用 BoundingBox 为模型添加碰撞体。
                    val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
                    val collisionComponent = CollisionComponent(
                        collisionShape = listOf(ShapeResource.createSphere(boundingBox.size.x / 2f)),
                        physicsMaterial = PhysicsMaterialResource(),
                    )
                    components.set(collisionComponent)
                }

            bundle.close()

            content.addEntity(entity)
            // [Add] 添加动态光照
            val lightEntity = Entity().apply {
                components.set(
                    DirectionalLightComponent(
                        Color(0xFFFFFFFF).toColor4(),
                        500f
                    )
                )
            }
            content.addEntity(lightEntity)
        },
    )
}
```

## 设置可交互组件
为三维物体添加可交互组件是一个简单但容易被忽略的步骤。你只需将 `InteractableComponent` 添加到该物体上即可。

1. 使用下面的代码覆盖`HomeStage.kt`中的内容。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.ui.foundation.content.SpatialView
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.core.ecs.DirectionalLightComponent
   import androidx.compose.ui.graphics.Color
   import com.pico.spatial.ui.foundation.content.toColor4
   import com.pico.spatial.core.ecs.CollisionComponent
   import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
   import com.pico.spatial.core.ecs.resource.ShapeResource
   // [Add] 添加 import
   import com.pico.spatial.core.ecs.InteractableComponent
   
   @Composable
   fun HomeStage() {
       SpatialView(
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-asset-earth-pack.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "earth_outline", bundle = bundle)
                   .apply {
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(0.15f)
                           position = Vector3(0f, 1.5f, -2f)
                       }
                       val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
   
                       val collisionComponent = CollisionComponent(
                           collisionShape = listOf(ShapeResource.createSphere(boundingBox.size.x / 2f)),
                           physicsMaterial = PhysicsMaterialResource(),
                       )
   
                       components.set(collisionComponent)
                       // [Add] 设置可交互组件
                       components.set(InteractableComponent())
                   }
   
               bundle.close()
   
               content.addEntity(entity)
               val lightEntity = Entity().apply {
                   components.set(
                       DirectionalLightComponent(
                           Color(0xFFFFFFFF).toColor4(),
                           500f
                       )
                   )
               }
               content.addEntity(lightEntity)
           },
       )
   }
   ```

2. 打开 PICO Emulator，在 **设置** 面板的 **调试** 页面勾选 **碰撞包围盒**。然后在 PICO Emulator 中运行空间应用，检查物体的碰撞组件和交互组件是否被正确设置。关于 **调试** 页面的详细用法，参考 [《UI 调试》](./spatial-toolkit_pico-emulator_ui-调试.md)。

   如果碰撞组件设置正确，物体的碰撞体形状会由绿色的线条展示。如果可交互组件设置正确，当光标移动到物体表面上，物体的碰撞体形状会变成粉色。

## 增加物体交互提示
为了让用户明确正在与哪个物体交互，提供清晰的视觉反馈至关重要。
在空间应用中，除了直接用手触摸，“眼手协同”是一种更常见、高效的交互方式。它指的是用你的视线瞄准一个物体，然后通过手势与其交互。这种方式无需大幅度的肢体动作，交互体验更舒适流畅。
为了让用户知道视线当前正聚焦于哪个物体，你需要提供一个明确的视觉提示。只需为物体添加 `HoverEffectComponent` 组件，即可轻松实现高亮效果：当用户的视线落在物体上时，它会自动亮起。

1. 使用下面的代码覆盖`HomeStage.kt`中的内容。

```Kotlin
package com.pico.spatial.tutorial.interaction.content

import androidx.compose.runtime.Composable
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.ui.foundation.content.SpatialView
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.core.ecs.DirectionalLightComponent
import androidx.compose.ui.graphics.Color
import com.pico.spatial.ui.foundation.content.toColor4
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.core.ecs.InteractableComponent
// [Add] 添加 import
import com.pico.spatial.core.ecs.HoverEffectComponent

@Composable
fun HomeStage() {
    SpatialView(
        initial = { content, attachments ->
            val bundle = withContext(Dispatchers.IO) {
                AssetBundle.load("asset://editor-asset-earth-pack.bundle")
            }

            val entity = Entity.loadSuspend(
                modelName = "earth_outline", bundle = bundle)
                .apply {
                    components[TransformComponent::class.java]?.apply {
                        scaleVector = Vector3(0.15f)
                        position = Vector3(0f, 1.5f, -2f)
                    }
                    val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)

                    val collisionComponent = CollisionComponent(
                        collisionShape = listOf(ShapeResource.createSphere(boundingBox.size.x / 2f)),
                        physicsMaterial = PhysicsMaterialResource(),
                    )

                    components.set(collisionComponent)
                    components.set(InteractableComponent())
                    // [Add] 添加交互高亮提示
                    components.set(HoverEffectComponent())
                }

            bundle.close()

            content.addEntity(entity)
            val lightEntity = Entity().apply {
                components.set(
                    DirectionalLightComponent(
                        Color(0xFFFFFFFF).toColor4(),
                        500f
                    )
                )
            }
            content.addEntity(lightEntity)
        },
    )
}
```


2. 运行空间应用。如果你已正确设置碰撞体和可交互组件，当用户和物体有交互时，物体就会被白色的光晕包围。

   需要注意的是，高亮效果的轮廓是由物体自身的模型形状决定的，而可交互的范围则由其碰撞体决定。因此，即便你为地球模型设置一个立方体碰撞体，其高亮效果依然是球形。下面的视频展示了这一点：虽然物体的碰撞体是立方体，但高亮效果仍然是球形。

# 第三步：和物体进行交互
为 3D 物体设置好交互所需的基础条件后，你就可以添加具体的交互功能，让用户能够真正地与物体互动。
## 物体交互动作
为了覆盖空间计算中常见的用户操作，PICO Spatial SDK 提供了一系列以 `detectSpatial` 开头的基础交互函数。这些函数构成了空间交互逻辑的基础，能够精准捕获并响应用户的各种操作意图。详情参阅《[3D 物体的基础交互](./spatial-sdk_交互_3d-物体的基础交互.md)》。
| **交互手势** | **示意图** | **具体操作** | **使用接口** |
| --- | --- | --- | --- |
| **点击** |  | 单手两指迅速并拢再略微张开，做出捏物体的操作 | `detectSpatialTapGesture()` |
| **拖拽** |  | 单手两指并拢，捏住物体上的一点，然后在空间中移动 ;   | `detectSpatialDragGesture()` |
| **缩放** |  | 双手捏住物体上的两个点，然后双手靠近或者远离 | `detectSpatialScaleGesture()` |
| **旋转** |  | 双手捏住物体上的两个点，然后双手同时顺时针或者逆时针旋转 | `detectSpatialRotateGesture()` |
当开发者完成了物体基础交互组件的配置后，当需要实现具体的交互功能时，你需在承载三维物体的 `SpatialView` 上挂载相应的 `Modifier`，用来监听并捕获用户的交互事件。你可以沿用 Jetpack Compose 标准的 `Modifier.pointerInput` 来统一监听用户输入（包括眼动、手势及手柄）。在 `pointerInput` 的 DSL 内，通过调用上述手势接口，系统会自动对用户的输入进行解析与判断。一旦系统识别出特定的交互动作，便会触发相应的回调函数。
使用下面的代码覆盖`HomeStage.kt`中的内容。下面的代码展示了如何通过挂载 Modifier 监听用户输入并调用手势接口 `detectSpatialDragGesture()`，以实现对用户拖拽手势的响应。
```Kotlin
package com.pico.spatial.tutorial.interaction.content

import androidx.compose.runtime.Composable
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.ui.foundation.content.SpatialView
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.core.ecs.DirectionalLightComponent
import androidx.compose.ui.graphics.Color
import com.pico.spatial.ui.foundation.content.toColor4
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.HoverEffectComponent
// [Add] 添加 import
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture

@Composable
fun HomeStage() {
     // [Add] 添加 context 变量
    val context = LocalContext.current
    SpatialView(
     // [Add] 添加 Modifier.pointerInput 来统一监听用户输入
        Modifier.pointerInput(Unit) {
            detectSpatialDragGesture(context) {
                // Handle your own drag logic here.
                // For example, moving object align with your fingers.
            }
        },
        initial = { content, attachments ->
            val bundle = withContext(Dispatchers.IO) {
                AssetBundle.load("asset://editor-asset-earth-pack.bundle")
            }

            val entity = Entity.loadSuspend(
                modelName = "earth_outline", bundle = bundle)
                .apply {
                    components[TransformComponent::class.java]?.apply {
                        scaleVector = Vector3(0.15f)
                        position = Vector3(0f, 1.5f, -2f)
                    }
                    val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)

                    val collisionComponent = CollisionComponent(
                        collisionShape = listOf(ShapeResource.createSphere(boundingBox.size.x / 2f)),
                        physicsMaterial = PhysicsMaterialResource(),
                    )

                    components.set(collisionComponent)
                    components.set(InteractableComponent())
                    components.set(HoverEffectComponent())
                }

            bundle.close()

            content.addEntity(entity)
            val lightEntity = Entity().apply {
                components.set(
                    DirectionalLightComponent(
                        Color(0xFFFFFFFF).toColor4(),
                        500f
                    )
                )
            }
            content.addEntity(lightEntity)
        },
    )
}
```

## 物体交互效果
完成基础设置后，接下来最关键的一步是构建交互反馈。通过直观的视觉或物理反馈，你可以将零散的交互逻辑整合为用户能够清晰感知的完整体验。
在本场景中，当你拖拽地球时，地球模型会跟随你的手部移动。要实现这种效果，你需要使用 `detectSpatialDragGesture()` 返回的 `dragAmount` 值来实时更新物体在三维空间中的坐标。在实际应用中，你需要处理两个关键的适配问题：

1. **单位换算**：为了与 Jetpack Compose 标准接口保持一致，`dragAmount` 以像素 (px) 为单位返回位移数据。然而，物体的 `TransformComponent` 使用米 (Meters) 作为单位。因此，在更新实体 (Entity) 位置前，你必须先将像素值转换为米。具体换算逻辑请参阅《[长度单位转换](./spatial-sdk_空间数学_长度单位转换.md)》。
2. **坐标系映射**：`dragAmount` 遵循 Compose View 坐标系，而物体的移动发生在空间物理坐标系中。这两个坐标系的 Y 轴方向相反（View 坐标系向下为正，空间坐标系向上为正）。因此，在应用位移时，你必须对 Y 轴的数值取反（即使用 `-dragAmount.y`）。更多细节请参阅《[坐标空间转换](./spatial-sdk_空间数学_坐标空间转换.md)》。

使用下面的代码覆盖`HomeStage.kt`中的内容。以下代码片段展示了如何实现精准的物体随手拖拽效果。
```Kotlin
package com.pico.spatial.tutorial.interaction.content

import androidx.compose.runtime.Composable
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.ui.foundation.content.SpatialView
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.core.ecs.DirectionalLightComponent
import androidx.compose.ui.graphics.Color
import com.pico.spatial.ui.foundation.content.toColor4
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.HoverEffectComponent
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
// [Add] 添加 import
import com.pico.spatial.ui.platform.LengthUnit
import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter

@Composable
fun HomeStage() {
    val context = LocalContext.current
    // [Add] 添加 converter 变量
    val converter = LocalPhysicalLengthConverter.current
    SpatialView(
        Modifier.pointerInput(Unit) {
            // [Update] 构建交互反馈
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
        },
        initial = { content, attachments ->
            val bundle = withContext(Dispatchers.IO) {
                AssetBundle.load("asset://editor-asset-earth-pack.bundle")
            }

            val entity = Entity.loadSuspend(
                modelName = "earth_outline", bundle = bundle)
                .apply {
                    components[TransformComponent::class.java]?.apply {
                        scaleVector = Vector3(0.15f)
                        position = Vector3(0f, 1.5f, -2f)
                    }
                    val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)

                    // Use a sphere as collision
                    val collisionComponent = CollisionComponent(
                        collisionShape = listOf(ShapeResource.createSphere(boundingBox.size.x / 2f)),
                        physicsMaterial = PhysicsMaterialResource(),
                    )

                    components.set(collisionComponent)
                    components.set(InteractableComponent())
                    components.set(HoverEffectComponent())
                }

            bundle.close()

            content.addEntity(entity)
            val lightEntity = Entity().apply {
                components.set(
                    DirectionalLightComponent(
                        Color(0xFFFFFFFF).toColor4(),
                        500f
                    )
                )
            }
            content.addEntity(lightEntity)
        },
    )
}
```

再次运行应用，你将看到最终的拖拽效果：

# 总结
恭喜你完成本阶段的教程。
本阶段的教程覆盖了与空间物体交互的基本流程：

1. 放置物体
2. 设置碰撞体组件
3. 设置可交互组件
4. 添加交互动作
5. 展示交互效果

# 接下来
在下一阶段教程中，你将学习如何实现更复杂的交互逻辑，包括与多个物体交互或对一个物体实现多种交互方式。详情参阅《[第二阶段：从基础交互到复合交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第二阶段：从基础交互到复合交互.md)》。
