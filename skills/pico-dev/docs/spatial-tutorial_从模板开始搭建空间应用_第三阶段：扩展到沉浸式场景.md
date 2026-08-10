# 开始之前
在之前的教程中，你已经学会了如何在 Planar 和 Volumetric 窗口中展示 UI 和 3D 物体。这些窗口如同一个个“带边界的盒子”，将内容限制在固定区域。
现在，我们将打破这些限制，带你认识一个无边界的容器——Stage。
## 你将实现什么
本阶段教程将指导你在《[第二阶段：加入 3D 窗口和模型](./spatial-tutorial_从模板开始搭建空间应用_第二阶段：加入-3d-窗口和模型.md)》的基础上，从主窗口打开一个 Stage，使空间进入 Full Space 状态。
这个 Stage 将包含：

* 一个用于提供沉浸感的天空球。
* 一个简单的地球-卫星系统，其中卫星将环绕地球运动。
* 一个悬浮 UI 面板，你可以用它来：
   * 控制轨道动画的时长（速度）。
   * 打开或关闭主窗口。
   * 退出 Stage。

## 你将学习什么

* Stage 与 WindowContainer 两种空间容器的本质区别。
* Shared Space（共享空间）与 Full Space（全空间）两种空间状态的概念和区别。
* 空间容器和空间状态的联系。
* 如何配置和启动一个 Stage（默认与非默认）。
* 如何使用天空球和环境光照提升场景的真实感和沉浸感。
* 如何在一个 Stage 中布局和管理你的 UI 和 3D 物体。

## 你将需要什么

* 完成 [第一阶段：从平面窗口和 2D 内容开始](./spatial-tutorial_从模板开始搭建空间应用_第一阶段：从平面窗口和-2d-内容开始.md) 和 [第二阶段：加入 3D 窗口和模型](./spatial-tutorial_从模板开始搭建空间应用_第二阶段：加入-3d-窗口和模型.md) 的所有步骤。
* **预计耗时**：约 20 分钟。

---

# 第 1 步：理解 Stage 与空间形态
**目标：**通过 Full Stage 模板，感受 Stage 与 WindowContainer 的差异，理解 Shared Space 与 Full Space 在用户感知上的区别。
在之前的教程中，你已经接触过 Planar 和 Volumetric Window Container 模板。这些模板具有以下共同点：

* **代码结构**：初始内容都包裹在 `DefaultWindowContainer{}` 中。
* **meta-data**：`AndroidManifest.xml` 文件中的元数据都与 `"pico.spatial.windowcontainer"` 属性相关。

这些设置使应用在启动时以窗口（Window Container）的形式呈现。此时，应用处于**共享空间**（Shared Space），即当前空间由所有正在运行的应用共享。在共享空间中，你可以同时运行多个应用的窗口，例如浏览器、聊天工具和视频播放器。只要所有应用都以窗口形式存在，空间就会一直保持在共享状态。

## 操作步骤
**基于 Full Stage 模板新建一个空间应用**
你会发现：

* 应用的初始内容包裹在 `app/src/main/java/.../Main.kt` 文件的 `DefaultStage{}` 中。
* 在 `AndroidManifest.xml` 中配置的 meta-data 都是和 "pico.spatial.stage" 相关的属性。

应用启动后，会通过 Stage 呈现内容，使空间进入 **全空间**（Full Space）状态。你可以将 Stage 理解为一个没有边界、不受裁剪的“场地”，而 Full Space 则意味着当前空间被此应用独占。在 Full Space 状态下，你可以运行一个 Stage（有且仅有一个）和当前应用的多个 Window Container。例如，你可以开启一个 Stage 来展现沉浸式游戏，并同时使用多个 Window Container 作为物品栏、任务页面或聊天窗口。空间状态的切换时机如下：

* 只要 Stage 保持开启，空间就会处于 Full Space 状态。
* 当 Stage 关闭时，空间将恢复为 Shared Space 状态。

当应用使用 Stage 进入 Full Space 状态后，除了内容不再受窗口边界的裁剪外，还与仅使用 WindowContainer 的 Shared Space 状态有以下区别：

* **追踪功能**：头戴显示器（HMD）、手部、手柄等追踪功能仅在 Full Space 状态下可用。
* **环境感知**：空间锚点、空间网格、平面检测等部分环境感知功能仅在 Full Space 状态下可用。
* **坐标空间**：Stage 和 WindowContainer 使用的坐标空间不同，在它们之间传递数据时需要进行转换。
* **环境与光照**：
   * 在 **Shared Space** 中，系统会自动提供环境光照，你也可以调节虚拟环境的沉浸度。
   * 在 **Full Space** 中，系统默认不提供光照和虚拟环境，你必须自行设置天空球或场景模型。
   在 `StageStyle.Full` 模式或 `immersion = 100` 的 `StageStyle.Progressive` 模式下，如果你不自行设置场景模型或天空球，应用将显示为没有场景和光照的纯黑背景。

## 预期结果
完成此步骤后，你应该能用自己的话回答以下问题：

* Window Container 与 Stage 的区别是什么？
* Shared Space 与 Full Space 的区别是什么？
* 空间状态的切换时机是什么？
* 什么时候应在 Shared Space 中使用 Window Container 展现内容？
* 什么时候应在 Full Space 中使用 Stage 提供沉浸式体验？

这里再帮你回顾一下刚才提到的几个概念：Shared Space、Full Space 和空间状态的切换。

* **Shared Space**：允许多个应用以 Window Container 的形式同时运行并共享空间。
* **Full Space**：只允许一个应用运行并独占整个空间。该应用以一个 Stage 为核心，但也可以同时打开多个属于自己的 Window Container。
* **空间状态的切换**：Stage 的开启与关闭决定了空间状态的切换。
   * 当应用开启 Stage 时，空间会进入 Full Space，其他应用则会进入后台。
   * 当应用关闭 Stage 后，空间将恢复为 Shared Space，其他应用可以重新回到前台。

---

# 第 2 步：创建并打开 Stage
**目标：**在 [第二阶段：加入 3D 窗口和模型](./spatial-tutorial_从模板开始搭建空间应用_第二阶段：加入-3d-窗口和模型.md) 的基础上，新建一个 Stage，并从主窗口打开 Stage。
在之前的步骤中，你已经了解了如何将应用设置为默认以 Stage 形式启动。这与设置默认 Window Container 类似，需要完成以下两步：

1. 在 `AndroidManifest.xml` 文件中声明 meta-data，其中必须包含 `"pico.spatial.stage.id"`。
2. 在 `Main.kt` 文件中，于 `DefaultStage{}` 内定义其内容。

现在，你将学习如何通过 DSL 来声明一个 **非默认** 的 Stage。
## 操作步骤

1. **使用 DSL 声明一个 Stage**
   打开 `app/src/main/java/.../Main.kt`，在 `mainApp` 中添加一个新的 Stage，并设置相关参数。
   ```Kotlin
   // ... 原 import 语句
   
   // [新增]import 语句
   import androidx.compose.foundation.layout.Box
   import com.pico.spatial.ui.foundation.dsl.Immersion
   import com.pico.spatial.ui.foundation.dsl.Stage
   import com.pico.spatial.ui.platform.ability.UpperLimbRenderMode
   
   
   fun mainApp(scope: SpatialAppScope) = with(scope) {
       // ... 原有 DefaultWindowContainer 和其他 WindowContainer 的声明
   
       // [新增]声明 Stage
       Stage(
           id = "Stage",
           immersion = Immersion(default = 50),
           upperLimbRenderMode = UpperLimbRenderMode.Default
       ) {
           PicoTheme {
               // Stage 的内容，临时使用 Box，稍后进行替换
               Box {}
           }
       }
   }
   ```

   在这段代码中为 Stage 设置了以下参数：
   * `id`：（必须） Stage 的唯一标识符。
   * `immersion`：（可选） 用于控制 `Progressive` 类型 Stage 的虚拟场景沉浸度。如果未设置，则采用默认值。
   * `upperLimbRenderMode`：（可选） 用于控制上肢在 Stage 中的可见效果。你可以在声明 `Stage()` 时为其设置初始值，并在调用 `openStage()` 时动态修改。最终会以 `openStage()` 中指定的值为准。
2. **从主窗口添加打开 Stage 的按钮**
   回到 `HomePage.kt`，在底部的 `Row` 布局中再添加一个按钮，用于在点击时打开在上一步声明的 Stage。这个按钮将与之前的按钮并排显示。
   ```Kotlin
   // ... 原 import 语句
   
   // [新增]import 语句
   import com.pico.spatial.ui.platform.containers.StageStyle
   import kotlinx.coroutines.launch
   import androidx.compose.runtime.rememberCoroutineScope
   
   @Composable
   fun HomePage(modifier: Modifier) {
       val navigator = LocalSpatialNavigator.current
       // [新增] 通过 rememberCoroutineScope 函数获取协程作用域
       val scope = rememberCoroutineScope()
       Column(
           modifier = modifier.padding(horizontal = 32.dp),
       ) {
           // ... 原有 Text 和 Row 布局
           Row(
               modifier = Modifier.fillMaxWidth(),
               horizontalArrangement = Arrangement.spacedBy(32.dp)
           ) {
               // ... 原有 Button
               
               // [新增] 用于打开 Stage 的 Button
               Button(
                   modifier = Modifier.padding(bottom = 32.dp),
                   onClick = {
                       scope.launch {
                           navigator.openStage(
                               id = "Stage",
                               style = StageStyle.Progressive,
                           )
                       }
                   }
               ) {
                   Text("Open A Stage")
               }
           }
       }
   }
   ```

   你会发现，在代码中仍然使用 `LocalSpatialNavigator` 来打开 `Stage`，但调用方式有所不同。由于 `openStage` 是一个 suspend 函数，因此它必须在协程（Coroutine）或其他 suspend 函数中执行。在代码中，通过 `rememberCoroutineScope` 获取协程作用域，并在 `launch` 代码块中调用了 `openStage`。
   在打开 `Stage` 时，代码中指定了以下参数：
   * `id`：目标 `Stage` 的唯一标识符。
   * `style`：`Stage` 的呈现样式。此处使用的 `Progressive` 样式表示 `Stage` 的内容由真实环境的视频透视（VST）与虚拟内容混合而成。两者的混合比例由 `immersion` 参数控制：
      * `immersion = 0`：VST 占比 100%，完全呈现周围真实环境的 VST，虚拟 3D 物体将不被渲染
      * `immersion = 100`：虚拟内容占比 100%，真实环境的 VST 消失，虚拟 3D 物体将完全显现。
      * `immersion` 介于 0 到 100 之间：真实环境与虚拟内容按指定比例混合显示。

## 预期结果
再次运行应用后，你将看到以下结果：

* 主窗口底部会新增第三个按钮，用于打开 Stage。
* 点击 **Open A Stage** 按钮，应用将进入一个 Stage。由于 `immersion` 参数被设为 `50`，你会看到一半是虚拟的黑色背景，另一半是真实环境的视频透视（VST）。
* 虽然还未编写用于关闭 Stage 的代码，但你目前可以先通过按 **Home** 键退出 Stage，返回共享空间（Shared Space）。

---

# 第 3 步：为 Stage 添加天空球与环境光照，并对比不同 Stage 样式
**目标：** 为 Stage 添加天空球和环境光，并对比不同 Stage 样式带来的视觉差异。
目前，你创建的 Stage 中还没有任何内容，既未放置 3D 物体，也未配置天空球或环境光。因此，当你打开 `Progressive` 样式的 Stage 时，会发现真实环境的视频透视（VST）与纯黑背景相融合。同时，主窗口中的模型也会变暗，因为它失去了在 Shared Space 中由系统默认的部分环境光照。
## 操作步骤

1. **使用 PICO Spatial Editor 创建 Stage 场景中的天空球，并添加环境光照**
   1. 在 Android Studio 中，前往 `editor-asset/.../ModelView`，点击右上角的 **Open In Editor** 使用 Spatial Editor 打开 **MyScene** 场景。在 Spatial Editor 中，点击顶部场景标签栏的加号新建一个名为 **StageContent** 的场景：

   2. 点击右上角的 **Assets library** 按钮，找到 **Sky Sphere** 并双击，即可将其添加到场景中。

   3. 展开 **Sky_Sphere**，找到材质节点 **Sky_Sphere_m**，在右侧 **Inspector** 窗口替换其 **Base Color** 的纹理贴图。
      你可以点击下方的按钮下载的纹理贴图 `SKY_Museum_night.exr` 并将其移动到 Spatial Editor 项目的 `/Sources/Assets` 目录下。你也可以使用自己的 360 度全景图（支持 `.jpg`，`.png`，`.exr` 等格式）作为天空球的贴图。
      <a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1ddc2319aad3475c86dc9471b3d37727~tplv-goo7wpa0wc-image.image" filename="SKY_Museum_night.exr" download>SKY_Museum_night.exr</a>

   4. 点击 **Sky_Sphere** 主节点，在右侧 **Inspector** 窗口中点击 **Add Component**，找到 **Stage Environment Lighting** 组件并双击将其添加到 **Sky_Sphere** 主节点。

   5. 在右侧 **Inspector** 窗口的 **Stage Environment Lighting** 组件模块，把 **Texture Resource 1** 设置为和`SKY_Museum_night.exr`相匹配的纹理贴图。
      点击下方的按钮下载和`SKY_Museum_night.exr`相匹配的纹理贴图 `SKY_Museum_night_linear.exr`并将其移动到 Spatial Editor 项目的 `/Sources/Assets` 目录下。你也可以使用自己的光照贴图，建议与天空球的贴图相匹配。配置完成后，保存 Spatial Editor 项目。
      <a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/753bc10b568144aeaa778809922528ac~tplv-goo7wpa0wc-image.image" filename="SKY_Museum_night_linear.exr" download>SKY_Museum_night_linear.exr</a>

2. **设置 Stage 的内容**
   在 `content` 包下新建 `StageContent.kt` 文件，并粘贴以下代码，以将你在 Spatial Editor 中创建的场景模型设为 Stage 的内容。
   这里额外用代码创建了一个金属球并添加到 `Stage` 场景中，以帮助你探索不同 `Stage` 样式下的渲染特性。
   ```Kotlin
   package com.pico.spatial.sample.myapplication.content
   
   import androidx.compose.runtime.Composable
   import kotlinx.coroutines.withContext
   import kotlinx.coroutines.Dispatchers
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.ModelEntity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.ecs.resource.BlendingMode
   import com.pico.spatial.core.ecs.resource.MeshResource
   import com.pico.spatial.core.ecs.resource.PhysicallyBasedMaterial
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.foundation.content.SpatialView
   
   
   @Composable
   fun StageContent() {
       SpatialView(
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-asset.bundle")
               }
               val scene = Entity.loadSuspend(modelName = "StageContent", bundle = bundle)
               bundle.close()
               content.addEntity(scene)
   
               val metalBall = ModelEntity(
                   mesh = MeshResource.createSphere(0.2f),
                   material = PhysicallyBasedMaterial.create(BlendingMode.OPAQUE).apply {
                       setMetallic(1f)
                       setRoughness(0f)
                   }
               )
               metalBall.components[TransformComponent::class.java]?.apply {
                   setPosition(Vector3(0f, 1.3f, -1.5f))
               }
               content.addEntity(metalBall)
           }
       )
   }
   ```

   完成后，记得在 `Main.kt` 文件中，将占位的 `Box{}` 替换为 `StageContent()` 并添加对应的 import 语句。
   ```Kotlin
   // 原 import 语句
   
   //[新增] import 语句
   import com.pico.spatial.sample.myapplication.content.StageContent
   
   fun mainApp(scope: SpatialAppScope) =
       // ... 
   
           Stage(
               id = "Stage",
               immersion = Immersion(default = 50),
               upperLimbRenderMode = UpperLimbRenderMode.Default
           ) {
               PicoTheme {
                   // [更新]将占位的 Box{} 替换为 StageContent()
                   StageContent()
               }
           }
       }
   ```

3. **对比不同 Stage 样式的渲染效果**
   1. 重新运行应用并从主窗口打开 Stage。你会看到一个虚实结合的场景：一半是夜间美术馆的虚拟环境，另一半是你周围真实环境的视频透视（VST）。场景中的金属球也会因此同时反射出真实房间和虚拟美术馆的倒影。

      之所以呈现这种虚实结合的场景，是因为你在代码中进行了如下配置：
      * 在 `HomePage.kt` 文件中，调用 `openStage` 时指定了 `style = StageStyle.Progressive`。
      * 在 `Main.kt` 文件中，声明 Stage 时设置了 `immersion = Immersion(default = 50)`。
   2. 在 `HomePage.kt` 中，将 `openStage` 函数的 `style` 参数先后设置为 `StageStyle.Mixed` 和 `StageStyle.Full`，并打开 Stage 以观察三种不同样式下物体的渲染区别。
      ```Kotlin
      Button(
          modifier = Modifier.padding(bottom = 32.dp),
          onClick = {
              scope.launch {
                  navigator.openStage(
                      id = "Stage",
                      // 先后设置为 StageStyle.Mixed 和 StageStyle.Full
                      style = StageStyle.Progressive,
                  )
              }
          },
      ) {
          Text("Open A Stage")
      }
      ```

      你会发现不同 Stage 样式对环境光照和物体反射的影响：
      * `StageStyle.Mixed`：金属球完全反射真实房间的倒影。这是因为此模式的环境光照完全使用真实环境的采样作为贴图。
      * `StageStyle.Progressive`：金属球的反射效果是真实房间与虚拟美术馆的混合。这是因为此模式会根据 `immersion`（沉浸度）的数值，融合真实环境光照与你设置的 Stage Environment Lighting。
      * `StageStyle.Full`：金属球完全反射虚拟的夜间美术馆倒影。这是因为此模式完全使用你设置的 Stage Environment Lighting 作为环境光照。
      此外，主窗口中的木雕模型的亮度由高到低依次为 `Mixed` > `Progressive` > `Full`，这也是因为不同 Stage 样式下的环境光照不同。下图展示了不同 Stage 样式下的环境光照和物体反射。

      <strong>Mixed</strong>

      <strong>Progressive</strong>

      <strong>Full</strong>

   3. 为保证与后续教程内容的一致性，你需要将 `style` 参数设置为 `StageStyle.Mixed`。

## 预期结果
完成此步骤后，你已经为 Stage 添加了天空球和配套的环境光照，并通过观察金属球的渲染效果，理解了不同 Stage 样式的特点。

---

# 第 4 步：添加动态的 3D 模型和 UI 面板
**目标**：在 Stage 中添加大范围运动的 3D 模型，并通过悬浮 UI 面板进行交互。
在这一步，你将利用 Stage 的广阔空间，构建一个地球–卫星系统，其中卫星会持续环绕地球运动。
此外，你还将添加一个悬浮 UI 面板，用于实现以下功能：

* 控制动画速度
* 打开或关闭主窗口
* 退出 Stage

## 操作步骤

1. **在 Spatial Editor 中搭建地球-卫星系统**
   1. 在 Android Studio 中，前往 `editor-asset/.../StageContent.usda` 并点击右上角的 **Open In Editor** 在 Spatial Editor 中打开 **StageContent** 场景。

   2. 接着，在 Spatial Editor 中点击 **Assets library** 图标，找到并双击 **Artificial Satellite** 和 **Earth**，将它们添加到场景中：

   3. 按以下步骤调整节点层级与属性。
      1. 在 **Root** 节点下创建一个 **Empty** 节点，并重命名为 **Earth_Satellite**。然后将 **Artificial_Satellite** 和 **Earth** 移动到 **Earth_Satellite** 节点下。

      2. 参考截图分别调整 **Earth_Satellite** 和 **Earth** 的 Transform 属性。
         你暂时无需更改 **Artificial_Satellite** 的 Transform，其位置将在后续添加动画时进行调整。

2. **加载地球-卫星系统并为卫星添加轨道动画**
   由于地球-卫星系统现在会随 `StageContent.usda` 场景自动加载，你可以删除之前用于测试的金属球相关代码，并为卫星添加绕地球旋转的轨道动画（Orbit Animation）。
   你可以直接用下面的代码全量覆盖`StageContent.kt` 的原有代码：
   ```Kotlin
   package com.pico.spatial.sample.myapplication.content
   
   import androidx.compose.runtime.Composable
   import kotlinx.coroutines.withContext
   import kotlinx.coroutines.Dispatchers
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.animation.OrbitAnimation
   import com.pico.spatial.core.ecs.animation.RepeatMode
   import com.pico.spatial.core.ecs.resource.AnimationResource
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.math.EulerAngles
   import com.pico.spatial.core.math.Transform
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.foundation.content.SpatialView
   
   @Composable
   fun StageContent() {
       SpatialView(
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-asset.bundle")
               }
               val scene = Entity.loadSuspend(modelName = "StageContent", bundle = bundle)
               bundle.close()
               content.addEntity(scene)
   
               // 设置卫星绕地球的轨道动画
               val satellite = scene.findEntity("Artificial_Satellite")
               val orbitAnimation = OrbitAnimation.createOrbitAnimation(
                   name = "SatelliteOrbit", // 动画名称
                   duration = 20f, // 每 20 秒播放一次完成的动画
                   axis = Vector3(0f, 1f, 0f), // 旋转轴为 Y 轴
                   startTransform = Transform(
                       position = Vector3(0.6f, 0.25f, 0f), // 初始位置距原点 0.6 米，形成半径为 0.6 米的轨道
                       rotation = EulerAngles(90f, 90f, 0f), // 初始旋转角度，旋转卫星让其面朝地球
                       scale = Vector3(0.2f), // 初始缩放比例，将卫星模型整体等比缩放为原来的 0.2 倍
                   ),
                   spinClockwise = false, // 逆时针旋转
                   orientToPath = true, // 在绕行时始终随路径调整朝向
                   rotationCount = 1f, // 一次完整的动画期间，完成 1 圈旋转（共 360°）
                   repeatMode = RepeatMode.RESTART, // 每次循环时从起点重新开始
                   repeatCount = -1 // 无限循环播放
               )
               val animationResource = AnimationResource.generate(orbitAnimation)
               satellite?.playAnimation(animationResource)
           }
       )
   }
   ```

3. 重新运行应用并从主窗口打开 Stage。你将看到人造卫星围绕地球转动的轨道动画。

   代码中使用 `OrbitAnimation.createOrbitAnimation()` 来创建轨道动画。动画中的物体会围绕 `axis` 参数指定的轴线，在一个与该轴垂直的平面上进行圆周运动。该平面的具体位置由 `startTransform` 中的 `position` 参数决定。`OrbitAnimation.createOrbitAnimation()`各参数的作用如下：
   * `axis = Vector3(0f, 1f, 0f)` 和 `spinClockwise = false`：指定卫星围绕 Y 轴（垂直轴）进行逆时针旋转。
   * `position = Vector3(0.6f, 0.25f, 0f)`：设置卫星的初始位置。这意味着轨道的半径为 0.6 米，且轨道平面位于其父节点上方 0.25 米处。
   * `rotation = EulerAngles(90f, 90f, 0f)` 和 `orientToPath = true`：共同确保卫星在沿轨道运动时，其天线系统（Antenna）始终朝向地球。
   * `duration = 20f` 和 `rotationCount = 1f`：共同控制旋转速度，使卫星每 20 秒绕行一周。
4. **添加交互式 UI 控制面板**
   接下来，你将修改 `StageContent.kt` 文件，为其添加一个 UI 控制面板，以实现以下功能：
   * 控制动画时长
   * 打开或关闭主窗口
   * 退出 Stage
   为了提供更流畅的导航体验，你还将实现一个额外的逻辑：打开 Stage 时自动关闭主窗口，退出时再将其恢复。
   你可以直接用下面的代码全量覆盖`StageContent.kt` 的原有代码：
   ```Kotlin
   package com.pico.spatial.sample.myapplication.content
   
   import androidx.compose.foundation.background
   import androidx.compose.foundation.layout.Arrangement
   import androidx.compose.foundation.layout.Column
   import androidx.compose.foundation.layout.fillMaxWidth
   import androidx.compose.foundation.layout.padding
   import androidx.compose.foundation.layout.size
   import androidx.compose.foundation.shape.RoundedCornerShape
   import androidx.compose.runtime.Composable
   import androidx.compose.runtime.DisposableEffect
   import androidx.compose.runtime.getValue
   import androidx.compose.runtime.mutableFloatStateOf
   import androidx.compose.runtime.mutableStateOf
   import androidx.compose.runtime.remember
   import androidx.compose.runtime.rememberCoroutineScope
   import androidx.compose.runtime.setValue
   import androidx.compose.ui.Alignment
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.graphics.Color
   import androidx.compose.ui.unit.dp
   import androidx.compose.ui.unit.sp
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.animation.AnimationPlaybackController
   import com.pico.spatial.core.ecs.animation.OrbitAnimation
   import com.pico.spatial.core.ecs.animation.RepeatMode
   import com.pico.spatial.core.ecs.resource.AnimationResource
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.math.EulerAngles
   import com.pico.spatial.core.math.Transform
   import com.pico.spatial.core.math.Vector3
   import com.pico.spatial.ui.design.Button
   import com.pico.spatial.ui.design.Slider
   import com.pico.spatial.ui.design.SliderDefaults
   import com.pico.spatial.ui.design.Text
   import com.pico.spatial.ui.foundation.content.SpatialView
   import com.pico.spatial.ui.platform.containers.LocalSpatialNavigator
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.launch
   import kotlinx.coroutines.withContext
   
   /**
    * StageContent: 负责管理 3D 场景、动画逻辑和 UI 面板的主要 Composable。
    *
    * 架构设计：
    * 1. 状态提升 (State Hoisting)：UI 状态 (sliderValue, isMainPanelOpen) 由 StageContent 持有。
    * 2. 逻辑封装 (Logic Encapsulation)：动画资源管理逻辑封装在 StageAnimationManager 中。
    * 3. 关注点分离 (Separation of Concerns)：UI 渲染委托给 StageControlPanel，业务逻辑在 StageContent 中处理。
    */
   @Composable
   fun StageContent() {
       val navigator = LocalSpatialNavigator.current
       val scope = rememberCoroutineScope()
   
       // UI 状态
       var duration by remember { mutableFloatStateOf(20f) }
       var isMainPanelOpen by remember { mutableStateOf(false) }
   
       // 动画逻辑封装：使用 remember 缓存 Manager 实例，确保 Recomposition 保持状态一致
       val animationManager = remember { StageAnimationManager() }
   
   
       // 生命周期管理：使用 DisposableEffect 确保进入/退出时的副作用正确执行
       DisposableEffect(Unit) {
           // Enter：打开 Stage 时关闭主窗口
           navigator.closeWindowContainer("YourPlanarWindowContainer")
           isMainPanelOpen = false
   
           onDispose {
               // Exit：退出 Stage 时，如果主窗口处于关闭状态，恢复主窗口显示
               if (!isMainPanelOpen) navigator.openWindowContainer("YourPlanarWindowContainer")
               // 关键：清理所有资源
               animationManager.dispose()
           }
       }
   
       SpatialView(
           initial = { content, attachments ->
               // 1. 加载 AssetBundle 和场景模型
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-asset.bundle")
               }
               val scene = Entity.loadSuspend(modelName = "StageContent", bundle = bundle)
               bundle.close()
               content.addEntity(scene)
   
               // 2. 查找卫星实体，并应用轨道动画
               val satellite = scene.findEntity("Artificial_Satellite")
               if (satellite != null) {
                   // 将 Entity 引用交给 Manager 管理
                   animationManager.satellite = satellite
                   // 应用初始动画
                   animationManager.applyOrbitAnimation(duration)
               }
   
               // 3. 将控制面板 (Attachment) 放置在用户右前方
               attachments.entity(id = "stage_control_panel")?.apply {
                   components[TransformComponent::class.java]?.setPosition(Vector3(0.4f, 1.3f, -1.0f))
                   content.addEntity(this)
               }
           },
           attachments = {
               // 定义控制面板 UI
               AttachmentPanel(id = "stage_control_panel") {
                   StageControlPanel(
                       sliderValue = duration,
                       onSliderChange = { duration = it }, // 仅更新 UI 数值
                       onSliderCommit = { animationManager.applyOrbitAnimation(duration) }, // 仅在松手时触发动画更新
                       isMainPanelOpen = isMainPanelOpen,
                       onToggleMainPanel = {
                           if (isMainPanelOpen) navigator.closeWindowContainer("YourPlanarWindowContainer")
                           else navigator.openWindowContainer("YourPlanarWindowContainer")
                           isMainPanelOpen = !isMainPanelOpen
                       },
                       onExit = { scope.launch { navigator.closeStage() } }
                   )
               }
           }
       )
   }
   
   /**
    * StageAnimationManager: 简单的 State Holder 类，用于管理动画资源、动画控制器和卫星实体。
   
    * 作用：
    * 1. 封装 Controller, Resource, Entity 的引用。
    * 2. 确保 "关闭旧资源 -> 创建并播放新动画" 的正确逻辑。
    * 3. 提供 dispose 方法用于统一清理。
    */
   private class StageAnimationManager {
       var controller: AnimationPlaybackController? = null
       var resource: AnimationResource? = null
       var satellite: Entity? = null
   
       fun applyOrbitAnimation(duration: Float) {
           val entity = satellite ?: return
   
           // Step 1: 清理旧资源 (先停止并关闭 Controller，再关闭 Resource)
           controller?.let {
               if (it.valid) {
                   it.stop(); it.close()
               }
           }
           resource?.close()
   
           // Step 2: 创建新动画
           val orbitAnimation = OrbitAnimation.createOrbitAnimation(
               name = "SatelliteOrbit",
               duration = duration,
               axis = Vector3(0f, 1f, 0f),
               startTransform = Transform(
                   Vector3(0.6f, 0.25f, 0f),
                   EulerAngles(90f, 90f, 0f),
                   Vector3(0.2f)
               ),
               spinClockwise = false,
               orientToPath = true,
               rotationCount = 1f,
               repeatMode = RepeatMode.RESTART,
               repeatCount = -1
           )
   
           // Step 3: 生成新资源并播放
           val newResource = AnimationResource.generate(orbitAnimation)
           val newController = entity.playAnimation(newResource)
   
           // Step 4: 更新状态引用
           controller = newController
           resource = newResource
       }
   
       fun dispose() {
           controller?.let {
               if (it.valid) {
                   it.stop(); it.close()
               }
           }
           resource?.close()
           satellite?.destroy()
       }
   }
   
   /**
    * StageControlPanel: 纯 UI 组件 (Stateless Composable)。
    *
    * 作用：
    * 1. 负责 UI 布局和渲染。
    * 2. 通过回调函数 (Lambda) 将用户交互事件向上传递。
    * 3. 不包含任何业务逻辑，只负责显示。
    */
   @Composable
   private fun StageControlPanel(
       sliderValue: Float,
       onSliderChange: (Float) -> Unit,
       onSliderCommit: () -> Unit,
       isMainPanelOpen: Boolean,
       onToggleMainPanel: () -> Unit,
       onExit: () -> Unit
   ) {
       Column(
           modifier = Modifier
               .size(width = 400.dp, height = 300.dp)
               .background(
                   Color.LightGray.copy(alpha = 0.5f),
                   shape = RoundedCornerShape(16.dp)
               )
               .padding(24.dp),
           verticalArrangement = Arrangement.spacedBy(16.dp),
           horizontalAlignment = Alignment.CenterHorizontally
       ) {
           Text("Control Panel", fontSize = 24.sp, color = Color.Black)
   
           Column(horizontalAlignment = Alignment.CenterHorizontally) {
               Text(
                   "Animation Duration: ${sliderValue.toInt()}s",
                   fontSize = 16.sp,
                   color = Color.DarkGray
               )
               Slider(
                   value = sliderValue,
                   onValueChange = onSliderChange,
                   onValueChangeFinished = onSliderCommit,
                   valueRange = 5f..40f,
                   colors = SliderDefaults.sliderColors(
                       trackColor = Color.Gray,
                       progressColor = Color.White.copy(alpha = 0.8f),
                       progressHighColor = Color.White.copy(alpha = 0.9f)
                   ),
                   modifier = Modifier.fillMaxWidth()
               )
           }
   
           Button(
               onClick = onToggleMainPanel,
               modifier = Modifier.fillMaxWidth()
           ) {
               Text(if (isMainPanelOpen) "Close Main Panel" else "Open Main Panel")
           }
   
           Button(
               onClick = onExit,
               modifier = Modifier.fillMaxWidth()
           ) {
               Text("Exit Stage")
           }
       }
   }
   ```

   上面的代码通过封装，将逻辑拆分到三个独立的组件中，使整体架构更加清晰：
   * `StageContent`：作为组装者与协调者，`StageContent`创建并持有 `StageAnimationManager` 实例，同时在 UI 树中渲染 `StageControlPanel`，将逻辑与 UI 桥接起来。持有并管理所有 UI 状态（如 `duration` 和 `isMainPanelOpen`），作为唯一的数据源。利用 `DisposableEffect` 处理进入/退出 Stage 时的副作用，如隐藏/恢复主窗口和调用资源销毁逻辑。通过 `SpatialView` 加载 3D 模型、添加 UI 面板，并将找到的卫星实体传递给 `StageAnimationManager`。
   * `StageAnimationManager`：管理资源并封装动画逻辑，类似于一个“后台服务”。`StageAnimationManager`对 UI 无感知。只暴露 `applyOrbitAnimation(duration)` 这样的高级接口供 `StageContent` 调用。`StageAnimationManager`持有动画所需的关键对象，负责处理动画播放逻辑，并提供统一的资源清理方法。
   * `StageControlPanel` ：作为`StageContent` 的展示层，`StageControlPanel`只负责界面的渲染和响应手势，与具体的业务逻辑完全解耦。`StageControlPanel`不持有任何状态，所有显示的数据（如 `sliderValue`）都由 `StageContent` 通过参数传入。用户的操作（如滑动滑块、点击按钮）通过 Lambda 回调函数（如 `onSliderCommit`）向上传递。

## 预期结果
再次运行应用，点击主窗口上的 **Open A Stage** 按钮，你将体验到以下效果：

* **进入沉浸式场景**：主窗口会自动关闭，你将进入一个以夜间美术馆为背景的场景，视野中央是卫星围绕地球旋转的 3D 模型。
* **使用控制面板**：场景右侧的控制面板提供三项操作：
   * 拖动滑动条，可以调节卫星的绕行速度。
   * 点击第一个按钮，可以在不退出 Stage 的情况下，随时打开或关闭主窗口。
   * 点击第二个按钮，可以退出 Stage。如果此时主窗口处于关闭状态，退出后它会自动重新打开。

# 总结
恭喜你顺利完成本阶段教程！在这个实践中，你充分利用了 Stage 的空间能力，为应用创造了更具沉浸感的体验。通过本阶段教程，你学习了：

* Shared Space 与 Full Space 的区别，以及 `Stage` 和 `WindowContainer` 的本质差异。
* 如何创建并打开一个 Stage，并探索不同 Stage 样式的特点。
* 如何使用天空球和环境光照来增强应用的沉浸感。
* 如何在 Stage 中实现卫星绕地球运行的轨道动画，并采用符合最佳实践的架构进行设计。

# **延伸阅读**
如果你想更深入地探索本阶段教程涉及的知识点，可以阅读以下文档：

* 《[声明 Stage](./spatial-sdk_空间容器_管理-stage_声明-stage.md)》《[打开或关闭 Stage](./spatial-sdk_空间容器_管理-stage_打开或关闭-stage.md)》《[了解空间容器 & 空间状态](./spatial-sdk_空间容器_了解空间容器-&-空间状态.md)》章节：了解更多关于 Stage 的声明、打开和关闭，以及空间容器的相关知识。
* 《[轨道动画](./spatial-sdk_动画_轨道动画.md)》：关于轨道动画的创建、使用、注意事项等。
* 《[基于图像的光照](./spatial-sdk_渲染_基于图像的光照.md)》：关于如何通过 `StageEnvironmentLightingComponent`、`ImageBasedLightComponent` 等设置环境光照或基于图像的光照。
* 如果想了解更多关于 PICO Spatial Plugin、PICO Emulator 和 Spatial Editor 的使用，请阅读相关文档：
   * 《[什么是 PICO Spatial Plugin](./spatial-toolkit_pico-spatial-plugin_什么是-pico-spatial-plugin.md)》
   * 《[什么是 PICO Emulator](./spatial-toolkit_pico-emulator_什么是-pico-emulator.md)》
   * 《[什么是 PICO Spatial Editor](./spatial-toolkit_pico-spatial-editor_什么是-pico-spatial-editor.md)》

# 接下来
恭喜你完成了整个系列的学习！通过这三个循序渐进的教程，你已经从一个最基础的 Planar 窗口出发，构建了包含 Volumetric 窗口和 Stage 的完整空间体验。但是，你的空间创造之旅才刚刚开始。
## 下载 PICO Spatial SDK 代码示例
你也可以下载 [PICO Spatial SDK 代码示例](https://developer-cn.picoxr.com/document/spatial-example/)。通过查看这些示例项目的代码并运行这些项目，你可以更好地理解文档中的概念在真实项目中的应用。

* **欢迎来到 Space OS 6**：此示例项目是一个交互式的 3D 家居环境，旨在展示如何融合多种核心功能。你将从中学习如何管理 Window Container 和 Stage，实现平面 UI 与沉浸式内容间的无缝过渡；如何使用实体组件系统 (ECS) 管理复杂的 3D 对象及其行为；如何通过手势操作实现 3D 模型的旋转和缩放；以及如何利用基于图像的光照 (IBL) 实现逼真的环境反射。运行应用后，你将体验一个完整的三步流程：从主页进入家具库，选择家具，并将其放入一个全尺寸的虚拟房间进行装饰。
* **为应用添加物理效果**：此示例项目通过一个交互式的 3D 多米诺骨牌场景，此示例直观地演示了刚体动力学、碰撞检测和碰撞事件处理等核心物理功能，让你能亲身体验物理模拟的实现与应用。
* **为 3D 模型添加动画**：此示例项目使用一个机器人模型来演示骨骼动画和补间动画。你将学习如何播放模型内置的多种动画片段（如站立、挥手、跳跃），并调用 API 获取动画信息以播放特定片段，为后续通过 UI 控制动画切换打下基础。
* **创建沉浸式音频体验**：此示例项目演示了如何开发包含空间音频的应用，涵盖了环境音效、3D 空间音效、音频资源管理和交互式音频体验。你还可以自由开关各类声音，感受空间音频与虚拟环境的融合效果，并了解自定义组件的使用方法。
* **在应用中播放空间视频**：此示例项目展示了如何创建一个可在窗口化和沉浸式 3D 环境间无缝切换的空间视频播放器。运行应用后，你会看到一个带播放控件的浮动视频面板，并可以进入 360 度观看模式。你将从中学习如何使用 ECS 在不同 3D 几何体（平面和球体）上渲染视频，如何使用 Jetpack Compose 构建空间 UI，以及如何在不同观看场景下管理播放状态。
* **使用 SpatialML 框架实现实时超级分辨率**：此示例项目通过创建一个超级分辨率 (Super-Resolution) 相机应用，展示了如何在空间场景中集成机器学习模型。此示例项目利用 SpatialML 部署 Real-ESR GAN 模型，将相机捕捉的低分辨率图像进行超分重建，从而提升画面的清晰度和质量。
* **利用空间网格创建射击游戏**：此示例项目会实时扫描并渲染你周围真实环境的 Spatial Mesh。你将学习如何将 Spatial Mesh 用于物理碰撞，实现射击命中效果（变色、计分）和空间音效。项目采用 ECS 架构，并通过对象池（弹丸和音频）技术来优化运行时性能。

## 继续阅读 PICO Spatial SDK 文档
你可以借助 [官方文档](https://developer-cn.picoxr.com/document/spatial-sdk/)，继续深入探索 PICO Spatial SDK 的以下能力：

   建议选择一个与你当前需求最接近的模块并阅读，而不必一次性读完所有内容。

* **空间容器与应用形态**：深入理解 Shared Space 与 Full Space 的使用场景，学习如何在复杂应用中组合使用多个 `WindowContainer` 和 `Stage`。
* **内容布局与 Spatial UI**：学习扩展 2D / 2.5D 内容的呈现方式，如空间浮起、旋转、毛玻璃效果（`Vibrant Style`）等，并掌握如何统一应用的主题与组件风格。
* **ECS 与 3D 场景**：系统学习 ECS（`entity/component/system`）的组织方式，并结合资源管理（如网格、材质、`AssetBundle`）与渲染技术（如 `ShaderGraphMaterial`、基于图像的光照），为 3D 场景添加更复杂的视觉效果与逻辑。
* **动画系统**：探索更丰富的动画类型，如补间、骨骼、轨道、Timeline、BlendShape 等，并学习组合与控制这些动画，让模型“动起来”。
* **物理系统**：为应用加入物理引擎，通过设置碰撞、力与阻尼、射线检测等，构建具有真实物理反馈的空间交互。
* **交互与事件**：通过实现空间手势、3D 悬停高亮、UI 拖拽和交互音效等，构建完整的交互体验。
* **追踪能力**：学习如何获取并使用 HMD、手柄、手部、视线等追踪数据，为应用打造多维度的输入方式。
* **环境感知（混合现实）**：利用空间锚点、空间网格、平面检测等环境感知能力，让虚拟内容与真实环境更好地融合。
* **SpatialML**：探索如何在空间场景中集成 SpatialML 算法（如超级分辨率相机），并参考最佳实践来提升应用效果与性能。
* **多媒体体验**：为应用集成空间音频与空间视频，提供更具沉浸感的视听体验。
* **性能与调试 / 应用迁移**：学习性能优化与调试技巧（如场景复杂度管理、Trace 分析），并了解如何将现有的 Android 应用平滑迁移到空间应用。
