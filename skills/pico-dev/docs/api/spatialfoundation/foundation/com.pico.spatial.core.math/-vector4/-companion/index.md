# Companion | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Vector4 . 
Members 
## Properties
BACK 
```kotlin
@JvmField
```val  BACK :  Vector4 
The back  Vector4  instance, and its real value is  (0f, 0f, -1f, 0f) . 
DOWN 
```kotlin
@JvmField
```val  DOWN :  Vector4 
The down  Vector4  instance, and its real value is  (0f, -1f, 0f, 0f) . 
FORWARD 
```kotlin
@JvmField
```val  FORWARD :  Vector4 
The forward  Vector4  instance, and its real value is  (0f, 0f, 1f, 0f) . 
LEFT 
```kotlin
@JvmField
```val  LEFT :  Vector4 
The left  Vector4  instance, and its real value is  (-1f, 0f, 0f, 0f) . 
ONE 
```kotlin
@JvmField
```val  ONE :  Vector4 
The one  Vector4  instance, and its real value is  (1f, 1f, 1f, 1f) . 
RIGHT 
```kotlin
@JvmField
```val  RIGHT :  Vector4 
The right  Vector4  instance, and its real value is  (1f, 0f, 0f, 0f) . 
UP 
```kotlin
@JvmField
```val  UP :  Vector4 
The up  Vector4  instance, and its real value is  (0f, 1f, 0f, 0f) . 
ZERO 
```kotlin
@JvmField
```val  ZERO :  Vector4 
The zero  Vector4  instance, and its real value is  (0f, 0f, 0f, 0f) . 
## Functions
distance 
```kotlin
@JvmStatic
```fun  distance ( a :  Vector4 ,  b :  Vector4 ) :  Float 
Calculates the Euclidean distance between two 4D vectors,  a  and  b . 
dot 
```kotlin
@JvmStatic
```fun  dot ( a :  Vector4 ,  b :  Vector4 ) :  Float 
Calculates the dot product (scalar product) of two 4D vectors. 
face Forward 
```kotlin
@JvmStatic
```fun  faceForward ( n :  Vector4 ,  i :  Vector4 ,  nRef :  Vector4 ) :  Vector4 
Orients a 4D vector  n  to face in a direction consistent with an incident vector  i , using a reference vector  nRef  to determine orientation. 
lerp 
```kotlin
@JvmStatic
```fun  lerp ( a :  Vector4 ,  b :  Vector4 ,  t :  Float ) :  Vector4 
Performs a linear interpolation between two 4D vectors  a  and  b  by an interpolant  t . 
lerp Unclamped 
```kotlin
@JvmStatic
```fun  lerpUnclamped ( a :  Vector4 ,  b :  Vector4 ,  t :  Float ) :  Vector4 
Performs an unclamped linear interpolation between two 4D vectors  a  and  b  by an interpolation factor  t . 
move Towards 
```kotlin
@JvmStatic
```fun  moveTowards ( from :  Vector4 ,  target :  Vector4 ,  maxDistanceDeltaInput :  Float ) :  Vector4 
Moves a 4D point  from  towards a  target  point by a maximum distance specified by  maxDistanceDeltaInput . 
project 
```kotlin
@JvmStatic
```fun  project ( a :  Vector4 ,  b :  Vector4 ) :  Vector4 
Calculates the vector projection of vector  a  onto vector  b  for 4D vectors. 
reflect 
```kotlin
@JvmStatic
```fun  reflect ( i :  Vector4 ,  n :  Vector4 ) :  Vector4 
Calculates the reflection of an incident vector  i  across a surface defined by the normal vector  n .