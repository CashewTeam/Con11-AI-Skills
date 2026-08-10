# StageImmersionManager | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / StageImmersionManager 
# StageImmersionManager
```kotlin
interface StageImmersionManager
```
The  StageImmersionManager  is responsible for provider and listen the immersion level of a progressive Stage. 
Members 
## Properties
current Immersion Level 
```kotlin
abstract val currentImmersionLevel: IntState
```
The current immersion level of the Stage. 
immersion Max Level 
```kotlin
abstract val immersionMaxLevel: Int
```
The maximum immersion level of the Stage. 
immersion Min Level 
```kotlin
abstract val immersionMinLevel: Int
```
The minimum immersion level of the Stage. 
## Functions
add Immersion Listener 
```kotlin
abstract fun addImmersionListener(listener: StageImmersionListener)
```
Add a  StageImmersionListener  to the  StageImmersionManager . 
remove Immersion Listener 
```kotlin
abstract fun removeImmersionListener(listener: StageImmersionListener)
```
Remove a  StageImmersionListener  from the  StageImmersionManager .