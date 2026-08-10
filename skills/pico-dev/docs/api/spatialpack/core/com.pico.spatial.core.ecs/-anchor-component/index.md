# AnchorComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AnchorComponent 
# AnchorComponent
```kotlin
@MainThread
```class  AnchorComponent  :  Component 
The  Component  that defines a spatial anchoring relationship between entities and real-world objects. 
When this component is attached to an entity, the entity gains the ability to anchor itself to a specific point or marker in the physical world, enabling spatial alignment and persistence. 
This component is currently effective only when used in full space. 
Members 
## Constructors
Anchor Component 
```kotlin
constructor(anchorTarget: AnchorTarget = AnchorTarget.createCameraTarget(), trackingMode: AnchorComponent.TrackingMode = TrackingMode.CONTINUOUS)
```
Creates an  AnchorComponent  with the specified  AnchorTarget  and tracking mode. 
## Types
Tracking Mode 
```kotlin
class TrackingMode
```
Controls how an entity follows its target in the scene. 
## Properties
anchor Target 
```kotlin
var anchorTarget: AnchorTarget
```
The  AnchorTarget . 
position Offset 
```kotlin
var positionOffset: Vector3
```
Position offset of the actual object relative to its  AnchorTarget . 
rotation Offset 
```kotlin
var rotationOffset: Quat
```
The rotation offset of the actual object relative to its  AnchorTarget . 
tracking Mode 
```kotlin
var trackingMode: AnchorComponent.TrackingMode
```
Controls how the entity follows its  AnchorTarget . 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
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