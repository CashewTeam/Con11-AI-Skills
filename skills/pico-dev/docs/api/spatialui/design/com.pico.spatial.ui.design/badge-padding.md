# badgePadding | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / badgePadding 
# badgePadding
```kotlin
@Composable
```fun  BadgeSize . badgePadding ( ) :  PaddingValues 
Calculates the inner padding values for a badge based on its size. 
This function uses a  when  expression to map different  BadgeSize  instances to corresponding  PaddingValues . It provides a convenient way to define consistent padding rules for various badge sizes. 
#### Return
The  PaddingValues  representing the inner padding for the badge. 
#### Receiver
The  BadgeSize  for which the padding values are calculated.