# JsonType | PICO Spatial SDK

foundation / com.pico.spatial.core.json.annotations / JsonType 
# JsonType
```kotlin
@Target(allowedTargets = [AnnotationTarget.CLASS])
```annotation class  JsonType ( val  fieldNameStyle :  JsonNameStyle  =  JsonNameStyle.HUMP ,  val  fieldNamePrefix :  String  =  "" ,  val  allowEmpty :  Boolean  =  true ,  val  deserializer :  KClass < out  Deserializer < * > >  =  Deserializer::class ) 
Annotation for marking a class to be serialized to and deserialized from JSON. 
Members 
## Properties
allow Empty 
```kotlin
val allowEmpty: Boolean = true
```
Whether fields are allowed to be empty. 
deserializer 
```kotlin
val deserializer: KClass<out Deserializer<*>>
```
Specifies a custom  Deserializer  to use for this class. The deserializer must be a subclass of  Deserializer . 
field Name Prefix 
```kotlin
val fieldNamePrefix: String
```
Prefix to add to each JSON field name. 
field Name Style 
```kotlin
val fieldNameStyle: JsonNameStyle
```
The naming style for JSON fields.