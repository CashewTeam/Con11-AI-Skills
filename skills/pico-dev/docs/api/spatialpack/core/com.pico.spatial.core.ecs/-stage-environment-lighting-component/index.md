# StageEnvironmentLightingComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / StageEnvironmentLightingComponent 
# StageEnvironmentLightingComponent
```kotlin
@MainThread
```class  StageEnvironmentLightingComponent  :  Component 
A  Component  that provides image-based environment lighting. 
This component utilizes environment maps to simulate realistic lighting conditions for the entire scene. It contributes to diffuse lighting, specular reflections, and ambient occlusion for objects using Physically Based Rendering (PBR) materials. 
The behavior of this component varies depending on the current  StageStyle : 
- 
In  StageStyle.FULL , it provides the complete environmental lighting that defines the virtual world's atmosphere. 
- 
In  StageStyle.MIXED , the stage environment lighting is inactive, as the system's image-based lighting (IBL) derived from the real-world environment takes precedence to ensure consistent visual integration. 
- 
In  StageStyle.PROGRESSIVE , the lighting is a blend of the stage environment lighting and the system IBL, with the blend ratio determined by the current immersion level. 
Members 
## Constructors
Stage Environment Lighting Component 
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
The intensity exponent for the current image-based lighting. The intensity is 2^intensityExponent. 
rotation 
```kotlin
var rotation: Quat
```
The rotation of image-based lighting. 
source 
```kotlin
var source: ImageBasedLightSource
```
The source of image-based lighting. 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a new instance of the current object. 
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