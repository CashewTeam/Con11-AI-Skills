# unaryMinus | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / unaryMinus 
# unaryMinus
```kotlin
operator fun unaryMinus(): Vector3
```
Overloads the unary minus operator ( - ). 
Returns a new  Vector3  instance where each component ( x ,  y , and  z ) of this vector is negated. This operation does not modify the original vector. 
For example, if  v  is  Vector3(1f, -2f, 3f) , then  -v  would result in  Vector3(-1f, 2f, -3f) . 
#### Return
A new  Vector3  with components  (-x, -y, -z) .