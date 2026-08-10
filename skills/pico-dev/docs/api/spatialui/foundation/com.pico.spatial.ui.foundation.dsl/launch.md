# launch | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / launch 
# launch
```kotlin
fun Application.launch(block: SpatialAppScope.() -> Unit)
```
Extension function for android platform, use  Application  as receiver to start a spatial app context so we can create dsl like this 

```
class App : Application {  fun onCreate(){    launch(::mainApp)  }}// Main.kt// Here we hide android platform specific concept behinds [SpatialAppScope]fun mainApp(appScope:SpatialAppScope) = with(appScope) {     // Put code there}
```