# outputSounds | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / outputSounds 
# outputSounds
```kotlin
fun outputSounds(sampleRate: Int, audioTrack: Tensor)
```
Play sounds from an audio track. The audio track must be encoded in PCM format. 
#### Parameters
sample Rate 
the sample rate in Hz. It must be a positive integer within the range of 8000~96000Hz. 
audio Track 
The audio track to be played. The track will be treated as a stereo-audio track if (1) it is a point2 array, where the X field of a point is regarded as the LEFT-channel audio sample, and Y field as the RIGHT-channel sample; (2) it is an image tensor of 2-channel pixel type, where the R channel of a pixel is regarded as the LEFT-channel audio sample, and G channel as the RIGHT-channel sample; (3) it is a multi-dimensional tensor of non-multi-channel-pixel datatype, but its last dimension is 2. In this case, the data container in the tensor will be read as interweaved stereo-audio:  {{LEFT, RIGHT}, {LEFT, RIGHT}, {LEFT, RIGHT}, ...} . Otherwise, the audio track is treated as a mono-audio track. 
The tensor's datatype must be one of  DataType.INT16 ,  DataType.INT32 ,  DataType.FLOAT32 ,  DataType.Image.R16_U ,  DataType.Image.R16_S ,  DataType.Image.R32_S ,  DataType.Image.R_FLOAT ,  DataType.Image.R16G16_U ,  DataType.Image.R16G16_S ,  DataType.Image.R32G32_S , or  DataType.Image.RG_FLOAT .