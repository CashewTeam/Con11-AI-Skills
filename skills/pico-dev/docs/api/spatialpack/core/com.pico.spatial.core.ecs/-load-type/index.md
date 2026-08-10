# LoadType | PICO Spatial SDK

core / com.pico.spatial.core.ecs / LoadType 
# LoadType
```kotlin
enum LoadType : Enum<LoadType>
```
Enum representing different ways of loading data. 
Members Entries 
## Entries
FROM_ASSETS 
```kotlin
FROM_ASSETS
```
Loads a resource from the asset directory, specified by a URI using the asset:// scheme. 
FROM_STORAGE 
```kotlin
FROM_STORAGE
```
Loads a resource from device storage, specified by its absolute file path. 
## Properties
entries 
```kotlin
val entries: EnumEntries<LoadType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): LoadType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<LoadType>
```
Returns an array containing the constants of this enum type, in the order they're declared.