# LookAtComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / LookAtComponent 
# LookAtComponent
```kotlin
@MainThread
```class  LookAtComponent  :  Component 
A  Component  that controls the "look at" behavior of entities in 3D space, allowing entities to face specific targets (such as viewers or other entities) and providing control over alignment methods and forward direction. 
Members 
## Constructors
Look At Component 
```kotlin
constructor()
```
The default constructor for  LookAtComponent  with no parameters. 
## Properties
align Local Up To World Up 
```kotlin
var alignLocalUpToWorldUp: Boolean
```
Controls whether the entity's local up direction should be aligned with the world's up direction. 
look At Forward Direction 
```kotlin
var lookAtForwardDirection: LookAtForwardDirection
```
Specifies the forward direction of the entity's "look at" behavior. 
## Functions
clear Target 
```kotlin
fun clearTarget()
```
Clears the target for the entity's "look at" behavior. 
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get Look At Target Type 
```kotlin
fun getLookAtTargetType(): LookAtTargetType
```
Gets the type of target currently set for the entity's "look at" behavior. 
hash Code 
```kotlin
open override fun hashCode(): Int
```set Entity As Target 
```kotlin
fun setEntityAsTarget(entity: Entity)
```
Sets the specified entity as the target for the entity's "look at" behavior. If the entity is not valid, it will not be set as the target and will remain unchanged. 
set Viewer As Target 
```kotlin
fun setViewerAsTarget()
```
Sets the viewer as the target for the entity's "look at" behavior. 
to String 
```kotlin
open override fun toString(): String
```