# offsetByRotation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShapeResource / offsetByRotation 
# offsetByRotation
```kotlin
fun offsetByRotation(rotation: Quat): ShapeResource
```
Creates a new  ShapeResource  by applying the specified rotation. 
#### Return
A new  ShapeResource  with the rotation applied. 
#### Parameters
rotation 
The rotation quaternion to apply. 
#### Throws
Illegal State Exception 
If this resource is closed or invalid. 
```kotlin
fun offsetByRotation(eulerAngles: EulerAngles): ShapeResource
```
Creates a new  ShapeResource  by applying the specified rotation using euler angles. 
#### Return
A new  ShapeResource  with the rotation applied. 
#### Parameters
euler Angles 
The rotation to apply as  EulerAngles . 
#### Throws
Illegal State Exception 
If this resource is closed or invalid.