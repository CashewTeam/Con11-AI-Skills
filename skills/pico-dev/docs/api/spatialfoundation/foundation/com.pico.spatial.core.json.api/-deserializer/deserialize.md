# deserialize | PICO Spatial SDK

foundation / com.pico.spatial.core.json.api / Deserializer / deserialize 
# deserialize
```kotlin
abstract fun deserialize(model: Any?, key: String?, json: Any?): T
```
Deserializes a JSON object into a model instance. 
#### Return
The deserialized model. 
#### Parameters
model 
The model to deserialize with. 
key 
The key of the JSON object. 
json 
The original JSON object. 
#### Throws
JSONException 
If exception occurs during deserialization.