# Alignment | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AttachmentPanelComponent / Alignment 
# Alignment
```kotlin
enum Alignment : Enum<AttachmentPanelComponent.Alignment>
```
Anchor point of the panel in normalized coordinates. 
The  x  and  y  values are in the range 0, 1, where  (0,0)  is top-left and  (1,1)  is bottom-right.  UNSPECIFIED  indicates the center will align to the entity by default. 
Members Entries 
## Entries
UNSPECIFIED 
```kotlin
UNSPECIFIED
```
The unspecified alignment point of the AttachmentPanelComponent. 
TOP_LEFT 
```kotlin
TOP_LEFT
```
The top-left corner of the AttachmentPanelComponent. 
TOP_CENTER 
```kotlin
TOP_CENTER
```
The top-center point of the AttachmentPanelComponent. 
TOP_RIGHT 
```kotlin
TOP_RIGHT
```
The top-right corner of the AttachmentPanelComponent. 
CENTER_LEFT 
```kotlin
CENTER_LEFT
```
The left-center point of the AttachmentPanelComponent. 
CENTER 
```kotlin
CENTER
```
The center point of the AttachmentPanelComponent. 
CENTER_RIGHT 
```kotlin
CENTER_RIGHT
```
The right-center point of the AttachmentPanelComponent. 
BOTTOM_LEFT 
```kotlin
BOTTOM_LEFT
```
The bottom-left corner of the AttachmentPanelComponent. 
BOTTOM_CENTER 
```kotlin
BOTTOM_CENTER
```
The bottom-center point of the AttachmentPanelComponent. 
BOTTOM_RIGHT 
```kotlin
BOTTOM_RIGHT
```
The bottom-right corner of the AttachmentPanelComponent. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AttachmentPanelComponent.Alignment>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AttachmentPanelComponent.Alignment
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AttachmentPanelComponent.Alignment>
```
Returns an array containing the constants of this enum type, in the order they're declared.