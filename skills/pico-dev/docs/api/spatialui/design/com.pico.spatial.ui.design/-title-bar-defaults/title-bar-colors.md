# titleBarColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / TitleBarDefaults / titleBarColors 
# titleBarColors
```kotlin
@Composable
```fun  titleBarColors ( ) :  TitleBarColors 
The default colors used for  TitleBar 
```kotlin
@Composable
```fun  titleBarColors ( titleColor :  Color  =  Color.Unspecified ,  leadingColor :  Color  =  Color.Unspecified ,  trailingColor :  Color  =  Color.Unspecified ) :  TitleBarColors 
custom colors for linear progress indicator 
#### Return
The new  ProgressColors  instance with expected indicatorColor and backgroundColor. 
#### Parameters
title Color 
The color of title 
leading Color 
The color of leading actions 
trailing Color 
The color of trailing actions