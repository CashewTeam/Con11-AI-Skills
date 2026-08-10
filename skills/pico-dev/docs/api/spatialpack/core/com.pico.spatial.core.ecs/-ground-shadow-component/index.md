# GroundShadowComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / GroundShadowComponent 
# GroundShadowComponent
```kotlin
@MainThread
```class  GroundShadowComponent  :  Component 
A  Component  that adds a ground shadow to the entity. 
A ground shadow creates the illusion of a directional light above an entity. Attach this component to the entity that casts the shadow and the entity that should receive the shadow. 
Notes: 
- 
You need to add this component to each entity that requires a ground shadow; it does not propagate to children. 
- 
Entities without this component will neither cast nor receive ground shadows. 
Members 
## Constructors
Ground Shadow Component 
```kotlin
constructor(castsShadowEnabled: Boolean, receivesShadowEnabled: Boolean)
```
Constructs a  GroundShadowComponent . 
## Properties
casts Shadow Enabled 
```kotlin
var castsShadowEnabled: Boolean
```
Whether the entity casts ground shadow. 
receives Shadow Enabled 
```kotlin
var receivesShadowEnabled: Boolean
```
Whether the entity receives ground shadow. 
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