# JsonModel | PICO Spatial SDK

foundation / com.pico.spatial.core.json.api / JsonModel 
# JsonModel
```kotlin
abstract class JsonModel : JsonContract
```
A class for serializing and deserializing JSON objects. 
If you want to serialize object instance params to a JSON string or deserialize a JSON string to an object instance with related params, you can extend and implement this class. 
- 
You can use  com.pico.spatial.core.json.annotations.JsonType  to define the summary JSON type of this class, such as style, prefix, allowing params empty, or customizing serialize rule class. 

```
// For example, the final serialized JSON string in this class will be "m_name" and "m_style" in key.@JsonType(fieldNameStyle = JsonNameStyle.UNDERLINE, fieldNamePrefix = "m")class CustomClass : JsonModel() {  var name: String? = null  var style: Int = 0}
```
- 
You can use  com.pico.spatial.core.json.annotations.JsonField  to define the JSON field config of this class, such as renaming field param name, ignoring specific param, or customizing serialize rule class. 

```
class CustomClass : JsonModel() {  // For example, the final serialized JSON string in this param will be "customName" in key  @JsonField(name = "customName") var name: String? = null  var style: Int = 0  // For example, this param will be ignored during serialization and there will be no tags in  // the serialized JSON string  @JsonField(ignore = true) var tags: List<String>? = null}
```
- 
You can use  Deserializer  to customize define classes with rules dealing params to solve nested class complex problems. 

```
class CustomClass : JsonModel() {        // For example, the final serialized JSON string in this param will be "customName" in key        @JsonField(name = "customName") var name: String? = null        var style: Int = 0        // For example, the original JSON string is "color": [0x00, 0xff, 0xff, 0xff], with a specific ARGB array        @JsonField(name = "color", deserializer = Color4Deserializer::class) var color: Color4? = null    }    class Color4Deserializer : Deserializer<Color4?> {        override fun deserialize(model: Any?, key: String?, json: Any?): Color4? {            if (json == null) {                return null            }            var item: Color4? = null            if (json is JSONObject) {                val value = json.optJSONArray("color")                if (value != null && value.length() != 4) {                    return null                }                if (value != null) {                    item =                        Color4(                            value.optInt(1) / 255f,                            value.optInt(2) / 255f,                            value.optInt(3) / 255f,                            value.optInt(0) / 255f                        )                }            }            return item        }    }
```Members 
## Constructors
Json Model 
```kotlin
constructor()
```
## Functions
decode From Json 
```kotlin
open override fun decodeFromJson(jsonObject: JSONObject)
```
Decode from JSONObject to current object. 
encode To Json 
```kotlin
open override fun encodeToJson(): JSONObject
```
Encode current object to JSONObject.