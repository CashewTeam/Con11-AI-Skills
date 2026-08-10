# Badge | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Badge 
# Badge
```kotlin
@Composable
```fun  Badge ( modifier :  Modifier  =  Modifier ,  badgeColor :  BadgeColors  =  BadgeDefaults.badgeColors() ,  badgeSize :  BadgeSize  =  BadgeDefaults.Small ,  radius :  Dp  =  badgeSize.badgeRadius() ,  contentPadding :  PaddingValues  =  badgeSize.badgePadding() ,  textStyle :  TextStyle  =  PicoTheme.typography.bodySmall ,  content :  @ Composable RowScope . ( )  ->  Unit ?  =  null ) 
Badge is a component that can contain dynamic information, such as the presence of a new notification or a number of pending requests. Badges can be icon only or contain short text. 
#### Parameters
modifier 
optional  Modifier  for this item. 
badge Color 
the colors for the badge. 
badge Size 
the size for the badge. 
radius 
badge's radius , used by  RoundedCornerShape . 
content Padding 
the inner paddings of this component. 
text Style 
the  TextStyle  of the number text. 
content 
optional content to be rendered inside the badge. 
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
   Row(horizontalArrangement = Arrangement.spacedBy(20.dp)) {
    BadgeColumn(
        extraSmallContent = { Text("58%") },
        smallContent = { Text("text") },
        regularContent = { Text("text") },
    )
    BadgeColumn(
        extraSmallContent = {
            BadgeIcon()
            Spacer(modifier = Modifier.width(3.dp))
            Text("58%")
        },
        smallContent = {
            BadgeIcon()
            Spacer(modifier = Modifier.width(5.dp))
            Text("text")
        },
        regularContent = {
            BadgeIcon()
            Spacer(modifier = Modifier.width(6.dp))
            Text("text")
        },
    )
    BadgeColumn(
        extraSmallContent = {
            Text("58%")
            Spacer(modifier = Modifier.width(3.dp))
            BadgeIcon()
        },
        smallContent = {
            Text("text")
            Spacer(modifier = Modifier.width(5.dp))
            BadgeIcon()
        },
        regularContent = {
            Text("text")
            Spacer(modifier = Modifier.width(6.dp))
            BadgeIcon()
        },
    )
    BadgeColumn(
        extraSmallContent = {
            BadgeIcon()
            Spacer(modifier = Modifier.width(3.dp))
            Text("58%")
            Spacer(modifier = Modifier.width(3.dp))
            BadgeIcon()
        },
        smallContent = {
            BadgeIcon()
            Spacer(modifier = Modifier.width(5.dp))
            Text("text")
            Spacer(modifier = Modifier.width(3.dp))
            BadgeIcon()
        },
        regularContent = {
            BadgeIcon()
            Spacer(modifier = Modifier.width(6.dp))
            Text("text")
            Spacer(modifier = Modifier.width(3.dp))
            BadgeIcon()
        },
    )
    BadgeColumn(
        extraSmallContent = { BadgeIcon() },
        smallContent = { BadgeIcon() },
        regularContent = { BadgeIcon() },
    )
} 
   //sampleEnd
}
```