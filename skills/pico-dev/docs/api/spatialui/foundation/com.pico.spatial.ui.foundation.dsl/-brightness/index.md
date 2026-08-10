# Brightness | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / Brightness 
# Brightness
```kotlin
@Stable
```sealed  class  Brightness 
Presents  Stage 's brightness 
#### Inheritors
Automatic Bright Dim Dark Members 
## Constructors
Brightness 
```kotlin
protected constructor()
```
## Types
Automatic 
```kotlin
data object Automatic : Brightness
```
The brightness is system default 
Bright 
```kotlin
data object Bright : Brightness
```
The brightness is bright 
Dark 
```kotlin
data object Dark : Brightness
```
The brightness is dark 
Dim 
```kotlin
data object Dim : Brightness
```
The brightness is dim 
## Properties
value 
```kotlin
@get:FloatRange(from = 0.0, to = 1.0)
```abstract  val  value :  Float 
The value of the brightness