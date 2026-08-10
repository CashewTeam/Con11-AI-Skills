# AnimationResourceLibraryComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AnimationResourceLibraryComponent 
# AnimationResourceLibraryComponent
```kotlin
@MainThread
```class  AnimationResourceLibraryComponent  :  Component 
AnimationResourceLibraryComponent is a component designed to manage animation resources. 
This component organizes resources in the form of a map, where each resource is associated with a unique, non-null, and valid name. Developers using this component should ensure that the resource names meet these criteria. 
When interacting with this component, it is important to carefully check the return values of the provided interfaces to confirm whether the operations were successful. 
Members 
## Constructors
Animation Resource Library Component 
```kotlin
constructor()
```
## Functions
add 
```kotlin
fun add(name: String, animationResource: AnimationResource): Boolean
```
Adds a new animation resource to the library with the specified name. 
clear 
```kotlin
fun clear()
```
Clears all animation resources from the library. 
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
contains 
```kotlin
fun contains(name: String): Boolean
```
Checks whether a resource with the specified name exists. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get 
```kotlin
fun get(name: String): AnimationResource?
```
Retrieves the animation resource associated with the specified name. 
get All Animation Resource 
```kotlin
fun getAllAnimationResource(): List<AnimationResource>
```
Retrieves all animation resources currently stored in the library. 
get All Names 
```kotlin
fun getAllNames(): List<String>
```
Retrieves all resource names currently stored in the library. 
hash Code 
```kotlin
open override fun hashCode(): Int
```remove 
```kotlin
fun remove(name: String): Boolean
```
Removes the animation resource associated with the specified name. 
to String 
```kotlin
open override fun toString(): String
```