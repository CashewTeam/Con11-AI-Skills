# com.pico.spatial.core.json.annotations | PICO Spatial SDK

foundation / com.pico.spatial.core.json.annotations 
# Package-level declarations
Types 
## Types
Json Field 
```kotlin
@Target(allowedTargets = [AnnotationTarget.FIELD])
```annotation class  JsonField ( val  name :  String  =  "" ,  val  ignore :  Boolean  =  false ,  val  deserializer :  KClass < out  Deserializer < * > >  =  Deserializer::class ) 
Annotation for marking a field to be serialized to and deserialized from JSON. 
Json Type 
```kotlin
@Target(allowedTargets = [AnnotationTarget.CLASS])
```annotation class  JsonType ( val  fieldNameStyle :  JsonNameStyle  =  JsonNameStyle.HUMP ,  val  fieldNamePrefix :  String  =  "" ,  val  allowEmpty :  Boolean  =  true ,  val  deserializer :  KClass < out  Deserializer < * > >  =  Deserializer::class ) 
Annotation for marking a class to be serialized to and deserialized from JSON.