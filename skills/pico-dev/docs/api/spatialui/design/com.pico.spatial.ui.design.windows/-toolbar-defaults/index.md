# ToolbarDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / ToolbarDefaults 
# ToolbarDefaults
```kotlin
object ToolbarDefaults
```
The default values of  Toolbar . 
Members 
## Functions
content Configuration 
```kotlin
fun contentConfiguration(enableMaterial: Boolean = true, backgroundColor: Color = Color.Transparent, cornerSize: Dp = CornerRadius, contentPadding: PaddingValues = SegmentContentPadding, itemGap: Dp = ItemGap, minWidth: Dp = SegmentMinWidth): ToolbarSegmentConfiguration
```
Create a configuration for the content segment of the toolbar. 
supporting Configuration 
```kotlin
fun supportingConfiguration(enableMaterial: Boolean = true, backgroundColor: Color = Color.Transparent, cornerSize: Dp = CornerRadius, contentPadding: PaddingValues = SegmentContentPadding, itemGap: Dp = ItemGap, minWidth: Dp = SegmentMinWidth): ToolbarSegmentConfiguration
```
Create a configuration for the supporting segment of the toolbar.