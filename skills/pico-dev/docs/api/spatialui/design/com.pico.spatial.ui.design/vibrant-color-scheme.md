# vibrantColorScheme | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / vibrantColorScheme 
# vibrantColorScheme
```kotlin
fun vibrantColorScheme(fillPrimary: Color = Color.Vibrant.withVibrant(Vibrant.Darker), fillSecondary: Color = Color.Vibrant.withVibrant(Vibrant.SemiLight), fillTertiary: Color = Color.Vibrant.withVibrant(Vibrant.Neutral), fillLight: Color = Color.Vibrant.withVibrant(Vibrant.Light), labelPrimaryLight: Color = ColorTokens.Default.SubWhite100.withVibrant(Vibrant.None), labelPrimary: Color = Color.Vibrant.withVibrant(Vibrant.Darkest), labelSecondary: Color = Color.Vibrant.withVibrant(Vibrant.UltraDark), labelTertiary: Color = Color.Vibrant.withVibrant(Vibrant.Semidark), labelQuaternary: Color = Color.Vibrant.withVibrant(Vibrant.Dark), lightenHover: Color = Color.Vibrant.withVibrant(Vibrant.SemiLight), lightenPressed: Color = Color.Vibrant.withVibrant(Vibrant.SemiLight), error: Color = ColorTokens.Default.SubRed100.withVibrant(Vibrant.None), alert: Color = ColorTokens.Default.SubOrange100.withVibrant(Vibrant.None), passable: Color = ColorTokens.Default.SubGreen100.withVibrant(Vibrant.None), interaction: Color = ColorTokens.Default.SubBlue100.withVibrant(Vibrant.None), dividerLine: Color = ColorTokens.Default.SubBlack12.withVibrant(Vibrant.None)): ColorScheme
```
A vibrant color scheme. 
This function only provides the default vibrant role mapping. It does not read system resources. You can use  ColorScheme.copy  to customize the color scheme. 
#### Return
Returns a default PICO design  ColorScheme .