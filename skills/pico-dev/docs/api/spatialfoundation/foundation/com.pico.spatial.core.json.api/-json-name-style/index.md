# JsonNameStyle | PICO Spatial SDK

foundation / com.pico.spatial.core.json.api / JsonNameStyle 
# JsonNameStyle
```kotlin
enum JsonNameStyle : Enum<JsonNameStyle>
```
Json field name style. 
Members Entries 
## Entries
HUMP 
```kotlin
HUMP
```
HUMP (camelCase) style. Example: "fieldName" -> "fieldName". The first word is lowercase, and each subsequent word starts with an uppercase letter. 
UNDERLINE 
```kotlin
UNDERLINE
```
UNDERLINE (snake_case) style. Example: "field_name" -> "field_name". All words are lowercase, separated by underscores. 
## Properties
entries 
```kotlin
val entries: EnumEntries<JsonNameStyle>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): JsonNameStyle
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<JsonNameStyle>
```
Returns an array containing the constants of this enum type, in the order they're declared.