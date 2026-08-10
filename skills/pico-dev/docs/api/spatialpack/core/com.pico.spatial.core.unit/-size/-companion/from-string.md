# fromString | PICO Spatial SDK

core / com.pico.spatial.core.unit / Size / Companion / fromString 
# fromString
```kotlin
@JvmStatic
```fun  fromString ( string :  String ) :  Size 
Parses the specified string into a  Size  instance. 
The ASCII characters  \``u002a  ('*') and  \``u0078  ('x') are recognized as separators between the width and height. 
For any  Size s :  Size.parseSize(s.toString()).equals(s) . However, the method also handles sizes expressed in the following forms: 
" width x height x depth " or " width * height * depth "  => new Size(width, height, depth) , where  width  and  height  and  depth  are string integers potentially containing a sign, such as "-10", "+7" or "5". 
#### 
#### 
#### 
```
`Size.parseSize("3*+6*7").equals(new Size(3, 6, 7)) == true
Size.parseSize("-3x-6x-7").equals(new Size(-3, -6, -7)) == true
Size.parseSize("4 by 3 by 7") => throws NumberFormatException.

ReturnThe string representation of a size value.ParametersstringThe string representation of a size value.ThrowsNumberFormatExceptionIf the string cannot be parsed as a valid size.NullPointerExceptionIf string is null.
```