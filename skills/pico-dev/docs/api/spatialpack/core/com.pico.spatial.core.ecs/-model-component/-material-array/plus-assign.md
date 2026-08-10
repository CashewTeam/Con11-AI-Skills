# plusAssign | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ModelComponent / MaterialArray / plusAssign 
# plusAssign
```kotlin
operator fun plusAssign(element: Material)
```
Overloads the  +=  operator to append a single material to the end of the array. 
#### Parameters
element 
The  Material  instance to add. 
```kotlin
operator fun plusAssign(elements: Array<Material>)
```
Overloads the  +=  operator to append an array of materials to the end of the array. 
#### Parameters
elements 
The array of  Material  instances to add.