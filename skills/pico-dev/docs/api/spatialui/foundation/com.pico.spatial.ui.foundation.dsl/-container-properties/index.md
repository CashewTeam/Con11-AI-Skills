# ContainerProperties | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / ContainerProperties 
# ContainerProperties
```kotlin
interface ContainerProperties
```
Interface that defines the properties of a  WindowContainer . 
Members 
## Properties
default Caption Bar Type 
```kotlin
abstract var defaultCaptionBarType: CaptionBarType?
```
Whether the caption bar should automatically hide 
default Resize Restriction 
```kotlin
abstract var defaultResizeRestriction: ContainerResizeRestriction?
```
The default  ContainerResizeRestriction  of this  WindowContainer  when form is  Form.Planar , specifying the initial resizing behavior applied when the window is first created. 
default Size 
```kotlin
abstract var defaultSize: WindowContainerSize?
```
The size of the  WindowContainer  will be set to this value when the  WindowContainer  is opened. 
default Volume Base Panel Type 
```kotlin
abstract var defaultVolumeBasePanelType: VolumeBasePanelType?
```
Whether show the base panel for the  WindowContainer  when the form is  Form.Volumetric 
enable Material Background 
```kotlin
abstract var enableMaterialBackground: Boolean?
```
Whether to enable material background for  WindowContainer . If the value is true, the material will be  com.pico.spatial.ui.platform.Material.Regular . 
placement 
```kotlin
abstract var placement: PlacementContext.() -> Placement?
```
The  Placement  of the  WindowContainer  when it is created. 
resize Type 
```kotlin
abstract var resizeType: ContainerResizeType?
```
The  ContainerResizeType  of this  WindowContainer , defines how this  WindowContainer  can be resized. 
target Activity 
```kotlin
abstract var targetActivity: Class<out ComponentActivity>?
```
The activity to launch when this  WindowContainer  is opened. 
volume Alignment 
```kotlin
abstract var volumeAlignment: VolumeAlignment?
```
The  VolumeAlignment  of the  WindowContainer  when the form is  Form.Volumetric 
world Scale 
```kotlin
abstract var worldScale: WorldScale?
```
The  WorldScale  of the  WindowContainer .