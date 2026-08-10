# 开始之前
在本阶段教程中，你将从 PICO Spatial SDK 提供的标准模板项目开始，迈出构建空间应用的第一步。你将学习如何理解并扩展应用中的 **Planar Window Container**，这是用于承载应用内容最常用的空间容器。
## 你将实现什么
一个含有 2D 和 3D 内容的 Planar Window Container 作为应用主窗口，并且可以控制打开和关闭另一个含有 2D 和 2.5D 内容的 Planar Window Container。
“2.5D 内容”指添加了空间效果的 2D 内容。这类内容被放置在三维虚拟环境中，从而获得了深度和立体感，但与真正的 3D 对象不同，“2.5D 内容”不支持自由移动或从多个角度进行渲染。

## 你将学习什么

* 一个 PICO 空间应用的基本结构和代码入口。
* `WindowContainer` 的基本概念及其在空间应用中的作用。
* 如何在 `AndroidManifest.xml` 中声明默认启动窗口的属性。
* 如何使用 DSL（Domain-Specific Language，领域特定语言）声明默认窗口的内容。
* 如何使用 DSL 声明非默认窗口的属性和内容。
* 如何在窗口中添加基于 Jetpack Compose 的 2D UI 元素，并为其添加空间效果。
* 如何实现一个简单的交互方式，用于打开和关闭窗口。

## 你将需要什么

* 配置完成的 PICO Spatial SDK 开发环境，包括 Android Studio 2025.1.x 和 PICO 空间应用开发工具（PICO Spatial Plugin、PICO Spatial Editor 和 PICO Emulator）。详情参阅《[第一步：准备开发环境](/document/spatial-sdk/set-up-development-environment)》。
* 一个基于 Planar Window Container 模板创建的空间应用项目。本教程所有步骤以 Planar Window Container 模板为起点，如果你当前项目使用的是 Volumetric Window Container / Full Stage 模板，建议先重新创建一个 Planar Window Container 模板项目。详情参阅《[第二步：创建你的第一个空间应用](./spatial-sdk_快速开始_第二步：创建并运行-spatial-项目.md)》。
* PICO 设备或 PICO Emulator。
* **预计耗时**：约 20 分钟

---

# 第 1 步：理解**模板项目与默认窗口的属性**
**目标：**理解默认入口窗口的来源，并建立对模板项目最小结构的直观认知。
在开始编码之前，让我们先来分析该模板项目，以了解其基本工作原理。
## 操作步骤

1. **观察项目结构**
   在 Android Studio 中，将项目文件的视图从 Android 视图切换至 Project 视图，展开 `app` 模块和 `editor-asset` 模块。你会看到如下内容。

  左侧的文件层级中包括以下模块：

   * **app 模块**：是应用的主模块，包含应用的运行逻辑、UI 界面和启动入口。
   * **editor-asset 模块**：用于存放 [Spatial Editor 项目](/document/spatial-toolkit/spatial-editor-project-management/)。你可以使用 PICO Spatial Editor 编辑和管理 3D 资源，包括纹理、材质、模型等。编译时，com.pico.spatial.tools 插件会将这些资源以资源包（.bundle 文件）的形式构建至应用 APK 中。
2. **理解应用入口和启动逻辑**

  首先，让我们来梳理一下和应用启动相关的文件（均在 `app` 模块中）：

   * `AndroidManifest.xml` 配置了`Application`、入口 `Activity` 和 `<meta-data>`，用户点击应用图标后，系统会首先读取这些信息。
   * `Main.kt` 定义了 `mainApp()` 函数，你可以在其中使用一系列 DSL 方法（如 `DefaultWindowContainer`, `WindowContainer`）声明式地定义所有空间容器。比如模板项目中，`DefaultWindowContainer` DSL 块声明了默认窗口的内容。其中包裹的 `HomePage` 就是你看到的初始窗口内容。
   * `SpatialApplication.kt` 是应用逻辑的入口，应用启动时，系统会在其 `onCreate` 中调用 `launch(::mainApp)`，将 `mainApp` 函数注册到 SDK 中，等待 Activity 启动后挂载。
   * `LaunchActivity.kt` 继承自 `SpatialLaunchActivity`，是应用的启动桩（Stub）。它启动时，会自动查找在 Application 中注册的 `mainApp` 内容；根据 `AndroidManifest.xml` 中的 `meta-data` 创建一个 3D 空间窗口，并将 `mainApp` 的内容渲染到这个窗口上。

  项目的启动逻辑如下：

   1. **第 1 阶段：系统引导（AndroidManifest.xml）**
   用户点击应用图标，系统读取清单：识别 `Application`（`SpatialApplication`）、入口 `Activity`（`LaunchActivity`），并读取 `<meta-data>` 作为默认窗口的属性配置。
   2. **第 2 阶段：应用初始化（SpatialApplication.kt）**
   系统调用 `onCreate()`，执行 `launch(::mainApp)`，将 mainApp 中声明的所有容器注册到 PICO Spatial SDK，并将默认容器的 UI 根节点记录，等待入口 Activity 启动后进行挂载。
   3. **第 3 阶段：窗口容器创建（LaunchActivity.kt + Main.kt）**
   系统启动 `LaunchActivity`（继承 `SpatialLaunchActivity`）；PICO Spatial SDK 根据清单中的 `meta-data` 创建空间窗口，并将 `mainApp` 中的 `DefaultWindowContainer` 内容渲染到该窗口。
3. **查看默认窗口的属性声明**
   上面提到，在 `AndroidManifest.xml` 中会配置 `<meta-data>`，这里就是在对默认窗口的属性进行声明。打开 `app/src/main/AndroidManifest.xml` 文件。找到主 `Activity` 声明，你会看到一段特殊的 `meta-data`：
   ```XML
   <activity
       android:name=".platform.LaunchActivity"
       android:exported="true"
       android:theme="@android:style/Theme.NoDisplay">
       <intent-filter>
           <action android:name="android.intent.action.MAIN" />
           <category android:name="android.intent.category.LAUNCHER" />
       </intent-filter>
   
       <!-- Planar DefaultWindowContainer Configuration -->
       
       <!-- The unique name/id of a WindowContainer -->
       <meta-data android:name="pico.spatial.windowcontainer.id" android:value="YourPlanarWindowContainer"/>
       
       <!-- Form/style of the WindowContainer
           "0": Form.Automatic, a system default setting, set to Form.Planar currently (default)
           "1": Form.Planar, a form where the WindowContainer behaves like a normal plane with default depth (default)
           "2": Form.Volumetric, a form where the WindowContainer behaves like a volume allowing custom depth
        -->
       <meta-data
           android:name="pico.spatial.windowcontainer.style"
           android:value="1" />
       ...
   </activity>
   ```

   `<intent-filter>` 将这个 LaunchActivity 设置为了 App 的启动入口。
   `pico.spatial.windowcontainer.id` 用于指定 `WindowContainer` 的 ID。当启动该 `Activity` 时，系统会依据此 ID (`"YourPlanarWindowContainer"`) 自动创建一个 `WindowContainer`，并将 `mainApp` 中 `DefaultWindowContainer` 的内容渲染至其中。`pico.spatial.windowcontainer.style` 则用于将窗口类型定义为 `Form.Planar`。其余的 `meta-data` 标签分别用于配置特定的窗口属性，部分说明已在代码注释中提供。如需全面了解所有可通过 `meta-data` 配置的窗口属性，请参阅《[声明 WindowContainer](./spatial-sdk_空间容器_管理-windowcontainer_声明-windowcontainer.md)》文档。

## 预期结果
虽然你没有修改任何代码，但你现在应该已经清晰地了解：

* 模板项目包含 `app` 和 `editor-asset` 两个模块，前者是主模块，包含源代码；后者负责 PICO Spatial Editor 资源的管理和打包。
* 应用的入口是什么，启动逻辑是什么。
* 默认窗口的属性在 `AndroidManifest.xml` 中通过 `meta-data` 声明；而默认窗口的内容在 `Main.kt` 中的 `DefaultWindowContainer` 里定义。

---

# 第 2 步：理解并修改默认窗口的内容
**目标**：通过检查并微调默认 Planar 窗口中的内容，深入了解其 2D 和 3D 内容的构成方式，并安全地替换这些内容。
在对项目结构、启动流程及默认窗口的声明方式有了基本认知后，现在让我们来详细分析默认窗口的具体内容。
## 操作步骤

1. **查看窗口内容** **`HomePage.kt`**
   打开 `app/src/main/java/.../content/HomePage.kt` 文件，其中的 `HomePage` 函数是一个 Composable 函数。如果你使用过 [Jetpack Compose](https://developer.android.com/develop/ui/compose/documentation) 开发 UI，你会发现里面包含了 `Image`、`Text`、`Row`、`Column` 等你熟悉的 Jetpack Compose 组件。另外，`HomePage` 函数还包含一个用于承载 3D 模型的 `SpatialView`：
   ```Kotlin
   @Composable
   fun HomePage(modifier: Modifier = Modifier) {
       // 统一定义卡片样式，便于左右两侧内容保持一致
       val cardShape = RoundedCornerShape(8.dp)
       val cardBackgroundColor = Color.White.copy(alpha = 0.2f)
       val cardModifier =
           Modifier
               .size(width = 400.dp, height = 309.dp)
               .background(color = cardBackgroundColor, shape = cardShape)
       val descriptionColor = Color(0x80000000)
   
   
       Column(
           modifier = modifier.padding(horizontal = 32.dp),
           verticalArrangement = Arrangement.spacedBy(20.dp),
       ) {
           // 1. 页面标题与简介
           Column(
               modifier = Modifier.padding(top = 32.dp),
               verticalArrangement = Arrangement.spacedBy(8.dp),
           ) {
               Text(
                   text = stringResource(R.string.homepage_title),
                   style = PicoTheme.typography.displaySmall,
                   fontSize = 28.sp,
               )
               Text(
                   text = stringResource(R.string.homepage_body_definition),
                   fontWeight = FontWeight.SemiBold,
                   fontSize = 20.sp,
                   color = descriptionColor,
               )
           }
   
   
           // 2. 核心内容区域：左侧 2D 图片 vs 右侧 3D 模型
           Row(
               modifier = Modifier.fillMaxWidth(),
               horizontalArrangement = Arrangement.spacedBy(16.dp),
           ) {
               // 左侧：传统的 2D 图片展示
               Column(
                   modifier = Modifier.weight(1f),
                   verticalArrangement = Arrangement.spacedBy(12.dp),
               ) {
                   Image(
                       modifier = cardModifier,
                       painter = painterResource(id = R.drawable.sci_fi_box),
                       contentDescription = "A sci-fi metal box",
                       contentScale = ContentScale.Fit,
                   )
                   Text(
                       text = stringResource(R.string.homepage_body_use_case_1),
                       style = PicoTheme.typography.bodyLarge,
                       fontSize = 16.sp,
                       color = descriptionColor,
                   )
               }
   
   
               // 右侧：3D 空间视图 (SpatialView)
               Column(
                   modifier = Modifier.weight(1f),
                   verticalArrangement = Arrangement.spacedBy(12.dp),
               ) {
                   SpatialView(
                       modifier = cardModifier,
                       // 初始化 3D 场景
                       initial = { content, _ ->
                           // A. 加载 AssetBundle 资源包
                           val bundle = withContext(Dispatchers.IO) {
                               AssetBundle.load("asset://editor-asset.bundle")
                           }
                           // B. 加载模型实体 ("MyScene")
                           val model = Entity.loadSuspend(modelName = "MyScene", bundle = bundle)
                           bundle.close()
   
                           // C. 设置模型位置与缩放
                           model.components[TransformComponent::class.java]?.apply {
                               setPosition(Vector3(0f, 0f, -0.2f))
                               scaleBy(0.75f)
                           }
   
                           // D. 将模型添加到场景中
                           content.addEntity(model)
                       },
                   )
                   Text(
                       text = stringResource(R.string.homepage_body_use_case_2),
                       style = PicoTheme.typography.bodyLarge,
                       fontSize = 16.sp,
                       color = descriptionColor,
                   )
               }
           }
       }
   }
   ```


以上代码定义了页面的核心布局，其结构如下：

* **整体框架**：页面使用 `Column` 作为根布局，将所有内容自上而下垂直排列。
* **顶部区域**：包含标题和简介文字。
* **核心区域**：使用 `Row` 布局，将 2D 与 3D 内容水平并排，形成左右对比。
   * **左侧 (2D 内容)**：使用标准的 Jetpack Compose `Image` 组件展示一张静态图片，并配有文字说明。
   * **右侧 (3D 内容)**：通过 `SpatialView` 组件嵌入一个 3D 模型。该组件负责加载 `AssetBundle` 资源包、实例化模型、调整其位置和缩放，并最终将其添加到场景中。底部同样配有文字说明，与左侧形成对称。
2. **修改模板中的 2D 内容**

  在`app/src/main/java/.../content/HomePage.kt` 文件中：

   * 修改 `Text` 组件中 `text` 参数对应的字符串，你也可以尝试调整其他参数，个性化定制你的文字内容：
      ```Kotlin
      Text(
          ...
          text = "我的文字内容",
          ...
      )
      ```

   * 修改 `Image` 组件中 `painterResource` 参数对应的图片资源（假设你已经把一张名为 `my_image.png` 的图片放在 `app/src/main/res/drawable` 目录下，这里作为演示将使用一张木质小鸟摆件的图片），你也可以调整其他参数，修改图片的呈现效果：
      <a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ee2c83f85f564253b5f125f6ef79cecb~tplv-goo7wpa0wc-image.image" filename="my_image.png" download>my_image.png</a>
      ```Kotlin
      Image(
          ...
          painter = painterResource(id = R.drawable.my_image),
          contentDescription = "我的图片内容描述",
          ...
      )
      ```

    你可以再次运行 Spatial 项目查看修改后的效果。

3. **理解 3D 内容的显示过程**
   在 `app/src/main/java/.../content/HomePage.kt` 文件中，找到 `SpatialView` 这个 Composable 函数，它主要包含了一个初始化的步骤，进行了模型的加载、调整和添加至场景：
   ```Kotlin
   SpatialView(
       // 初始化 3D 场景的 lambda
       initial = { sceneContent, _ ->
           // 1. 加载资源包 (AssetBundle)
           val bundle = withContext(Dispatchers.IO) {
               AssetBundle.load("asset://editor-asset.bundle")
           }
       
           // 2. 加载模型实体 (Entity)
           // "MyScene" 是 Spatial Editor 中，USD 场景的名称
           val model = Entity.loadSuspend(modelName = "MyScene", bundle = bundle)
           bundle.close() // 加载完成后释放资源包
       
           // 3. 调整模型的 Transform
           model.getComponent<TransformComponent>()?.apply {
               setPosition(Vector3(0f, 0f, -0.2f)) // 设置模型 root 相对于 SpatialView 中心点的位置 (x, y, z)
               scaleBy(0.75f) // 设置缩放比例
           }
       
           // 4. 将模型添加到场景中
           sceneContent.addEntity(model)
       }
   )
   ```

   此处的 3D 模型加载自名为 `editor-asset.bundle` 的 AssetBundle，它是 Spatial Editor 项目成功构建后的产物。在你编译应用时，`com.pico.spatial.tools` Gradle 插件会自动执行此构建任务，并将生成的 `.bundle` 文件打包到 APK 的 `asset://` 目录下。因此，若要更改显示的 3D 内容，你只需在 Spatial Editor 项目中打开并修改对应的 3D 模型，保存更改后，再重新构建并运行应用即可。
4. **在 Spatial Editor 中打开 3D 内容**
   打开 `editor-asset/src/main/res3d/SpatialPackContent/ModelView` 文件，你会进入模型预览界面，点击右上角的 **Open In Editor**，你可以打开对应的 Spatial Editor 项目：

   在 Spatial Editor 中，展开左侧 **Hierarchy** 窗口的节点树，你会发现当前场景中使用的是一个名为 box.usdz 的模型，它存放在 `Sources/Assets` 目录下。

5. **在 Spatial Editor 中替换 3D 模型**
   点击右上角的 **Assets library** 图标打开 Spatial Editor 的资源库，找到并双击木质小鸟（Wooden Bird Ornament）。该资源会以 .usdz 文件的格式，被默认保存在 `Sources` 目录下并会被自动添加到当前场景中。接下来，你可以隐藏或删除初始的 box.usdz 模型完成模型替换。
   当你在 Spatial Editor 中修改场景后，相应的场景标签页右上角会出现一个星号（*），这表示你有未保存的更改。你必须手动保存这些修改。否则，当你返回 Android Studio 重新运行项目时，加载的将是未修改前的旧版本。

6.  **调整模型的 Transform**
   替换模型后，你可以参考下面的代码在 `app/src/main/java/.../content/HomePage.kt` 文件中通过 `TransformComponent` 调整场景的根节点的 Transform（位置、旋转、大小），确保其可以显示在合适的位置和角度。详情参阅《[AssetBundle](./spatial-sdk_资源管理_assetbundle.md)》了解场景节点的树状结构。
   ```Kotlin
   model.components[TransformComponent::class.java]?.apply {
       setPosition(Vector3(-0.04f, -0.05f, -0.2f))
       scaleBy(0.65f)
   }
   ```

   另外，你也可以在 Spatial Editor 中调整节点的 Transform。下图显示了如何在 Spatial Editor 中修改场景顶层节点（即下图中名为 **Root** 的节点）的 Transform。你可以在视口上方把 Spatial Container 设置为 Planar，模拟当前的 2D 平面窗口环境，然后通过所见即所得的方式进行修改。
   在 Planar 模板项目中，代码会调用 `setPosition()` 来修改 **场景根节点** 的 `TransformComponent`。需要注意的是，这里的 **场景根节点** 不是 Spatial Editor 中的场景顶层节点（例如下图中名为 **Root** 的节点），而是该场景顶层节点的 **父节点**。
   如果你同时在 Spatial Editor 中为场景顶层节点或模型节点设置了 Transform，那么 Spatial Editor 中的变换会与代码中的变换叠加，可能导致模型位置不符合预期。
   因此，若你决定使用 Spatial Editor 来调整模型的 Transform，需要注释掉代码中相关的 `TransformComponent` 设置，避免变换叠加。

   调整完成后，应用显示如下：

   模板项目中的 Planar Window Container 可以被理解为一个有边界的 2D 面板。这个面板不仅限制内容的宽度和高度，还为其中的 3D 内容设置了固定的厚度（当前为 `640.dp`）。任何超出这些边界（宽度、高度或厚度）的内容都将被裁剪。

## 预期结果
在这一步，你达成了以下目标：

* **理解窗口构成**：了解模板项目中默认窗口的内容，以及如何使用 PICO Spatial UI 结合 Jetpack Compose，将 2D 界面和 3D 内容融合在同一布局中。
* **验证修改能力**：重新构建并运行应用后，你应该会看到以下变化：
   * 窗口中的文字和左侧的 2D 图片已替换为你自己的内容。
   * 右侧的 3D 模型已更换，其位置和大小也已调整，但仍保留在同一面板布局中。

此步骤的重点是确认你已掌握修改 2D 与 3D 内容的基本方法，而不是实现复杂的功能。

---

# 第 3 步：创建并打开新的 Planar 窗口
**目标**：创建一个新的 Planar Window Container，并实现窗口的打开与关闭功能。
你已经熟悉了默认窗口的结构并改造了其内容。现在，你将为应用添加第二个窗口，把它变成一个多窗口应用。你将学习如何使用 DSL 来声明一个新窗口，并添加 `Button`，通过 `LocalSpatialNavigator` 控制窗口间的导航。
## 操作步骤

1. **使用 DSL 声明一个新的 Planar 窗口**
   打开 `app/src/main/java/.../Main.kt`，在 `DefaultWindowContainer` 之后声明一个名为 `SecondaryWindow` 的 `WindowContainer`：
   ```Kotlin
   package com.pico.spatial.sample.myapplication
   
   import com.pico.spatial.ui.design.PicoTheme
   import com.pico.spatial.ui.foundation.dsl.DefaultWindowContainer
   import com.pico.spatial.ui.foundation.dsl.SpatialAppScope
   import com.pico.spatial.sample.myapplication.content.HomePage
   
   // 新增以下 import
   import androidx.compose.foundation.layout.Box
   import androidx.compose.ui.unit.dp
   import com.pico.spatial.ui.foundation.dsl.Form
   
   import com.pico.spatial.ui.foundation.dsl.WindowContainer
   import com.pico.spatial.ui.foundation.dsl.WindowContainerSize
   import com.pico.spatial.ui.platform.resize.ContainerResizeRestriction
   import com.pico.spatial.ui.platform.resize.ContainerResizeType
   
   
   fun mainApp(scope: SpatialAppScope) = with(scope) {
       DefaultWindowContainer {
           PicoTheme { HomePage() }
       
       // [新增]声明一个新的 WindowContainer
       WindowContainer(
           id = "SecondaryWindow",
           form = Form.Planar,
           defaultSize = WindowContainerSize(width = 1280.dp, height = 720.dp),
           resizeType = ContainerResizeType.ContentSize,
           defaultResizeRestriction = ContainerResizeRestriction.UniformResizable,
           enableMaterialBackground = true
       ) {
           PicoTheme {
               // 新窗口的内容，临时使用 Box，之后进行替换
               Box {}
           }
       }
   }
   ```

   当你使用 DSL 声明非默认的 `WindowContainer` 时，你必须为它指定一个唯一的 `id`，并设置窗口内容。其他属性都是可选的；如果你不设置，SDK 会使用默认值。
   在上面的示例中，为了将新窗口设置为 Planar 类型，指定了 `form = Form.Planar`。同时，还通过 `defaultSize`、`resizeType` 和 `defaultResizeRestriction` 控制窗口的默认打开尺寸和缩放行为。
   如果你想进一步了解各个窗口属性的含义，请参阅《[声明 WindowContainer](./spatial-sdk_空间容器_管理-windowcontainer_声明-windowcontainer.md)》。
2. **为新窗口添加 2D 和 2.5D 内容**
   在上面设置新窗口的内容时，你暂时使用了一个 `Box{}`，现在你把它替换为想要的内容。在 `content` 包下新建 `SecondaryPage.kt`，然后粘贴以下代码：
   ```Kotlin
   package com.pico.spatial.sample.myapplication.content
   
   import androidx.compose.animation.core.LinearEasing
   import androidx.compose.animation.core.RepeatMode
   import androidx.compose.animation.core.animateFloat
   import androidx.compose.animation.core.infiniteRepeatable
   import androidx.compose.animation.core.rememberInfiniteTransition
   import androidx.compose.animation.core.tween
   import androidx.compose.foundation.layout.Arrangement
   import androidx.compose.foundation.layout.Column
   import androidx.compose.foundation.layout.fillMaxSize
   import androidx.compose.foundation.layout.padding
   import androidx.compose.runtime.Composable
   import androidx.compose.runtime.getValue
   import androidx.compose.ui.Alignment
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.text.font.FontWeight
   import androidx.compose.ui.unit.dp
   import androidx.compose.ui.unit.sp
   import com.pico.spatial.ui.design.Text
   import com.pico.spatial.ui.foundation.effect3d.rotate3D
   import com.pico.spatial.ui.foundation.geometry.Rotation3D
   import com.pico.spatial.ui.foundation.geometry.RotationAxis3D
   import com.pico.spatial.ui.foundation.layout.offset
   
   @Composable
   fun SecondaryPage(modifier: Modifier = Modifier) {
       // 设置无限循环动画，用于文字摆动效果
       val infiniteTransition = rememberInfiniteTransition(label = "text_rotation")
       val degree by infiniteTransition.animateFloat(
           initialValue = -7f,
           targetValue = 7f,
           animationSpec = infiniteRepeatable(
               animation = tween(durationMillis = 1500, easing = LinearEasing),
               repeatMode = RepeatMode.Reverse
           ),
           label = "degree"
       )
       // 垂直布局，内容居中并设置间距
       Column(
           modifier = modifier
               .fillMaxSize()
               .padding(32.dp),
           verticalArrangement = Arrangement.spacedBy(48.dp, Alignment.CenterVertically),
           horizontalAlignment = Alignment.CenterHorizontally
       ) {
           // 对该文字内容应用 3D 旋转效果
           Text(
               modifier = Modifier.rotate3D { Rotation3D(degree = degree, axis = RotationAxis3D.Z) },
               text = "🎊 Congratulations! 🎉",
               fontWeight = FontWeight.SemiBold,
               fontSize = 32.sp,
           )
   
           // 对该文字内容应用 3D 浮起效果
           Text(
               modifier = Modifier.offset(60.dp),
               text = "You've successfully opened a NEW Planar Window Container!",
               fontWeight = FontWeight.Medium,
               fontSize = 28.sp,
           )
       }
   }
   ```

   完成后，记得在 `Main.kt` 文件中，将占位的 `Box{}` 替换为 `SecondaryPage()` 并添加对应的 import 语句。
   ```Kotlin
   // ... 原 import 语句
   
   // 新增 import
   import com.pico.spatial.sample.myapplication.content.SecondaryPage
   
   fun mainApp(scope: SpatialAppScope) = with(scope) {
       DefaultWindowContainer {
           PicoTheme { HomePage() }
   
       WindowContainer(
           id = "SecondaryWindow",
           form = Form.Planar,
           defaultSize = WindowContainerSize(width = 1280.dp, height = 720.dp),
           resizeType = ContainerResizeType.ContentSize,
           defaultResizeRestriction = ContainerResizeRestriction.UniformResizable,
           enableMaterialBackground = true
       ) {
           PicoTheme {
               // 把 Box {} 替换为 SecondaryPage()
               SecondaryPage()
           }
       }
   }
   ```

   你刚刚为新窗口添加的内容包含一个垂直布局和两段文本，并利用 Spatial UI 特有的 `Modifier` 实现了以下空间效果：
      * **上方文字**：通过 3D 旋转动画，实现左右摆动的效果。
      * **下方文字**：通过 3D 浮起效果，在 Z 轴正方向（朝向屏幕外）浮起 `60.dp`。
   为了能看到这个新窗口，你还需要添加一种打开它的方法。
3. **在两个窗口添加控制打开/关闭的按钮**
   现在，你要在已有的两个窗口里分别添加一个按钮，用来控制新窗口的打开和关闭。回到 `HomePage.kt`，在 `Column` 布局底部增加一个按钮，并用 `SpatialNavigator` 实例打开新窗口。
   首先，你需要获取一个 `SpatialNavigator` 实例来控制窗口的打开。然后，修改 `Row` 布局，将 `fillMaxSize()` 改为 `fillMaxWidth()`，为下方的 `Button` 留出空间。最后，添加一个 `Button` 组件，设置其显示的文字，并在点击时通过名称打开新窗口。
   ```Kotlin
   // ... 原 import 语句
   
   // [新增] import 语句
   import androidx.compose.foundation.layout.fillMaxWidth
   import com.pico.spatial.ui.design.Button
   import com.pico.spatial.ui.platform.containers.LocalSpatialNavigator
   
   @Composable
   fun HomePage(modifier: Modifier) {
       // [新增]获取 SpatialNavigator 实例
       val navigator = LocalSpatialNavigator.current
   
       Column(
           modifier = modifier.padding(horizontal = 32.dp),
       ) {
           // ... 保留原有的 Text 布局
           Spacer(modifier = Modifier.height(20.dp))
           
           // [更新]将 Row 从 fillMaxSize() 改为 fillMaxWidth()，为 Button 留出空间
           Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
               ...
           }
           
           // [新增]将按钮推到底部
           Spacer(modifier = Modifier.weight(1f)) 
           // [新增]添加用于打开新窗口的按钮
           Button(
               modifier = Modifier.padding(bottom = 32.dp),
               onClick = {
                   // 使用之前定义的名字来打开新窗口
                   navigator.openWindowContainer("SecondaryWindow")
               }
           ) {
               Text("Open A New Planar Window Container")
           }
       }
   }
   ```

   接下来，前往 `SecondaryPage.kt` ，在底部添加一个按钮，用于关闭当前窗口。同样地，你需要先获取 `SpatialNavigator` 实例，用来控制窗口的关闭；然后在 `Column` 布局的底部，添加一个 `Button`，设置显示的文字，并设置在点击时关闭 `Button` 所在的当前窗口。如果需要关闭具有特定 id 和 tag 的窗口，需要在 `closeWindowContainer()` 中指定相关参数。如果你想了解更多有关窗口打开和关闭的信息，可以阅读《[打开或关闭 WindowContainer](./spatial-sdk_空间容器_管理-windowcontainer_打开或关闭-windowcontainer.md)》文档。
   ```Kotlin
   // ... 原 import 语句
   
   // [新增] import 语句
   import com.pico.spatial.ui.design.Button
   import com.pico.spatial.ui.platform.containers.LocalSpatialNavigator
   
   @Composable
   fun SecondaryPage(modifier: Modifier = Modifier) {
       // [新增]获取 SpatialNavigator 实例
       val navigator = LocalSpatialNavigator.current
       
       // ... 保留原有代码逻辑
       
       Column(
           modifier = modifier
               .fillMaxSize()
               .padding(32.dp),
           verticalArrangement = Arrangement.spacedBy(48.dp, Alignment.CenterVertically),
           horizontalAlignment = Alignment.CenterHorizontally
       ) {
           // ... 保留原有的 Text 布局
           
           // [新增]添加用于关闭当前窗口的按钮
           Button(onClick = {
               // 关闭当前窗口
               navigator.closeWindowContainer()
           }) {
               Text("Close Current Window Container")
           }
       }
   }
   ```


## 预期结果
再次构建并运行应用后，你将看到以下效果：

1. 主窗口下方会出现一个 **Open A New Planar Window Container** 按钮。
2. 点击该按钮，一个新的 Planar 窗口会弹出并显示在主窗口前方。此新窗口包含：
   * 顶部文字“🎊 **Congratulations!** 🎉”会左右摆动。
   * 中间文字 **You've successfully opened a NEW Planar Window Container!** 会从窗口表面浮起。要观察此效果，你可以凑近并从侧面查看。
   * 底部是一个 **Close Current Window Container** 按钮。
3. 点击 **Close Current Window Container** 按钮后，该窗口将关闭，主窗口会重新出现在视野中。

完成这一步后，你已经能创建新的 Planar 窗口，并且能成功地在窗口之间实现导航。
# 总结
恭喜你顺利完成本阶段教程！你已经掌握了 PICO Spatial SDK 的核心概念和基础操作：

* 空间应用的基础项目结构、应用入口和启动逻辑。
* 如何使用 `meta-data` 在 `AndroidManifest.xml` 中声明默认窗口的属性，并使用 DSL 在 `mainApp` 中定义默认及非默认窗口的内容和属性。
* 如何使用 Spatial UI 提供的 Composable 函数和 `Modifier` 构建包含 2D、2.5D 和 3D 内容的界面。

# 接下来
目前，你的应用仍局限于一个厚度固定的平面窗口，这可能导致 3D 内容因超出边界而被裁剪。在下一节教程中，你将学习如何让窗口拥有“体积”，并在其中置入可交互的 3D 对象。详情参阅《[第二阶段：加入 3D 窗口和模型](./spatial-tutorial_从模板开始搭建空间应用_第二阶段：加入-3d-窗口和模型.md)》。
## **延伸阅读**
如需深入了解本章所涉及的概念，推荐阅读以下文档：

* 《[项目结构与依赖配置](./spatial-sdk_项目结构与依赖配置.md)》：了解项目的模块划分与依赖管理方式。
* 《[声明 WindowContainer](./spatial-sdk_空间容器_管理-windowcontainer_声明-windowcontainer.md)》：学习如何声明默认与非默认窗口，并了解其所有可配置的属性。
* 《[为 2D 内容添加空间效果](./spatial-sdk_内容布局与呈现_为-2d-内容添加空间效果_tooltip.md)》：掌握如何使用 Spatial UI 为 2D 内容添加空间效果。
* 《[模型](./spatial-sdk_资源管理_模型.md)》、《[AssetBundle](./spatial-sdk_资源管理_assetbundle.md)》与《[添加 3D 内容](./spatial-sdk_内容布局与呈现_在-spatialmodelview-和-spatialview-中添加-3d-内容.md)》：了解 3D 资源的加载、管理与显示方法。
* 《[什么是 PICO Spatial Editor](./spatial-toolkit_pico-spatial-editor_什么是-pico-spatial-editor.md)》与《[管理 Spatial 项目](./spatial-toolkit_pico-spatial-plugin_管理-spatial-项目.md)》：深入了解 PICO Spatial Editor 的使用方法及 `com.pico.spatial.tools` 插件的工作原理。

