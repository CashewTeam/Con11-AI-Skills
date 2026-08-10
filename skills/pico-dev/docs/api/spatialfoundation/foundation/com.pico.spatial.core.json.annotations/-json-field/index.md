# JsonField | PICO Spatial SDK

foundation / com.pico.spatial.core.json.annotations / JsonField 
# JsonField
```kotlin
@Target(allowedTargets = [AnnotationTarget.FIELD])
```annotation class  JsonField ( val  name :  String  =  "" ,  val  ignore :  Boolean  =  false ,  val  deserializer :  KClass < out  Deserializer < * > >  =  Deserializer::class ) 
Annotation for marking a field to be serialized to and deserialized from JSON. 
Members 
## Properties
deserializer 
```kotlin
val deserializer: KClass<out Deserializer<*>>
```
Specifies a custom  Deserializer  to use for this field. The deserializer must be a subclass of  Deserializer . 
ignore 
```kotlin
val ignore: Boolean = false
```
Indicates whether this field should be ignored during serialization or deserialization. 
name 
```kotlin
val name: String
```
Specifies the name of the JSON field. If left empty, the field name will be used by default.