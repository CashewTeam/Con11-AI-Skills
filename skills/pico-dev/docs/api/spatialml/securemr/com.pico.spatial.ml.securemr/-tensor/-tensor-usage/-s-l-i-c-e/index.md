# SLICE | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / TensorUsage / SLICE 
# SLICE
```kotlin
SLICE
```
A slice array, the data in the tensor will be interpreted as an array of 

```
template <typename T>struct { T begin; T end; T skip = 1;};
```
along all dimensions of the source tensor