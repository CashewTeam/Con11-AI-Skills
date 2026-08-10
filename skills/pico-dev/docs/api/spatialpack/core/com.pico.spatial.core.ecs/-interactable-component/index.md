# InteractableComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / InteractableComponent 
# InteractableComponent
```kotlin
@MainThread
```class  InteractableComponent  :  Component 
The  Component  that marks an entity as interactable, allowing it to receive and process input events. 
Note: To be interactable, the entity must also have a  CollisionComponent . 
Members 
## Constructors
Interactable Component 
```kotlin
constructor()
```
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a new instance cloned from the current object. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```