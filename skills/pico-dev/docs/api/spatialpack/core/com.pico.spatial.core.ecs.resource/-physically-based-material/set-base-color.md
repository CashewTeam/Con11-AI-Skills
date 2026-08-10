# setBaseColor | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setBaseColor 
# setBaseColor
```kotlin
fun setBaseColor(color: Color4)
```
Sets the base color of the  PhysicallyBasedMaterial  using a color value. 
This method allows you to specify the color directly using a  Color4  object, which provides a straightforward way to define the material's base color. 
#### Parameters
color 
The  Color4  object representing the desired color in linear space. The default value is  Color4(1f, 1f, 1f, 1f) . 
#### Throws
Illegal State Exception 
If this material is closed or invalid.