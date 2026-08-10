# moveTowards | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / Companion / moveTowards 
# moveTowards
```kotlin
@JvmStatic
```fun  moveTowards ( from :  Vector4 ,  target :  Vector4 ,  maxDistanceDeltaInput :  Float ) :  Vector4 
Moves a 4D point  from  towards a  target  point by a maximum distance specified by  maxDistanceDeltaInput . 
The  maxDistanceDeltaInput  is clamped to be non-negative; if a negative value is provided, it's treated as  0.0f  (resulting in no movement unless  from  is already at  target ). 
- 
If  from  is already at  target , or if  target  is within the (non-negative)  maxDistanceDelta  distance, this function returns  target . 
- 
If  maxDistanceDelta  (after clamping) is  0.0f  and  from  is not at  target , this function returns  from  (no movement). 
- 
Otherwise,  from  is moved along the straight line towards  target  by exactly  maxDistanceDelta  units. 
#### Return
A new  Vector4  instance representing the new position after moving. 
#### Parameters
from 
The starting  Vector4  point. 
target 
The destination  Vector4  point towards which  from  is moved. 
max Distance Delta Input 
The maximum distance  from  should move. Negative values are effectively treated as  0.0f .