# RequiredFullSpace | PICO Spatial SDK

foundation / com.pico.spatial.core.annotation / RequiredFullSpace 
# RequiredFullSpace
```kotlin
@Target(allowedTargets = [AnnotationTarget.CLASS, AnnotationTarget.FUNCTION])
```annotation class  RequiredFullSpace 
Indicates that the annotated class or function must be used within the "FullSpace" state. 
Using it outside the "FullSpace" state may result in errors or invalid data.