# dec | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / dec 
# dec
```kotlin
operator fun dec(): Matrix3
```
Overloads the unary decrement operator ( -- ). 
Returns a new  Matrix3  instance where each component of this matrix has been decremented by  1.0f . This operation does not modify the original  Matrix3  instance. 
When this operator is used on a  var  variable (e.g.,  matrix-- ), the variable  matrix  will be reassigned to the new, decremented  Matrix3  instance. 
#### Return
A new  Matrix3  where each element is  this_element - 1.0f .