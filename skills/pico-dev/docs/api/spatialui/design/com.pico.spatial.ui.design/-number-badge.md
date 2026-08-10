# NumberBadge | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / NumberBadge 
# NumberBadge
```kotlin
@Composable
```fun  NumberBadge ( modifier :  Modifier  =  Modifier ,  number :  Int ,  threshold :  Int  =  BadgeDefaults.OverflowThreshold ,  overflow :  Overflow  =  Overflow.Plus ,  textStyle :  TextStyle  =  BadgeDefaults.NumberTextStyle ,  badgeSize :  BadgeSize  =  BadgeDefaults.NumberSmall ,  badgeColor :  BadgeColors  =  BadgeDefaults.numberBadgeColors() ,  contentPadding :  PaddingValues  =  badgeSize.badgePadding() ) 
A  Badge  that is used to show numbers 
#### Parameters
modifier 
The  Modifier  used for badge. 
number 
the number shown inside the badge. 
threshold 
A  overflow  appearance will be shown when number is larger than  threshold 
overflow 
which overflow appearance should be shown. 
text Style 
the  TextStyle  of the number text. 
badge Size 
a  BadgeSize , each built-in  BadgeSize  has a corresponding  contentPadding . caller's Modifier.size will override this. 
badge Color 
the colors for the badge. 
content Padding 
the inner paddings of this component. 
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
    NumberBadgeColumn(1)
    NumberBadgeColumn(10)
    NumberBadgeColumn(99)
    NumberBadgeColumn(100, Overflow.Ellipsis)
    NumberBadgeColumn(1000, Overflow.Plus)
} 
   //sampleEnd
}
```