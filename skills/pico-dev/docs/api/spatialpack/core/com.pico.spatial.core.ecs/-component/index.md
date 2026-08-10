# Component | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Component 
# Component
```kotlin
@MainThread
```open  class  Component  :  JsonModel 
The representation of a  Component  in the ECS architecture. 
The  Component  is any struct of data. 
When extending this class to define a custom component, you must provide a default constructor. 
#### Inheritors
AmbientAudioComponent AnchorComponent AnimationResourceLibraryComponent AttachmentPanelComponent AudioMixerGroupsComponent AudioResourceLibraryComponent BlendShapeControllerComponent ChannelAudioComponent CollisionComponent DirectionalLightComponent DrawOrderGroupComponent EnvironmentLightingSettingsComponent GaussianSplattingComponent GroundShadowComponent HoverEffectComponent ImageBasedLightComponent ImageBasedLightReceiverComponent InteractableComponent LookAtComponent ModelComponent ObjectAudioComponent OpacityControllerComponent ParticleComponent PhysicsForceComponent PhysicsVelocityComponent PhysicsWorldComponent PointLightComponent PortalComponent PortalCrossableComponent PortalWorldComponent RigidBodyComponent SortAsUIElementComponent SpotLightComponent StageEnvironmentLightingComponent TransformComponent VideoComponent VideoPlayerComponent Members 
## Constructors
Component 
```kotlin
constructor()
```
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Component . 
## Functions
clone 
```kotlin
open fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```