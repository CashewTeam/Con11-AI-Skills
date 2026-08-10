# JsonContract | PICO Spatial SDK

foundation / com.pico.spatial.core.json.api / JsonContract 
# JsonContract
```kotlin
abstract class JsonContract
```
Public serialize contract for JSON encode/decode. 
#### Inheritors
JsonModel Members 
## Constructors
Json Contract 
```kotlin
constructor()
```
## Functions
decode From Json 
```kotlin
abstract fun decodeFromJson(jsonObject: JSONObject)
```
Decode from JSONObject to current object. 
encode To Json 
```kotlin
abstract fun encodeToJson(): JSONObject
```
Encode current object to JSONObject.