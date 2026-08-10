# obtainVibrant | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.vibrant / obtainVibrant 
# obtainVibrant
```kotlin
fun Color.obtainVibrant(): Vibrant
```
Decodes the vibrant style from the  Color . 
This method extracts the vibrant style information embedded in the color value. If no vibrant style is encoded,  Vibrant.Unspecified  is returned. 
#### Return
The decoded  Vibrant  style.