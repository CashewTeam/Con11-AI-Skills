# ModelInferenceType | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / ModelInferenceType 
# ModelInferenceType
```kotlin
enum ModelInferenceType : Enum<Pipeline.ModelInferenceType>
```
LiteRT / TensorFlow Lite model inference backend used to accelerate model inference. 
The  runModelInference modelBinary  parameter must contain a TensorFlow Lite FlatBuffer model for all inference types. 
Members Entries 
## Entries
LITE_RT_CPU 
```kotlin
LITE_RT_CPU
```
Running a TensorFlow Lite model by using the LiteRT / TFLite runtime on the CPU backend. 
LITE_RT_GPU 
```kotlin
LITE_RT_GPU
```
Running a TensorFlow Lite model by using the LiteRT / TFLite runtime on the GPU backend. 
LITE_RT_NPU 
```kotlin
LITE_RT_NPU
```
Running a TensorFlow Lite model by using the LiteRT / TFLite runtime on the NPU backend. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Pipeline.ModelInferenceType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Pipeline.ModelInferenceType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Pipeline.ModelInferenceType>
```
Returns an array containing the constants of this enum type, in the order they're declared.