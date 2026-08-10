# get | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / get 
# get
```kotlin
operator fun get(row: Int, col: Int): Float
```
Gets the item with the row and column index from the  Matrix4  instance. 
#### Return
The value of  Matrix4  instance in the specific row and column index. 
#### Parameters
row 
The row index of the  Matrix4  instance. 
col 
The column index of the  Matrix4  instance. 
#### Throws
Index Out Of Bounds Exception 
If the passed row index or column index is invalid.