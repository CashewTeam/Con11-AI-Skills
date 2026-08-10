# ScrollIndicator | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ScrollIndicator 
# ScrollIndicator
```kotlin
@Composable
```fun  BoxScope . ScrollIndicator ( state :  ScrollState ,  orientation :  Orientation ,  modifier :  Modifier  =  Modifier ,  alignment :  Alignment  =  if (orientation == Orientation.Vertical) Alignment.CenterEnd else Alignment.BottomCenter ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.defaultHotAreaPadding(orientation, alignment) ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  minVisibleSize :  Dp  =  ScrollIndicatorDefaults.MinSize ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  dismissAfter :  Long  =  3000 ) 
Scroll indicator is used to indicate scrolling progress of a scrollable view with Modifier.verticalScroll or Modifier.horizontalScroll, like  Column  or  Row . You can also drag the indicator to scroll the content of scrollable view. 
Scrolling indicator is only visible when the list view is scrolling or user drag the indicator. The indicator will be hidden after  dismissAfter  seconds if the list view is not scrolling or user is not dragging the indicator. 
The best practice is to put the scrollable view and indicator in same  Box  to auto place the indicator. You can also use params  alignment  to control the position of the indicator. To place the indicator any where, you can wrap it with a  Box  and then place the  Box  anywhere 
#### Parameters
state 
The scroll state that applied to Modifier.verticalScroll or Modifier.horizontalScroll of  Column  or  Row . 
orientation 
The orientation of the scroll indicator.  Orientation.Vertical  for  Column  and  Orientation.Horizontal  for  Row . 
modifier 
Compose modifier applied to this indicator. 
alignment 
Alignment of the indicator in the parent  Box . 
padding For Interaction 
Add this padding value to make a larger interactive area. 
colors 
The colors of the indicator. 
min Visible Size 
The minimum size of the indicator. If the scrollable view size is smaller than the minimum size, the indicator will not be shown. You can set it to  Dp.Unspecified  to disable this feature. 
scrolling Mark Size 
The size of the scrolling mark. 
dismiss After 
The time in milliseconds to dismiss the indicator after it is not scrolling or user is not dragging the indicator. 
#### Samples
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a scroll state
    val state = rememberScrollState()
    Column(
        modifier =
            Modifier.fillMaxSize()
                // 2. apply the scroll state to the column
                .verticalScroll(state)
    ) {
        repeat(times = 100) {
            Box(
                modifier = Modifier.fillMaxWidth().height(50.dp),
                contentAlignment = Alignment.Center,
            ) {
                Text("Item $it")
            }
            Divider()
        }
    }
    // 3. apply the scroll state to the scroll indicator
    ScrollIndicator(state = state, orientation = Orientation.Vertical)
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a scroll state
    val state = rememberScrollState()
    Row(
        modifier =
            Modifier.fillMaxSize()
                // 2. apply the scroll state to the Row
                .horizontalScroll(state)
    ) {
        repeat(times = 100) {
            // add your content here
            Text("item $it")
            Divider(orientation = Orientation.Vertical)
        }
    }
    // 3. apply the scroll state to the scroll indicator
    ScrollIndicator(state = state, orientation = Orientation.Horizontal)
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a scroll state
    val state = rememberScrollState()
    Column(
        modifier =
            Modifier.fillMaxSize()
                // 2. apply the scroll state to the column
                .verticalScroll(state)
    ) {
        // add your content here
    }
    ScrollIndicator(
        state = state,
        orientation = Orientation.Vertical,
        // 3. use Box alignment to control the position of the scroll indicator
        alignment = Alignment.CenterStart,
    )
} 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  BoxScope . ScrollIndicator ( state :  LazyListState ,  modifier :  Modifier  =  Modifier ,  alignment :  Alignment  =  if (state.layoutInfo.orientation == Orientation.Vertical) Alignment.CenterEnd
        else Alignment.BottomCenter ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.defaultHotAreaPadding(state.layoutInfo.orientation, alignment) ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  minVisibleSize :  Dp  =  ScrollIndicatorDefaults.MinSize ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  dismissAfter :  Long  =  3000 ) 
Scroll indicator is used to indicate scrolling progress of a list view, just like  LazyColumn  or  LazyRow . You can also drag the indicator to scroll the content of list view. 
Scrolling indicator is only visible when the list view is scrolling or user drag the indicator. The indicator will be hidden after  dismissAfter  seconds if the list view is not scrolling or user is not dragging the indicator. 
The best practice is to put the scrollable view and indicator in same  Box  to auto place the indicator. You can also use params  alignment  to control the position of the indicator. To place the indicator any where, you can wrap it with a  Box  and then place the  Box  anywhere 
#### Parameters
state 
The scroll state that applied to  LazyColumn  or  LazyRow . 
modifier 
Compose modifier applied to this indicator. 
alignment 
Alignment of the indicator in the parent  Box . 
padding For Interaction 
Add this padding value to make a larger interactive area. 
colors 
The colors of the indicator. 
min Visible Size 
The minimum size of the indicator. If the scrollable view size is smaller than the minimum size, the indicator will not be shown. You can set it to  Dp.Unspecified  to disable this feature. 
scrolling Mark Size 
The size of the scrolling mark. 
dismiss After 
The time to dismiss the indicator after the list view is not scrolling or user is not dragging the indicator. 
#### Samples
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a scroll state
    val state = rememberLazyListState()
    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        // 2. apply the scroll state to the LazyColumn
        state = state,
    ) {
        items(count = 100) {
            Box(modifier = Modifier.fillMaxWidth().height(50.dp)) { Text("Item $it") }
            Divider()
        }
    }
    // 3. apply the scroll state to the scroll indicator
    ScrollIndicator(state = state)
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a scroll state
    val state = rememberLazyListState()
    LazyRow(
        modifier = Modifier.fillMaxSize(),
        // 2. apply the scroll state to the LazyRow
        state = state,
    ) {
        items(count = 100) {
            // add your content here
            Text("item $it")
            Divider(orientation = Orientation.Vertical)
        }
    }
    // 3. apply the scroll state to the scroll indicator
    ScrollIndicator(state = state)
} 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  BoxScope . ScrollIndicator ( state :  LazyGridState ,  modifier :  Modifier  =  Modifier ,  alignment :  Alignment  =  if (state.layoutInfo.orientation == Orientation.Vertical) Alignment.CenterEnd
        else Alignment.BottomCenter ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.defaultHotAreaPadding(
            orientation = state.layoutInfo.orientation,
            alignment = alignment,
        ) ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  minVisibleSize :  Dp  =  ScrollIndicatorDefaults.MinSize ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  dismissAfter :  Long  =  3000 ) 
Scroll indicator is used to indicate scrolling progress of a grid view, just like  LazyHorizontalGrid  or  LazyVerticalGrid . You can also drag the indicator to scroll the content of grid view. 
Scrolling indicator is only visible when the list view is scrolling or user drag the indicator. The indicator will be hidden after  dismissAfter  seconds if the list view is not scrolling or user is not dragging the indicator. 
The best practice is to put the scrollable view and indicator in same  Box  to auto place the indicator. You can also use params  alignment  to control the position of the indicator. To place the indicator any where, you can wrap it with a  Box  and then place the  Box  anywhere 
#### Parameters
state 
The scroll state that applied to  LazyVerticalGrid  or  LazyHorizontalGrid . 
modifier 
Compose modifier applied to this indicator. 
alignment 
Alignment of the indicator in the parent  Box . 
padding For Interaction 
Add this padding value to make a larger interactive area. 
colors 
The colors of the indicator. 
min Visible Size 
The minimum size of the indicator. If the scrollable view size is smaller than the minimum size, the indicator will not be shown. You can set it to  Dp.Unspecified  to disable this feature. 
scrolling Mark Size 
The size of the scrolling mark. 
dismiss After 
The time to dismiss the indicator after the list view is not scrolling or user is not dragging the indicator. 
#### Samples
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a grid state
    val gridState = rememberLazyGridState()
    LazyVerticalGrid(
        columns = GridCells.Adaptive(200.dp),
        modifier = Modifier.fillMaxSize(),
        // 2. apply the state to the LazyVerticalGrid
        state = gridState,
    ) {
        items(GridItemCount) { idx ->
            Box(modifier = Modifier.fillMaxWidth().height(80.dp)) { Text(text = "Item $idx") }
        }
    }
    // 3. apply the state to the scroll indicator
    ScrollIndicator(state = gridState)
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a grid state
    val gridState = rememberLazyGridState()
    LazyHorizontalGrid(
        rows = GridCells.Fixed(3),
        modifier = Modifier.fillMaxSize(),
        // 2. apply the state to the LazyHorizontalGrid
        state = gridState,
    ) {
        items(GridItemCount) { idx ->
            Box(modifier = Modifier.fillMaxHeight().width(80.dp)) { Text(text = "Item $idx") }
        }
    }
    // 3. apply the state to the scroll indicator
    ScrollIndicator(state = gridState)
} 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  BoxScope . ScrollIndicator ( state :  LazyStaggeredGridState ,  modifier :  Modifier  =  Modifier ,  alignment :  Alignment  =  if (state.layoutInfo.orientation == Orientation.Vertical) Alignment.CenterEnd
        else Alignment.BottomCenter ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.defaultHotAreaPadding(
            orientation = state.layoutInfo.orientation,
            alignment = alignment,
        ) ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  minVisibleSize :  Dp  =  ScrollIndicatorDefaults.MinSize ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  dismissAfter :  Long  =  3000 ) 
Scroll indicator is used to indicate scrolling progress of a staggered grid view, just like  LazyHorizontalStaggeredGrid  or  LazyVerticalStaggeredGrid . You can also drag the indicator to scroll the content of grid view. 
Scrolling indicator is only visible when the list view is scrolling or user drag the indicator. The indicator will be hidden after  dismissAfter  seconds if the list view is not scrolling or user is not dragging the indicator. 
The best practice is to put the scrollable view and indicator in same  Box  to auto place the indicator. You can also use params  alignment  to control the position of the indicator. To place the indicator any where, you can wrap it with a  Box  and then place the  Box  anywhere 
#### Parameters
state 
The scroll state that applied to  LazyVerticalStaggeredGrid  or  LazyHorizontalStaggeredGrid . 
modifier 
Compose modifier applied to this indicator. 
alignment 
Alignment of the indicator in the parent  Box . 
padding For Interaction 
Add this padding value to make a larger interactive area. 
colors 
The colors of the indicator. 
min Visible Size 
The minimum size of the indicator. If the scrollable view size is smaller than the minimum size, the indicator will not be shown. You can set it to  Dp.Unspecified  to disable this feature. 
scrolling Mark Size 
The size of the scrolling mark. 
dismiss After 
The time to dismiss the indicator after the list view is not scrolling or user is not dragging the indicator. 
#### Samples
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a staggered grid state
    val sState = rememberLazyStaggeredGridState()
    LazyHorizontalStaggeredGrid(
        rows = StaggeredGridCells.Fixed(3),
        modifier = Modifier.fillMaxSize(),
        // 2. apply the state to the LazyHorizontalStaggeredGrid
        state = sState,
    ) {
        items(GridItemCount) { idx ->
            Box(modifier = Modifier.fillMaxHeight().width(80.dp)) { Text(text = "Item $idx") }
        }
    }
    // 3. apply the state to the scroll indicator
    ScrollIndicator(state = sState)
} 
   //sampleEnd
}
```
```
import androidx.compose.foundation.gestures.Orientation
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyHorizontalGrid
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.lazy.staggeredgrid.LazyHorizontalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.BasicScrollIndicator
import com.pico.spatial.ui.design.Divider
import com.pico.spatial.ui.design.ScrollIndicator
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.rememberScrollIndicatorState

fun main() { 
   //sampleStart 
   Box {
    // 1. define a grid state
    val sState = rememberLazyStaggeredGridState()
    LazyVerticalStaggeredGrid(
        columns = StaggeredGridCells.Adaptive(200.dp),
        modifier = Modifier.fillMaxSize(),
        // 2. apply the state to the LazyVerticalStaggeredGrid
        state = sState,
    ) {
        items(GridItemCount) { idx ->
            Box(modifier = Modifier.fillMaxWidth().height(50.dp)) { Text(text = "Item $idx") }
        }
    }
    // 3. apply the state to the scroll indicator
    ScrollIndicator(state = sState)
} 
   //sampleEnd
}
```