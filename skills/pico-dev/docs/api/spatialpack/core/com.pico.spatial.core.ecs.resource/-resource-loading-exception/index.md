# ResourceLoadingException | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ResourceLoadingException 
# ResourceLoadingException
```kotlin
class ResourceLoadingException(errorCode: Int, message: String) : Exception
```
Exception thrown when an error occurs during resource or entity loading. 
Members 
## Constructors
Resource Loading Exception 
```kotlin
constructor(errorCode: Int, message: String)
```
## Types
Resource Error Code 
```kotlin
enum ResourceErrorCode : Enum<ResourceLoadingException.ResourceErrorCode>
```
Enumeration for resource-related error codes. 
## Properties
error Code 
```kotlin
val errorCode: ResourceLoadingException.ResourceErrorCode
```
Error code of the exception. See  ResourceErrorCode  for more information.