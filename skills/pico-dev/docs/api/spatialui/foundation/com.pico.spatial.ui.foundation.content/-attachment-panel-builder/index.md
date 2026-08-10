# AttachmentPanelBuilder | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / AttachmentPanelBuilder 
# AttachmentPanelBuilder
```kotlin
interface AttachmentPanelBuilder
```
A builder for spatial UI attachments 
Members 
## Functions
Attachment Panel 
```kotlin
abstract fun AttachmentPanel(id: Any, size: IntSize? = null, alignment: AttachmentPanelComponent.Alignment = AttachmentPanelComponent.Alignment.UNSPECIFIED, content: @Composable () -> Unit)
```
Add attachment by invoking this function 
clear All Attachments 
```kotlin
abstract fun clearAllAttachments()
```
Clears all attachments