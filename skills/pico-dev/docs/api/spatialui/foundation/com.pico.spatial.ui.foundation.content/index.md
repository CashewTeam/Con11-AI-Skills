# com.pico.spatial.ui.foundation.content | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content 
# Package-level declarations
Types Functions Properties 
## Types
Attachment Panel Builder 
```kotlin
interface AttachmentPanelBuilder
```
A builder for spatial UI attachments 
Loaded Model 
```kotlin
@Stable
```abstract  class  LoadedModel 
Loaded model. 
Model Loading State 
```kotlin
@Stable
```sealed  class  ModelLoadingState 
The state of loading a 3D model. 
Resizability 
```kotlin
enum Resizability : Enum<Resizability>
```
The resizability of a 3D model. 
Source 
```kotlin
@Stable
```open  class  Source < T > 
Define datasource support by  SpatialModelView . 
Spatial Model Scope 
```kotlin
abstract class SpatialModelScope
```
Scope for  SpatialModelView  content function. 
Spatial View Attachments 
```kotlin
interface SpatialViewAttachments
```
The attachments belong to a  SpatialView 
## Properties
orientation 
```kotlin
val ViewPoint.orientation: Rotation3D
```
Get the rotation of the volume towards to observer . 
## Functions
attachment Panel Component 
```kotlin
@Composable
```fun  attachmentPanelComponent ( context :  Context  =  LocalContext.current ,  size :  IntSize  =  panelSize(Dp.Unspecified, Dp.Unspecified) ,  alignment :  AttachmentPanelComponent.Alignment  =  AttachmentPanelComponent.Alignment.UNSPECIFIED ,  content :  @ Composable ( )  ->  Unit ) :  AttachmentPanelComponent 
Creates a  AttachmentPanelComponent  in another Composable. Notice that this function is for your convenience to create a AttachmentPanelComponent in your Composable, once the return value set to an Entity, your later changes will not take effect. 
content 
```kotlin
fun AttachmentPanelComponent.content(compositionContext: CompositionContext? = null, content: @Composable () -> Unit): AttachmentPanelComponent
```
Sets the content of the AttachmentPanelComponent. 
load From 
```kotlin
suspend fun Entity.Companion.loadFrom(source: Source<*>): Entity
```
Load entity from  Source . Its running on IO thread. will auto destroy entity when coroutine is canceled 
Model 
```kotlin
@Composable
```fun  SpatialModelScope . Model ( model :  LoadedModel ,  modifier :  Modifier  =  Modifier ) 
Display 3d model when load success. 
panel Size 
```kotlin
@Composable
```fun  panelSize ( @ FloatRange ( from  =  0.0 ,  to  =  2048.0 ) width :  Dp ,  @ FloatRange ( from  =  0.0 ,  to  =  2048.0 ) height :  Dp ) :  IntSize 
Converts the  Dp  size to  IntSize  in pixel for  AttachmentPanelComponent  using. If the  Dp  is  Dp.Unspecified , the  IntSize  will be  WRAP_CONTENT . 
```kotlin
@Composable
```fun  panelSize ( width :  Float ,  height :  Float ,  lengthUnit :  LengthUnit  =  LengthUnit.Meters ) :  IntSize 
Converts the  Float  size of length unit to  IntSize  in pixel for  AttachmentPanelComponent  using. If the  Float  is  Float.NaN , the  IntSize will be  WRAP_CONTENT . 
set Base Color 
```kotlin
fun PhysicallyBasedMaterial.setBaseColor(color: Color)
```
Set compose color to  PhysicallyBasedMaterial  for convenience. 
```kotlin
fun UnlitMaterial.setBaseColor(color: Color)
```
Set compose color to  UnlitMaterial  for convenience. 
Spatial Model View 
```kotlin
@Composable
```fun  SpatialModelView ( source :  Source < * > ,  modifier :  Modifier  =  Modifier ,  resizability :  Resizability  =  Resizability.None ,  content :  @ Composable SpatialModelScope . ( state :  ModelLoadingState )  ->  Unit  =  { state ->
        if (state is ModelLoadingState.Success) {
            Model(state.model)
        }
    } ) 
A view that asynchronously loads and displays a 3D model from  source . 
```kotlin
@Composable
```fun  SpatialModelView ( source :  Source < * > ,  modifier :  Modifier  =  Modifier ,  resizability :  Resizability  =  Resizability.None ,  onLoad :  ( )  ->  Unit ?  =  null ,  onError :  ( String )  ->  Unit ?  =  null ,  onSuccess :  ( LoadedModel )  ->  Unit ?  =  null ,  content :  @ Composable SpatialModelScope . ( )  ->  Unit  =  {} ) 
A view that asynchronously loads and displays a 3D model from  source , while exposing the load lifecycle through callbacks. 
Spatial View 
```kotlin
@Composable
```fun  SpatialView ( modifier :  Modifier  =  Modifier ,  update :  ( content :  SpatialViewContent ,  attachments :  SpatialViewAttachments )  ->  Unit ?  =  null ,  attachments :  AttachmentPanelBuilder . ( )  ->  Unit ?  =  null ,  initial :  suspend  ( content :  SpatialViewContent ,  attachments :  SpatialViewAttachments )  ->  Unit ) 
The container for 3D content. 
to Color4 
```kotlin
fun Color.toColor4(): Color4
```
convert compose  Color  to ecs  Color4  for compose developers