# copy | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / copy 
# copy
```kotlin
fun copy(src: Tensor, dst: Tensor)
```
Copy from one pipeline tensor to another. The two pipeline tensors, respectively denoted as  src  and  dst , must have the same number of values. 
For example, the  src  can be an RGB-color-array tensor of size 10, which means it has 10 * 3 = 30 values, where a multi-dimensional tensor with dimensions = 2x5x3 will be a valid candidate for  dst , as it has 2 * 5 * 3 = 30 values. However, a scalar array tensor of size 10 will be an invalid choice of  dst . 
The copy operation will handle the type conversion automatically, with 1.0 scaling and 0.0 offsetting. 
#### Parameters
src 
the source of this copying operation. The tensor must not be declared as of scene-graph usage. 
dst 
the destination of this copying operation. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun copy(src: PipelineTensorSlice, dst: Tensor)
```
Copy from one slice of a pipeline tensor to another. The slice of the copy source must contain the same number of values as the total number of values in the copy destination. 
The copy operation will handle the type conversion automatically, with 1.0 scaling and 0.0 offsetting. 
#### Parameters
src 
the source of this copying operation. 
dst 
the destination of this copying operation. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun copy(src: Tensor, dst: PipelineTensorSlice)
```
Copy from one pipeline tensor to a slice of another tensor. The slice of the copy source must contain the same number of values as the total number of values in the copy destination. 
The copy operation will handle the type conversion automatically, with 1.0 scaling and 0.0 offsetting. 
#### Parameters
src 
the source of this copying operation. 
dst 
the destination of this copying operation. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior. 
```kotlin
fun copy(src: PipelineTensorSlice, dst: PipelineTensorSlice)
```
Copy from a slice of one pipeline tensor to a slice of another tensor. The slice of the copy source must contain the same number of values as the total number of values in the copy destination. 
The copy operation will handle the type conversion automatically, with 1.0 scaling and 0.0 offsetting. 
#### Parameters
src 
the source of this copying operation. 
dst 
the destination of this copying operation. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.