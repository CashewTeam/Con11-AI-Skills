# animateColorVibrantAsState | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.vibrant / animateColorVibrantAsState 
# animateColorVibrantAsState
```kotlin
@Composable
```fun  animateColorVibrantAsState ( targetValue :  Color ,  animationSpec :  AnimationSpec < Color >  =  spring() ,  label :  String  =  "ColorAnimation" ,  finishedListener :  ( Color )  ->  Unit ?  =  null ) :  State < Color > 
Animates a  Color  that possesses a  Vibrant  style (blending intensity). 
Why use this instead of  androidx.compose.animation.animateColorAsState ? 
- 
androidx.compose.animation.animateColorAsState : Will  lose  the Vibrant style during the animation. This causes the special rendering effect to vanish or flicker while the color changes. 
- 
animateColorVibrantAsState : Guarantees that the Vibrant style is  preserved  throughout the entire animation, ensuring a smooth visual transition without losing the material effect. 
Important Limitation:  This function only supports animating colors with the  same Vibrant  style. It does  not  support animating between different Vibrant styles. 
- 
Supported :  Color.Red.withVibrant(Vibrant.Dark)  -> Color.Blue.withVibrant(Vibrant.Dark) 
- 
Not Supported :  Color.Red.withVibrant(Vibrant.Dark)  -> Color.Red.withVibrant(Vibrant.Light) 
- 
Not Supported : Use  Color.Vibrant  to play color animation. 
Usage:  Use this function exclusively when animating colors that have a Vibrant style attached. 
#### Parameters
target Value 
The target color containing the Vibrant style. 
animation Spec 
The animation spec, defaults to  spring . 
label 
Animation label for debugging and tooling. 
finished Listener 
Callback when animation finishes.