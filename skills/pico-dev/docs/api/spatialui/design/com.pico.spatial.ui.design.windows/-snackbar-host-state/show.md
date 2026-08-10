# show | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / SnackbarHostState / show 
# show
```kotlin
abstract suspend fun show(message: String, description: String = "", leadingIcon: @Composable () -> Unit? = null, action: String = "", duration: SnackbarDuration = SnackbarDuration.Default, enableBackgroundMaterial: Boolean = true, backgroundColor: Color? = null): SnackbarResult
```
Shows or queues a snack, will be shown at bottom of the  SnackbarHost 's window 
#### Return
The result of the snack action, which will be:     - SnackResult.Dismissed if snack dismissed by timeout or user cancel     - SnackResult.ActionPerformed if user clicked the action button     - SnackResult.Failure if called in a non-window container context or on other errors 
#### Parameters
message 
The message to be displayed in the snack. 
description 
The description to be displayed in the snack. Defaults to an empty string. 
leading Icon 
The leading icon to be displayed in the snack. Defaults to null. 
action 
The action to be performed when the snack is clicked. Defaults to an empty string. 
duration 
The duration for which the snack should be displayed. Defaults to  SnackbarDuration.Default . 
enable Background Material 
Whether to use the glass material background. Defaults to true. 
background Color 
The background color of the snack. Defaults to null. 
#### Samples
com.pico.spatial.ui.design.samples.SnackSample 
```kotlin
abstract suspend fun show(message: @Composable () -> Unit, description: @Composable () -> Unit? = null, leadingIcon: @Composable () -> Unit? = null, trailingActions: @Composable SnackbarAction.() -> Unit? = null, duration: SnackbarDuration = SnackbarDuration.Default, enableBackgroundMaterial: Boolean = true, backgroundColor: Color? = null): SnackbarResult
```
Displays a snack with the provided message, description, leading icon, trailing actions, and duration. 
#### Return
The result of the snack action, which will be:     - SnackResult.Dismissed if snack dismissed by timeout or user cancel     - SnackResult.ActionPerformed if user clicked the action button     - SnackResult.Failure if called in a non-window container context or on other errors 
#### Parameters
message 
The composable function that provides the message content of the snack. 
description 
The composable function that provides the description content of the snack. 
leading Icon 
The composable function that provides the leading icon content of the snack. 
trailing Actions 
The composable function that provides the trailing actions content of the snack. 
duration 
The duration for which the snack should be displayed. Defaults to  SnackbarDuration.Default . 
enable Background Material 
Whether to use the glass material background. Defaults to true. 
background Color 
The background color of the snack. Defaults to null. 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.tooling.preview.Preview
import com.pico.spatial.ui.design.Button
import com.pico.spatial.ui.design.Icon
import com.pico.spatial.ui.design.IconButton
import com.pico.spatial.ui.design.R
import com.pico.spatial.ui.design.Text
import com.pico.spatial.ui.design.windows.LocalSnackbarHostState
import com.pico.spatial.ui.design.windows.SnackbarHost
import com.pico.spatial.ui.design.windows.SnackbarResult
import kotlinx.coroutines.launch

fun main() { 
   //sampleStart 
   SnackbarHost {
    val state = LocalSnackbarHostState.current
    val coroutineScope = rememberCoroutineScope()
    Button(
        onClick = {
            coroutineScope.launch {
                state.show(
                    message = { Text("Hello") },
                    leadingIcon = {
                        Icon(
                            painter = painterResource(R.drawable.ic_sui_rating_star),
                            contentDescription = null,
                        )
                    },
                    trailingActions = {
                        Button(onClick = { this.performAction() }) { Text("OK") }
                        IconButton(onClick = { this.dismiss() }) {
                            Icon(
                                painter = painterResource(R.drawable.ic_sui_close),
                                contentDescription = null,
                            )
                        }
                    },
                )
            }
        }
    ) {
        Text("Show snack")
    }
} 
   //sampleEnd
}
```