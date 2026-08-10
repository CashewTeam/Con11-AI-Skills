# runModelInference | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / runModelInference 
# runModelInference
```kotlin
fun runModelInference(modelName: String, modelType: Pipeline.ModelInferenceType, modelBinary: SharedMemory, inputs: Array<Pipeline.ModelNodeEncoding>, outputs: Array<Pipeline.ModelNodeEncoding>)
```
Run the inference of an algorithm model provided in binary package. 
This API supports TensorFlow Lite FlatBuffer models. The binary format stored in  modelBinary  must be a TensorFlow Lite FlatBuffer model, and  modelType  selects the LiteRT / TFLite backend: 
- 
ModelInferenceType.LITE_RT_CPU : TensorFlow Lite FlatBuffer model executed on CPU. 
- 
ModelInferenceType.LITE_RT_GPU : TensorFlow Lite FlatBuffer model executed on GPU. 
- 
ModelInferenceType.LITE_RT_NPU : TensorFlow Lite FlatBuffer model executed on NPU. 
#### Parameters
model Name 
the name tag for the algorithm binary package. 
model Type 
the type of the algorithm model. 
model Binary 
the shared memory which stored the algorithm binary package. The binary package must be a TensorFlow Lite FlatBuffer model for every  modelType . 
inputs 
the descriptions and tensor association of inputs to the selected model when it is executed. You can use this array to select which computation graph nodes will accept data from pipeline tensors. 
outputs 
the descriptions and tensor association of outputs from the selected model after execution. You can use this array to select from which computation graph nodes you would like to read values into pipeline tensors.