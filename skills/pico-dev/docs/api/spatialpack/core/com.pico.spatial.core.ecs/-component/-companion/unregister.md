# unregister | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Component / Companion / unregister 
# unregister
```kotlin
@JvmStatic
```fun  unregister ( clazz :  Class < out  Component > ) 
Unregisters a previously registered custom component class. 
This method only affects resolving custom component types when loading/parsing component data from resource/asset files. After calling this, the SDK will stop mapping the corresponding custom component "type" from asset data to  clazz . 
It does NOT make the component type itself unusable: 
- 
You can still create the component instance and use it in code. 
- 
Existing instances/components already attached to entities are unaffected. 
- 
Call  register  again to enable loading/parsing from asset data. 
#### Parameters
clazz 
The custom component class to unregister.