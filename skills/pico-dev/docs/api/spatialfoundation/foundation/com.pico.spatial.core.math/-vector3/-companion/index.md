# Companion | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Vector3 . 
Members 
## Properties
BACK 
```kotlin
@JvmField
```val  BACK :  Vector3 
The back Vector3 instance, and its real value is (0f, 0f, -1f). 
DOWN 
```kotlin
@JvmField
```val  DOWN :  Vector3 
The down Vector3 instance, and its real value is (0f, -1f, 0f). 
FORWARD 
```kotlin
@JvmField
```val  FORWARD :  Vector3 
The forward Vector3 instance, and its real value is (0f, 0f, 1f). 
LEFT 
```kotlin
@JvmField
```val  LEFT :  Vector3 
The left Vector3 instance, and its real value is (-1f, 0f, 0f). 
ONE 
```kotlin
@JvmField
```val  ONE :  Vector3 
The one Vector3 instance, and its real value is (1f, 1f, 1f). 
RIGHT 
```kotlin
@JvmField
```val  RIGHT :  Vector3 
The right Vector3 instance, and its real value is (1f, 0f, 0f). 
UP 
```kotlin
@JvmField
```val  UP :  Vector3 
The up Vector3 instance, and its real value is (0f, 1f, 0f). 
ZERO 
```kotlin
@JvmField
```val  ZERO :  Vector3 
The zero Vector3 instance, and its real value is (0f, 0f, 0f). 
## Functions
angle 
```kotlin
@JvmStatic
```fun  angle ( from :  Vector3 ,  to :  Vector3 ) :  Float 
Calculates the angle in degrees between two 3D vectors. 
cross 
```kotlin
@JvmStatic
```fun  cross ( a :  Vector3 ,  b :  Vector3 ) :  Vector3 
Calculates the cross product (vector product) of two  Vector3  vectors. 
distance 
```kotlin
@JvmStatic
```fun  distance ( a :  Vector3 ,  b :  Vector3 ) :  Float 
Calculates the Euclidean distance between two 3D vectors. 
dot 
```kotlin
@JvmStatic
```fun  dot ( a :  Vector3 ,  b :  Vector3 ) :  Float 
Calculates the dot product (scalar product) of two  Vector3  vectors. 
face Forward 
```kotlin
@JvmStatic
```fun  faceForward ( n :  Vector3 ,  i :  Vector3 ,  nRef :  Vector3 ) :  Vector3 
Orients a vector  n  to face in the direction opposite to an incident vector  i , using  nRef  as a reference to determine if  i  is arriving from the front or back side. 
lerp 
```kotlin
@JvmStatic
```fun  lerp ( a :  Vector3 ,  b :  Vector3 ,  t :  Float ) :  Vector3 
Performs a linear interpolation between two vectors  a  and  b  by an interpolant  t . 
lerp Unclamped 
```kotlin
@JvmStatic
```fun  lerpUnclamped ( a :  Vector3 ,  b :  Vector3 ,  t :  Float ) :  Vector3 
Performs an unclamped linear interpolation between two vectors  a  and  b  by an interpolant  t . 
move Towards 
```kotlin
@JvmStatic
```fun  moveTowards ( from :  Vector3 ,  target :  Vector3 ,  maxDistanceDeltaInput :  Float ) :  Vector3 
Moves a point  from  towards a  target  point by a maximum distance specified by  maxDistanceDeltaInput . 
project 
```kotlin
@JvmStatic
```fun  project ( a :  Vector3 ,  b :  Vector3 ) :  Vector3 
Calculates the vector projection of vector  a  onto vector  b . 
reflect 
```kotlin
@JvmStatic
```fun  reflect ( i :  Vector3 ,  n :  Vector3 ) :  Vector3 
Calculates the reflection vector of an incident vector 'i' across a surface defined by its normal 'n'. 
slerp 
```kotlin
@JvmStatic
```fun  slerp ( a :  Vector3 ,  b :  Vector3 ,  t :  Float ) :  Vector3 
Performs Spherical Linear Interpolation between two 3D vectors  a  and  b  by an interpolant  t . 
slerp Unclamped 
```kotlin
@JvmStatic
```fun  slerpUnclamped ( a :  Vector3 ,  b :  Vector3 ,  t :  Float ) :  Vector3 
Performs unclamped spherical linear interpolation (slerp) between two 3D vectors.