# EventSource | PICO Spatial SDK

core / com.pico.spatial.core.ecs / EventSource 
# EventSource
```kotlin
sealed class EventSource
```
The base class for defining sources of events. 
Currently, it is extended by  Scene  and  Entity  classes, which represent specific types of event sources. This class can be used to facilitate event subscription and filtering in an event system. 
#### Inheritors
Entity Scene Members 
## Constructors
Event Source 
```kotlin
protected constructor()
```