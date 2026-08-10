# com.pico.spatial.core.json.api | PICO Spatial SDK

foundation / com.pico.spatial.core.json.api 
# Package-level declarations
Types 
## Types
Deserializer 
```kotlin
interface Deserializer<T>
```
Deserializer is used to convert JSON objects into model instances. 
Json Contract 
```kotlin
abstract class JsonContract
```
Public serialize contract for JSON encode/decode. 
Json Model 
```kotlin
abstract class JsonModel : JsonContract
```
A class for serializing and deserializing JSON objects. 
Json Name Style 
```kotlin
enum JsonNameStyle : Enum<JsonNameStyle>
```
Json field name style.