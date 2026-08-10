# ResourceErrorCode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ResourceLoadingException / ResourceErrorCode 
# ResourceErrorCode
```kotlin
enum ResourceErrorCode : Enum<ResourceLoadingException.ResourceErrorCode>
```
Enumeration for resource-related error codes. 
Members Entries 
## Entries
UNKNOWN_ERROR 
```kotlin
UNKNOWN_ERROR
```
Unknown error occurred. 
SUCCESS 
```kotlin
SUCCESS
```
No error occurred, the operation was successful. Not possible to be returned. 
NO_PERMISSION 
```kotlin
NO_PERMISSION
```
The operation was not permitted due to insufficient permissions. 
NO_ENTRY 
```kotlin
NO_ENTRY
```
The specified resource entry was not found. 
NO_MEMORY 
```kotlin
NO_MEMORY
```
There was not enough memory to complete the operation. 
INVALID_INSTANCE 
```kotlin
INVALID_INSTANCE
```
The instance is invalid. Usually the system service is unavailable. 
INVALID_ARGS 
```kotlin
INVALID_ARGS
```
The provided arguments are invalid or inappropriate for the operation. 
INVALID_OPERATION 
```kotlin
INVALID_OPERATION
```
The operation is invalid in the current context or state. 
INVALID_CONTENT 
```kotlin
INVALID_CONTENT
```
The content of the resource is invalid or corrupted. 
INVALID_OBJECT 
```kotlin
INVALID_OBJECT
```
The object is invalid, possibly null or corrupted. 
IS_DIR 
```kotlin
IS_DIR
```
The resource is a directory, but a non-directory was expected. 
NOT_DIR 
```kotlin
NOT_DIR
```
The resource is not a directory, but a directory was expected. 
FORMAT_UNSUPPORTED 
```kotlin
FORMAT_UNSUPPORTED
```
The resource format is not supported, or file extension is not correct. 
MANY_RESOURCES 
```kotlin
MANY_RESOURCES
```
There are too many resources allocated. 
BIG_RESOURCE 
```kotlin
BIG_RESOURCE
```
The resource is too large to be processed. 
READ_ONLY 
```kotlin
READ_ONLY
```
The resource is read-only and cannot be modified. 
VERSION_INCOMPATIBILITY 
```kotlin
VERSION_INCOMPATIBILITY
```
The resource version is incompatible with the current operation or system. 
TIMED_OUT 
```kotlin
TIMED_OUT
```
The operation timed out before completion. 
UNKNOWN_VERSION 
```kotlin
UNKNOWN_VERSION
```
The resource or bundle version is invalid. 
EXIST 
```kotlin
EXIST
```
The resource already exists. 
## Properties
entries 
```kotlin
val entries: EnumEntries<ResourceLoadingException.ResourceErrorCode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the error code. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): ResourceLoadingException.ResourceErrorCode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<ResourceLoadingException.ResourceErrorCode>
```
Returns an array containing the constants of this enum type, in the order they're declared.