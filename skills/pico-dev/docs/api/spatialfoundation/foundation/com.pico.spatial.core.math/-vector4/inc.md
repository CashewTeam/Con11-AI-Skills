# inc | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / inc 
# inc
```kotlin
operator fun inc(): Vector4
```
Overloads the unary increment operator ( ++ ). 
Returns a new  Vector4  instance where each component ( x ,  y ,  z , and  w ) of this vector has been incremented by  1.0f . This operation does not modify the original  Vector4  instance. 
When this operator is used on a  var  variable (e.g.,  v++ ), the variable  v  will be reassigned to the new, incremented  Vector4  instance. 
#### Return
A new  Vector4  with components  (this.x + 1f, this.y + 1f, this.z + 1f, this.w + 1f) .