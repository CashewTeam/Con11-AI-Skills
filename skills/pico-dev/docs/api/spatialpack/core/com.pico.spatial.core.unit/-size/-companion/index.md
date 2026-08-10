# Companion | PICO Spatial SDK

core / com.pico.spatial.core.unit / Size / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Size . 
Members 
## Properties
unspecified 
```kotlin
@JvmField
```val  unspecified :  Size 
Factory for building a  Size  instance with unspecified dimensions witch will be specified by system later. 
UNSPECIFIED_ SIZE 
```kotlin
const val UNSPECIFIED_SIZE: Int
```
Constant value representing an unspecified size. 
## Functions
from Array 
```kotlin
@JvmStatic
```fun  fromArray ( array :  IntArray ) :  Size 
Creates a new  Size  instance from a 3-element integer array. 
from String 
```kotlin
@JvmStatic
```fun  fromString ( string :  String ) :  Size 
Parses the specified string into a  Size  instance.