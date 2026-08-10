# Bool3 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Bool3 
# Bool3
```kotlin
class Bool3
```
Represents a structure containing three boolean values. 
Members 
## Constructors
Bool3 
```kotlin
constructor(x: Boolean, y: Boolean, z: Boolean)
```
Constructs a new  Bool3  instance with the specified x, y, z components. 
```kotlin
constructor(value: Boolean)
```
Constructs a  Bool3  instance where all three values (x, y, z) are set to the specified boolean value. 
```kotlin
constructor(other: Bool3)
```
Constructs a  Bool3  instance by copying values from another  Bool3  instance. 
## Properties
x 
```kotlin
val x: Boolean
```
The boolean value representing the x-axis. 
y 
```kotlin
val y: Boolean
```
The boolean value representing the y-axis. 
z 
```kotlin
val z: Boolean
```
The boolean value representing the z-axis. 
## Functions
and 
```kotlin
infix fun and(other: Bool3): Bool3
```
Performs a logical  AND  operation between this  Bool3  instance and another  Bool3  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```not 
```kotlin
fun not(): Bool3
```
Performs a logical  NOT  operation on this  Bool3  instance. 
or 
```kotlin
infix fun or(other: Bool3): Bool3
```
Performs a logical  OR  operation between this  Bool3  instance and another  Bool3  instance. 
to String 
```kotlin
open override fun toString(): String
```