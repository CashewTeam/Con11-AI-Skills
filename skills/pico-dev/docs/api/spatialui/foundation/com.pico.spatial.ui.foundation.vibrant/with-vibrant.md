# withVibrant | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.vibrant / withVibrant 
# withVibrant
```kotlin
fun Color.withVibrant(vibrant: Vibrant): Color
```
Encodes the specified  Vibrant  style into the  Color . 
This method embeds the vibrant style information into the color value, allowing it to be recognized and rendered with the corresponding material effect by the spatial rendering system. 
Constraints & Usage: 
- 
This is designed for use within the SpatialUI framework where the rendering pipeline supports     vibrant effect decoding from colors. 
- 
The resulting color retains its original color components (RGB) but carries the additional     vibrant metadata. 
- 
WARNING: The vibrant info is encoded directly into the color bits. Operations such as: 
- 
Animation interpolation 
- 
Gradients 
- 
Shader manipulations 
- 
Android blending will destroy the encoded vibrant info. Consequence: The vibrant effect       will be LOST, and the rendering will fall back to the original, non-vibrant color. This       results in a visual downgrade (plain color) rather than graphical errors. 
Animation Support : 
Note: The vibrant style itself is discrete and categorical, not a continuous value. Therefore, it cannot be interpolated (lerp) like RGB channels. This means you cannot animate "from Vibrant.Light to Vibrant.Dark". 
Using  animateColorAsState  directly on a color with vibrant style will result in a unpredictable result. 
To support color animations with vibrant effects, use one of the following approaches: 
- 
Animate the raw color, then apply .withVibrant():  `` val animatedColor by        animateColorAsState(targetColor) // Apply vibrant to the current animated value val finalColor        = animatedColor.withVibrant(vibrant) `` 
- 
Use Modifier.vibrantEffect (Recommended for Composable): val animatedColor by        animateColorAsState(targetColor)  `` Box( Modifier .vibrantEffect(vibrant)        .background(animatedColor) ) `` 
- 
Use animateColorVibrantAsState (Limited): Supports animating between colors that share the        SAME vibrant style. 
Important Limitation: 
 Only supports animating colors with the  same Vibrant  style. It does  not  support     animating between different Vibrant styles. 
- 
Supported :  Color.Red.withVibrant(Vibrant.Dark)  -> Color.Blue.withVibrant(Vibrant.Dark) 
- 
Not Supported :  Color.Red.withVibrant(Vibrant.Dark)  -> Color.Red.withVibrant(Vibrant.Light) 
Gradient Support : 
 Similar to animations, gradients (e.g., androidx.compose.ui.graphics.Brush.linearGradient)     interpolate colors between stops. This interpolation corrupts the encoded vibrant bits, causing     the vibrant effect to be LOST and resulting in a standard 2D gradient. 
 To use vibrant effects with gradients: 
- 
Do NOT use .withVibrant() on the gradient colors. 
- 
Use Modifier.vibrantEffect(vibrant) on the component instead. 
 Example: Box( Modifier .vibrantEffect(vibrant) .background( Brush.linearGradient( colors =     listOf(Color.Red, Color.Blue) // Pure colors without vibrant encoding ) ) ) 
 @param vibrant The  Vibrant  style to encode into the color.     @return A new  Color  instance containing the encoded vibrant information.     @see vibrantEffect