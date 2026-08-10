# sequence | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AnimationResource / Companion / sequence 
# sequence
```kotlin
@JvmStatic
```fun  sequence ( with :  List < AnimationResource > ) :  AnimationResource 
Creates a sequence of multiple  AnimationResource  objects in the given list order. 
#### Return
The new  AnimationResource  representing the sequenced animation resources. 
#### Parameters
with 
The list of  AnimationResource  objects to be sequenced, in order. 
#### Throws
Illegal State Exception 
If any resource in  with  is closed or invalid. 
Resource Loading Exception 
If sequencing fails at the native layer.