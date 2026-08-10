# com.pico.spatial.ui.platform | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform 
# Package-level declarations
Types Functions Properties 
## Types
Controller Haptic Configuration 
```kotlin
@Stable
```class  ControllerHapticConfiguration ( val  hover :  HandControllerHapticType  =  HandControllerHapticType.Hover ,  val  press :  HandControllerHapticType  =  HandControllerHapticType.Press ,  val  step :  HandControllerHapticType  =  HandControllerHapticType.Step ,  val  none :  HandControllerHapticType  =  HandControllerHapticType.None ) 
hand controller haptic configuration, provide 
Hand Controller 
```kotlin
enum HandController : Enum<HandController>
```
hand controller type in Pico OS, provide 
Hand Controller Haptic Type 
```kotlin
@Stable
```class  HandControllerHapticType ( level :  Int ,  frequency :  Int ,  duration :  Int ) 
hand controller haptic type, provide default haptic type 
Length Unit 
```kotlin
enum LengthUnit : Enum<LengthUnit>
```
the type of physical lengthUnit 
Local Physical Length Converter 
```kotlin
object LocalPhysicalLengthConverter
```
The LocalPhysicalLengthConverter for convert between physicalLength and Dp 
Material 
```kotlin
enum Material : Enum<Material>
```
Material in PICO design system is made up of two colors with blend mode. 
Physical Length Converter 
```kotlin
interface PhysicalLengthConverter : Density
```
Interface for converting length between physical lengthUnit and Dp 
Scaled Type 
```kotlin
enum ScaledType : Enum<ScaledType>
```
the type of Scale 
Spatial Audio Effect Configuration 
```kotlin
@Stable
```class  SpatialAudioEffectConfiguration ( val  opClickEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpClick ,  val  opDragBeginEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpDragBegin ,  val  opDragEndEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpDragEnd ,  val  opDragScaleEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpDragScale ,  val  opCloseEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpClose ,  val  opLongPressEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpLongPress ,  val  stateSelectEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateSelected ,  val  stateUnselectEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateUnselected ,  val  stateOnEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateOn ,  val  stateOffEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateOff ,  val  stateSuccessEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateSuccess ,  val  stateFailureEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateFailure ) 
Configuration for  SpatialAudioEffectPlayer . Provide default sound effect for each operation. 
Spatial Audio Effect Player 
```kotlin
interface SpatialAudioEffectPlayer
```
Player for spatial audio effects. we will provider the default implementation. callers should use  LocalAudioEffectPlayer  to get the instance. 
Spatial Hand Controller Haptic 
```kotlin
interface SpatialHandControllerHaptic
```
hand controller haptic interface, provide feedback for hand controller haptic when user interact with hand controller, such as press, hover, step, etc. 
Spatial Sound Effect 
```kotlin
enum SpatialSoundEffect : Enum<SpatialSoundEffect>
```
Spatial sound effects. Current supported effects in PICO OS 
Stage Immersion Listener 
```kotlin
interface StageImmersionListener
```
The  StageImmersionListener  is responsible for listening the immersion level of a progressive Stage. 
Stage Immersion Manager 
```kotlin
interface StageImmersionManager
```
The  StageImmersionManager  is responsible for provider and listen the immersion level of a progressive Stage. 
Stage Upper Limb Render Model Manager 
```kotlin
interface StageUpperLimbRenderModelManager
```
Manager for upper limb render model of stage. 
View Point 
```kotlin
enum ViewPoint : Enum<ViewPoint>
```
The ViewPoint enum. 
Volume View Point Listener 
```kotlin
interface VolumeViewPointListener
```
The  VolumeViewPointListener  interface. 
Volume View Point Manager 
```kotlin
interface VolumeViewPointManager
```
The interface of volume View Point. when you register a  VolumeViewPointListener  to the  VolumeViewPointManager , the  VolumeViewPointListener  will be called when the viewpoint of the container changes. 
## Properties
Centimeter2Meter 
```kotlin
const val Centimeter2Meter: Float = 0.01f
```
centimeter to meter 
centimeters 
```kotlin
@Stable
```@get: Composable val  Double . centimeters :  Dp 
Double centimeters that equivalent in Dp 
```kotlin
@Stable
```@get: Composable val  Float . centimeters :  Dp 
Float centimeters that equivalent in Dp 
```kotlin
@Stable
```@get: Composable val  Int . centimeters :  Dp 
Int centimeters that equivalent in Dp 
centimeters2Meters 
```kotlin
@Stable
```val  Float . centimeters2Meters :  Float 
Convert size from centimeters to meters 
centimeters To Dp 
```kotlin
@Stable
```@get: Composable val  Float . centimetersToDp :  Dp 
Convert centimeters to Dp 
Local Controller Haptic Configuration 
```kotlin
val LocalControllerHapticConfiguration: ProvidableCompositionLocal<ControllerHapticConfiguration>
```
local hand controller haptic configuration 
Local Hand Controller Haptic 
```kotlin
val LocalHandControllerHaptic: ProvidableCompositionLocal<SpatialHandControllerHaptic>
```
The CompositionLocal containing the current  SpatialHandControllerHaptic . 
Local Is Material Background Enabled 
```kotlin
val LocalIsMaterialBackgroundEnabled: ProvidableCompositionLocal<Boolean>
```
Whether the Window (e.g WindowContainer's main window , dialog , popup) has a material background. 
Local Spatial Audio Effect Configuration 
```kotlin
val LocalSpatialAudioEffectConfiguration: ProvidableCompositionLocal<SpatialAudioEffectConfiguration>
```
Local composition value for  SpatialAudioEffectConfiguration . 
Local Spatial Container State Manager 
```kotlin
val LocalSpatialContainerStateManager: ProvidableCompositionLocal<SpatialContainerStateManager>
```
The CompositionLocal containing the  SpatialContainerStateManagerImpl  of current  com.pico.spatial.core.container.SpatialContainer . 
Local Spatial Container State Owner 
```kotlin
val LocalSpatialContainerStateOwner: ProvidableCompositionLocal<SpatialContainerStateOwner>
```
The CompositionLocal containing the current  SpatialContainerStateOwner . 
Local Stage Immersion Manager 
```kotlin
val LocalStageImmersionManager: ProvidableCompositionLocal<StageImmersionManager>
```
The CompositionLocal containing the current StageProgressiveImmersion. 
Local Stage Upper Limb Render Model Manager 
```kotlin
val LocalStageUpperLimbRenderModelManager: ProvidableCompositionLocal<StageUpperLimbRenderModelManager>
```
The CompositionLocal containing the current  StageUpperLimbRenderModelManager . 
Local Volume View Point Manager 
```kotlin
val LocalVolumeViewPointManager: ProvidableCompositionLocal<VolumeViewPointManager>
```
The CompositionLocal containing the current LocalSpatialViewPointManager. 
meters 
```kotlin
@Stable
```@get: Composable val  Double . meters :  Dp 
Double meters that equivalent in Dp 
```kotlin
@Stable
```@get: Composable val  Float . meters :  Dp 
Float meters that equivalent in Dp 
```kotlin
@Stable
```@get: Composable val  Int . meters :  Dp 
Integer meters that equivalent in Dp 
meters2Centimeters 
```kotlin
@Stable
```val  Float . meters2Centimeters :  Float 
Convert size from meters to centimeters 
meters To Dp 
```kotlin
@Stable
```@get: Composable val  Float . metersToDp :  Dp 
Convert meters to Dp 
to Centimeters 
```kotlin
@Stable
```@get: Composable val  Dp . toCentimeters :  Float 
Convert Dp to centimeters 
to Meters 
```kotlin
@Stable
```@get: Composable val  Dp . toMeters :  Float 
Convert Dp to meters 
## Functions
convert From Meters 
```kotlin
fun Float.convertFromMeters(toUnit: LengthUnit): Float
```
Convert to the  LengthUnit  value from a  LengthUnit.Meters  value. 
convert To Meters 
```kotlin
fun Float.convertToMeters(fromUnit: LengthUnit): Float
```
Convert to a  LengthUnit.Meters  value from the  LengthUnit  value. 
Provide Physical Length Converter 
```kotlin
@Composable
```fun  ProvidePhysicalLengthConverter ( scaledType :  ScaledType ,  content :  @ Composable ( )  ->  Unit ) 
ProvidePhysicalLengthConverter  binds values to  LocalPhysicalLengthConverter 's Reading the  LocalPhysicalLengthConverter  using  LocalPhysicalLengthConverter.current 
Spatial Locals For Preview 
```kotlin
@Composable
```fun  SpatialLocalsForPreview ( content :  @ Composable ( )  ->  Unit ) 
A helper to provides some default impl of PICO OS specific CompositionLocal for @Preview functions  DO NOT USE THIS FUNCTION IN PRODUCTION . 
to Hand Controller 
```kotlin
fun InteractionKindExtra.toHandController(): HandController
```
Converts this  InteractionKindExtra  to the corresponding  HandController .