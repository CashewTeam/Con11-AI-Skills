# Chip | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Chip 
# Chip
```kotlin
@Composable
```fun  Chip ( label :  @ Composable ( )  ->  Unit ,  onClick :  ( )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  colors :  ChipColors  =  ChipsDefaults.chipColors() ,  chipSize :  ChipSize  =  ChipsDefaults.Small ,  contentPadding :  PaddingValues  =  chipSize.contentPadding(leading = leadingIcon != null) ,  contentGap :  Dp  =  chipSize.contentGap() ,  shape :  Shape  =  RoundedCornerShape(chipSize.cornerRadius()) ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Basic chip. 
#### Parameters
label 
the content of the ButtonChip, typically a  Text . Text color is defined by  ChipColors.contentColor . 
on Click 
called when the chip is clicked. 
modifier 
Modifier to be applied to the chip. 
leading Icon 
Optional icon at the start of the chip, preceding the content text. 
trailing Icon 
Optional icon at the end of the chip, following the content text. 
enabled 
When disabled, chip will not respond to user input. It will also appear visually disabled to accessibility services. 
colors 
the colors for content including  label ,  leadingIcon ,  trailingIcon  and background of chip. 
chip Size 
the size of chip. 
content Padding 
padding for content of this chip. 
content Gap 
the gap between  leadingIcon , label , trailingIcon . 
shape 
the shape of this chip. 
interaction Source 
the  MutableInteractionSource  representing the stream of Interactions for this chip. 
#### See also
Button Chip Removable Chip Toggleable Chip