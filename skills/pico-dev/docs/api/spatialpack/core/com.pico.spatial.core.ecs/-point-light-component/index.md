# PointLightComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PointLightComponent 
# PointLightComponent
```kotlin
@MainThread
```class  PointLightComponent  :  Component 
A  Component  that emits omnidirectional light from the entity's position. 
This component creates a light source that radiates equally in all directions (like a light bulb), with configurable properties for realistic lighting scenarios. 
### Key properties:
- 
Position-based : Light originates from the entity's world position. 
- 
Distance Attenuation : Light intensity falls off with distance based on  attenuationRadius . 
- 
Color  &  Intensity : Fully customizable light appearance with  color  and  intensity . 
- 
No Shadow Casting : Optimized for performance (see notes below). 
To receive lighting effects, the  Entity  must use a  Material  that supports lighting. For example,  PhysicallyBasedMaterial  respond to lighting, while  UnlitMaterial  does not. 
### Code sample:

```
val bulbEntity = Entity().apply {     components.set(TransformComponent().apply { setPosition(Vector3(0f, 2f, 0f)) })     components.set(PointLightComponent(         color = Color4(1f, 0.9f, 0.8f, 1f),         intensity = 1500f,      // Measured in lumens         attenuationRadius = 2f  // Measured in meters     ))}
```
### Performance notes:
- 
Multiple point lights impact rendering performance. 
- 
Larger  attenuationRadius  values increase shaded area complexity. 
- 
Consider using  SpotLightComponent  or  DirectionalLightComponent  for needs of shadows. 
### Related components:
- 
DirectionalLightComponent  - For sunlight-style parallel lighting. 
- 
SpotLightComponent  - For directional cone lighting. 
#### See also
Directional Light Component Spot Light Component Members 
## Constructors
Point Light Component 
```kotlin
constructor(color: Color4, intensity: Float, attenuationRadius: Float)
```
## Properties
attenuation Radius 
```kotlin
var attenuationRadius: Float
```
The attenuation radius of the light, measured in meters. 
color 
```kotlin
var color: Color4
```
The color of the light. 
intensity 
```kotlin
var intensity: Float
```
The intensity of the light, measured in lumen. 
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