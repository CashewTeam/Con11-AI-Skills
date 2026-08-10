# moveTowards | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / moveTowards 
# moveTowards
```kotlin
@JvmStatic
```fun  moveTowards ( current :  Vector2 ,  target :  Vector2 ,  maxDistanceDeltaInput :  Float ) :  Vector2 
Moves a point  current  towards a  target  point by a maximum distance. 
The input  maxDistanceDeltaInput  is treated as a non-negative distance; if a negative value is supplied, it's clamped to  0.0f . 
- 
If  current  is already at  target , or if  target  is within the (non-negative)  maxDistanceDelta  distance, this function returns  target . 
- 
If  maxDistanceDelta  (non-negative) is  0.0f  and  current  is not at  target , this function returns  current  (no movement). 
- 
Otherwise,  current  is moved along the straight line towards  target  by exactly  maxDistanceDelta  units. 
#### Return
A new  Vector2  instance representing the new position after moving. 
#### Parameters
current 
The starting point (Vector2). 
target 
The destination point (Vector2) towards which  current  is moved. 
max Distance Delta Input 
The maximum distance  current  should move. Negative values are treated as  0.0f .