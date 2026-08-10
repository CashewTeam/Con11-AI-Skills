# com.pico.spatial.ui.design.menu | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.menu 
# Package-level declarations
Types Functions 
## Types
Menu Item Colors 
```kotlin
@Stable
```class  MenuItemColors 
Represents the container and content colors used in a list item in different states. 
Menu Item Defaults 
```kotlin
object MenuItemDefaults
```
MenuItemDefaults 
Menu Item Text Styles 
```kotlin
class MenuItemTextStyles
```
text style 
## Functions
Basic Menu Item 
```kotlin
@Composable
```fun  BasicMenuItem ( modifier :  Modifier  =  Modifier ,  subMenu :  @ Composable ( )  ->  Unit ?  =  null ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
Custom menu item for  Menu / Menu . 
Menu 
```kotlin
@Composable
```fun  Menu ( onDismissRequest :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  positionProvider :  PopupPositionProvider  =  rememberMenuPositionProvider() ,  scrollState :  ScrollState  =  rememberScrollState() ,  properties :  PopupProperties  =  MenuDefaults.DefaultPopupProperties ,  padding :  PaddingValues  =  MenuDefaults.DefaultMenuPadding ,  cornerRadius :  Dp  =  MenuDefaults.DefaultMenuCornerRadius ,  hasScrollIndicator :  Boolean  =  false ,  content :  @ Composable ColumnScope . ( )  ->  Unit ) 
A dropdown menu is a compact way of displaying multiple choices. It appears upon interaction with an element (such as an icon or button) or when users perform a specific action. 
Menu Item 
```kotlin
@Composable
```fun  MenuItem ( title :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  subMenu :  @ Composable ( )  ->  Unit ?  =  null ,  onClick :  ( )  ->  Unit ?  =  null ,  subtitle :  @ Composable ( )  ->  Unit ?  =  null ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  contentColors :  MenuItemColors  =  MenuItemDefaults.menuItemColors() ,  paddings :  PaddingValues  =  MenuItemDefaults.DefaultPadding ,  cornerSize :  Dp  =  MenuItemDefaults.RoundRadius ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Standard menuItem for  Menu / SubMenu . Some slot was provide for developers to fastly build standard menu, such as  title , subtitle ,  leadingIcon ,  trailingIcon . 
remember Menu Position Provider 
```kotlin
@Composable
```fun  rememberMenuPositionProvider ( horizontalPlacement :  HorizontalPlacement  =  HorizontalPlacement.alignStart() ,  verticalPlacement :  VerticalPlacement  =  VerticalPlacement.below(offset = MenuDefaults.DefaultMenuOffset) ) :  PopupPositionProvider 
Provides a  SpatialPositionProvider  that places the menu relative to it's anchor view. 
remember Sub Menu Position Provider 
```kotlin
@Composable
```fun  rememberSubMenuPositionProvider ( horizontalPlacement :  HorizontalPlacement  =  HorizontalPlacement.toEndOf() ) :  PopupPositionProvider 
Provides a  SpatialPositionProvider  that places the sub menu relative to it's parent menu. 
Sub Menu 
```kotlin
@Composable
```fun  SubMenu ( onDismissRequest :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  positionProvider :  PopupPositionProvider  =  rememberSubMenuPositionProvider() ,  scrollState :  ScrollState  =  rememberScrollState() ,  properties :  PopupProperties  =  MenuDefaults.DefaultPopupProperties ,  padding :  PaddingValues  =  MenuDefaults.DefaultMenuPadding ,  cornerRadius :  Dp  =  MenuDefaults.DefaultMenuCornerRadius ,  hasScrollIndicator :  Boolean  =  false ,  content :  @ Composable ColumnScope . ( )  ->  Unit ) 
A submenu is a compact way of displaying multiple choices of  Menu .