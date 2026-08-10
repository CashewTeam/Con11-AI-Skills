# OpenStageResult | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / OpenStageResult 
# OpenStageResult
```kotlin
sealed class OpenStageResult
```
The result of  openStage 
#### Inheritors
Allowed NotAllowed Error Members 
## Constructors
Open Stage Result 
```kotlin
protected constructor()
```
## Types
Allowed 
```kotlin
object Allowed : OpenStageResult
```
Means Stage allowed to open 
Error 
```kotlin
class Error(val code: Int, val reason: String) : OpenStageResult
```
Failed 
Not Allowed 
```kotlin
object NotAllowed : OpenStageResult
```
Means Stage not allowed to open