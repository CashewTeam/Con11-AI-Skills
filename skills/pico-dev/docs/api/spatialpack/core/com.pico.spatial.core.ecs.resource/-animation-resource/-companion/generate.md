# generate | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AnimationResource / Companion / generate 
# generate
```kotlin
@JvmStatic
```fun  generate ( animation :  SpatialAnimation ) :  AnimationResource 
Generates an  AnimationResource  instance based on the provided subclass of  SpatialAnimation . 
#### Return
The generated  AnimationResource  instance based on the input  SpatialAnimation  subclass. 
#### Parameters
animation 
The subclass instance of  SpatialAnimation  used to generate the corresponding  AnimationResource . 
#### Throws
Illegal Argument Exception 
If the  animation  type is not supported. 
Resource Loading Exception 
If generation fails at the native layer.