# loadFrom | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / loadFrom 
# loadFrom
```kotlin
suspend fun Entity.Companion.loadFrom(source: Source<*>): Entity
```
Load entity from  Source . Its running on IO thread. will auto destroy entity when coroutine is canceled 
#### Return
Entity instance