# Size | PICO Spatial SDK

core / com.pico.spatial.core.unit / Size 
# Size
```kotlin
class Size(val width: Int, val height: Int, val depth: Int = UNSPECIFIED_SIZE)
```
Immutable class that represents width, height, and depth dimensions in pixels. 
Members 
## Constructors
Size 
```kotlin
constructor(width: Int, height: Int, depth: Int = UNSPECIFIED_SIZE)
```
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Size . 
## Properties
depth 
```kotlin
val depth: Int
```
Gets the depth of the  Size  instance. 
height 
```kotlin
val height: Int
```
Gets the height of the  Size  instance. 
width 
```kotlin
val width: Int
```
Gets the width of the  Size  instance. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```
Checks whether this  Size  instance is equal to another object. 
hash Code 
```kotlin
open override fun hashCode(): Int
```to Array 
```kotlin
fun toArray(): IntArray
```
Converts this  Size  to an  IntArray . 
to String 
```kotlin
open override fun toString(): String
```