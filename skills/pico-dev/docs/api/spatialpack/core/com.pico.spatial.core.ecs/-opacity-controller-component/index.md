# OpacityControllerComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / OpacityControllerComponent 
# OpacityControllerComponent
```kotlin
@MainThread
```class  OpacityControllerComponent ( @ FloatRange ( from  =  0.0 ,  to  =  1.0 ) opacity :  Float  =  1.0f )  :  Component 
A Component that controls the opacity of an entity and its descendants. 
Operates hierarchically: ancestor and descendant opacities are multiplied to produce the final effective opacity. 
Members 
## Constructors
Opacity Controller Component 
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) opacity: Float = 1.0f)
```
## Properties
opacity 
```kotlin
var opacity: Float
```
The property that defines a value for the initial value of opacity. 
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