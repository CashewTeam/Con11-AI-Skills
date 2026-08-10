本文档介绍如何在你的 Spatial 项目中把 PICO Spatial SDK 的版本从 0.13.3 升级到 6.0.0。
## 更新 Spatial 项目配置
按照以下步骤修改配置：

1. **更新 PICO Spatial SDK 的 BOM 版本**
   在 `gradle/libs.versions.toml` 中，将 PICO Spatial SDK 的 BOM 版本（对应 `"com.pico.spatial:bom"`）更新为 `"6.0.0"`。
   ```TOML
   [versions]
   spatialBom = "6.0.0"
   ```

   如果你未使用版本目录（version catalogs），请在模块级 `build.gradle.kts` 文件的 `dependencies{}` 代码块中更新 BOM 版本。

2. **更新 Spatial Tools 的版本**
   如果你使用了 `editor-asset` 模块，则需要在 `editor-asset` 的模块级 `build.gradle` 文件中，更新 `'com.pico.spatial.tools'` 和 `spatialToolsVersion` 的版本。
   ```Groovy
   plugins {
       ...
       id 'com.pico.spatial.tools' version '6.0.0'
   }
   
   spatial {
       name = "editor-asset"
       spatialToolsVersion = 6.0
   }
   ```


## 更新空间手势回调
`detectSpatialDragGesture` 、`detectSpatialRotateGesture` 和 `detectSpatialScaleGesture` 的 `onStart`、`onEnd`、`onCancel` 回调由无参 lambda 变更为携带手势数据。你需要为这些回调补充手势值参数：
```Kotlin
// 旧版
detectSpatialDragGesture(
    context = context,
    onDragStart = { offset -> /* ... */ },
    onDragEnd = { /* ... */ },
    onDragCancel = { /* ... */ },
    onDrag = { value -> /* ... */ },
)

// 新版：start/end/cancel 回调现在也会收到 SpatialDragValue
detectSpatialDragGesture(
    context = context,
    onDragStart = { offset, value -> /* ... */ },
    onDragEnd = { value -> /* ... */ },
    onDragCancel = { value -> /* ... */ },
    onDrag = { value -> /* ... */ },
)
```

`detectSpatialRotateGesture` 与 `detectSpatialScaleGesture` 的迁移方式相同：`onRotateStart/End/Cancel` 现在接收 `SpatialRotateValue`，`onScaleStart/End/Cancel` 现在接收 `SpatialScaleValue`。
## 更新 SpatialML 推理类型
若此前使用 `Pipeline.ModelInferenceType.QNN_HTP`，请改用 LiteRT 后端（`LITE_RT_CPU` / `LITE_RT_GPU` / `LITE_RT_NPU`）或默认推理类型。

