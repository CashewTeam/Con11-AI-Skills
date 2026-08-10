# ModelLoadingState | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / ModelLoadingState 
# ModelLoadingState
```kotlin
@Stable
```sealed  class  ModelLoadingState 
The state of loading a 3D model. 
#### Inheritors
Loading Success Error Members 
## Constructors
Model Loading State 
```kotlin
protected constructor()
```
## Types
Error 
```kotlin
class Error(val reason: String) : ModelLoadingState
```
Load model failed. 
Loading 
```kotlin
object Loading : ModelLoadingState
```
Model is loading. 
Success 
```kotlin
class Success(val model: LoadedModel) : ModelLoadingState
```
Load model success.