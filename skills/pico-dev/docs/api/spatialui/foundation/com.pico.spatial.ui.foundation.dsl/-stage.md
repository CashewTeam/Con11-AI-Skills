# Stage | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / Stage 
# Stage
```kotlin
fun SpatialAppScope.Stage(id: String, immersion: Immersion? = null, brightness: Brightness? = null, upperLimbRenderMode: UpperLimbRenderMode? = null, targetActivity: Class<out ComponentActivity>? = null, content: @Composable StageScope.() -> Unit)
```
Declare a Stage with unique  id . the  id  is used to executes open/close operation 
Stage is a boundless container provides by PICO OS. 
When Stage is opened, the system will hide windows from other apps. 
#### Parameters
id 
The unique id of Stage. 
immersion 
The immersion of the Stage when it's opened, only take effects when  openStage 's style is  StageStyle.Progressive , the default is  DefaultImmersionLevel , the range in  MinImmersionLevel .. MaxImmersionLevel . 
brightness 
which  Brightness  will be applied with this time for  Stage  , cannot be changed during stage alive 
upper Limb Render Mode 
the upperLimbRenderMode of Stage 
target Activity 
The activity that bind to this  Stage . 
content 
a  Composable  describe the content of Stage, typically use a  com.pico.spatial.ui.foundation.content.SpatialView  to present 3D content.