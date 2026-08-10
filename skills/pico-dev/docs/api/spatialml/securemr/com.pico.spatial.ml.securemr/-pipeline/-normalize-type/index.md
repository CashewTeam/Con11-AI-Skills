# NormalizeType | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / NormalizeType 
# NormalizeType
```kotlin
enum NormalizeType : Enum<Pipeline.NormalizeType>
```
Normalization type for  normalize . 
Members Entries 
## Entries
L1 
```kotlin
L1
```
L1 normalization, the L1 norm of the normalized tensor will be equal to the alpha parameter. 
L2 
```kotlin
L2
```
L2 normalization, the L2 norm of the normalized tensor will be equal to the alpha parameter. 
INF 
```kotlin
INF
```
Infinite normalization, the infinite norm of the normalized tensor will be equal to the alpha parameter. 
MINMAX 
```kotlin
MINMAX
```
Min-Max normalization, the normalized tensor's minimum absolute value will be equal to the alpha parameter, whereas the maximum absolute value will be equal to the beta parameter. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Pipeline.NormalizeType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Pipeline.NormalizeType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Pipeline.NormalizeType>
```
Returns an array containing the constants of this enum type, in the order they're declared.