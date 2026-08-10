# content | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / content 
# content
```kotlin
fun AttachmentPanelComponent.content(compositionContext: CompositionContext? = null, content: @Composable () -> Unit): AttachmentPanelComponent
```
Sets the content of the AttachmentPanelComponent. 
#### Return
The  AttachmentPanelComponent  instance. 
#### Parameters
composition Context 
The parent composition context. Default value is null. Note that if you need  androidx.compose.runtime.CompositionLocal s that provide by parent composition, please pass the parent composition context to this function. 
content 
The content of the AttachmentPanelComponent.