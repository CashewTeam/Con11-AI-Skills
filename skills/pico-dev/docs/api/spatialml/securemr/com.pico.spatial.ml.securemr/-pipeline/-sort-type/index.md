# SortType | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / SortType 
# SortType
```kotlin
enum SortType : Enum<Pipeline.SortType>
```
Enum to determine how a matrix will be sorted. 
Members Entries 
## Entries
BY_COLUMN 
```kotlin
BY_COLUMN
```
Sort the matrix column-by-column, i.e., each column of the matrix will be treated as a column vector, and applied vector sorting individually. 
BY_ROW 
```kotlin
BY_ROW
```
Sort the matrix row-by-row, i.e., each row of the matrix will be treated as a row vector, and applied vector sorting individually. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Pipeline.SortType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Pipeline.SortType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Pipeline.SortType>
```
Returns an array containing the constants of this enum type, in the order they're declared.