# observeCurrentVibrantEffect | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.vibrant / observeCurrentVibrantEffect 
# observeCurrentVibrantEffect
```kotlin
fun Modifier.observeCurrentVibrantEffect(observer: (vibrant: Vibrant?) -> Unit): Modifier
```
A utility function that helps you to observe the current vibrant effect. 
#### Return
Modifier. 
#### Parameters
observer 
The observer function. 
#### Samples
```
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.pico.spatial.ui.foundation.vibrant.Vibrant
import com.pico.spatial.ui.foundation.vibrant.observeCurrentVibrantEffect
import com.pico.spatial.ui.foundation.vibrant.vibrantEffect
import com.pico.spatial.ui.foundation.vibrant.withVibrant
import com.pico.spatial.ui.graphics.Vibrant

fun main() { 
   //sampleStart 
   Column(
    modifier =
        Modifier.size(200.dp)
            // 1. Set a Vibrant Dark effect
            .vibrantEffect(Vibrant.Dark)
) {
    Box(modifier = Modifier.background(Color.Red)) {
        var currentVibrant by remember { mutableStateOf<Vibrant?>(null) }
        Text(
            "current vibrant is: $currentVibrant",
            color = Color.Yellow,
            modifier =
                Modifier
                    // 2. Observer vibrant here
                    .observeCurrentVibrantEffect { currentVibrant = it },
        )
    }
} 
   //sampleEnd
}
```