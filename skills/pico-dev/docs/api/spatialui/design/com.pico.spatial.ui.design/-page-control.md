# PageControl | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / PageControl 
# PageControl
```kotlin
@Composable
```fun  PageControl ( currentIndex :  Int ,  onClickAction :  ( Int )  ->  Unit ,  @ IntRange ( from  =  0 ) totalDots :  Int ,  modifier :  Modifier  =  Modifier ,  colors :  PageControlColors  =  PageControlDefaults.pageControlColors() ,  selectIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  maxDisplayCount :  Int  =  PageControlDefaults.NormalMax ,  pageControlSpec :  PageControlSpec  =  PageControlDefaults.Spec ) 
PageControl used to create a page indicator. 
#### Parameters
current Index 
The index of the page currently indicated by the page indicator. 
on Click Action 
A callback function triggered when the user clicks on a dot in the page indicator. The parameter is the index of the page corresponding to the clicked dot. 
total Dots 
The number of dots displayed in the page indicator, representing the total number of pages. This value must be greater than or equal to 0. 
modifier 
A modifier used to customize the layout of the page indicator. The default value is an empty modifier. 
colors 
The color configuration used by the page indicator. By default, it uses the colors provided by  PageControlDefaults.pageControlColors . 
select Icon 
A custom icon component used to replace the currently selected dot. The default value is null, indicating that the default highlighting effect is used. 
enabled 
Controls the enabled state of the page indicator. When set to  false , click events are disabled, and the component appears disabled in accessibility services. 
max Display Count 
The maximum number of pages that can be displayed at once in the page indicator. The default value is  PageControlDefaults.NormalMax . 
page Control Spec 
The specification configuration for the page indicator, including the radius of the dots, the spacing between dots, and the vertical padding. By default, it uses  PageControlDefaults.Spec . 
#### Samples
```
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.PageControl
import com.pico.spatial.ui.design.PageControlDefaults
import com.pico.spatial.ui.design.ProgressPageControl
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   PageControl(
    currentIndex = 1,
    onClickAction = {},
    modifier = Modifier.background(BackGroundColor),
    totalDots = 5,
    colors = PageControlDefaults.pageControlColors(),
    enabled = true,
    maxDisplayCount = PageControlDefaults.NormalMax,
    pageControlSpec = PageControlDefaults.Spec,
) 
   //sampleEnd
}
```