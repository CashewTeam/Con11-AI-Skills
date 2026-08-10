Kotlin Spatial SDK 中的 SpatialML 运行在 **空间模式（Spatial mode）**下：你的应用被启动到 PICO 空间 shell 中，由 SpatialEngine 渲染，SpatialML 的输出也应用在同一个空间场景上。本页说明"空间模式"对你组织应用结构意味着什么，以及 SpatialML 在其中处于什么位置。
**为什么这很重要**
在其他平台上，SpatialML 还有一种 *XR 模式*，应用渲染自己的内容，SpatialML 绘制到应用自有的 glTF 表面上。而这里所记录的 Kotlin Spatial SDK 路径**完全是空间模式**——不存在需要你自行喂数据的应用管理渲染循环。输出要么表现为对 SpatialEngine 场景图的更改，要么以[回读](concepts-secure-and-readback-modes)形式进入你的应用。
## 空间模式应用长什么样
一个空间模式下的 SpatialML 应用就是一个基于 Spatial SDK 构建的普通 Android 应用：

* Activity 继承自 [SpatialLaunchActivity](https://developer.picoxr.com/document/spatial-sdk/)：
   ```kotlin
   class MainActivity : SpatialLaunchActivity()
   ```

* 应用声明一个空间窗口容器（spatial window container），并在其中承载 Jetpack Compose UI：
   ```kotlin
   class MainApplication : Application() {
       override fun onCreate() {
           super.onCreate()
           launch {
               DefaultWindowContainer {
                   Box(Modifier.windowConstraints(width = 640.dp, height = 640.dp)) {
                       MainContainer()
                   }
               }
           }
       }
   }
   ```

* 清单文件（manifest）启用实验性的 SpatialML 接口，并声明空间窗口容器：
   ```xml
   <meta-data android:name="pico.spatial.use_experimental_api" android:value="1" />
   <meta-data android:name="pico.spatial.windowcontainer.id" android:value="Home" />
   ```


完整的清单文件和 Gradle 设置请参见[前置条件](getting-started-prerequisites)。
## SpatialML 处于什么位置
SpatialML 独立于你的 Compose UI。你创建一个 [SpatialMLInstance](reference-core-api#spatialmlinstance)，打开一个[会话](reference-core-api#spatialmlsession)，然后运行[管线](reference-core-api#pipeline)。输出通过以下两种方式之一到达用户：

* **场景图输出** —— 管线更新一个 SpatialML 从 glTF 资源加载的场景（[newSceneFromGLTF](reference-core-api#spatialmlsession)），使用诸如 [updateSceneGraphProperty](reference-operators-update-scene-graph-property) 和 [switchSceneVisibility](reference-operators-switch-scene-visibility) 之类的算子。这种方式让源自相机的像素始终留在运行时内部；参见[安全模式](concepts-secure-and-readback-modes)。
* **回读到应用** —— 管线写入一个[全局张量](concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F)，你的应用通过[回读 API](workflows-read-back-results)把结果取出来，然后自行将其应用到一个 SpatialEngine 实体上（例如作为材质的基础色纹理）。

安全模式的场景输出受限于会话的 [SpatialML 容器](concepts-containers-and-portals)。常规 Volume 会在其盒子处裁剪内容；启用 Portal 的 Volume 适用于相机锚定的追踪输出——当此类输出必须在该边界之外保持可见时。
[SuperResolutionApp](samples-super-resolution) 在一个应用中同时演示了这两条路径。
## 两种 SpatialEngine 表面
由于一切都运行在空间模式下，有必要弄清楚这里涉及的两个不同场景表面：
| 表面 | 归属者 | SpatialML 如何触及它 |
| --- | --- | --- |
| **SpatialML 场景** | 运行时，通过 `newSceneFromGLTF` 加载 | 由管线通过场景图算子直接驱动。内容在安全模式下始终受到保护。 |
| **应用实体** | 你的应用，使用 `Entity.load(...)` / Spatial `content` DSL 创建 | 在[回读](workflows-read-back-results)之后由你的应用代码更新。需要回读模式以及相应的权限。 |
你可以按功能选择使用哪个表面。二者之间的隐私权衡是下一页的主题。
## 延伸阅读

* [安全模式与回读模式](concepts-secure-and-readback-modes) —— 选择输出路径与隐私边界。
* [容器与传送门](concepts-containers-and-portals) —— 比较 Planar、常规 Volume、Portal 和 Disabled 容器。
* [驱动场景图输出](workflows-drive-scene-graph-output) —— 从管线更新 SpatialEngine 内容。
* [将数据回读到应用](workflows-read-back-results) —— 把结果取回到应用代码中。

