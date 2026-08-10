# controllerHapticFeedback | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.haptic / controllerHapticFeedback 
# controllerHapticFeedback
```kotlin
@Stable
```fun  Modifier . controllerHapticFeedback ( type :  HandControllerHapticType ?  =  null ,  interactionSource :  InteractionSource ?  =  null ) :  Modifier 
Adds haptic feedback support for spatial hand controllers in PicoOS. 
This modifier automatically plays a haptic feedback effect when the hand controller is pressed. It is highly recommended to apply this modifier when a click event or similar interactive action is triggered. 
#### Return
The modified  Modifier  with haptic feedback capabilities. 
#### Parameters
type 
The type of haptic feedback to play, optional. Defaults to  HandControllerHapticType.Press . 
interaction Source 
The  InteractionSource  to use for haptic feedback. when the haptic feedback is triggered, the  InteractionSource  will be used to check if the hand controller is pressed. If not provided, the modifier will use the default  InteractionSource  from the  pointerInput  modifier. 
#### Samples
com.pico.spatial.foundation.samples.ControllerHapticFeedbackSample