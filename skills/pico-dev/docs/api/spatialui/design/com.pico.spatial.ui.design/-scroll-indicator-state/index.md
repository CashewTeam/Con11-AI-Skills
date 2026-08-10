# ScrollIndicatorState | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ScrollIndicatorState 
# ScrollIndicatorState
```kotlin
@Stable
```interface  ScrollIndicatorState 
State for a scroll indicator. 
Members 
## Properties
indicator Height 
```kotlin
abstract val indicatorHeight: Dp
```
The height of the indicator. 
indicator Offset 
```kotlin
abstract val indicatorOffset: Dp
```
The offset of the indicator. 
is Scroll In Progress 
```kotlin
open val isScrollInProgress: Boolean
```
Whether the scrollable view is scrolling or the indicator is pressed. 
orientation 
```kotlin
abstract val orientation: Orientation
```
The orientation of the scroll indicator. 
position Updater 
```kotlin
abstract val positionUpdater: @Composable ScrollIndicatorState.() -> Unit
```
The function to update the scroll position of the indicator. 
pressed 
```kotlin
abstract var pressed: Boolean
```
Whether the indicator is pressed. 
scrollable State Of View 
```kotlin
abstract val scrollableStateOfView: ScrollableState
```
The scrollable state of the scrollable view bind to this indicator. 
scrolled Px 
```kotlin
abstract var scrolledPx: Float
```
Distance that the scrollable view has been scrolled. 
scroll View Axis Size 
```kotlin
abstract var scrollViewAxisSize: Float
```
Width or Height of the scrollable view. 
total Scrollable Distance Px 
```kotlin
abstract var totalScrollableDistancePx: Float
```
Total scrollable value of the scrollable view. 
track Height 
```kotlin
abstract var trackHeight: Dp
```
The height of the track. 
track Width 
```kotlin
abstract var trackWidth: Dp
```
The width of the track.