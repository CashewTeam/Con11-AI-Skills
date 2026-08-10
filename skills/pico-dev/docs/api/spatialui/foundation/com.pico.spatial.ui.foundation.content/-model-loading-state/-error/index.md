# Error | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / ModelLoadingState / Error 
# Error
```kotlin
class Error(val reason: String) : ModelLoadingState
```
Load model failed. 
#### Parameters
reason 
Failed reason. 
Members 
## Constructors
Error 
```kotlin
constructor(reason: String)
```
## Properties
reason 
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
```