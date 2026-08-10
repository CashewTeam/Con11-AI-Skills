# ImageBasedLightComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ImageBasedLightComponent 
# ImageBasedLightComponent
```kotlin
@MainThread
```class  ImageBasedLightComponent  :  Component 
A  Component  that provides localized image-based lighting (IBL) for entities with an  ImageBasedLightReceiverComponent . 
This component creates lighting effects for specific objects with the following features: 
- 
Realistic environment lighting effects: Use HDR environment cubemaps (only support  .ktx  file currently) as light sources. 
- 
Targeted illumination: Only affects entities with  ImageBasedLightReceiverComponent . 
- 
Dynamic Control: Adjust rotation, intensity and source textures at runtime. 
Members 
## Constructors
Image Based Light Component 
```kotlin
constructor(source: ImageBasedLightSource, @FloatRange(from = -24.0, to = 24.0) intensityExponent: Float)
```
```kotlin
constructor(source: ImageBasedLightSource, @FloatRange(from = -24.0, to = 24.0) intensityExponent: Float, rotation: Quat)
```
## Properties
intensity Exponent 
```kotlin
var intensityExponent: Float
```
The intensity exponent of the current image-based lighting. The intensity is 2^intensityExponent. 
rotation 
```kotlin
var rotation: Quat
```
The rotation of the current image-based lighting. 
source 
```kotlin
var source: ImageBasedLightSource
```
The source of the current image-based lighting. 
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