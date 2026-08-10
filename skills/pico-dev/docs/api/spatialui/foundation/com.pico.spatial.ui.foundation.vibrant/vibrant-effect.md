# vibrantEffect | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.vibrant / vibrantEffect 
# vibrantEffect
```kotlin
fun Modifier.vibrantEffect(vibrant: Vibrant): Modifier
```
A modifier that make current node and its subsequent node in vibrant render mode. 
- 
Vibrant effect is always inheritable. This means that when you add a  Modifier.vibrantEffect      to Modifier chain, all of its subsequent node will be rendered in vibrant mode, including its     child views. 
- 
While in vibrant mode, you should manually call  Modifier.vibrantEffect(Vibrant.None)  to     terminate vibrant effect if you want to display child views in normal mode. Terminate effect     means that current node and its subsequent node and child views will be rendered in normal     android mode. 
- 
You can use  Modifier.observeCurrentVibrantEffect  to observe the current vibrant effect. 
#### Return
Modifier. 
#### Parameters
vibrant 
The vibrant type. 
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
   Column {
    // sample 1: Background is vibrant dark, and text is vibrant light.
    Box(
        modifier =
            Modifier.size(200.dp)
                // 1. Set a Vibrant Dark effect
                .vibrantEffect(Vibrant.Dark)
                // 2. use Color.Vibrant to make pure vibrant effect
                .background(Color.Vibrant)
    ) {
        Text(
            "Hello",
            // Color.Vibrant is a special placeholder color
            color = Color.Vibrant,
            modifier = Modifier.vibrantEffect(Vibrant.Light),
        )
    }
    // sample 2: mixing vibrant effect.
    // background mix Color.Red with Vibrant.Dark, and text mix Color.Blue with Vibrant.Light.
    Box(
        modifier =
            Modifier.size(200.dp)
                // 1. Set a Vibrant Dark effect
                .vibrantEffect(Vibrant.Dark)
                // 2. Use normal color, such as Color.Red, to mix with Vibrant effect.
                .background(Color.Red)
    ) {
        Text("Hello", color = Color.Blue, modifier = Modifier.vibrantEffect(Vibrant.Light))
    }
    // sample 3: Background is vibrant, and text is yellow.
    Box(
        modifier =
            Modifier.size(200.dp)
                // 1. Set a Vibrant Dark effect
                .vibrantEffect(Vibrant.Dark)
                // 2. use Color.Vibrant to make pure vibrant effect
                .background(Color.Vibrant)
                // 3. Terminate the effect.
                // So the following modifier and child views will be rendered in normal mode.
                .vibrantEffect(Vibrant.None)
    ) {
        // because vibrant effect is terminated, so text is in yellow color.
        Text("Hello", color = Color.Yellow)
    }
} 
   //sampleEnd
}
```