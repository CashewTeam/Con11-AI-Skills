# fromArray | PICO Spatial SDK

core / com.pico.spatial.core.unit / Size / Companion / fromArray 
# fromArray
```kotlin
@JvmStatic
```fun  fromArray ( array :  IntArray ) :  Size 
Creates a new  Size  instance from a 3-element integer array. 
#### Return
A  Size  instance with the values from the array. 
#### Parameters
array 
A 3-element  IntArray  representing width, height, and depth. Index 0 is the width, index 1 is the height, index 2 is the depth. 
#### Throws
Illegal Argument Exception 
If  array  does not contain exactly three elements.