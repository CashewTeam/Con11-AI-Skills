# ProvidePhysicalLengthConverter | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / ProvidePhysicalLengthConverter 
# ProvidePhysicalLengthConverter
```kotlin
@Composable
```fun  ProvidePhysicalLengthConverter ( scaledType :  ScaledType ,  content :  @ Composable ( )  ->  Unit ) 
ProvidePhysicalLengthConverter  binds values to  LocalPhysicalLengthConverter 's Reading the  LocalPhysicalLengthConverter  using  LocalPhysicalLengthConverter.current 
- 
will return the value provided for composable functions called directly or indirectly in the  content  lambda. 
  @param scaledType TNew ScaledType type.     @param content The composable content to be bound to the  LocalPhysicalLengthConverter .