本文介绍如何在 Android Studio 中创建 Spatial 项目、把 Spatial Editor 项目导入到 Spatial 项目、基于 Spatial 项目构建一个空间应用，以及在 PICO Emulator 中调试 Spatial 项目。
## 什么是 Spatial 项目
安装 PICO Spatial 插件后，你可以在 Android Studio 中创建 **Spatial 项目**。Spatial 项目可以被构建为空间应用。
Spatial 项目是基于标准 Android 项目的扩展，用于支持 3D 空间内容的开发。它遵循 Android 的设计理念，将 3D 资源封装为独立的 Android 库模块。一个 Spatial 项目由一个主模块和一个或多个包含 **Spatial Editor 项目** 的库模块组成。Spatial Editor 项目是通过 Spatial Editor 创建的，用于为 Spatial 项目提供 3D 资源。详情参阅 [什么是 Spatial Editor](./spatial-toolkit_pico-spatial-editor_什么是-pico-spatial-editor.md)。
一个库模块只能包含一个 Spatial Editor 项目。你可以把外部的 Spatial Editor 项目作为库模块导入到 Spatial 项目中。详情参阅 [把 Spatial Editor 项目导入到 Spatial 项目](/editor/manage-projects)。

你新创建的 Spatial 项目默认包含一个主模块和一个名为 `editor-asset` 的库模块。在 Project 视图下，你可以看到 `editor-asset` 库模块包含了一个名为 `spatialPackContent` 的 Spatial Editor 项目。

## 创建 Spatial 项目
详情参阅以下步骤在 Android Studio 中创建一个 Spatial 项目。

1. 在 **Welcome to Android Studio** 页面单击 **New Spatial Project** 或访问 **File** > **New** > **New Spatial Project...**。

2. 在 **New Project** 页面，选择一个模板。模板包含样例代码和资源文件。选择后单击 **Next**。
   你可以选择以下类型的模版。每种模版使用了不同类型的空间容器。详情参阅 [了解空间容器 & 空间状态](./spatial-sdk_空间容器_了解空间容器-&-空间状态.md)。
   * **Planar Window Container**：一种厚度有限的、类似于 “平面面板” 的 WindowContainer。它主要用于承载传统 Android 开发中常见的 2D 界面，并可用于展示尺寸较小的 3D 对象。
   * **Volumetric Window Container**：是另一种以窗口形式呈现内容的容器，可以被理解为尺寸可动态调整的 “长方体”。相比厚度有限的 Planar 容器，Volumetric 占据更大的空间体积，能够承载更大尺寸的 3D 物体，从而在有限范围内最大化用户的 3D 交互体验。
   * **Full Stage**：Stage 可以被视为一块无边界限制的 ”场地“，支持放置更多内容，包括 UI 组件、2D 布局、3D 模型等。Stage 分为不同的样式，允许用户在不同沉浸度上与所处的真实环境进行交互。Full Stage 代表 Stage 的样式是 Full，即 `immersion` 为 100。在 Full Stage 下，应用将用户置于与真实环境完全隔离的虚拟环境中。

3. 配置项目的名称、包名、保存地址和最低 PICO OS 6 版本。然后单击 **Finish**。
   不同的 PICO OS 6 版本对应不同的 PICO Spatial SDK 版本。例如，PICO OS 6 v6.0 对应 PICO Spatial SDK 6.0.0。

## 把 Spatial Editor 项目导入到 Spatial 项目
详情参阅以下步骤在 Android Studio 中把 Spatial Editor 项目导入到 Spatial 项目。Spatial Editor 项目会作为一个类型为 **Spatial Resource Library** 的库模块被导入到 Spatial 项目。

1. 在 Android Studio 中选择 **File **> **** **New **> **** **New Module**。

2. 在 **Create New Module** 页面的 **Templates** 区域，选择 **Spatial Resource Library**，然后设置以下参数。
   | 参数 | 说明 |
   | --- | --- |
   | **New Spatial Editor Project** | 是否创建一个新的 Spatial Editor 项目。 ;; * **勾选**：创建一个新的 Spatial Editor 项目。 ;  * **不勾选**：导入已有的 Spatial Editor 项目。 |
   | **Editor project directory** | 需要导入的 Spatial Editor 项目的根目录。你可以直接输入地址，也可以点击右侧的文件夹图标选择 Spatial Editor 项目的根目录。如下图所示，Spatial Editor 项目的根目录就是 .spatialproject 文件所在的目录。 ;   |
   | **Module name** | 库模块名称，例如 mylibrary。 |
   | **Package name** | 库模块的包名，例如 com.example.mylibrary。 |
   | **Minimum OS version** | 最低 PICO OS 6 版本。不同的 PICO OS 6 版本对应不同的 PICO Spatial SDK 版本。例如，PICO OS 6 v0.13 preview 对应 PICO Spatial SDK 0.13.x。 |

3. 单击 **Finish**。你创建的 **Spatial Resource Library** 会出现在 Spatial 项目的 **Project** 视图中，同时也会被自动添加到settings.gradle.kts 文件中。

4. 在 app 的 `build.gradle.kts` 文件中添加一条 implementation 语句，引用你添加的 **Spatial Resource Library**。例如 `implementation(project(":mylibrary"))`。

## 构建 Spatial 项目
你在编译 Spatial 项目时，Gradle 会自动把 Spatial Editor 项目所在的库模块会打包为 .bundle 文件，然后再将 .bundle 文件打包到 APK 的 `assets` 文件夹中。因此，你可以像构建一个普通 Android 项目一样把一个 Spatial 项目构建为空间应用。例如，你可以把 Spatial 项目构建为 APK。

## 自定义 Spatial Editor 项目打包
在 Spatial 项目中，Spatial 插件会自动在 `editor-asset` 库模块的 `build.gradle` 文件中添加一个名为 Spatial Tools 的 Gradle 插件，其 ID 为 `com.pico.spatial.tools`。该插件来自 https://artifact.bytedance.com/repository/Volcengine。
```Kotlin
plugins {
    id 'com.pico.spatial.tools' version '0.13.1'
}
```

在  `editor-asset` 库模块的`build.gradle` 文件中，你可以对 Spatial Tools 的以下参数进行设置：

* **name**：指定 Spatial Editor 项目打包后生成的 .bundle 文件的名称。
* **spatialToolsVersion**：指定 Spatial 项目依赖的工具链版本，包括 Spatial Editor 和 PICO Emulator 的版本。
* **bundleOptions**：提供可选的打包配置。如果未配置此项，Gradle 将在每次构建时强制重新打包。
   * **forceBuild**：设置是否强制重新打包。
      *  **true**：每次构建都会重新打包。
      *  **false**：仅在 `name`、`spatialToolsVersion` 或 `files` 参数发生变化时才重新打包，否则将跳过此步骤以提高构建效率。这样就可以以 .bundle 文件为粒度实现增量打包。
   * **useBundleIncremental**：设置是否开启增量编译。
      *  **true**：开启增量编译。推荐开启以提升打包速度。
      *  **false**：关闭增量编译。
   * **files**：指定参与打包的资源文件。只有在此处声明的文件才会被打包，且必须至少包含一个 `.usda` 文件。
      * **include**：用于添加需要打包的特定文件或文件夹。

如果你修改了 Spatial Editor 项目中的资源文件，需要将 `forceBuild` 设置为 `true` 以强制重新打包，否则所做的修改将不会生效。

Gradle 依据 Spatial Tools 的参数将 `editor-asset` 库模块打包成符合要求的 .bundle 文件，并进一步将其打包到 APK 的 `assets` 文件夹中。 下面的示例代码展示了如何配置Spatial Tools 的参数。
```Kotlin
spatial {
    name = "editor-asset"
    spatialToolsVersion = 0.13
    
    
    bundleOptions {
        forceBuild = true
        useBundleIncremental = true
        
        files {
            include("/Sources/Assets/MyScene.usda")
            include("/Sources/Assets/box.usda")
        }
    }
}
```

另外，如果你向 Spatial 项目导入了其他的 Spatial Editor 项目，那么在这些 Spatial Editor 项目对应的库模块的 `build.gradle.kts` 文件中，Spatial Plugin 也会自动添加 id 为 `com.pico.spatial.tools` 的 Gradle Plugin。Gradle 也会依据这些 Gradle Plugin 所指定的参数，将这些新导入的 Spatial Editor 项目对应的库模块打包成符合要求的 .bundle 文件，并将其打包到 APK 的 assets 文件夹中。
例如，在下面的示例中，Spatial 项目中的两个 Spatial Editor 项目对应的库模块（mylibrary 和 editor-asset）都被打包为 .bundle 文件。然后，这些 .bundle 文件被打包到 APK 的 assets 文件夹中。

## 把 Spatial Editor 项目打包为多个 .bundle 文件
在开发大型项目时，为了实现按需加载和更精细的增量编译，建议你将资源按业务模块拆分到不同的 `.bundle` 文件中。下面的示例演示了如何将核心资源和 UI 资源分别打包。
```Kotlin
spatial {
    spatialToolsVersion = 0.13

    bundles {
        coreModule {
            bundleName = "core" 
            bundleOptions {
                files { include "Sources/Scenes/Core.usda" }
            }
        }
        uiModule {
            bundleName = "ui" 
            bundleOptions {
                files { include "Sources/Scenes/UI.usda" }
            }
        }
    }
}
```

## 在 PICO Emulator 中调试 Spatial 项目
安装 PICO Emulator 后，你可以使用 Android Studio 打开一个 Spatial 项目，选择需要运行的模块（如 app），然后单击 **Run** 或 **Debug** 按钮，即可构建你的 Spatial 项目，并将其安装到 PICO Emulator 中运行和调试。详情参阅 [添加和管理 PICO Emulator](manage-pico-emulator)。

