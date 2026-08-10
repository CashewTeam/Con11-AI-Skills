# SpatialAudioEffectConfiguration | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / SpatialAudioEffectConfiguration 
# SpatialAudioEffectConfiguration
```kotlin
@Stable
```class  SpatialAudioEffectConfiguration ( val  opClickEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpClick ,  val  opDragBeginEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpDragBegin ,  val  opDragEndEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpDragEnd ,  val  opDragScaleEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpDragScale ,  val  opCloseEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpClose ,  val  opLongPressEffect :  SpatialSoundEffect  =  SpatialSoundEffect.OpLongPress ,  val  stateSelectEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateSelected ,  val  stateUnselectEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateUnselected ,  val  stateOnEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateOn ,  val  stateOffEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateOff ,  val  stateSuccessEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateSuccess ,  val  stateFailureEffect :  SpatialSoundEffect  =  SpatialSoundEffect.StateFailure ) 
Configuration for  SpatialAudioEffectPlayer . Provide default sound effect for each operation. 
Members 
## Constructors
Spatial Audio Effect Configuration 
```kotlin
constructor(opClickEffect: SpatialSoundEffect = SpatialSoundEffect.OpClick, opDragBeginEffect: SpatialSoundEffect = SpatialSoundEffect.OpDragBegin, opDragEndEffect: SpatialSoundEffect = SpatialSoundEffect.OpDragEnd, opDragScaleEffect: SpatialSoundEffect = SpatialSoundEffect.OpDragScale, opCloseEffect: SpatialSoundEffect = SpatialSoundEffect.OpClose, opLongPressEffect: SpatialSoundEffect = SpatialSoundEffect.OpLongPress, stateSelectEffect: SpatialSoundEffect = SpatialSoundEffect.StateSelected, stateUnselectEffect: SpatialSoundEffect = SpatialSoundEffect.StateUnselected, stateOnEffect: SpatialSoundEffect = SpatialSoundEffect.StateOn, stateOffEffect: SpatialSoundEffect = SpatialSoundEffect.StateOff, stateSuccessEffect: SpatialSoundEffect = SpatialSoundEffect.StateSuccess, stateFailureEffect: SpatialSoundEffect = SpatialSoundEffect.StateFailure)
```
## Types
Companion 
```kotlin
object Companion
```
the companion object of SpatialAudioEffectConfiguration 
## Properties
op Click Effect 
```kotlin
val opClickEffect: SpatialSoundEffect
```
click sound effect in configuration 
op Close Effect 
```kotlin
val opCloseEffect: SpatialSoundEffect
```
close sound effect in configuration 
op Drag Begin Effect 
```kotlin
val opDragBeginEffect: SpatialSoundEffect
```
drag begin sound effect in configuration 
op Drag End Effect 
```kotlin
val opDragEndEffect: SpatialSoundEffect
```
drag end sound effect in configuration 
op Drag Scale Effect 
```kotlin
val opDragScaleEffect: SpatialSoundEffect
```
drag scale sound effect in configuration 
op Long Press Effect 
```kotlin
val opLongPressEffect: SpatialSoundEffect
```
long press sound effect in configuration 
state Failure Effect 
```kotlin
val stateFailureEffect: SpatialSoundEffect
```
failure state sound effect in configuration 
state Off Effect 
```kotlin
val stateOffEffect: SpatialSoundEffect
```
off state sound effect in configuration 
state On Effect 
```kotlin
val stateOnEffect: SpatialSoundEffect
```
on state sound effect in configuration 
state Select Effect 
```kotlin
val stateSelectEffect: SpatialSoundEffect
```
select state sound effect in configuration 
state Success Effect 
```kotlin
val stateSuccessEffect: SpatialSoundEffect
```
success state sound effect in configuration 
state Unselect Effect 
```kotlin
val stateUnselectEffect: SpatialSoundEffect
```
unselect state sound effect in configuration 
## Functions
copy 
```kotlin
fun copy(opClickEffect: SpatialSoundEffect = this.opClickEffect, opDragBeginEffect: SpatialSoundEffect = this.opDragBeginEffect, opDragEndEffect: SpatialSoundEffect = this.opDragEndEffect, opDragScaleEffect: SpatialSoundEffect = this.opDragScaleEffect, opCloseEffect: SpatialSoundEffect = this.opCloseEffect, opLongPressEffect: SpatialSoundEffect = this.opLongPressEffect, stateSelectEffect: SpatialSoundEffect = this.stateSelectEffect, stateUnselectEffect: SpatialSoundEffect = this.stateUnselectEffect, stateOnEffect: SpatialSoundEffect = this.stateOnEffect, stateOffEffect: SpatialSoundEffect = this.stateOffEffect, stateSuccessEffect: SpatialSoundEffect = this.stateSuccessEffect, stateFailureEffect: SpatialSoundEffect = this.stateFailureEffect): SpatialAudioEffectConfiguration
```
Copy this configuration with new values. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```
override equals function 
hash Code 
```kotlin
open override fun hashCode(): Int
```
override hashCode function