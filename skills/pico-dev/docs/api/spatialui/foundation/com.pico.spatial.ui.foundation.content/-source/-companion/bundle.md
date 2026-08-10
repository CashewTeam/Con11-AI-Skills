# bundle | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / Source / Companion / bundle 
# bundle
```kotlin
fun bundle(modelName: String, bundle: AssetBundle): Source<Any>
```
```kotlin
fun bundle(modelName: String, @WorkerThread bundleProvider: () -> AssetBundle): Source<Any>
```
Source in  AssetBundle . 
#### Return
model source