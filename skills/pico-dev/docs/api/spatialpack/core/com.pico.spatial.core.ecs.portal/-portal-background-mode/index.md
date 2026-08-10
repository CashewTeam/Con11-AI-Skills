# PortalBackgroundMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.portal / PortalBackgroundMode 
# PortalBackgroundMode
```kotlin
enum PortalBackgroundMode : Enum<PortalBackgroundMode>
```
Represents the background mode of the portal. 
- 
SOLID_COLOR : Solid color background mode. 
- 
PASSTHROUGH : Passthrough background mode (shows real world). 
- 
UNKNOWN : Reserved value for forward compatibility. 
Members Entries 
## Entries
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
SOLID_COLOR 
```kotlin
SOLID_COLOR
```
Solid color background mode. 
PASSTHROUGH 
```kotlin
PASSTHROUGH
```
Passthrough background mode. 
## Properties
entries 
```kotlin
val entries: EnumEntries<PortalBackgroundMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): PortalBackgroundMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<PortalBackgroundMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.