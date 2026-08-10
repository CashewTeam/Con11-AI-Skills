本页涵盖编写 SpatialML 代码之前你需要准备的一切：硬件、项目设置、依赖项以及清单文件配置。面向的是运行在[空间模式](zh-concepts-spatial-mode)下、基于 PICO Spatial SDK 构建的 Kotlin 应用。
## 硬件与操作系统

* 一台**运行 PICO OS 6 的 PICO 设备**。SpatialML 会使用设备端的传感器和加速器。
* **PICO 模拟器**可以运行 SpatialML，但存在一些限制——参见[在模拟器上运行](#%E5%9C%A8%E6%A8%A1%E6%8B%9F%E5%99%A8%E4%B8%8A%E8%BF%90%E8%A1%8C)。
* 已启用 USB 调试，以便通过 `adb` 部署。

### 在模拟器上运行
PICO 模拟器提供基础的 SpatialML 支持，因此你可以在没有实体头显的情况下创建实例和会话、搭建管线、运行图。它适合用来打通代码、检查 API 接口，以及迭代图结构。
有些算子依赖模拟器不具备的物理传感器，在模拟器上无法产生真实数据：

* 透视相机访问 —— [rectifiedVSTAccess](zh-reference-operators-rectified-vst-access)。
* 深度 —— [getDepthMap](zh-reference-operators-get-depth-map)。
* 麦克风采集 —— [captureMicrophone](zh-reference-operators-capture-microphone)。
* 由它们派生出的任何内容（例如 [uvTo3DInCameraSpace](zh-reference-operators-uv-to-3d-in-camera-space)，它需要实时的 VST 图像和相机矩阵）。

对于依赖相机驱动或基于透视图像的机器学习功能——包括 [Pipeline Zoo](zh-workflows-use-pipeline-packages) 中诸如 [FaceDetection](zh-samples-face-detection) 之类的包——请部署到真实设备上以查看真实效果。
## 开发环境
在配置 SpatialML 之前，请先按照官方安装指南完成设置：

* [PICO Spatial SDK Setup Guide (Outside Chinese Mainland)](https://developer.picoxr.com/document/spatial-sdk/set-up-development-environment/)
* [PICO Spatial SDK Setup Guide (Chinese Mainland)](https://developer-cn.picoxr.com/document/spatial-sdk/set-up-development-environment/)

本仓库中的示例使用以下版本构建：
| 工具 | 版本 |
| --- | --- |
| Android Gradle Plugin | 8.9.1 |
| Kotlin | 2.0.21 |
| `compileSdk` / `targetSdk` | 35 |
| `minSdk` | 31 |
| PICO Spatial SDK BOM | 0.13.3 |
**API 级别**
SpatialML 的 API 标注了 `@RequiresApi(27)`。示例代码设置了 `minSdk = 31`；请让你的 `minSdk` 保持在这个值或你其他 Spatial SDK 用法所要求的值之上。
## Gradle 依赖
SpatialML 以两个制品（artifact）的形式发布，版本通过 Spatial SDK BOM 统一管理。先以 platform 方式添加 BOM，再依赖 ML 模块（以及 Spatial 应用所需的 core 和 UI 模块）。
```TOML
// gradle/libs.versions.toml
[versions]
spatialBom = "0.13.3"

[libraries]
spatial-bom          = { module = "com.pico.spatial:bom", version.ref = "spatialBom" }
spatial-core         = { group = "com.pico.spatial.core", name = "core" }
spatial-ml-securemr  = { group = "com.pico.spatial.ml",   name = "securemr" }
spatial-ml-readback  = { group = "com.pico.spatial.ml",   name = "readback" }
spatial-ui-platform  = { group = "com.pico.spatial.ui",   name = "platform" }
spatial-ui-foundation = { group = "com.pico.spatial.ui",  name = "foundation" }
spatial-ui-design    = { group = "com.pico.spatial.ui",   name = "design" }
```

```Kotlin
// app build.gradle.kts
dependencies {
    implementation(platform(libs.spatial.bom))
    implementation(libs.spatial.core)
    implementation(libs.spatial.ml.securemr)   // SpatialML pipeline API
    implementation(libs.spatial.ml.readback)   // readback extensions (Readback Mode)
    implementation(libs.spatial.ui.foundation)
    implementation(libs.spatial.ui.platform)
    implementation(libs.spatial.ui.design)
    // ... Compose, coroutines, lifecycle, etc.
}
```

| 制品 | 包 | 提供内容 |
| --- | --- | --- |
| `com.pico.spatial.ml:securemr` | `com.pico.spatial.ml.securemr` | `SpatialMLInstance`、`SpatialMLSession`、`Pipeline`、`Tensor`、`GlobalTensor`、各类算子 |
| `com.pico.spatial.ml:readback` | `com.pico.spatial.ml.readback` | `readbackContent`、`readbackAsTextureResource` 扩展函数、`TensorContent` |
只有在使用[回读模式](zh-concepts-secure-and-readback-modes)时才需要添加 `readback`。
**保持模型资源不被压缩**
如果你以 assets 形式随包分发模型或 glTF 文件，请禁用压缩，以便它们可以被内存映射（memory-mapped）：
```Kotlin
androidResources {
    noCompress.add(".glb")
    noCompress.add(".bundle")
}
```

## 清单文件配置
空间模式应用需要启用实验性的 SpatialML 接口，并声明一个空间窗口容器。核心配置如下：
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-feature android:name="android.hardware.camera" android:required="false" />
    <uses-permission android:name="android.permission.CAMERA" />        <!-- Readback Mode only -->
    <uses-permission android:name="android.permission.INTERNET" />      <!-- if you upload results -->
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <application android:name=".MainApplication" ...>

        <!-- opt into the SpatialML experimental API -->
        <meta-data android:name="pico.spatial.use_experimental_api" android:value="1" />

        <activity android:name=".MainActivity" android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <meta-data android:name="pico.spatial.windowcontainer.id" android:value="Home" />
            <!-- other pico.spatial.windowcontainer.* metadata as needed -->
        </activity>
    </application>
</manifest>
```

| 权限 | 什么时候需要 |
| --- | --- |
| `CAMERA` | 仅在[回读模式](zh-concepts-secure-and-readback-modes)下需要，此时处理后的相机数据会回到你的应用。[安全模式](zh-concepts-secure-and-readback-modes)不需要相机权限。 |
| `INTERNET` | 仅在应用需要把结果发送到设备之外时需要（例如示例中的 VQA 上传）。 |
| `POST_NOTIFICATIONS` | 标准的应用通知权限。 |
## 应用入口点
一个空间模式应用需要接好三部分（详见[空间模式](zh-concepts-spatial-mode)）：

* 一个启动 `DefaultWindowContainer`、承载你的 Compose UI 的 `Application`，
* 一个 `MainActivity : SpatialLaunchActivity()`，以及
* 同时创建 SpatialML 实体/场景的 Compose 内容。

## 验证你的配置

1. 构建并部署到 PICO 设备：在 Android Studio 中**运行 'app'**，或执行 `./gradlew installDebug`。
2. 按 `SpatialML` 标签过滤 logcat，查看 instance/session/pipeline 相关日志。
3. 确认应用启动后进入的是空间 shell（而不是平面 Activity）。

应用运行起来之后，继续阅读[第一个 SpatialML 场景](zh-getting-started-first-spatialml-scene)。
## 延伸阅读

* [第一个 SpatialML 场景](zh-getting-started-first-spatialml-scene) —— 一个最小的端到端图。
* [空间模式](zh-concepts-spatial-mode) —— 空间模式应用的组织结构。
* [安全模式与回读模式](zh-concepts-secure-and-readback-modes) —— 在开始构建之前先选择隐私路径。

