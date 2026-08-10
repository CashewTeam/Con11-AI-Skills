# StepperIconStyle | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / StepperIconStyle 
# StepperIconStyle
```kotlin
sealed class StepperIconStyle
```
default icon style 
#### Inheritors
MinusAndAdd Arrow Members 
## Constructors
Stepper Icon Style 
```kotlin
protected constructor()
```
## Types
Arrow 
```kotlin
object Arrow : StepperIconStyle
```
arrow style 
Minus And Add 
```kotlin
object MinusAndAdd : StepperIconStyle
```
add minus style 
## Functions
icon Decrease 
```kotlin
abstract fun iconDecrease(): @Composable () -> Unit
```
iconDecrease 
icon Increase 
```kotlin
abstract fun iconIncrease(): @Composable () -> Unit
```
iconIncrease