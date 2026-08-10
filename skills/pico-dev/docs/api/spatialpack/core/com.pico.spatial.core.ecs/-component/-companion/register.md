# register | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Component / Companion / register 
# register
```kotlin
@JvmStatic
```fun  register ( clazz :  Class < out  Component > ) 
Registers a custom component class. 
This method affects resolving custom component types when loading/parsing component data from resource/asset files. After calling this, the SDK can map the corresponding custom component "type" from asset data to  clazz . 
It does NOT automatically create/attach components, and is not required if you only create and use the component instances in code. 
Call  unregister  to stop loading/parsing this custom component from asset data. 
#### Parameters
clazz 
The custom component class to register.