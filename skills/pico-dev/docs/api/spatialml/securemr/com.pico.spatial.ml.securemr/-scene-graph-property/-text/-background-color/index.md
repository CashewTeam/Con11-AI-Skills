# BackgroundColor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Text / BackgroundColor 
# BackgroundColor
```kotlin
object BackgroundColor : SceneGraphProperty.Text
```
Update the text's background color. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a color array of size 1, i.e., a single color element.