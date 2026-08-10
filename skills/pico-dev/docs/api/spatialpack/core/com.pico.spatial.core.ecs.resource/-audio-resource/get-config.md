# getConfig | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioResource / getConfig 
# getConfig
```kotlin
fun getConfig(): AudioResourceConfig
```
Gets the configuration of the audio resource. 
This method returns the  AudioResourceConfig  that was specified when this audio resource was loaded. The configuration contains settings such as mixer group ID, random start, loop enable, and ambisonics type. 
Note: If no configuration is set or an error occurs, a default  AudioResourceConfig  will be returned with the following values: empty mixer group ID, randomStart = false, loopEnable = false, and ambisonicsType =  AmbisonicsType.NONE . 
#### Return
The  AudioResourceConfig  of the audio resource. 
#### Throws
Illegal State Exception 
If this resource has been closed or is invalid.