# WindowContainer | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / WindowContainer 
# WindowContainer
```kotlin
fun SpatialAppScope.WindowContainer(id: String, form: Form? = null, defaultSize: WindowContainerSize? = null, resizeType: ContainerResizeType? = null, defaultResizeRestriction: ContainerResizeRestriction? = null, enableMaterialBackground: Boolean? = null, volumeAlignment: VolumeAlignment? = null, defaultVolumeBasePanelType: VolumeBasePanelType? = null, defaultCaptionBarType: CaptionBarType? = null, placement: PlacementContext.() -> Placement? = null, targetActivity: Class<out ComponentActivity>? = null, worldScale: WorldScale? = null, content: @Composable WindowContainerScope.() -> Unit)
```
Declare a WindowContainer with unique  id . the  id  is used to open/close the WindowContainer. 
WindowContainer is a window-like container provides by PICO OS. 
Currently, every  WindowContainer  is associated with a single  android.app.Activity 
#### Parameters
id 
The WindowContainer id. 
form 
Style of the  WindowContainer , could be one of  Form.Planar  and  Form.Volumetric 
default Size 
The  WindowContainerSize  to define the  WindowContainer 's size. 
resize Type 
The  ContainerResizeType  of this  WindowContainer , defines how this  WindowContainer  can be resized. 
default Resize Restriction 
The default  ContainerResizeRestriction  of this  WindowContainer  when form is  Form.Planar , specifying the initial resizing behavior applied when the window is first created. 
enable Material Background 
Whether to enable material background for  WindowContainer . If the value is true, the material will be  Material.Regular . 
volume Alignment 
the  VolumeAlignment  of the  WindowContainer  when the form is  Form.Volumetric 
default Volume Base Panel Type 
Whether show the base panel for the  WindowContainer  when the form is  Form.Volumetric 
default Caption Bar Type 
Whether the caption bar should automatically hide 
placement 
The  Placement  of the  WindowContainer  when it is created. 
target Activity 
The activity to launch when this  WindowContainer  is opened. 
world Scale 
The  WorldScale  of the  WindowContainer . 
content 
Receives a  Composable  to display app content, will be called after  WindowContainer  is opened. 
```kotlin
fun SpatialAppScope.WindowContainer(id: String, form: Form? = null, properties: ContainerProperties.() -> Unit = {}, content: @Composable WindowContainerScope.() -> Unit)
```
Declare a WindowContainer with unique  id . the  id  is used to open/close the WindowContainer. 
WindowContainer is a window-like container provides by PICO OS. 
Currently, every  WindowContainer  is associated with a single  android.app.Activity 
You can update container's properties dynamically by using  properties  function. 
#### Parameters
id 
The WindowContainer id. 
form 
Style of the  WindowContainer , could be one of  Form.Planar  and  Form.Volumetric 
properties 
The  ContainerProperties  of the  WindowContainer . 
content 
Receives a  Composable  to display app content, will be called after  WindowContainer  is opened.