# TransformComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / TransformComponent 
# TransformComponent
```kotlin
@MainThread
```class  TransformComponent  :  Component 
A  Component  that manipulates the scale, rotation, and position of the entity. 
Members 
## Constructors
Transform Component 
```kotlin
constructor()
```
The default constructor. 
```kotlin
constructor(transform: Transform)
```
Creates a  TransformComponent  initialized with the values from the given  Transform . 
```kotlin
constructor(position: Vector3, rotation: EulerAngles, scale: Vector3)
```
Creates a  TransformComponent  with the specified position, rotation, and scale. 
```kotlin
constructor(position: Vector3, rotation: Quat, scale: Vector3)
```
Creates a  TransformComponent  with the specified position, rotation, and scale. 
## Properties
euler Angles 
```kotlin
var eulerAngles: EulerAngles
```
Euler angles in local space used to control the transform. Default is  EulerAngles(0f, 0f, 0f) . 
position 
```kotlin
var position: Vector3
```
The position in the local coordinate which is used to control the transform. The default value is  Vector3(0F, 0F, 0F) , measured in meters (m). 
quaternion 
```kotlin
var quaternion: Quat
```
Quaternion in local space used to control the transform. Default is  Quat.identity() . 
scale Vector 
```kotlin
var scaleVector: Vector3
```
The scale vector in the local coordinate which is used to control the transform. The default value is  Vector3(1F, 1F, 1F) . 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get Local Matrix 
```kotlin
fun getLocalMatrix(): Matrix4
```
Gets the local matrix of the  TransformComponent . 
hash Code 
```kotlin
open override fun hashCode(): Int
```scale By 
```kotlin
fun scaleBy(factor: Float): TransformComponent
```
Scales the current  TransformComponent  by the given factor. 
set Euler Angles 
```kotlin
fun setEulerAngles(eulerAngles: EulerAngles): TransformComponent
```
Sets the eulerAngles of the  TransformComponent . 
set Position 
```kotlin
fun setPosition(position: Vector3): TransformComponent
```
Sets the location of the  TransformComponent . 
set Quaternion 
```kotlin
fun setQuaternion(quaternion: Quat): TransformComponent
```
Sets the quaternion for the TransformComponent. 
set Scale Vector 
```kotlin
fun setScaleVector(scaleVector: Vector3): TransformComponent
```
Sets the scale vector of the  TransformComponent . 
to String 
```kotlin
open override fun toString(): String
```