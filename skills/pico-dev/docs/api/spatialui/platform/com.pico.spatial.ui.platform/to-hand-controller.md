# toHandController | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / toHandController 
# toHandController
```kotlin
fun InteractionKindExtra.toHandController(): HandController
```
Converts this  InteractionKindExtra  to the corresponding  HandController . 
This is useful for determining which hand (left or right) an interaction originated from. 
#### Return
HandController.Left ,  HandController.Right , or  HandController.Unknown  if it cannot be determined.