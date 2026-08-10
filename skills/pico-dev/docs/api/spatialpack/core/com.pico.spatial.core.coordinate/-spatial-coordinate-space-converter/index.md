# SpatialCoordinateSpaceConverter | PICO Spatial SDK

core / com.pico.spatial.core.coordinate / SpatialCoordinateSpaceConverter 
# SpatialCoordinateSpaceConverter
```kotlin
interface SpatialCoordinateSpaceConverter
```
Converts the coordinate space between  SpatialCoordinateSpace  and  ViewCoordinateSpace . 
#### Inheritors
SpatialViewContent Members 
## Properties
local Spatial Coordinate Space 
```kotlin
abstract val localSpatialCoordinateSpace: SpatialCoordinateSpace
```
The  SpatialCoordinateSpace  that indicates the SpatialView root's Entity where the converter implemented. 
## Functions
convert Position 
```kotlin
abstract fun convertPosition(position: Vector3, from: SpatialCoordinateSpace, to: ViewCoordinateSpace): Vector3
```
Converts a position from  SpatialCoordinateSpace  to  ViewCoordinateSpace . 
```kotlin
abstract fun convertPosition(position: Vector3, from: ViewCoordinateSpace, to: SpatialCoordinateSpace): Vector3
```
Converts a position from  ViewCoordinateSpace  to  SpatialCoordinateSpace . 
convert Rotation 
```kotlin
abstract fun convertRotation(rotation: Quat, from: SpatialCoordinateSpace, to: ViewCoordinateSpace): Quat
```
Convert a rotation from  SpatialCoordinateSpace  to  ViewCoordinateSpace . 
```kotlin
abstract fun convertRotation(rotation: Quat, from: ViewCoordinateSpace, to: SpatialCoordinateSpace): Quat
```
Convert a rotation from  ViewCoordinateSpace  to  SpatialCoordinateSpace . 
convert Scale 
```kotlin
abstract fun convertScale(scale: Vector3, from: SpatialCoordinateSpace, to: ViewCoordinateSpace): Vector3
```
Convert a scale from  SpatialCoordinateSpace  to  ViewCoordinateSpace . 
```kotlin
abstract fun convertScale(scale: Vector3, from: ViewCoordinateSpace, to: SpatialCoordinateSpace): Vector3
```
Convert a scale from  ViewCoordinateSpace  to  SpatialCoordinateSpace . 
convert Size 
```kotlin
abstract fun convertSize(size: Vector3, from: SpatialCoordinateSpace, to: ViewCoordinateSpace): Vector3
```
Convert a size from  SpatialCoordinateSpace  to  ViewCoordinateSpace . 
```kotlin
abstract fun convertSize(size: Vector3, from: ViewCoordinateSpace, to: SpatialCoordinateSpace): Vector3
```
Convert a size from  ViewCoordinateSpace  to  SpatialCoordinateSpace .