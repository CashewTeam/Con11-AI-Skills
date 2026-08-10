# ToolbarSegmentConfiguration | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / ToolbarSegmentConfiguration 
# ToolbarSegmentConfiguration
```kotlin
@Immutable
```class  ToolbarSegmentConfiguration 
Configuration for a single toolbar segment. 
Members 
## Properties
background Color 
```kotlin
val backgroundColor: Color
```
The solid color overlay of the segment. 
content Padding 
```kotlin
val contentPadding: PaddingValues
```
The padding of the segment. 
corner Size 
```kotlin
val cornerSize: Dp
```
The corner radius of the segment. 
enable Material 
```kotlin
val enableMaterial: Boolean
```
Whether to render material background for the segment. 
item Gap 
```kotlin
val itemGap: Dp
```
The gap between items of the segment. 
min Width 
```kotlin
val minWidth: Dp
```
The minimum width of the segment. 
## Functions
copy 
```kotlin
fun copy(enableMaterial: Boolean = this.enableMaterial, backgroundColor: Color = this.backgroundColor, cornerSize: Dp = this.cornerSize, contentPadding: PaddingValues = this.contentPadding, itemGap: Dp = this.itemGap, minWidth: Dp = this.minWidth): ToolbarSegmentConfiguration
```
Copy the configuration with optional overrides.