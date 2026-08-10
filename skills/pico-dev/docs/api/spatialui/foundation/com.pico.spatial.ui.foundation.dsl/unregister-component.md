# unregisterComponent | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / unregisterComponent 
# unregisterComponent
```kotlin
inline fun <T : Component> unregisterComponent()
```
Unregister previously registered custom  Component  type. 
This only stops the SDK from resolving/loading the corresponding custom component data from resource/asset files. It does NOT make the component type itself unusable: 
Note: this helper is a no-op on non-Spatial platforms. 
- 
You can still create and use it in code. 
- 
Existing instances are unaffected. 
- 
Call  registerComponent  again to enable loading/parsing from asset data.