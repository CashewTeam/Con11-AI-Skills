# LocalSpatialContainerStateManager | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / LocalSpatialContainerStateManager 
# LocalSpatialContainerStateManager
```kotlin
val LocalSpatialContainerStateManager: ProvidableCompositionLocal<SpatialContainerStateManager>
```
The CompositionLocal containing the  SpatialContainerStateManagerImpl  of current  com.pico.spatial.core.container.SpatialContainer . 
If your @Preview function depends on this, look  SpatialLocalsForPreview .