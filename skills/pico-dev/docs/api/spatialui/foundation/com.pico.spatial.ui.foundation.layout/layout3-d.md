# layout3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / layout3D 
# layout3D
```kotlin
fun Modifier.layout3D(measure: MeasureScope.(Measurable, Constraints3D) -> MeasureResult): Modifier
```
This is a convenience API of creating a custom  LayoutModifierNode  modifier which implements 3D measurement, without having to create a class or an object that implements the  LayoutModifierNode  interface. 
#### Return
The  Modifier  with expected offset value. 
#### Samples
```
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.foundation.layout.layout3D

fun main() { 
   //sampleStart 
   Column {
    Box(
        modifier =
            Modifier.layout3D { measurable, constraint3d ->
                val place = measurable.measure(constraint3d)
                layout(place.width, place.height, place.depth) { place.place3D(0, 0, 0) }
            }
    ) {
        BasicText(text = "SpatialLayout3DSample", color = { Color.Yellow })
    }
} 
   //sampleEnd
}
```