# BoundingBox | PICO Spatial SDK

core / com.pico.spatial.core.ecs / BoundingBox 
# BoundingBox
```kotlin
class BoundingBox
```
Represents the bounding box for 3D content. All measurements are expressed in meters (m). 
This class represents an Axis-Aligned Bounding Box (AABB), which is a bounding box whose edges are always aligned with the coordinate axes. It is defined by its center position and half extent, making it symmetrical along each axis. 
Key characteristics: 
- 
Axis-aligned: The bounding box is always aligned with the coordinate axes, without any rotation or skew. 
- 
Symmetrical: The bounding box is defined by its center ( center ) and half extent ( halfExtent ), ensuring symmetry along all axes. 
- 
Precision: All calculations have a precision error of 0.00001F. 
Members 
## Constructors
Bounding Box 
```kotlin
constructor(center: Vector3 = Vector3.ZERO, halfExtent: Vector3 = Vector3.ZERO)
```
## Properties
bounding Sphere Radius 
```kotlin
val boundingSphereRadius: Float
```
The radius of the bounding sphere that circumscribes the bounding box. Precision error: 0.00001F. 
center 
```kotlin
val center: Vector3
```
The center of the bounding box. Precision error: 0.00001F. 
half Extent 
```kotlin
val halfExtent: Vector3
```
The half extent of the bounding box. Precision error: 0.00001F. 
max 
```kotlin
val max: Vector3
```
The maximum coordinate vertex of the bounding box. Precision error: 0.00001F. 
min 
```kotlin
val min: Vector3
```
The minimum coordinate vertex of the bounding box. Precision error: 0.00001F. 
size 
```kotlin
val size: Vector3
```
The size of the bounding box, represented as a vector. Precision error: 0.00001F. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```is Empty 
```kotlin
fun isEmpty(): Boolean
```
Checks if the bounding box is empty. 
to String 
```kotlin
open override fun toString(): String
```