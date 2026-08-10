# offsetByTranslationAndRotation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShapeResource / offsetByTranslationAndRotation 
# offsetByTranslationAndRotation
```kotlin
fun offsetByTranslationAndRotation(rotation: Quat, translation: Vector3): ShapeResource
```
Creates a new  ShapeResource  by applying both a rotation and a translation. 
#### Return
A new  ShapeResource  with the rotation and translation applied. 
#### Parameters
rotation 
The rotation quaternion to apply. 
translation 
The translation vector to apply. 
#### Throws
Illegal State Exception 
If this resource is closed or invalid. 
```kotlin
fun offsetByTranslationAndRotation(eulerAngles: EulerAngles, translation: Vector3): ShapeResource
```
Creates a new  ShapeResource  by applying both a rotation (as euler angles) and a translation. 
#### Return
A new  ShapeResource  with the eulerAngles and translation applied. 
#### Parameters
euler Angles 
The rotation to apply as  EulerAngles . 
translation 
The translation  Vector3  to apply. 
#### Throws
Illegal State Exception 
If this resource is closed or invalid.