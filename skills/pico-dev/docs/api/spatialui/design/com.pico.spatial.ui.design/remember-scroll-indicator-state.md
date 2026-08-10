# rememberScrollIndicatorState | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / rememberScrollIndicatorState 
# rememberScrollIndicatorState
```kotlin
@Composable
```fun  rememberScrollIndicatorState ( orientation :  Orientation ,  state :  ScrollState ) :  ScrollIndicatorState 
Create a  ScrollIndicatorState  for  ScrollState . 
#### Parameters
orientation 
The orientation of the scroll indicator.  Orientation.Vertical  for  Column  and  Orientation.Horizontal  for  Row . 
state 
The  ScrollState  that applied to Modifier.verticalScroll or Modifier.horizontalScroll of  Column  or  Row . 
```kotlin
@Composable
```fun  rememberScrollIndicatorState ( state :  LazyListState ) :  ScrollIndicatorState 
Create a  ScrollIndicatorState  for  LazyListState . 
#### Parameters
state 
The  LazyListState  that applied to  LazyColumn  or  LazyRow . 
```kotlin
@Composable
```fun  rememberScrollIndicatorState ( state :  LazyGridState ) :  ScrollIndicatorState 
Create a  ScrollIndicatorState  for  LazyGridState . 
Estimation strategy: 
- 
Compute per-line max main-axis item size and average it as the "average line height/width". 
- 
Total lines ≈  ceil(totalItemsCount / maxSpan) . 
- 
scrolledPx  ≈ average line main-axis size × current line index +  firstVisibleItemScrollOffset . 
- 
totalScrollableDistancePx  ≈ average line main-axis size × total lines − viewport length. 
```kotlin
@Composable
```fun  rememberScrollIndicatorState ( state :  LazyStaggeredGridState ) :  ScrollIndicatorState 
Create a  ScrollIndicatorState  for  LazyStaggeredGridState . 
Estimation strategy: 
- 
Infer maximum lane count  spanMax  from visible items'  lane . 
- 
scrolledPx  ≈ average item main-axis size × current line index +  firstVisibleItemScrollOffset . Current line index is approximated by  firstVisibleItemIndex / spanMax . 
- 
totalScrollableDistancePx  ≈ average item main-axis size × total items /  spanMax  − viewport length.