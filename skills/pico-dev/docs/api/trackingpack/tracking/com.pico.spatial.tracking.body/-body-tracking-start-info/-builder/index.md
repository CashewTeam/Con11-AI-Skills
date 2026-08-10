# Builder | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyTrackingStartInfo / Builder 
# Builder
```kotlin
class Builder
```
Builder for creating a  BodyTrackingStartInfo  instance. 
Members 
## Constructors
Builder 
```kotlin
constructor()
```
## Properties
need Calibration 
```kotlin
var needCalibration: Boolean
```
If  true , body tracking will perform calibration during startup. 
## Functions
build 
```kotlin
fun build(): BodyTrackingStartInfo
```
Builds a  BodyTrackingStartInfo  instance with the configured settings.