# com.pico.spatial.ui.design.tokens | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.tokens 
# Package-level declarations
Types Functions 
## Types
Motion Tokens 
```kotlin
object MotionTokens
```
PICO Design's motion tokens. 
Spring Easing Args 
```kotlin
@Immutable
```class  SpringEasingArgs ( val  dampingRatio :  Float ,  val  stiffness :  Float ) 
A data class to hold  androidx.compose.animation.core.SpringSpec 's args 
## Functions
to Spring 
```kotlin
@Stable
```fun  < T >  SpringEasingArgs . toSpring ( visibilityThreshold :  T ?  =  null ) :  SpringSpec < T > 
Utils function to convert  SpringEasingArgs  to  SpringSpec