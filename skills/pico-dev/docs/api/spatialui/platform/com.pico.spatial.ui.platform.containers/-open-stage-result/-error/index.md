# Error | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / OpenStageResult / Error 
# Error
```kotlin
class Error(val code: Int, val reason: String) : OpenStageResult
```
Failed 
#### Parameters
code 
error code 
reason 
cause of failure 
Members 
## Constructors
Error 
```kotlin
constructor(code: Int, reason: String)
```
## Properties
code 
```kotlin
val code: Int
```reason 
```kotlin
val reason: String
```
## Functions
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