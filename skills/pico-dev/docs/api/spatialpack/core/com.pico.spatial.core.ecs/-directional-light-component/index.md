# DirectionalLightComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / DirectionalLightComponent 
# DirectionalLightComponent
```kotlin
@MainThread
```class  DirectionalLightComponent  :  Component 
A  Component  that emits directional light along an entity's local forward (-Z) axis. 
This component creates light that behaves like a distant light source, where all light rays are parallel and the intensity does not diminish with distance, such as the sunlight. 
### Key Properties:
- 
Direction : Inherited from the entity's transform (uses -Z axis by convention). 
- 
Uniform illumination : Affects all objects in the scene equally. 
- 
Color  &  Intensity : Fully customizable light appearance with  color  and  intensity . 
- 
Shadow Casting : Configurable through  castsShadowEnabled  and related shadow properties. 
To receive lighting effects, the  Entity  must use a  Material  that supports lighting. For example,  PhysicallyBasedMaterial  respond to lighting, while  UnlitMaterial  does not. 
### Code sample:

```
val sunEntity = Entity().apply {    components.set(DirectionalLightComponent(        color = Color4(1f, 0.95f, 0.9f, 1f),        intensity = 2000f, // Measured in lux        castsShadowEnabled = true    ))    components[DirectionalLightComponent::class.java]!!.apply {        shadowDepthBias = 0.01f        shadowFaceCullingMode = ShadowFaceCullingMode.BACK        shadowProjectionType = ShadowProjectionType.Auto()    }}
```
Related components: 
- 
PointLightComponent  - For bulb-like omnidirectional lighting. 
- 
SpotLightComponent  - For directional cone lighting. 
Members 
## Constructors
Directional Light Component 
```kotlin
constructor(color: Color4, intensity: Float)
```
```kotlin
constructor(color: Color4, intensity: Float, castsShadowEnabled: Boolean)
```
## Properties
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
intensity 
```kotlin
var intensity: Float
```
The intensity of the light in lux, defined as luminous flux per unit area. One lux equals one lumen per square metre. 
shadow Depth Bias 
```kotlin
var shadowDepthBias: Float
```
The shadow depth bias of the light. 
shadow Face Culling Mode 
```kotlin
var shadowFaceCullingMode: ShadowFaceCullingMode
```
The shadow culling mode of the light. 
shadow Projection Type 
```kotlin
var shadowProjectionType: ShadowProjectionType
```
The shadow projection type of the light. 
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