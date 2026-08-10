# ExperimentalFoundationApi | PICO Spatial SDK

foundation / com.pico.spatial.foundation.annotation / ExperimentalFoundationApi 
# ExperimentalFoundationApi
```kotlin
@Target(allowedTargets = [AnnotationTarget.CLASS, AnnotationTarget.ANNOTATION_CLASS, AnnotationTarget.FUNCTION, AnnotationTarget.PROPERTY, AnnotationTarget.PROPERTY_GETTER, AnnotationTarget.PROPERTY_SETTER, AnnotationTarget.CONSTRUCTOR, AnnotationTarget.FIELD, AnnotationTarget.VALUE_PARAMETER])
```annotation class  ExperimentalFoundationApi 
Indicates that a public API of the annotated element (class, method or field) is not in stable state yet. 
An experimental API may be renamed, changed or even removed in a future version. This annotation refers to API status only, it doesn't mean that the implementation has an 'experimental' quality. 
Note: Applications that use APIs marked with this annotation might be blocked from being published to the market.