# SpotLightComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / SpotLightComponent 
# SpotLightComponent
```kotlin
@MainThread
```class  SpotLightComponent  :  Component 
A  Component  that emits conical light along the entity's forward (-Z) axis. 
This component creates a directional light source with controllable spread (like a flashlight or stage spotlight), supporting advanced features including light color and intensity, shadow casting and clipping plane configuration. 
### Key properties:
- 
Direction : Inherited from entity's transform (uses -Z axis). 
- 
Color  &  Intensity : Fully customizable light appearance with  color  and  intensity . 
- 
Angular Falloff : Controlled via  innerAngle  (full intensity) and  outerAngle  (falloff edge). 
- 
Distance Attenuation : Light intensity diminishes over  attenuationRadius . 
- 
Shadow Casting : Configurable through  castsShadowEnabled  and related shadow properties. 
To receive lighting effects, the  Entity  must use a  Material  that supports lighting. For example,  PhysicallyBasedMaterial  respond to lighting, while  UnlitMaterial  does not. 
### Angular behavior:
- 
Light is at full intensity within  innerAngle  cone. 
- 
Smoothly falls to zero between  innerAngle  and  outerAngle . 
- 
No light emitted beyond  outerAngle . 
### Code sample:

```
val spotlightEntity = Entity().apply{    components.set(SpotLightComponent(        color = Color4(1f, 0.95f, 0.9f, 1f),        intensity = 10000f,         // Measured in lumens        attenuationRadius = 10f,    // Measured in meters        innerAngle = 15f,           // Measured in degrees        outerAngle = 30f,           // Measured in degrees        castsShadowEnabled = true,   ))    components[SpotLightComponent::class.java]!!.apply {        shadowFaceCullingMode = ShadowFaceCullingMode.BACK        shadowClippingPlaneType = ShadowClippingPlaneType.Auto    }}
```
### Performance Notes:
- 
Shadow casting impacts rendering performance. 
- 
Wider angles ( outerAngle ) increase shaded area complexity. 
- 
Multiple active spotlights require careful optimization. 
### Related components:
- 
PointLightComponent  - For bulb-like omnidirectional lighting. 
- 
DirectionalLightComponent  - For sunlight-style parallel lighting. 
Members 
## Constructors
Spot Light Component 
```kotlin
constructor(color: Color4, intensity: Float, attenuationRadius: Float, innerAngle: Float, outerAngle: Float)
```
```kotlin
constructor(color: Color4, intensity: Float, attenuationRadius: Float, innerAngle: Float, outerAngle: Float, castsShadowEnabled: Boolean)
```
## Properties
attenuation Radius 
```kotlin
var attenuationRadius: Float
```
The radius of the light's attenuation. 
casts Shadow Enabled 
```kotlin
var castsShadowEnabled: Boolean
```
Whether the light casts shadow. 
color 
```kotlin
var color: Color4
```
The color of the light. 
inner Angle 
```kotlin
var innerAngle: Float
```
The inner cone angle of the spotlight, measured in degrees. 
intensity 
```kotlin
var intensity: Float
```
The intensity of the light, measured in lumen. 
outer Angle 
```kotlin
var outerAngle: Float
```
The outer angle of the spotlight, measured in degrees. 
shadow Clipping Plane Type 
```kotlin
var shadowClippingPlaneType: ShadowClippingPlaneType
```
The shadow clipping plane type of the light. 
shadow Face Culling Mode 
```kotlin
var shadowFaceCullingMode: ShadowFaceCullingMode
```
The culling behavior for shadow rendering. 
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