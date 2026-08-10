# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / AnimationBindTarget / Companion 
# Companion
```kotlin
object Companion
```
Companion object for  AnimationBindTarget . 
Provides easy-to-use factory methods for creating bind targets. 
Members 
## Functions
bind Blend Shape Subset Weights 
```kotlin
@JvmStatic
```fun  bindBlendShapeSubsetWeights ( subsetName :  String ) :  AnimationBindTarget 
Binds to an entity's BlendShape subset weights. 
bind Blend Shape Weights 
```kotlin
@JvmStatic
```fun  bindBlendShapeWeights ( ) :  AnimationBindTarget 
Binds to an entity's BlendShape weights. 
bind Euler Angles 
```kotlin
@JvmStatic
```fun  bindEulerAngles ( ) :  AnimationBindTarget 
Binds to an entity's rotation represented as euler angles. 
bind Material 
```kotlin
@JvmStatic
```fun  bindMaterial ( materialIndex :  Int  =  0 ,  materialTarget :  MaterialTarget ) :  AnimationBindTarget 
Binds to a material property of an entity. See  MaterialTarget  to choose the property. 
```kotlin
@JvmStatic
```fun  bindMaterial ( materialIndex :  Int  =  0 ,  materialPropertyName :  String ) :  AnimationBindTarget 
Binds to a material property by its string name. 
bind Position 
```kotlin
@JvmStatic
```fun  bindPosition ( ) :  AnimationBindTarget 
Binds to an entity's position. 
bind Rotation 
```kotlin
@JvmStatic
```fun  bindRotation ( ) :  AnimationBindTarget 
Binds to an entity's rotation. 
bind Scale 
```kotlin
@JvmStatic
```fun  bindScale ( ) :  AnimationBindTarget 
Binds to an entity's scale. 
bind Transform 
```kotlin
@JvmStatic
```fun  bindTransform ( ) :  AnimationBindTarget 
Binds to an entity's  com.pico.spatial.core.math.Transform .