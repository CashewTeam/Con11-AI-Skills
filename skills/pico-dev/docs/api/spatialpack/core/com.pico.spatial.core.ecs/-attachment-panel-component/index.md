# AttachmentPanelComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AttachmentPanelComponent 
# AttachmentPanelComponent
```kotlin
class AttachmentPanelComponent(width: Int = WRAP_CONTENT, height: Int = WRAP_CONTENT, alignment: AttachmentPanelComponent.Alignment = Alignment.UNSPECIFIED) : Component
```
Component that attaches a 2D Android  View  to an  Entity  in spatial space. 
#### Parameters
width 
The panel width. Defaults to  WRAP_CONTENT . 
height 
The panel height. Defaults to  WRAP_CONTENT . 
alignment 
The panel alignment relative to the entity. 
Members 
## Constructors
Attachment Panel Component 
```kotlin
constructor(width: Int = WRAP_CONTENT, height: Int = WRAP_CONTENT, alignment: AttachmentPanelComponent.Alignment = Alignment.UNSPECIFIED)
```
```kotlin
constructor(context: Context, width: Int = WRAP_CONTENT, height: Int = WRAP_CONTENT, alignment: AttachmentPanelComponent.Alignment = Alignment.UNSPECIFIED)
```
Component that attaches a 2D Android  View  to an  Entity  in spatial space. 
## Types
Alignment 
```kotlin
enum Alignment : Enum<AttachmentPanelComponent.Alignment>
```
Anchor point of the panel in normalized coordinates. 
Companion 
```kotlin
object Companion
```
Static values and utilities for  AttachmentPanelComponent . 
## Properties
content 
```kotlin
var content: View?
```
The 2D Android View content to be displayed on this panel. 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```