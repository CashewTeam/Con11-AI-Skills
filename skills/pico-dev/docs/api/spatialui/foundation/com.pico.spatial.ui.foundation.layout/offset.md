# offset | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / offset 
# offset
```kotlin
@Stable
```fun  Modifier . offset ( z :  Dp ) :  Modifier 
Offset content by  z  dp 
If z offset can be changed, use  zOffset  to avoid recomposition 
#### Return
The  Modifier  with expected offset value. 
#### See also
graphics Layer 
#### Samples
```
import androidx.compose.animation.core.animateDpAsState
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.layout.offset
import com.pico.spatial.ui.foundation.layout.zOffset

fun main() { 
   //sampleStart 
   Box(modifier = Modifier.offset(z = 10.dp).size(100.dp).background(color = Color.Red)) {
    //
} 
   //sampleEnd
}
```