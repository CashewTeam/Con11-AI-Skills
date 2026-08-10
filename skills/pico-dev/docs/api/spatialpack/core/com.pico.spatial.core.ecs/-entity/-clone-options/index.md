# CloneOptions | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / CloneOptions 
# CloneOptions
```kotlin
class CloneOptions(val recursive: Boolean = false, val shouldShareMaterialInstance: Boolean = false)
```
Represents options for cloning operations. 
Members 
## Constructors
Clone Options 
```kotlin
constructor(recursive: Boolean = false, shouldShareMaterialInstance: Boolean = false)
```
## Properties
recursive 
```kotlin
val recursive: Boolean
```
Indicates whether the cloning should be performed recursively. If  true , all child objects will also be cloned. 
should Share Material Instance 
```kotlin
val shouldShareMaterialInstance: Boolean
```
Indicates whether the material instance should be shared. If  true , the material instance will be shared between the original and the cloned object.