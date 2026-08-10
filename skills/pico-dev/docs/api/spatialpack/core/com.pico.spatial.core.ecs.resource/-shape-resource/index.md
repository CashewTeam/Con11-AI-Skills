# ShapeResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShapeResource 
# ShapeResource
```kotlin
class ShapeResource : Resource
```
Represents a shape resource. 
Members 
## Types
Companion 
```kotlin
object Companion
```
Static functions for  ShapeResource  generator. 
## Functions
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies. 
offset By Rotation 
```kotlin
fun offsetByRotation(eulerAngles: EulerAngles): ShapeResource
```
Creates a new  ShapeResource  by applying the specified rotation using euler angles. 
```kotlin
fun offsetByRotation(rotation: Quat): ShapeResource
```
Creates a new  ShapeResource  by applying the specified rotation. 
offset By Translation 
```kotlin
fun offsetByTranslation(translation: Vector3): ShapeResource
```
Creates a new  ShapeResource  by applying the specified translation. 
offset By Translation And Rotation 
```kotlin
fun offsetByTranslationAndRotation(eulerAngles: EulerAngles, translation: Vector3): ShapeResource
```
Creates a new  ShapeResource  by applying both a rotation (as euler angles) and a translation. 
```kotlin
fun offsetByTranslationAndRotation(rotation: Quat, translation: Vector3): ShapeResource
```
Creates a new  ShapeResource  by applying both a rotation and a translation.