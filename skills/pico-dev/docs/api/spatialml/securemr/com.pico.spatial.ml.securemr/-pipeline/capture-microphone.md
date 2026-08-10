# captureMicrophone | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / captureMicrophone 
# captureMicrophone
```kotlin
fun captureMicrophone(sampleRate: Int, stereoTrackResult: Tensor, timestampResult: Tensor? = null)
```
Captures microphone stereo-audio track into tensors, encoded in compatible PCM format. 
#### Parameters
sample Rate 
the sample rate of the captured audio data in Hz. 
stereo Track Result 
the tensor to store the stereo audio track data. The tensor can only be a multi-dimensional or a point2 array tensor where the X field of each point stores the LEFT-channel audio sample, and Y stores the RIGHT-channel sample. 
It is allowed, though not recommended, to use an image tensor (i.e., a multi-dimensional tensor with  Tensor.DataType.Image  pixel type as its datatype) to store the audio track. In such case, the pixel type must have exactly 2 channels: R and G, where the R channel of a pixel stores the LEFT-channel audio sample, and G stores the RIGHT-channel sample. 
If the tensor is a multi-dimensional tensor with non-multi-channel-pixel datatype, its last dimension must be 2, so that the stereo-audio will be stored in an interweaved manner:  {{LEFT, RIGHT}, {LEFT, RIGHT}, {LEFT, RIGHT}, ...} 
The datatype (or pixel type for image tensor) of the tensor can only be:  Tensor.DataType.INT16 ,  Tensor.DataType.INT32 ,  Tensor.DataType.FLOAT32 ,  Tensor.DataType.Image.R16G16_U ,  Tensor.DataType.Image.R16G16_S ,  Tensor.DataType.Image.R32G32_S ,  Tensor.DataType.Image.RG_FLOAT . 
timestamp Result 
the optional tensor to store the timestamp when the audio capture begins. The tensor must be created with  Tensor.TimeStampInitInfo . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior. 
```kotlin
fun captureMicrophone(sampleRate: Int, leftTrackResult: Tensor? = null, rightTrackResult: Tensor? = null, timestampResult: Tensor? = null)
```
Captures microphone left and right audio track into separated tensors, encoded in compatible PCM format.  Note:  at least one of the  leftTrackResult  and the  rightTrackResult  must be present. 
If both  leftTrackResult  and  rightTrackResult  are present, their numbers of elements and their datatype must be the same. 
#### Parameters
sample Rate 
the sample rate of the captured audio data in Hz. It must be a positive number within the range 8000~96000Hz. 
left Track Result 
the tensor to store the left-channel audio track data. The tensor can only be: 
- 
A multi-dimensional tensor (i.e., created with  Tensor.MultiDimensionalInitInfo ), with a     non-multi-channel-pixel datatype, i.e., one of Tensor.DataType.INT16,     Tensor.DataType.INT32, Tensor.DataType.FLOAT32, Tensor.DataType.Image.R16_U,     Tensor.DataType.Image.R16_S, Tensor.DataType.Image.R32_S, or     Tensor.DataType.Image.R_FLOAT. 
- 
One directly casted from  IntArray ,  ShortArray  or  FloatArray  using     Pipeline.newLocalTensor 
- 
Or equivalently, a scalar array tensor created using  Tensor.ShortArrayInitInfo ,     Tensor.IntArrayInitInfo or Tensor.FloatArrayInitInfo. 
right Track Result 
the tensor to store the right-channel audio track data. The tensor can only be: 
- 
A multi-dimensional tensor (i.e., created with  Tensor.MultiDimensionalInitInfo ), with a     non-multi-channel-pixel datatype, i.e., one of Tensor.DataType.INT16,     Tensor.DataType.INT32, Tensor.DataType.FLOAT32,     Tensor.DataType.Image.R16_U,mTensor.DataType.Image.R16_S,     Tensor.DataType.Image.R32_S or Tensor.DataType.Image.R_FLOAT. 
- 
One directly casted from  IntArray ,  ShortArray  or  FloatArray  using     Pipeline.newLocalTensor 
- 
Or equivalently, a scalar array tensor created using  Tensor.ShortArrayInitInfo ,     Tensor.IntArrayInitInfo or Tensor.FloatArrayInitInfo. 
timestamp Result 
the optional tensor to store the timestamp when the audio capture begins. The tensor must be created with  Tensor.TimeStampInitInfo . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior.