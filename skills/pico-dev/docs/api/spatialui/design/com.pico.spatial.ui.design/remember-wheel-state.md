# rememberWheelState | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / rememberWheelState 
# rememberWheelState
```kotlin
@Composable
```fun  rememberWheelState ( vararg  inputs :  Any ? ,  initialFirstVisibleItemIndex :  Int  =  0 ,  initialFirstVisibleItemScrollOffset :  Int  =  0 ) :  LazyListState 
state for  WheelPicker 
#### Parameters
inputs 
inputs - A set of inputs such that, when any of them have changed, will cause the state to reset 
initial First Visible Item Index 
the initial value for  LazyListState.firstVisibleItemIndex 
initial First Visible Item Scroll Offset 
the initial value for LazyListState.firstVisibleItemScrollOffset