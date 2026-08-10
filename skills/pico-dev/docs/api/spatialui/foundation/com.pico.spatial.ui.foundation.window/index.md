# com.pico.spatial.ui.foundation.window | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.window 
# Package-level declarations
Types Functions 
## Types
Augment Content Alignment 
```kotlin
@JvmInline
```value  class  AugmentContentAlignment 
A normalized point relative to the Augment itself 
Window Params Modifier 
```kotlin
typealias WindowParamsModifier = (attributes: WindowManager.LayoutParams, triggerView: View) -> Unit
```Window Size Behaviors 
```kotlin
enum WindowSizeBehaviors : Enum<WindowSizeBehaviors>
```
Window size behaviors 
## Functions
Augment 
```kotlin
@Composable
```fun  Augment ( anchor :  NormalizedPoint3D ,  alignment :  AugmentContentAlignment ,  offset :  DpOffset3D  =  DpOffset3D.Zero ,  rotation3D :  Rotation3D ?  =  null ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  cornerRadius :  Dp  =  AugmentDefaults.defaultCornerRadius ,  enableMaterialBackground :  Boolean  =  true ,  focusable :  Boolean  =  true ,  windowSizeBehaviors :  WindowSizeBehaviors  =  WindowSizeBehaviors.Adaptive ,  content :  @ Composable ( )  ->  Unit ) 
```kotlin
@Composable
```fun  Augment ( anchor :  NormalizedPoint3D ,  alignment :  AugmentContentAlignment ,  offset :  IntOffset3D ,  rotation3D :  Rotation3D ?  =  null ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  cornerRadius :  Dp  =  AugmentDefaults.defaultCornerRadius ,  enableMaterialBackground :  Boolean  =  true ,  focusable :  Boolean  =  true ,  windowSizeBehaviors :  WindowSizeBehaviors  =  WindowSizeBehaviors.Adaptive ,  content :  @ Composable ( )  ->  Unit ) 
A Augment is a container that can be placed around the main window. 
Augment Content Alignment 
```kotlin
@Stable
```fun  AugmentContentAlignment ( x :  Float ,  y :  Float ) :  AugmentContentAlignment 
Creates an  AugmentContentAlignment  from a given x and y.