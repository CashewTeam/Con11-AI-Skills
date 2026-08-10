# BasicScrollIndicator | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / BasicScrollIndicator 
# BasicScrollIndicator
```kotlin
@Composable
```fun  BasicScrollIndicator ( state :  ScrollIndicatorState ,  modifier :  Modifier  =  Modifier ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.ZeroPadding ,  contentPadding :  PaddingValues  =  ScrollIndicatorDefaults.TrackPadding ) 
Basic implementation of scroll indicator. Different to  ScrollIndicator  with  BoxScope , this implementation can be placed anywhere in the tree. And it's always visible. 
#### Parameters
state 
The state of the indicator. Use  rememberScrollIndicatorState  to create it. 
modifier 
Compose modifier applied to this indicator. 
colors 
The colors of the indicator. 
scrolling Mark Size 
The size of the scrolling mark. 
padding For Interaction 
Extra hot interaction space. 
content Padding 
The padding of the track. 
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
   Row {
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
    // 3. add scroll indicator
    val scrollIndicatorState = rememberScrollIndicatorState(Orientation.Vertical, state)
    BasicScrollIndicator(scrollIndicatorState)
} 
   //sampleEnd
}
```