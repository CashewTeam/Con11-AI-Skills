# SpatialMLInstance | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLInstance 
# SpatialMLInstance
```kotlin
@RequiresApi(value = 27)
```interface  SpatialMLInstance 
The interface of SpatialML instance. An  SpatialMLInstance  must be created before any SpatialML APIs or commands are executed. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion of  SpatialMLInstance . 
## Properties
app Context 
```kotlin
abstract val appContext: Context
```
The Android app context. The instance will be associated with the given context. 
ready 
```kotlin
abstract val ready: Boolean
```
Whether the instance is ready. Call  createSession  before  ready  is true will get null. 
## Functions
create Session 
```kotlin
abstract fun createSession(config: SpatialMLSession.InitInfo): SpatialMLSession?
```
Create a  SpatialMLSession  from this instance.