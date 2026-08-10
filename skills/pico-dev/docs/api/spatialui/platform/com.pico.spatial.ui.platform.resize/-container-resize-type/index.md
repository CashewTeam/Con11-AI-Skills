# ContainerResizeType | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.resize / ContainerResizeType 
# ContainerResizeType
```kotlin
enum ContainerResizeType : Enum<ContainerResizeType>
```
ContainerResizeType is used to declare the resize type of  com.pico.spatial.core.container.WindowContainer , it contains three types: 
- 
Automatic : the default resize type of  com.pico.spatial.core.container.WindowContainer  which behavior is decided by System. 
- 
ContentMinSize : declare the  com.pico.spatial.core.container.WindowContainer  size no smaller than content's minimum size, can customize the minimum size of the window by calling the method Modifier.windowConstraints on the root node 
- 
ContentSize : declare the  com.pico.spatial.core.container.WindowContainer  size within content's minimum and maximum size, can customize the minimum and maximum size of the window by calling the method Modifier.windowConstraints on the root node 
Members Entries 
## Entries
Automatic 
```kotlin
Automatic
```
the default resize type of  com.pico.spatial.core.container.WindowContainer  which behavior is decided by System. 
ContentMinSize 
```kotlin
ContentMinSize
```
declare the  com.pico.spatial.core.container.WindowContainer  size no smaller than content's minimum size, can customize the minimum size of the window by calling the method Modifier.windowConstraints on the root node 
ContentSize 
```kotlin
ContentSize
```
declare the  com.pico.spatial.core.container.WindowContainer  size within content's minimum and maximum size, can customize the minimum and maximum size of the window by calling the method Modifier.windowConstraints on the root node 
## Properties
entries 
```kotlin
val entries: EnumEntries<ContainerResizeType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
convert To Pack Type 
```kotlin
fun convertToPackType(): ContainerResizeType
```
Convert  ContainerResizeType  to  com.pico.spatial.core.container.ContainerResizeType 
value Of 
```kotlin
fun valueOf(value: String): ContainerResizeType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<ContainerResizeType>
```
Returns an array containing the constants of this enum type, in the order they're declared.