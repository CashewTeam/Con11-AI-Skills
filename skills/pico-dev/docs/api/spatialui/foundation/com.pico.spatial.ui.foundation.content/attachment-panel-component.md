# attachmentPanelComponent | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / attachmentPanelComponent 
# attachmentPanelComponent
```kotlin
@Composable
```fun  attachmentPanelComponent ( context :  Context  =  LocalContext.current ,  size :  IntSize  =  panelSize(Dp.Unspecified, Dp.Unspecified) ,  alignment :  AttachmentPanelComponent.Alignment  =  AttachmentPanelComponent.Alignment.UNSPECIFIED ,  content :  @ Composable ( )  ->  Unit ) :  AttachmentPanelComponent 
Creates a  AttachmentPanelComponent  in another Composable. Notice that this function is for your convenience to create a AttachmentPanelComponent in your Composable, once the return value set to an Entity, your later changes will not take effect. 
#### Return
The  AttachmentPanelComponent  instance. 
#### Parameters
context 
The context usually is an Activity. 
size 
The size of the AttachmentPanelComponent in pixel. Default value is  panelSize(Dp.Unspecified, Dp.Unspecified) , which means the size will be determined by the content of AttachmentPanelComponent. If you want to set the size in dp, please use  panelSize(width: Dp, height: Dp) . If you want to set the size in meters, please use  panelSize(width: Float, height: Float, lengthUnit: LengthUnit = LengthUnit.Meters) . 
alignment 
The alignment point of the AttachmentPanelComponent, which describes the position of the AttachmentPanelComponent relative to the Entity. When not specified, panel aligns its center to the Entity. 
content 
The content of the AttachmentPanelComponent.