# Deserializer | PICO Spatial SDK

foundation / com.pico.spatial.core.json.api / Deserializer 
# Deserializer
```kotlin
interface Deserializer<T>
```
Deserializer is used to convert JSON objects into model instances. 
#### Parameters
T 
The type of the model to deserialize. 
Members 
## Functions
deserialize 
```kotlin
abstract fun deserialize(model: Any?, key: String?, json: Any?): T
```
Deserializes a JSON object into a model instance.