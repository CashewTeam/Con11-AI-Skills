# PicoIndication | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / PicoIndication 
# PicoIndication
```kotlin
class PicoIndication(pressedColorProducer: () -> Color) : IndicationNodeFactory
```
Default state indication of PICO design. will draw a color behind content when pressed. Hover effect is support by spatialHoverEffect modifier. 
Members 
## Constructors
Pico Indication 
```kotlin
constructor(pressedColorProducer: () -> Color)
```
## Functions
create 
```kotlin
open override fun create(interactionSource: InteractionSource): DelegatableNode
```equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```