# DotBadge | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DotBadge 
# DotBadge
```kotlin
@Composable
```fun  DotBadge ( modifier :  Modifier  =  Modifier ,  color :  Color  =  BadgeDefaults.DotColor ) 
Dot badge 
#### Parameters
modifier 
The  Modifier  used for badge. 
color 
Dot color. 
#### Samples
```
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.RowScope
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Badge
import com.pico.spatial.ui.design.BadgeDefaults
import com.pico.spatial.ui.design.DotBadge
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.NumberBadge
import com.pico.spatial.ui.design.Overflow
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   Row(
    horizontalArrangement = Arrangement.spacedBy(10.dp),
    verticalAlignment = Alignment.CenterVertically,
) {
    // Default appearance
    DotBadge()
    // With customized color
    DotBadge(color = Color(color = 0xFF00F99A))
    DotBadge(modifier = Modifier.size(20.dp), color = Color(color = 0xFF00F99A))
} 
   //sampleEnd
}
```