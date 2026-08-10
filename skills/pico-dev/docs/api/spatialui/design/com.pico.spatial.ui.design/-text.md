# Text | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / Text 
# Text
```kotlin
@Composable
```fun  Text ( text :  String ,  modifier :  Modifier  =  Modifier ,  color :  Color  =  Color.Unspecified ,  autoSize :  TextAutoSize ?  =  null ,  fontSize :  TextUnit  =  TextUnit.Unspecified ,  fontStyle :  FontStyle ?  =  null ,  fontWeight :  FontWeight ?  =  null ,  fontFamily :  FontFamily ?  =  null ,  letterSpacing :  TextUnit  =  TextUnit.Unspecified ,  textDecoration :  TextDecoration ?  =  null ,  textAlign :  TextAlign  =  TextAlign.Unspecified ,  lineHeight :  TextUnit  =  TextUnit.Unspecified ,  overflow :  TextOverflow  =  TextOverflow.Clip ,  softWrap :  Boolean  =  true ,  maxLines :  Int  =  Int.MAX_VALUE ,  minLines :  Int  =  1 ,  onTextLayout :  ( TextLayoutResult )  ->  Unit ?  =  null ,  style :  TextStyle  =  LocalTextStyle.current ) 
High level PICO design component to display text. 
Its  TextStyle  uses  LocalTextStyle  provided by PICO design components. 
For easy use, put some  TextStyle 's params here as it is. 
#### Parameters
text 
The text to be displayed. 
modifier 
Modifier  to apply to this layout node. 
color 
Color  to apply to the text. If  Color.Unspecified , and  style  has no color set, this will be  Color.Unspecified . 
auto Size 
Enable auto sizing for this text composable. Finds the biggest font size that fits in the available space and lays the text out with this size. This performs multiple layout passes and can be slower than using a fixed font size. This takes precedence over sizes defined through  fontSize  and  style . See  TextAutoSize . 
font Size 
The size of glyphs to use when painting the text. See  TextStyle.fontSize . 
font Style 
The typeface variant to use when drawing the letters (e.g., italic). See  TextStyle.fontStyle . 
font Weight 
The typeface thickness to use when painting the text (e.g.,  FontWeight.Bold ). 
font Family 
The font family to be used when rendering the text. See  TextStyle.fontFamily . 
letter Spacing 
The amount of space to add between each letter. See  TextStyle.letterSpacing . 
text Decoration 
The decorations to paint on the text (e.g., an underline). See  TextStyle.textDecoration . 
text Align 
The alignment of the text within the lines of the paragraph. See  TextStyle.textAlign . 
line Height 
Line height for the  Paragraph  in  TextUnit  units, e.g. SP or EM. See  TextStyle.lineHeight . 
overflow 
How visual overflow should be handled. 
soft Wrap 
Whether the text should break at soft line breaks. If false, the glyphs in the text will be positioned as if there was unlimited horizontal space. If  softWrap  is false,  overflow  and TextAlign may have unexpected effects. 
max Lines 
An optional maximum number of lines for the text to span, wrapping if necessary. If the text exceeds the given number of lines, it is truncated according to  overflow  and  softWrap . It is required that 1 <=  minLines <=  maxLines . 
min Lines 
The minimum height in terms of minimum number of visible lines. It is required that 1 <=  minLines <=  maxLines . 
on Text Layout 
Callback that is executed when a new text layout is calculated. A  TextLayoutResult  object that callback provides contains paragraph information, size of the text, baselines and other details. The callback can be used to add additional decoration or functionality to the text. For example, to draw selection around the text. 
style 
Style configuration for the text such as color, font, line height etc. 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.sp
import com.pico.spatial.ui.design.ProvideTextStyle
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   ProvideTextStyle(TextStyle.Default) {
    Text("Text sample", color = Color.White, fontSize = 30.sp)
} 
   //sampleEnd
}
```
```kotlin
@Composable
```fun  Text ( text :  AnnotatedString ,  modifier :  Modifier  =  Modifier ,  color :  Color  =  Color.Unspecified ,  autoSize :  TextAutoSize ?  =  null ,  fontSize :  TextUnit  =  TextUnit.Unspecified ,  fontStyle :  FontStyle ?  =  null ,  fontWeight :  FontWeight ?  =  null ,  fontFamily :  FontFamily ?  =  null ,  letterSpacing :  TextUnit  =  TextUnit.Unspecified ,  textDecoration :  TextDecoration ?  =  null ,  textAlign :  TextAlign  =  TextAlign.Unspecified ,  lineHeight :  TextUnit  =  TextUnit.Unspecified ,  overflow :  TextOverflow  =  TextOverflow.Clip ,  softWrap :  Boolean  =  true ,  maxLines :  Int  =  Int.MAX_VALUE ,  minLines :  Int  =  1 ,  inlineContent :  Map < String ,  InlineTextContent >  =  mapOf() ,  onTextLayout :  ( TextLayoutResult )  ->  Unit ?  =  null ,  style :  TextStyle  =  LocalTextStyle.current ) 
High level PICO design component to display text. 
Its  TextStyle  uses  LocalTextStyle  provided by PICO design components. 
For easy use, put some  TextStyle 's params here as it is. 
#### Parameters
text 
The text to be displayed. 
modifier 
Modifier  to apply to this layout node. 
color 
Color  to apply to the text. If  Color.Unspecified , and  style  has no color set, this will be  Color.Unspecified . 
auto Size 
Enable auto sizing for this text composable. Finds the biggest font size that fits in the available space and lays the text out with this size. This performs multiple layout passes and can be slower than using a fixed font size. This takes precedence over sizes defined through  fontSize  and  style . See  TextAutoSize . 
font Size 
The size of glyphs to use when painting the text. See  TextStyle.fontSize . 
font Style 
The typeface variant to use when drawing the letters (e.g., italic). See  TextStyle.fontStyle . 
font Weight 
The typeface thickness to use when painting the text (e.g.,  FontWeight.Bold ). 
font Family 
The font family to be used when rendering the text. See  TextStyle.fontFamily . 
letter Spacing 
The amount of space to add between each letter. See  TextStyle.letterSpacing . 
text Decoration 
The decorations to paint on the text (e.g., an underline). See  TextStyle.textDecoration . 
text Align 
The alignment of the text within the lines of the paragraph. See  TextStyle.textAlign . 
line Height 
Line height for the  Paragraph  in  TextUnit  units, e.g. SP or EM. See  TextStyle.lineHeight . 
overflow 
How visual overflow should be handled. 
soft Wrap 
Whether the text should break at soft line breaks. If false, the glyphs in the text will be positioned as if there was unlimited horizontal space. If  softWrap  is false,  overflow  and TextAlign may have unexpected effects. 
max Lines 
An optional maximum number of lines for the text to span, wrapping if necessary. If the text exceeds the given number of lines, it is truncated according to  overflow  and  softWrap . It is required that 1 <=  minLines <=  maxLines . 
min Lines 
The minimum height in terms of minimum number of visible lines. It is required that 1 <=  minLines <=  maxLines . 
inline Content 
A map store composables that replaces certain ranges of the text. It's used to insert composables into text layout. Check  InlineTextContent  for more information. 
on Text Layout 
Callback that is executed when a new text layout is calculated. A  TextLayoutResult  object that callback provides contains paragraph information, size of the text, baselines and other details. The callback can be used to add additional decoration or functionality to the text. For example, to draw selection around the text. 
style 
Style configuration for the text such as color, font, line height etc. 
#### Samples
```
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.sp
import com.pico.spatial.ui.design.ProvideTextStyle
import com.pico.spatial.ui.design.Text

fun main() { 
   //sampleStart 
   ProvideTextStyle(TextStyle.Default) {
    Text("Text sample", color = Color.White, fontSize = 30.sp)
} 
   //sampleEnd
}
```