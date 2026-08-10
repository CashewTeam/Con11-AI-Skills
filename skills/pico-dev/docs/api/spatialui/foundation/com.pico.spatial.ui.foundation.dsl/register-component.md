# registerComponent | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / registerComponent 
# registerComponent
```kotlin
inline fun <T : Component> registerComponent()
```
Register custom  Component  type. 
This enables the SDK to resolve/load the corresponding custom component data from resource/asset files. 
Note: this helper is a no-op on non-Spatial platforms. 
It does NOT automatically create/attach components, and is not required if you only create and use the component instances in code.