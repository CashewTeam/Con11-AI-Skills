# Icon | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Icon 
# Icon
```kotlin
@Composable
```fun  Icon ( imageVector :  ImageVector ,  contentDescription :  String ? ,  modifier :  Modifier  =  Modifier ,  tint :  Color  =  LocalContentColor.current ) 
A PICO design icon component that draws  imageVector  using  tint , with a default value of  LocalContentColor . If  imageVector  has no intrinsic size, this component uses the recommended default size. Icon is an opinionated component designed to be used with single-color icons so that they can be tinted correctly for the component they are placed in. For multicolored icons and icons that should not be tinted, use  Color.Unspecified  for  tint . For generic images that should not be tinted, and do not follow the recommended icon size, use the generic  androidx.compose.foundation.Image  instead. For a clickable icon, see  IconButton . 
#### Parameters
image Vector 
ImageVector  to draw inside this icon 
content Description 
text used by accessibility services to describe what this icon represents. This should always be provided unless this icon is used for decorative purposes, and does not represent a meaningful action that a user can take. This text should be localized, such as by using  androidx.compose.ui.res.stringResource  or similar 
modifier 
the  Modifier  to be applied to this icon 
tint 
tint to be applied to  imageVector . If  Color.Unspecified  is provided, then no tint is applied. 
```kotlin
@Composable
```fun  Icon ( bitmap :  ImageBitmap ,  contentDescription :  String ? ,  modifier :  Modifier  =  Modifier ,  tint :  Color  =  LocalContentColor.current ) 
A PICO design icon component that draws  bitmap  using  tint , with a default value of  LocalContentColor . If  bitmap  has no intrinsic size, this component uses the recommended default size. Icon is an opinionated component designed to be used with single-color icons so that they can be tinted correctly for the component they are placed in. For multicolored icons and icons that should not be tinted, use  Color.Unspecified  for  tint . For generic images that should not be tinted, and do not follow the recommended icon size, use the generic  androidx.compose.foundation.Image  instead. For a clickable icon, see  IconButton . 
#### Parameters
bitmap 
ImageBitmap  to draw inside this icon 
content Description 
text used by accessibility services to describe what this icon represents. This should always be provided unless this icon is used for decorative purposes, and does not represent a meaningful action that a user can take. This text should be localized, such as by using  androidx.compose.ui.res.stringResource  or similar 
modifier 
the  Modifier  to be applied to this icon 
tint 
tint to be applied to  bitmap . If  Color.Unspecified  is provided, then no tint is applied. 
```kotlin
@Composable
```fun  Icon ( painter :  Painter ,  contentDescription :  String ? ,  modifier :  Modifier  =  Modifier ,  tint :  Color  =  LocalContentColor.current ) 
A PICO design icon component that draws  painter  using  tint , with a default value of  LocalContentColor . If  painter  has no intrinsic size, this component uses the recommended default size. Icon is an opinionated component designed to be used with single-color icons so that they can be tinted correctly for the component they are placed in. For multicolored icons and icons that should not be tinted, use  Color.Unspecified  for  tint . For generic images that should not be tinted, and do not follow the recommended icon size, use the generic  androidx.compose.foundation.Image  instead. For a clickable icon, see  IconButton . 
#### Parameters
painter 
Painter  to draw inside this icon 
content Description 
text used by accessibility services to describe what this icon represents. This should always be provided unless this icon is used for decorative purposes, and does not represent a meaningful action that a user can take. This text should be localized, such as by using  androidx.compose.ui.res.stringResource  or similar 
modifier 
the  Modifier  to be applied to this icon 
tint 
tint to be applied to  painter . If  Color.Unspecified  is provided, then no tint is applied.