# Color4 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color4 / Color4 
# Color4
```kotlin
constructor(red: Float, green: Float, blue: Float, alpha: Float)
```
Constructs a new  Color4  instance with the specified red, green, blue, and alpha components. 
#### Parameters
red 
The red component of the color, typically in the range 0, 1. 
green 
The green component of the color, typically in the range 0, 1. 
blue 
The blue component of the color, typically in the range 0, 1. 
alpha 
The alpha component (opacity) of the color, typically in the range 0, 1. 
```kotlin
constructor(another: Color4)
```
The constructor to initialize from another  Color4  instance. 
#### Parameters
another 
Another  Color4  instance, and its values will be used to initialize a new  Color4  instance with the same data sequence. 
```kotlin
constructor(vector4: Vector4)
```
The constructor to initialize from a  Vector4  instance. 
#### Parameters
vector4 
The  Vector4  instance, and its values will be used to initialize a new  Color4  instance. 
```kotlin
constructor(vector3: Vector3)
```
The constructor to initialize from a  Vector3  instance, the default alpha value will be use 1f. 
#### Parameters
vector3 
The  Vector3  instance, and its values will be used to initialize a new  Color4  instance.