# TabBar | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / TabBar 
# TabBar
```kotlin
@Composable
```fun  TabBar ( followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  focusable :  Boolean  =  true ,  extraContentHeight :  Dp  =  TabBarDefaults.ExpandedContentHeight ,  content :  TabBarScope . ( )  ->  Unit ) 
TabBar is floating window will be placed at center Top of WindowContainer It is used to navigate between different views or pages for WindowContainer. It supports different item content by  TabBarScope . In  TabBarScope , you can define the item main content by MainContent which can be any image, text, or any other content. and the item label by SupportContent which is optional, badge used to show the unread count and some other information to alert the user. 
#### Parameters
follow Viewpoints 
The view points to follow. 
focusable 
Whether the tab bar is focusable. When a  TabBar  is not focusable, it can not receive input events, such as text input and accessibility events. 
extra Content Height 
The height of the expanded content area below the main tab row. 
content 
TabBar content, detail in  TabBarScope . 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.NumberBadge
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.TabBar
import com.pico.spatial.ui.platform.ViewPoint

fun main() { 
   //sampleStart 
   val items by remember {
    mutableStateOf(
        listOf(
            ItemInfo("Home", R.drawable.ic_sample_listitem_leading, unreadCount = 99),
            ItemInfo("Favourite", R.drawable.ic_sample_listitem_leading, unreadCount = 0),
            ItemInfo("Settings", R.drawable.ic_sample_listitem_leading, unreadCount = 120),
            ItemInfo("Mine", R.drawable.ic_sample_listitem_leading, unreadCount = 9),
            ItemInfo("More", R.drawable.ic_sample_listitem_leading, unreadCount = -10),
        )
    )
}
var currentIndex by remember { mutableIntStateOf(0) }
TabBar(followViewpoints = setOf(ViewPoint.Front, ViewPoint.Left)) {
    items.forEachIndexed { index, item ->
        item(
            selected = currentIndex == index,
            mainContent = {
                Icon(painter = painterResource(item.iconResId), contentDescription = null)
            },
            supportContent = { Text(item.title) },
            onClick = { currentIndex = index },
            modifier = Modifier,
            badge = { NumberBadge(number = item.unreadCount) },
        )
    }
} 
   //sampleEnd
}
```