# MassProperties | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / MassProperties 
# MassProperties
```kotlin
class MassProperties
```
Represents the mass properties of a rigid body. 
Members 
## Constructors
Mass Properties 
```kotlin
constructor(mass: Float = 1.0f, inertia: Vector3 = Vector3(0.1F), centerOfMass: Vector3 = Vector3(0F), orientationOfInertia: Quat = Quat(0F, 0F, 0F, 1F))
```
Constructs a  MassProperties  instance with default settings. 
```kotlin
constructor(other: MassProperties)
```
## Types
Companion 
```kotlin
object Companion
```
The companion object of  MassProperties . 
## Properties
center Of Mass 
```kotlin
var centerOfMass: Vector3
```
The center of mass of the  MassProperties  object. 
inertia 
```kotlin
var inertia: Vector3
```
The inertia of the  MassProperties  object, measured in kilogram-square meters (kg·m²). 
mass 
```kotlin
var mass: Float
```
The mass of the  MassProperties  object, measured in kilograms (kg). 
orientation Of Inertia 
```kotlin
var orientationOfInertia: Quat
```
The orientation of inertia of the  MassProperties  object. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```