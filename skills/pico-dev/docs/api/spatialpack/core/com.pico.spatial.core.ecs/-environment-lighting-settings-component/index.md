# EnvironmentLightingSettingsComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / EnvironmentLightingSettingsComponent 
# EnvironmentLightingSettingsComponent
```kotlin
@MainThread
```class  EnvironmentLightingSettingsComponent  :  Component 
Configures the intensity scale for environment image-based lighting (IBL). 
Members 
## Constructors
Environment Lighting Settings Component 
```kotlin
constructor(@FloatRange(from = 0.0) scale: Float)
```
## Properties
scale 
```kotlin
var scale: Float
```
Scale factor for environment IBL intensity. 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```