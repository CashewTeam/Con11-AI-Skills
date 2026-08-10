纹理为 3D 模型提供表面细节和视觉效果，是材质系统的重要组成部分。
## 支持的图像格式
目前支持以下标准动态范围（SDR）图像格式：

* **PNG** - 支持透明通道，适合需要 alpha 通道的贴图；
* **JPEG** - 压缩率高，适合漫反射贴图等不需要透明度的场景；
* **WebP** - 现代压缩格式，在保持质量的同时提供更小的文件大小；
* **KTX** - 专为 GPU 优化的纹理格式，支持压缩纹理。
* **EXR** - 高动态范围（HDR）格式，支持多通道和无损压缩，适用于影视后期处理、3D 渲染等领域。详情如下：
   | **技术项** | **支持情况与说明** |
   | --- | --- |
   | type | **Scan line images**（扫描线图像）：当前仅支持按行存储与读取的图像流。 |
   | compression | 当前支持以下无损压缩算法： ;; * NO_COMPRESSION：无压缩 ;  * RLE_COMPRESSION：适用于连续色块 ;  * ZIPS_COMPRESSION：单行块压缩 ;  * ZIP_COMPRESSION：16 行块压缩，适合低噪点 CG 图像 ;  * PIZ_COMPRESSION：基于小波算法的压缩方式，对高噪点图像表现更佳 |
   | channels | **RGB 基础色彩通道**：当前仅支持 RGB 三通道存储，可满足大多数色彩数据交换需求。 |
   | part | **singlepart**（单部分文件）：当前仅支持单图像结构文件。 |

## 使用限制
纹理内存大小受最大分辨率的影响如下：

* **单张纹理内存上限**：256MB，建议根据实际使用场景优化贴图分辨率，避免不必要的内存消耗
* **2D 纹理最大分辨率**：16384 × 16384
* **3D 纹理最大分辨率**：2048 × 2048 × 2048
* **Cubemap 纹理最大分辨率**：16384

* 根据 256MB 的内存限制以及纹理的压缩格式，系统会动态调整纹理的分辨率上限，而非固定使用上述的最大分辨率。
* 当纹理内存超过限制时，系统将输出错误日志并返回相应错误代码。

2D 纹理的压缩格式与内存占用示例如下：
| **压缩格式** | **是否有 Mipmap** | **最大分辨率** | **内存占用** |
| --- | --- | --- | --- |
| RGBA8 | 无 | 8192 × 8192 | ≤ 256MB |
| ASTC 4×4 | 无 | 16384 × 16384 | ≤ 256MB |
## 加载纹理
你可以通过静态函数 `TextureResource.load` 从文件中加载纹理数据，该函数直接返回一个 `TextureResource` 实例。调用时，指定 `path` 和 `loadType` 即可。
```Kotlin
fun load(path: String, loadType: LoadType = LoadType.FROM_ASSETS): TextureResource
```

你可以从 /app/src/main/assets 目录或设备文件系统加载纹理，对应的加载类型分别为 `LoadType.FROM_ASSETS` 和 `LoadType.FROM_STORAGE`，文件路径须满足以下要求：

* 如果加载类型为 `LoadType.FROM_ASSETS`，文件路径必须是相对于 /app/src/main/assets 目录的路径；
* 如果加载类型为 `LoadType.FROM_STORAGE`，文件路径必须是文件在设备存储中的绝对路径。

例如，要使用上述两种方式从 /app/src/main/assets/texture/your_custom_texture_map.png 文件中加载纹理，可以使用以下代码：
```Kotlin
fun loadTextureResourceExample(context: Context) {
    val subFolderName = "texture"
    val fileName = "your_custom_texture_map.png"
    // 从 /app/src/main/assets 目录中加载网格
    val textureFromAssets =
        TextureResource.load(path = "${subFolderName}/${fileName}", loadType = LoadType.FROM_ASSETS)

    // 将文件从 /app/src/main/assets 目录复制至设备的文件系统
    val outFile = File(context.filesDir, fileName)
    context.assets.open("${subFolderName}/${fileName}").use { inputStream ->
        FileOutputStream(outFile).use { outputStream ->
            inputStream.copyTo(outputStream)
            outputStream.flush()
        }
    }
    // 从设备的文件系统中加载网格
    val textureFromStorage = TextureResource(outFile.absolutePath, LoadType.FROM_STORAGE)
}
```

如果需要控制纹理加载相关的更精细的参数，可以使用以下重载后的 `load` 函数：
```Kotlin
public fun load(
    path: String,
    loadType: LoadType = LoadType.FROM_ASSETS,
    option: TextureCreateOption = TextureCreateOption(),
): TextureResource
```

其中，`option` 参数是一个 `TextureOption` 对象，你可以通过该对象设置纹理贴图的名称、颜色空间、是否使用 gamma 校正、是否生成 mipmap 等。
例如，在加载前文同样的纹理贴图时，可选择为其添加 `option` 参数，进行一些额外配置：
```Kotlin
fun loadTextureWithOptionExample(context: Context) {
    val subFolderName = "texture"
    val fileName = "your_custom_texture_map.png"
    // 从 /app/src/main/assets 目录加载纹理，携带 option 参数配置
    val textureFromAssets =
        TextureResource.load(
            path = "${subFolderName}/${fileName}",
            loadType = LoadType.FROM_ASSETS,
            option =
                TextureCreateOption().apply {
                    name = "your_texture_name" // 若未设置纹理的名称，则为 null
                    useGamma = false // 若未设置是否使用 gamma 校正，则默认为 true（使用）
                    colorSpace = TextureColorSpace.RAW // 若未设置纹理的颜色空间，则默认使用 extureColorSpace.SRGB
                    mipmapMode = TextureMipmapMode.NONE // 若未设置 mipmap 模式，则默认使用 TextureMipmapMode.GENERATE_ALL
                }
        )
}
```

## 创建纹理
你可以通过使用 SDK 所支持格式的纹理贴图或位图（bitmap）来创建纹理资源。
### 使用纹理贴图创建纹理
使用纹理贴图创建纹理时，你可以选择从 /app/src/main/assets 目录或设备文件系统获得图像文件，对应的加载类型分别为 `LoadType.FROM_ASSETS` 和 `LoadType.FROM_STORAGE`，文件路径须满足以下要求：

* 如果加载类型为 `LoadType.FROM_ASSETS`，文件路径必须是相对于 /app/src/main/assets 目录的路径；
* 如果加载类型为 `LoadType.FROM_STORAGE`，文件路径必须是文件在设备存储中的绝对路径。

```Kotlin
fun createTextureResourceExample(context: Context) {
    /**
     * 从纹理贴图创建纹理
     */
    val subFolderName = "texture"
    val fileName = "your_custom_texture_map.png"
    // 从 /app/src/main/assets 目录创建纹理
    val textureFromAssets =
        TextureResource(path = "${subFolderName}/${fileName}", loadType = LoadType.FROM_ASSETS)

    // 将文件从 /app/src/main/assets 目录复制至设备的文件系统
    val outFile = File(context.filesDir, fileName)
    context.assets.open("${subFolderName}/${fileName}").use { inputStream ->
        FileOutputStream(outFile).use { outputStream ->
            inputStream.copyTo(outputStream)
            outputStream.flush()
        }
    }
    // 从设备的文件系统创建纹理
    val textureFromStorage = TextureResource(outFile.absolutePath, LoadType.FROM_STORAGE)

}
```

在使用纹理贴图创建纹理资源时，可以添加 `option` 参数来进行额外的配置。
```Kotlin
fun createTextureWithOptionExample(context: Context) {
    val subFolderName = "texture"
    val fileName = "your_custom_texture_map.png"
    // Create texture from assets with option
    val textureFromAssets =
        TextureResource(
            path = "${subFolderName}/${fileName}",
            loadType = LoadType.FROM_ASSETS,
            option =
                TextureCreateOption().apply {
                    name = "your_texture_name"
                    useGamma = true
                    colorSpace = TextureColorSpace.SRGB
                    mipmapMode = TextureMipmapMode.GENERATE_ALL
                }
        )
}
```

### 使用 bitmap 创建纹理
PICO Spatial SDK 支持使用以下格式的 bitmap 来创建纹理资源。
| **格式** | **描述** |
| --- | --- |
| ALPHA_8 | 单通道透明度，每个像素仅存储 alpha 值占用的 1 字节。该格式适用于高效存储无需颜色信息的纹理，例如蒙板。 |
| RGB_565 | 紧凑型 RGB 格式，每个像素占用 2 字节（红/蓝 5 位，绿 6 位）。该格式适用于不透明、且对色彩保真度要求不高的纹理。该格式可能导致轻微色偏，需配合抖动算法进行优化。 |
| ARGB_8888 | 标准全彩格式，每个像素占用 4 字节，R、G、B 和 A 四个通道各为 8 位精度。该格式提供最佳画质和灵活性。 |
| RGBA_F16 | 高精度浮点格式，每个像素占用 8 字节，R、G、B 和 A 四个通道采用半精度浮点存储。该格式适用于广色域和 HDR 内容。 |
| HARDWARE | 硬件加速格式，纹理直接存储在显存中且不可修改。该格式适用于屏幕绘制，提供最佳渲染性能。 |
| RGBA_1010102 | 高色深紧凑格式，每个像素占用 4 字节（R、G 和 B 各 10 位，alpha 2 位）。在与 ARGB_8888 格式占用相同内存的前提下，该格式提供更高的色彩精度，适用于无需 alpha 混合的广色域和 HDR 内容。 |
假设 bitmap 文件的路径为 /app/src/main/assets/texture/your_custom_texture_map.png，可以使用以下代码创建纹理：
```Kotlin
fun createTextureResourceExample(context: Context) {  
    val bitmap = createBitmap(200, 100, Bitmap.Config.ARGB_8888)
    val textureFromBitmap = TextureResource.create(bitmap)
}
```

## API 参考
`TextureResource` 类提供相关的函数，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)

