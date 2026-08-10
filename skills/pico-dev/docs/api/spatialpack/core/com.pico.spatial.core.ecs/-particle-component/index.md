# ParticleComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ParticleComponent 
# ParticleComponent
```kotlin
@MainThread
```class  ParticleComponent  :  Component 
A  Component  that is used to play particle effects in the scene. 
Particle effects, such as fireworks, explosions, and other visual effects, can be created in the Spatial Editor. When a node containing particle effects is loaded from an  AssetBundle , its corresponding entity will automatically have a  ParticleComponent  added to it. 
At runtime, you can modify the exposed properties of an existing  ParticleComponent , but cannot create new instances. Neither copy construction nor manual instantiation is supported. 
Members 
## Properties
attractor Strength 
```kotlin
var attractorStrength: Float
```
The strength of the attractor effect. Only available when  isAttractorEnabled  is  true . 
is Attractor Enabled 
```kotlin
var isAttractorEnabled: Boolean
```
Whether the attractor effect is enabled. 
is Emitting 
```kotlin
var isEmitting: Boolean
```
Whether the emitter is emitting. This property is used to activate or deactivate the emitting of particles. 
is Vortex Enabled 
```kotlin
var isVortexEnabled: Boolean
```
Whether the vortex effect is enabled. 
start Color 
```kotlin
var startColor: ParticleColorVaryingProperty
```
The initial color of particles at spawn. 
vortex Strength 
```kotlin
var vortexStrength: Float
```
The strength of the vortex effect. Only available when  isVortexEnabled  is  true . 
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