# getLookAtTargetType | PICO Spatial SDK

core / com.pico.spatial.core.ecs / LookAtComponent / getLookAtTargetType 
# getLookAtTargetType
```kotlin
fun getLookAtTargetType(): LookAtTargetType
```
Gets the type of target currently set for the entity's "look at" behavior. 
#### Return
The type of target (viewer or entity) or  LookAtTargetType.NONE  if no target is set.