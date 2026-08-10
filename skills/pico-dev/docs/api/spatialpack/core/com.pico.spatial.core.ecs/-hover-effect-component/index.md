# HoverEffectComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / HoverEffectComponent 
# HoverEffectComponent
```kotlin
@MainThread
```class  HoverEffectComponent  :  Component 
A  Component  that apply visual effect when user interacts with it. 
Note: To be interactable, the entity must also have  CollisionComponent  and  InteractableComponent . 
Members 
## Constructors
Hover Effect Component 
```kotlin
constructor()
```
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