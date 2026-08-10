# Text | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Text 
# Text
```kotlin
sealed class Text : SceneGraphProperty
```
Update a property of one entity's Text component. If the entity has not been added a text component to, updating its text component property will create one for the entity. The component will render text at the origin of the entity's local coordination system. 
#### Parameters
property 
the name of the property. 
#### Inheritors
Content Color BackgroundColor FontSize HorizontalAlignment VerticalAlignment Members 
## Types
Background Color 
```kotlin
object BackgroundColor : SceneGraphProperty.Text
```
Update the text's background color. 
Color 
```kotlin
object Color : SceneGraphProperty.Text
```
Update the content of the text component. 
Content 
```kotlin
object Content : SceneGraphProperty.Text
```
Update the content of the text component. 
Font Size 
```kotlin
object FontSize : SceneGraphProperty.Text
```
Update the font size of text. 
Horizontal Alignment 
```kotlin
object HorizontalAlignment : SceneGraphProperty.Text
```
Update horizontal alignment of text. 
Vertical Alignment 
```kotlin
object VerticalAlignment : SceneGraphProperty.Text
```
Update vertical alignment of text.