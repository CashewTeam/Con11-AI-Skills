# AttachmentPanelComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AttachmentPanelComponent / AttachmentPanelComponent 
# AttachmentPanelComponent
```kotlin
constructor(width: Int = WRAP_CONTENT, height: Int = WRAP_CONTENT, alignment: AttachmentPanelComponent.Alignment = Alignment.UNSPECIFIED)
```
#### Parameters
width 
The panel width. Defaults to  WRAP_CONTENT . 
height 
The panel height. Defaults to  WRAP_CONTENT . 
alignment 
The panel alignment relative to the entity. 
```kotlin
constructor(context: Context, width: Int = WRAP_CONTENT, height: Int = WRAP_CONTENT, alignment: AttachmentPanelComponent.Alignment = Alignment.UNSPECIFIED)
```
Component that attaches a 2D Android  View  to an  Entity  in spatial space. 
#### Parameters
context 
The Android context. 
width 
The panel width. Defaults to  WRAP_CONTENT . 
height 
The panel height. Defaults to  WRAP_CONTENT . 
alignment 
The panel alignment relative to the entity.