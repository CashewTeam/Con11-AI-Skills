# WheelPicker | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / WheelPicker 
# WheelPicker
```kotlin
@Composable
```fun  WheelPicker ( count :  Int ,  getItemText :  ( Int )  ->  String ,  modifier :  Modifier  =  Modifier ,  itemHeight :  Dp  =  WheelPickerDefaults.DefaultItemHeight ,  itemMargin :  Dp  =  WheelPickerDefaults.defaultItemMargin ,  rowNumber :  Int  =  7 ,  onSelectedChange :  ( Int )  ->  Unit ?  =  null ,  semanticsContent :  String ?  =  null ,  colors :  WheelPickerColors  =  WheelPickerDefaults.wheelPickerColors() ,  initialSelectedIndex :  Int  =  rowNumber / 2 ,  indicatorBackgroundShape :  Shape  =  WheelPickerDefaults.DefaultIndicatorShape ,  indicatorCenterTextStyle :  TextStyle  =  PicoTheme.typography.headlineLarge ,  isInfinite :  Boolean  =  false ,  leftText :  @ Composable ( )  ->  Unit ?  =  null ,  rightText :  @ Composable ( )  ->  Unit ?  =  null ,  state :  LazyListState  =  with(count) {
            check(this > 0) { "count must lager than 0" }
            rememberWheelState(
                count,
                rowNumber,
                initialFirstVisibleItemIndex = initialSelectedIndex % this,
            )
        } ) 
A common picker widget defined by PICO Design. 
#### Parameters
count 
The items count. 
get Item Text 
Returns the text based on the given index. 
modifier 
The  Modifier  used by the WheelPicker. 
item Height 
The height of picker's item. 
item Margin 
The margin of picker's item. 
row Number 
The number of visible rows. 
on Selected Change 
Will be called with the current selected index when scrolling finished. 
semantics Content 
The semantic content of this picker. 
colors 
A  WheelPickerColors  to customize the appearance of pickers. 
initial Selected Index 
The initial selected item index, default is rowNumber/2. 
indicator Background Shape 
The indicator's background shape. 
indicator Center Text Style 
The  TextStyle  used by the indicator to draw text. 
is Infinite 
Whether the list can scroll infinitely. 
left Text 
The text will show at left of indicator center text. 
right Text 
The text will show at right of indicator center text. 
state 
The state object to be used to control or observe the list's state. See also  rememberWheelState .