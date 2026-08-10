# com.pico.spatial.ui.foundation.vibrant | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.vibrant 
# Package-level declarations
Types Functions 
## Types
Vibrant 
```kotlin
enum Vibrant : Enum<Vibrant>
```
Vibrant styles. 
## Functions
animate Color Vibrant As State 
```kotlin
@Composable
```fun  animateColorVibrantAsState ( targetValue :  Color ,  animationSpec :  AnimationSpec < Color >  =  spring() ,  label :  String  =  "ColorAnimation" ,  finishedListener :  ( Color )  ->  Unit ?  =  null ) :  State < Color > 
Animates a  Color  that possesses a  Vibrant  style (blending intensity). 
contains Vibrant 
```kotlin
fun Color.containsVibrant(): Boolean
```
Checks if the  Color  contains a  Vibrant  style. 
observe Current Vibrant Effect 
```kotlin
fun Modifier.observeCurrentVibrantEffect(observer: (vibrant: Vibrant?) -> Unit): Modifier
```
A utility function that helps you to observe the current vibrant effect. 
obtain Vibrant 
```kotlin
fun Color.obtainVibrant(): Vibrant
```
Decodes the vibrant style from the  Color . 
take Or Else 
```kotlin
inline fun Vibrant.takeOrElse(block: () -> Vibrant): Vibrant
```
Return the specified vibrant style if it is specified, otherwise return the default vibrant style. 
vibrant Effect 
```kotlin
fun Modifier.vibrantEffect(vibrant: Vibrant): Modifier
```
A modifier that make current node and its subsequent node in vibrant render mode. 
with Vibrant 
```kotlin
fun Color.withVibrant(vibrant: Vibrant): Color
```
Encodes the specified  Vibrant  style into the  Color .