# unaryMinus | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / unaryMinus 
# unaryMinus
```kotlin
operator fun unaryMinus(): Vector4
```
Overloads the unary minus operator ( - ). 
Returns a new  Vector4  instance where each component ( x ,  y ,  z , and  w ) of this vector is negated. This operation does not modify the original vector. 
For example, if  v  is  Vector4(1f, -2f, 3f, -4f) , then  -v  would result in  Vector4(-1f, 2f, -3f, 4f) . 
#### Return
A new  Vector4  with components  (-this.x, -this.y, -this.z, -this.w) .