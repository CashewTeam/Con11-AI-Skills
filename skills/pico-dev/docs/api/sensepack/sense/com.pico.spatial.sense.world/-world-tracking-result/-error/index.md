# Error | PICO Spatial SDK

sense / com.pico.spatial.sense.world / WorldTrackingResult / Error 
# Error
```kotlin
class Error : WorldTrackingResult<Nothing>
```
Represents an error for an operation. 
Contains an error code and an error message to provide details about the failure. 
Error codes: 
- 
0 : The operation is successful. 
- 
-1 : The operation failed. 
- 
-2 : A runtime error occurred. 
- 
-3 : Validation failed. 
- 
-4 : The maximum number of anchors has been reached. 
- 
-5 : Permission validation failed for this operation. 
- 
-6 : The provider is not ready. 
- 
-7 : The specified anchor was not found. 
- 
-8 : Load requests are too frequent. 
Members 
## Properties
error Code 
```kotlin
val errorCode: Int
```
An integer code representing the type of error. 
error Message 
```kotlin
val errorMessage: String
```
A string message that provides detailed information about the error.