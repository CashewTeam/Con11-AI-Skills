# SideNavigation | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SideNavigation 
# SideNavigation
```kotlin
@Composable
```fun  SideNavigation ( modifier :  Modifier  =  Modifier ,  scrollState :  ScrollState  =  rememberScrollState() ,  contentPadding :  PaddingValues  =  SideNavigationDefaults.DefaultContentPadding ,  headerColor :  Color  =  SideNavigationDefaults.headerColor ,  header :  @ Composable BoxScope . ( )  ->  Unit ?  =  null ,  content :  @ Composable ColumnScope . ( )  ->  Unit ) 
A vertical navigation component typically used for primary navigation patterns. 
#### Parameters
modifier 
Modifier to be applied to the root Column layout 
scroll State 
Controls the scroll state of the navigation content 
content Padding 
Padding values for the entire navigation component 
header Color 
The color of the header content. 
header 
Optional header content displayed at the top of the navigation 
content 
the content of this side navigation, typically several  SideNavigationItem s or  SideNavigationSection s 
#### Samples
```
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.LocalContentColor
import com.pico.spatial.ui.design.PicoTheme
import com.pico.spatial.ui.design.SearchField
import com.pico.spatial.ui.design.SearchFieldDefaults
import com.pico.spatial.ui.design.SideNavigation
import com.pico.spatial.ui.design.SideNavigationItem
import com.pico.spatial.ui.design.SideNavigationSection
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   val pins = listOf("Recents", "Favorites", "Apps", "Docs")

val tags =
    listOf(
        Color.Red to "Red",
        Color.Green to "Green",
        Color.Blue to "Blue",
        Color.Yellow to "Yellow",
        Color.Cyan to "Cyan",
        Color.Magenta to "Magenta",
        Color.White to "White",
    )

val currentSelectedText = remember { mutableStateOf("") }

SideNavigation(
    modifier = Modifier.fillMaxHeight(),
    header = {
        Column {
            Box(modifier = Modifier.padding(start = 8.dp, top = 26.dp, bottom = 26.dp)) {
                Text("Settings", style = PicoTheme.typography.titleLarge, maxLines = 1)
            }
            Box(modifier = Modifier.padding(bottom = 24.dp)) { SimpleSearch() }
        }
    },
) {
    pins.forEach {
        SideNavigationItem(
            selected = currentSelectedText.value == it,
            modifier = Modifier.clickable { currentSelectedText.value = it },
            leading = { AnyIcon(iconSize = 20.dp) },
        ) {
            Text(it, maxLines = 1)
        }
    }

    SideNavigationSection(title = { Text("Tags") }) {
        tags.forEach {
            SideNavigationItem(
                selected = currentSelectedText.value == it.second,
                modifier = Modifier.clickable { currentSelectedText.value = it.second },
                leading = {
                    Box(
                        modifier =
                            Modifier.padding(6.dp)
                                .size(20.dp)
                                .background(it.first, shape = CircleShape)
                                .padding(4.dp)
                    )
                },
            ) {
                Text(it.second, maxLines = 1)
            }
        }
    }
} 
   //sampleEnd
}
```