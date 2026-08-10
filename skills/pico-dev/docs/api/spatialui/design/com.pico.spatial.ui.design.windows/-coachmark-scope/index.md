# CoachmarkScope | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / CoachmarkScope 
# CoachmarkScope
```kotlin
interface CoachmarkScope
```
Scope for coachmark content. 
Members & Extensions 
## Functions
Image Coachmark 
```kotlin
@Composable
```fun  CoachmarkScope . ImageCoachmark ( image :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  button :  @ Composable ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  LocalTokensBearer.current.dimension.RadiusLarge ,  padding :  Dp  =  ImagePadding ) 
ImageCoachmark  usually used to display image for anchor UI. It typically contains an image and an optional button. 
Rich Coachmark 
```kotlin
@Composable
```fun  CoachmarkScope . RichCoachmark ( modifier :  Modifier  =  Modifier ,  image :  @ Composable ( )  ->  Unit ?  =  null ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  buttons :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  if (image != null) LocalTokensBearer.current.dimension.RadiusLarge
        else LocalTokensBearer.current.dimension.RadiusMedium ,  content :  @ Composable ( )  ->  Unit ) 
ImageCoachmark  usually used to display rich message for anchor UI. It typically contains an optional image, title, content and buttons. 
Simple Coachmark 
```kotlin
@Composable
```fun  CoachmarkScope . SimpleCoachmark ( text :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  button :  @ Composable ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  LocalTokensBearer.current.dimension.RadiusMedium ) 
SimpleCoachmark  usually used to display brevity message for anchor UI. It typically contains text and an optional button.