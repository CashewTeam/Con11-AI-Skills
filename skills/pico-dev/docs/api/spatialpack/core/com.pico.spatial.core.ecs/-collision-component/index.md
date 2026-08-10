# CollisionComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / CollisionComponent 
# CollisionComponent
```kotlin
@MainThread
```class  CollisionComponent  :  Component 
A  Component  responsible for managing collision settings and operations, including collision detection and response. 
This component is essential for enabling physics effects such as forces, motion, and interactions between objects. Attach this component to entities to integrate physics-based behavior into your application. 
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Members 
## Constructors
Collision Component 
```kotlin
constructor(collisionShape: List<ShapeResource>, physicsMaterial: PhysicsMaterialResource, collisionResponseMode: CollisionResponseMode = COLLIDER_FULL, collisionFilter: CollisionFilter = CollisionFilter.COLLISION_FILTER_DEFAULT, collisionInfoDetailLevel: CollisionInfoDetailLevel = CollisionInfoDetailLevel.BRIEF)
```
Creates a new  CollisionComponent  instance. 
## Properties
collision Filter 
```kotlin
var collisionFilter: CollisionFilter
```
The  CollisionFilter  of the  CollisionComponent . The  CollisionFilter  is used to group and classify entities into different collision groups. Default value is  CollisionFilter.COLLISION_FILTER_DEFAULT . 
collision Info Detail Level 
```kotlin
var collisionInfoDetailLevel: CollisionInfoDetailLevel
```
The  CollisionInfoDetailLevel  of the  CollisionComponent . Default value is  CollisionInfoDetailLevel.BRIEF . 
collision Response Mode 
```kotlin
var collisionResponseMode: CollisionResponseMode
```
The  CollisionResponseMode  of the  CollisionComponent . Default value is  CollisionResponseMode.COLLIDER_FULL . 
collision Shape 
```kotlin
var collisionShape: List<ShapeResource>
```
Represents the geometric shape of an object used for collision detection in physics simulations. This shape is a collection of  ShapeResource s, which is fundamental for determining whether two objects intersect or collide in a virtual environment. 
physics Material 
```kotlin
var physicsMaterial: PhysicsMaterialResource
```
The  PhysicsMaterialResource  of the  CollisionComponent . 
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