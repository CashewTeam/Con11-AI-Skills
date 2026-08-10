# nonMaximumSuppression | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / nonMaximumSuppression 
# nonMaximumSuppression
```kotlin
fun nonMaximumSuppression(iou: Float, scores: Tensor, boxes: Tensor, scoresResult: Tensor? = null, boxesResult: Tensor? = null, indicesResult: Tensor? = null)
```
Run non-maximum-suppression (NMS) on 2D bounding boxes. 
#### Parameters
iou 
a configuration value, determining the intersection-over-union threshold when the non-maximum suppression is run. 
scores 
the input tensor holding the scores for each bounding box. The tensor must be a multi-dimensional tensor of with dimensions =  N x1 or 1x N , where  N  is the number of input bounding boxes. The data type must be one of  DataType.FLOAT64 ,  DataType.FLOAT32 ,  DataType.Image.R_FLOAT , or  DataType.Image.R_DOUBLE . 
boxes 
the input tensor holding the box boundaries. The boundaries are expected to be expressed in  XXYY  format. The tensor must be a multi-dimensional tensor of datatype being one of  DataType.FLOAT64  or  DataType.FLOAT32 , with dimensions =  N x4, where  N  is the number of input bounding boxes and must match that of  scores . Alternatively, the tensor can also be a multi-dimensional image tensor with dimensions =  N x1 or 1x N , of a floating-point pixel type with 4 channels (R, G, B and A channels of one pixel will be treated as the Xmin, Xmax, Ymin, Ymax of a bounding box). 
scores Result 
an optional result, holding first  M  scores of bounding boxes passed NMS, sorted from highest to lowest. The tensor, if provided, must be a multi-dimensional tensor of with dimensions =  M x1 or 1x M . The data type must be one of  DataType.FLOAT64 ,  DataType.Image.R_FLOAT ,  DataType.Image.R_FLOAT_DYNAMIC ,  DataType.Image.R_DOUBLE . 
boxes Result 
an optional result, holding first  M  bounding boxes passed NMS, sorted from the highest score to the lowest, matching the scores output from  scoresResult . The tensor, if provided, must be a multi-dimensional tensor of datatype being one of  DataType.FLOAT64  or  DataType.FLOAT32 , with dimensions =  M x4, where  M  is the number of input bounding boxes and must match that of  scores . Alternatively, the tensor can also be a multi-dimensional image tensor with dimensions =  M x1 or 1x M , of a floating-point pixel type with 4 channels (R, G, B and A channels of one pixel will store the Xmin, Xmax, Ymin and Ymax of a bounding box). 
indices Result 
an optional result, holding the original indices in the  boxes  input of the first  M  bounding boxes passed NMS, sorted by the bounding boxes' scores, from the highest to the lowest, matching the scores and boxes output from  scoresResult  and  boxesResult . The tensor, if provided, must be a multi-dimensional tensor of a non-pixel datatype or a RED-channel-only pixel type, with dimensions =  M x1, or 1x M . The data type must be one of the integral types. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.