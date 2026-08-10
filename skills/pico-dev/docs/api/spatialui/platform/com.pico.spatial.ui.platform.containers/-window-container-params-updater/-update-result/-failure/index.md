# Failure | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / WindowContainerParamsUpdater / UpdateResult / Failure 
# Failure
```kotlin
class Failure(val code: Int, val reason: String? = null) : WindowContainerParamsUpdater.UpdateResult
```
Represents a failed parameter update operation. 
Members 
## Constructors
Failure 
```kotlin
constructor(code: Int, reason: String? = null)
```
## Properties
code 
```kotlin
val code: Int
```
Numeric error code identifying the specific failure type 
reason 
```kotlin
val reason: String?
```
Optional human-readable description of the failure cause