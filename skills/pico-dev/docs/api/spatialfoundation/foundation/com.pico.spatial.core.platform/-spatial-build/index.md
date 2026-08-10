# SpatialBuild | PICO Spatial SDK

foundation / com.pico.spatial.core.platform / SpatialBuild 
# SpatialBuild
```kotlin
object SpatialBuild
```
Provides information about the PICO OS build, extracted from the system. 
Use  SpatialBuild  to check whether the current running OS is PICO OS and to query its features or states. 
For example,  SpatialBuild.isSpatialPlatform  can be used to ensure certain code only runs on PICO OS rather than on other Android devices: 

```
if (SpatialBuild.isSpatialPlatform()) {    // Run PICO OS-specific code} else {    // Run non-PICO OS-specific code}
```Members 
## Functions
is Spatial Platform 
```kotlin
@JvmStatic
```fun  isSpatialPlatform ( ) :  Boolean 
Checks whether the current running OS supports PICO OS spatial features.