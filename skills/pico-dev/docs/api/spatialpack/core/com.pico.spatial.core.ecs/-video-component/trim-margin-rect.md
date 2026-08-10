# trimMarginRect | PICO Spatial SDK

core / com.pico.spatial.core.ecs / VideoComponent / trimMarginRect 
# trimMarginRect
```kotlin
fun trimMarginRect(marginRect: Rect)
```
Sets the margin rectangle of the  VideoComponent . 
It represents the area that remains visible; the excluded area will be removed. Due to discrepancies in aspect ratio, limitations of the display device, and encoding issues, the visible area might differ from the video size. Use this function to specify the margin rectangle for full video display. The  Rect  class uses four integer coordinates: left, top, right, and bottom, where 'left' and 'top' signify the top-left corner, and 'right' and 'bottom' signify the bottom-right corner. 
It is the user's responsibility to determine the margin rectangle, ensuring it is smaller than the actual video size. 
#### Parameters
margin Rect 
The margin rectangle for the video image.