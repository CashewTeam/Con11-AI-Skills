# SortAsUIElementComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / SortAsUIElementComponent 
# SortAsUIElementComponent
```kotlin
@MainThread
```class  SortAsUIElementComponent  :  Component 
Marks a 3D renderable to be sorted as a UI element. 
When attached to an entity with a renderable/interactive component (e.g.  ModelComponent ,  VideoComponent ), this component integrates the entity into the view-independent UI sorting system. 
The  distanceBias  is a float value in meters, applied to a view-independent reference distance used to compute a unified sort order for mixed 2D/3D ordering. 
- 
Positive  distanceBias  moves the element forward (rendered later, on top). 
- 
Negative  distanceBias  moves the element backward (rendered earlier, behind). 
The  distanceBias  only affects the sort order; it does not modify the entity's spatial position. 
NOTE: 
- 
This component is mutually exclusive with  DrawOrderGroupComponent . If both are present, this component will be ignored. 
- 
This component only affects the entity it is directly attached to; it does not affect any child entities. 
Members 
## Constructors
Sort As UIElement Component 
```kotlin
constructor(distanceBias: Float)
```
## Properties
distance Bias 
```kotlin
var distanceBias: Float
```
A bias (in meters) applied to the view-independent reference distance used for sorting. 
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