# UpdateResult | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.ability / StageParamsUpdater / UpdateResult 
# UpdateResult
```kotlin
sealed class UpdateResult
```
Represents the result of an update operation on Stage parameters. 
This sealed class provides two possible outcomes for update operations: 
- 
Success  - Indicates the parameter update was successful 
- 
Failure  - Indicates the parameter update failed with a specific error code and reason 
#### Inheritors
Success Failure Members 
## Constructors
Update Result 
```kotlin
protected constructor()
```
## Types
Failure 
```kotlin
class Failure(val code: Int, val reason: String? = null) : StageParamsUpdater.UpdateResult
```
Represents a failed parameter update operation. 
Success 
```kotlin
object Success : StageParamsUpdater.UpdateResult
```
Indicates a successful parameter update operation.