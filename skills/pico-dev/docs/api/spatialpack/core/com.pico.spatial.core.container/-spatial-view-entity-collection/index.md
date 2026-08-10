# SpatialViewEntityCollection | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialViewEntityCollection 
# SpatialViewEntityCollection
```kotlin
open class SpatialViewEntityCollection : Collection<Entity>
```
A  SpatialView  needs a  SpatialViewEntityCollection  to manage entities. 
Usually these entities are in a common layer of an entity tree. 
Members 
## Constructors
Spatial View Entity Collection 
```kotlin
constructor()
```
## Properties
size 
```kotlin
open override val size: Int
```
The current size of the  SpatialViewEntityCollection . 
## Functions
add 
```kotlin
open fun add(entity: Entity): Boolean
```
Binds an entity to the  SpatialViewEntityCollection . 
add All 
```kotlin
open fun addAll(elements: Collection<Entity>): Boolean
```
Adds all the entities of a  Collection  to the  SpatialViewEntityCollection . 
clear 
```kotlin
open fun clear()
```
Clears all entities in the  SpatialViewEntityCollection . 
contains 
```kotlin
open operator override fun contains(element: Entity): Boolean
```
Checks if the  SpatialViewEntityCollection  contains an entity. 
contains All 
```kotlin
open override fun containsAll(elements: Collection<Entity>): Boolean
```
Checks if the  SpatialViewEntityCollection  contains all the entities of a  Collection . 
is Empty 
```kotlin
open override fun isEmpty(): Boolean
```
Checks if a  SpatialViewEntityCollection  is empty. 
iterator 
```kotlin
open operator override fun iterator(): Iterator<Entity>
```
Gets an  Iterator  of the  SpatialViewEntityCollection . 
remove 
```kotlin
open fun remove(entity: Entity): Boolean
```
Removes an entity from the  SpatialViewEntityCollection . 
remove All 
```kotlin
open fun removeAll(elements: Collection<Entity>): Boolean
```
Removes all the entities of a  Collection  from the  SpatialViewEntityCollection . 
retain All 
```kotlin
open fun retainAll(elements: Collection<Entity>): Boolean
```
Retains all the entities of a  Collection  in the  SpatialViewEntityCollection . 
to String 
```kotlin
open override fun toString(): String
```