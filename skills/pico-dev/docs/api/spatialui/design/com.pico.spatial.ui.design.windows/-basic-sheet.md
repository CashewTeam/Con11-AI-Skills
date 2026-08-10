# BasicSheet | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / BasicSheet 
# BasicSheet
```kotlin
@Composable
```fun  BasicSheet ( onDismissRequest :  ( )  ->  Unit ,  properties :  DialogProperties  =  SheetDefaults.DefaultSheetsProperties ,  cornerRadius :  Dp  =  SheetDefaults.CornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  sheetContent :  @ Composable ( )  ->  Unit ) 
A basic sheet, can be used to show a sheet with custom content. usually used when the design is different from the default sheet, likes  Sheet 、 HeadImageSheet . 
#### Parameters
on Dismiss Request 
Executes when the user clicks outside the popup. 
properties 
see  DialogProperties . 
corner Radius 
The corner radius of the sheet. 
follow Viewpoints 
The viewpoints that the sheet will follow. 
sheet Content 
The content of sheet