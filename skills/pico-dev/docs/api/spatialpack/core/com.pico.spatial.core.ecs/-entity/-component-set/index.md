# ComponentSet | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / ComponentSet 
# ComponentSet
```kotlin
class ComponentSet : Collection<Component>
```
A set of stored components. The set represents all the components stored on an  Entity . Each  Entity  can hold only one  Component  of any given type. 
Members 
## Properties
size 
```kotlin
open override val size: Int
```
## Functions
clear 
```kotlin
@MainThread
```fun  clear ( ) 
Clears all components in the component set. 
contains 
```kotlin
@MainThread
```open  operator override  fun  contains ( element :  Component ) :  Boolean contains All 
```kotlin
@MainThread
```open  override  fun  containsAll ( elements :  Collection < Component > ) :  Boolean get 
```kotlin
inline fun <T : Component> get(): T?
```
Gets the component of the specific type. 
```kotlin
@MainThread
```operator  fun  < T  :  Component >  get ( componentType :  Class < T > ) :  T ? 
Gets the component of a specific type. 
has 
```kotlin
inline fun <T : Component> has(): Boolean
```
Check if the componentSet contains a component of a specific type. 
```kotlin
@MainThread
```fun  < T  :  Component >  has ( componentType :  Class < T > ) :  Boolean 
Checks if the component set contains the component of the specified type. 
is Empty 
```kotlin
@MainThread
```open  override  fun  isEmpty ( ) :  Boolean iterator 
```kotlin
open operator override fun iterator(): Iterator<Component>
```remove 
```kotlin
@MainThread
```fun  remove ( componentType :  Class < out  Component > ) 
Removes the component of a specific type. 
set 
```kotlin
inline fun <T : Component> set(component: T)
```
Sets a component of the specified type. If a component of the same type already exists, it will be replaced. 
```kotlin
@MainThread
```fun  set ( components :  List < Component > ) 
Sets multiple components. If the array contains components of the same type, the last one in the array will replace the previous ones. 
```kotlin
@MainThread
```operator  fun  < T  :  Component >  set ( componentType :  Class < T > ,  component :  T ) 
Sets a component as the specified type. If a component of the same type already exists, it will be replaced.