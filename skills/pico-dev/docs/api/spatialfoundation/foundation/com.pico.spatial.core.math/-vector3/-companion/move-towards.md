# moveTowards | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / moveTowards 
# moveTowards
```kotlin
@JvmStatic
```fun  moveTowards ( from :  Vector3 ,  target :  Vector3 ,  maxDistanceDeltaInput :  Float ) :  Vector3 
Moves a point  from  towards a  target  point by a maximum distance specified by  maxDistanceDeltaInput . 
The  maxDistanceDeltaInput  is clamped to be non-negative; if a negative value is provided, it's treated as  0.0f  (resulting in no movement unless  from  is already at  target ). 
- 
If  from  is already at  target , or if  target  is within the (non-negative)  maxDistanceDelta  distance, this function returns  target . 
- 
If  maxDistanceDelta  (after clamping) is  0.0f  and  from  is not at  target , this function returns  from  (no movement). 
- 
Otherwise,  from  is moved along the straight line towards  target  by exactly  maxDistanceDelta  units. 
#### Return
A new  Vector3  instance representing the new position after moving. 
#### Parameters
from 
The starting point (Vector3). 
target 
The destination point (Vector3) towards which  from  is moved. 
max Distance Delta Input 
The maximum distance  from  should move. Negative values are effectively treated as  0.0f .