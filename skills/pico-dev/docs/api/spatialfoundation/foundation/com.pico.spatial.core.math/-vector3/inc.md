# inc | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / inc 
# inc
```kotlin
operator fun inc(): Vector3
```
Overloads the unary increment operator ( ++ ). 
Returns a new  Vector3  instance where each component ( x ,  y , and  z ) of this vector has been incremented by  1.0f . This operation does not modify the original  Vector3  instance. 
When this operator is used on a  var  variable (e.g.,  v++ ), the variable  v  will be reassigned to the new, incremented  Vector3  instance. 
#### Return
A new  Vector3  with components  (this.x + 1f, this.y + 1f, this.z + 1f) .