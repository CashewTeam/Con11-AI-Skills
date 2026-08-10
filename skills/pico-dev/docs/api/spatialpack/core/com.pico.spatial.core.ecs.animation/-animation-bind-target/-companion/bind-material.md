# bindMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / AnimationBindTarget / Companion / bindMaterial 
# bindMaterial
```kotlin
@JvmStatic
```fun  bindMaterial ( materialIndex :  Int  =  0 ,  materialTarget :  MaterialTarget ) :  AnimationBindTarget 
Binds to a material property of an entity. See  MaterialTarget  to choose the property. 
#### Return
The created and bound  AnimationBindTarget  instance. 
#### Parameters
material Index 
Index of the material to bind (default 0). 
material Target 
The material property to animate. 
```kotlin
@JvmStatic
```fun  bindMaterial ( materialIndex :  Int  =  0 ,  materialPropertyName :  String ) :  AnimationBindTarget 
Binds to a material property by its string name. 
#### Return
The created and bound  AnimationBindTarget  instance. 
#### Parameters
material Index 
Index of the material to bind (default 0). 
material Property Name 
The material property name to animate.