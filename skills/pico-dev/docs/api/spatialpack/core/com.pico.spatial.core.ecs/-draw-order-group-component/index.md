# DrawOrderGroupComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / DrawOrderGroupComponent 
# DrawOrderGroupComponent
```kotlin
@MainThread
```class  DrawOrderGroupComponent  :  Component 
The  Component  that defines a draw order group for  ModelComponent  and  ParticleComponent . 
When this component is attached to an entity, it enables the associated model and particle components to be sorted within a specific group and sequence, allowing for precise control over the rendering hierarchy. 
This component is particularly effective for managing visual layering and preventing depth-sorting artifacts. 
Members 
## Constructors
Draw Order Group Component 
```kotlin
constructor(group: DrawOrderGroup, order: Int)
```
## Properties
draw Order Group 
```kotlin
var drawOrderGroup: DrawOrderGroup
```
Controls the draw order group of the entity. 
order 
```kotlin
var order: Int
```
Controls the draw order of the entity in the draw order group. 
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
```set Order 
```kotlin
fun setOrder(drawOrderGroup: DrawOrderGroup, order: Int)
```
Sets the drawing group and sorting priority for the entity's visual components. 
to String 
```kotlin
open override fun toString(): String
```