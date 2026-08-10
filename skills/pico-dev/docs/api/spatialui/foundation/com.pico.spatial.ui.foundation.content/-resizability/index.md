# Resizability | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / Resizability 
# Resizability
```kotlin
enum Resizability : Enum<Resizability>
```
The resizability of a 3D model. 
Members Entries 
## Entries
None 
```kotlin
None
```
The model is not resizable. 
FitInside 
```kotlin
FitInside
```
The model is scaled to fit inside of  SpatialModelView . 
FitOutside 
```kotlin
FitOutside
```
The model is scaled to fit outside of  SpatialModelView . 
FillBounds 
```kotlin
FillBounds
```
The model is stretch to fill the  SpatialModelView . 
## Properties
entries 
```kotlin
val entries: EnumEntries<Resizability>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Resizability
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Resizability>
```
Returns an array containing the constants of this enum type, in the order they're declared.