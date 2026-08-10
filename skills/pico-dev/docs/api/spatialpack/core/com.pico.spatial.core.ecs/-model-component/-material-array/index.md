# MaterialArray | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelComponent / MaterialArray 
# MaterialArray
```kotlin
class MaterialArray : Iterable<Material>
```
A dynamic array of  Material  instances for a  ModelComponent . 
You can append or remove materials at the end of the array in addition to standard array operations. 
Members 
## Properties
size 
```kotlin
val size: Int
```
Returns the number of materials in the array. 
## Functions
add 
```kotlin
fun add(element: Material)
```
Appends a material to the end of this list. 
```kotlin
fun add(elements: Array<out Material>)
```
Appends an array of materials to the end of this list. 
get 
```kotlin
operator fun get(index: Int): Material
```
Gets the material at the specified index from this component. 
iterator 
```kotlin
open operator override fun iterator(): Iterator<Material>
```
Creates an  Iterator  for iterating over the materials in the array. 
plus Assign 
```kotlin
operator fun plusAssign(element: Material)
```
Overloads the  +=  operator to append a single material to the end of the array. 
```kotlin
operator fun plusAssign(elements: Array<Material>)
```
Overloads the  +=  operator to append an array of materials to the end of the array. 
remove Last 
```kotlin
fun removeLast(): Material
```
Removes and returns the last material in the array. 
set 
```kotlin
operator fun set(index: Int, material: Material)
```
Sets the material at the specified index for this component. 
to String 
```kotlin
open override fun toString(): String
```