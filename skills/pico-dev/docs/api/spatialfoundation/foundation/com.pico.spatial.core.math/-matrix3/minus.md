# minus | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / minus 
# minus
```kotlin
operator fun minus(other: Matrix3): Matrix3
```
Overloads the  -  operator to perform element-wise subtraction of another  Matrix3  from this matrix. 
Each component of the resulting matrix is the difference between the corresponding components of this matrix and the  other  matrix ( this_component - other_component ). 
#### Return
A new  Matrix3  representing the difference ( this  -  other ). 
#### Parameters
other 
The  Matrix3  to subtract from this matrix.