# panelSize | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / panelSize 
# panelSize
```kotlin
@Composable
```fun  panelSize ( @ FloatRange ( from  =  0.0 ,  to  =  2048.0 ) width :  Dp ,  @ FloatRange ( from  =  0.0 ,  to  =  2048.0 ) height :  Dp ) :  IntSize 
Converts the  Dp  size to  IntSize  in pixel for  AttachmentPanelComponent  using. If the  Dp  is  Dp.Unspecified , the  IntSize  will be  WRAP_CONTENT . 
#### Return
The  IntSize  instance in pixel. 
#### Parameters
width 
The width of the AttachmentPanelComponent in dp. 
height 
The height of the AttachmentPanelComponent in dp. 
```kotlin
@Composable
```fun  panelSize ( width :  Float ,  height :  Float ,  lengthUnit :  LengthUnit  =  LengthUnit.Meters ) :  IntSize 
Converts the  Float  size of length unit to  IntSize  in pixel for  AttachmentPanelComponent  using. If the  Float  is  Float.NaN , the  IntSize will be  WRAP_CONTENT . 
#### Return
The  IntSize  instance in pixel. 
#### Parameters
width 
The width of the AttachmentPanelComponent in the unit of  lengthUnit . 
height 
The height of the AttachmentPanelComponent in the unit of  lengthUnit . 
length Unit 
The unit of the  width  and  height . Default value is  LengthUnit.Meters .