# Companion | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Vector2 . 
Members 
## Properties
DOWN 
```kotlin
@JvmField
```val  DOWN :  Vector2 
The down Vector2 instance, and its real value is (0f, -1f). 
LEFT 
```kotlin
@JvmField
```val  LEFT :  Vector2 
The left Vector2 instance, and its real value is (-1f, 0f). 
ONE 
```kotlin
@JvmField
```val  ONE :  Vector2 
A constant representing a vector with all components set to one (1, 1). 
RIGHT 
```kotlin
@JvmField
```val  RIGHT :  Vector2 
The right Vector2 instance, and its real value is (1f, 0f). 
UP 
```kotlin
@JvmField
```val  UP :  Vector2 
The up Vector2 instance, and its real value is (0f, 1f). 
ZERO 
```kotlin
@JvmField
```val  ZERO :  Vector2 
A constant representing a zero vector (0, 0). 
## Functions
angle 
```kotlin
@JvmStatic
```fun  angle ( from :  Vector2 ,  to :  Vector2 ) :  Float 
Calculates the angle between two 2D vectors and returns it in degrees. This version includes robustness improvements for numerical stability. This function throws an  IllegalArgumentException  if either input vector is a zero vector. The calculated angle represents the shortest angle between the two vectors and is typically in the range  [0, 180]  degrees. 
cross 
```kotlin
@JvmStatic
```fun  cross ( a :  Vector2 ,  b :  Vector2 ) :  Float 
Calculates the 2D cross product (also known as the perpendicular dot product or z-component of the 3D cross product) of two 2D vectors. 
distance 
```kotlin
@JvmStatic
```fun  distance ( a :  Vector2 ,  b :  Vector2 ) :  Float 
Calculates the Euclidean distance between two 2D points (represented by vectors). 
dot 
```kotlin
@JvmStatic
```fun  dot ( a :  Vector2 ,  b :  Vector2 ) :  Float 
Calculates the dot product (scalar product) of two 2D vectors. 
face Forward 
```kotlin
@JvmStatic
```fun  faceForward ( n :  Vector2 ,  i :  Vector2 ,  nRef :  Vector2 ) :  Vector2 
Orients a normal vector  n  to face towards an incident vector  i , using a reference normal  nRef  to determine the orientation. 
lerp 
```kotlin
@JvmStatic
```fun  lerp ( a :  Vector2 ,  b :  Vector2 ,  t :  Float ) :  Vector2 
Performs linear interpolation between two 2D vectors,  a  and  b . 
lerp Unclamped 
```kotlin
@JvmStatic
```fun  lerpUnclamped ( a :  Vector2 ,  b :  Vector2 ,  t :  Float ) :  Vector2 
Performs unclamped linear interpolation between two 2D vectors,  a  and  b . 
move Towards 
```kotlin
@JvmStatic
```fun  moveTowards ( current :  Vector2 ,  target :  Vector2 ,  maxDistanceDeltaInput :  Float ) :  Vector2 
Moves a point  current  towards a  target  point by a maximum distance. 
project 
```kotlin
@JvmStatic
```fun  project ( a :  Vector2 ,  b :  Vector2 ) :  Vector2 
Calculates the vector projection of vector  a  onto vector  b . 
reflect 
```kotlin
@JvmStatic
```fun  reflect ( i :  Vector2 ,  n :  Vector2 ) :  Vector2 
Calculates the reflection of an incident vector 'i' across a surface defined by its normal 'n'.