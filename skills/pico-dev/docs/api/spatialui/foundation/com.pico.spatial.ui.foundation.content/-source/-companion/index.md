# Companion | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / Source / Companion 
# Companion
```kotlin
object Companion
```
The companion of  Source . 
It provides some easy used static APIs for  Source . 
Members 
## Functions
assets 
```kotlin
fun assets(path: String): Source<String>
```
Source from Android assets. 
bundle 
```kotlin
fun bundle(modelName: String, bundle: AssetBundle): Source<Any>
```
```kotlin
fun bundle(modelName: String, @WorkerThread bundleProvider: () -> AssetBundle): Source<Any>
```
Source in  AssetBundle . 
file 
```kotlin
fun file(localFile: File): Source<String>
```
Create a data source from a local file. 
```kotlin
fun file(absolutePath: String): Source<String>
```
Create a data source from an absolute file path.