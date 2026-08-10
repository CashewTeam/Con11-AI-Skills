# ContainerResizeRestriction | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.resize / ContainerResizeRestriction 
# ContainerResizeRestriction
```kotlin
enum ContainerResizeRestriction : Enum<ContainerResizeRestriction>
```
Declares the resize restriction for  com.pico.spatial.core.container.WindowContainer 
Members Entries 
## Entries
NonUniformResizable 
```kotlin
NonUniformResizable
```
Independent width/height resizing without aspect ratio constraints 
UniformResizable 
```kotlin
UniformResizable
```
Maintains aspect ratio during resizing 
## Properties
entries 
```kotlin
val entries: EnumEntries<ContainerResizeRestriction>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): ContainerResizeRestriction
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<ContainerResizeRestriction>
```
Returns an array containing the constants of this enum type, in the order they're declared.