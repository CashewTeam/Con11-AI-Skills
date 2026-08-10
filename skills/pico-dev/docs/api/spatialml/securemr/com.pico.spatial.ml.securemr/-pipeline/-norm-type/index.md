# NormType | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / NormType 
# NormType
```kotlin
enum NormType : Enum<Pipeline.NormType>
```
Norm type for  norm . 
Members Entries 
## Entries
L1 
```kotlin
L1
```
L1 norm, i.e., the Manhattan distance 
L2 
```kotlin
L2
```
L2 norm, i.e., the Euclidean distance 
INF 
```kotlin
INF
```
Infinite norm, i.e., the biggest absolute element 
## Properties
entries 
```kotlin
val entries: EnumEntries<Pipeline.NormType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Pipeline.NormType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Pipeline.NormType>
```
Returns an array containing the constants of this enum type, in the order they're declared.