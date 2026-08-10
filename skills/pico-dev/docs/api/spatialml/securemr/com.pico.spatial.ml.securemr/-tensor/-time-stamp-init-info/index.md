# TimeStampInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / TimeStampInitInfo 
# TimeStampInitInfo
```kotlin
class TimeStampInitInfo : Tensor.SpecialUsageInitInfo
```
Initialization for a timestamp 
Note  here, since a timestamp is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A timestamp holds the time stamp output from certain pipeline methods. It also enables the auto-boxing of a Kotlin  LocalDataTime  into SecureMR Tensors. 
#### See also
Pipeline Members 
## Constructors
Time Stamp Init Info 
```kotlin
constructor()
```