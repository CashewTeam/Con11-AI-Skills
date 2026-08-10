# SpringEasingArgs | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.tokens / SpringEasingArgs 
# SpringEasingArgs
```kotlin
@Immutable
```class  SpringEasingArgs ( val  dampingRatio :  Float ,  val  stiffness :  Float ) 
A data class to hold  androidx.compose.animation.core.SpringSpec 's args 
Members Members & Extensions 
## Constructors
Spring Easing Args 
```kotlin
constructor(dampingRatio: Float, stiffness: Float)
```
## Types
Companion 
```kotlin
object Companion
```
The companion of  SpringEasingArgs . 
## Properties
damping Ratio 
```kotlin
val dampingRatio: Float
```
damping ratio of the spring 
stiffness 
```kotlin
val stiffness: Float
```
stiffness of the spring 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to Spring 
```kotlin
@Stable
```fun  < T >  SpringEasingArgs . toSpring ( visibilityThreshold :  T ?  =  null ) :  SpringSpec < T > 
Utils function to convert  SpringEasingArgs  to  SpringSpec 
to String 
```kotlin
open override fun toString(): String
```