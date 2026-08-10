# getName | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / getName 
# getName
```kotlin
fun getName(): String
```
Gets the name of the  PhysicallyBasedMaterial . 
The name of the  PhysicallyBasedMaterial  is a read-only property, meaning it can only be retrieved and not modified programmatically. Typically, you can set or change the material's name using the Spatial Editor, allowing for easier identification and management of materials within the development environment. 
#### Return
The name of the  PhysicallyBasedMaterial . 
#### Throws
Illegal State Exception 
If this material is closed or invalid.