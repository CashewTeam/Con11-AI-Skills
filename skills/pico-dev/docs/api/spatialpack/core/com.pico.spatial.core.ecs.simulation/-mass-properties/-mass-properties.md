# MassProperties | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / MassProperties / MassProperties 
# MassProperties
```kotlin
constructor(mass: Float = 1.0f, inertia: Vector3 = Vector3(0.1F), centerOfMass: Vector3 = Vector3(0F), orientationOfInertia: Quat = Quat(0F, 0F, 0F, 1F))
```
Constructs a  MassProperties  instance with default settings. 
#### Parameters
mass 
The mass in kilograms. The default value is  1 . 
inertia 
The inertia in kilograms per square meter. The default value is  Vector3(0.1F, 0.1F, 0.1F) . 
center Of Mass 
The position of the center of mass. The default value is  Vector3(0F, 0F, 0F) . 
orientation Of Inertia 
The orientation of the principal axes. The default value is  Quat(0F, 0F, 0F, 1F) . 
```kotlin
constructor(other: MassProperties)
```