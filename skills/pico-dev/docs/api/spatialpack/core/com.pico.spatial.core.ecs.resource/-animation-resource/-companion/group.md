# group | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AnimationResource / Companion / group 
# group
```kotlin
@JvmStatic
```fun  group ( with :  List < AnimationResource > ) :  AnimationResource 
Groups multiple  AnimationResource  objects into a single  AnimationResource . 
#### Return
The new  AnimationResource  representing the grouped animation resources. 
#### Parameters
with 
The list of  AnimationResource  objects to be grouped. 
#### Throws
Illegal State Exception 
If any resource in  with  is closed or invalid. 
Resource Loading Exception 
If grouping fails at the native layer.