# com.pico.spatial.core.ecs | PICO Spatial SDK

core / com.pico.spatial.core.ecs 
# Package-level declarations
Types 
## Types
Ambient Audio Component 
```kotlin
@MainThread
```class  AmbientAudioComponent  :  Component 
A  Component  used to create ambient audio effects in the scene, such as ambient sound effects, ambient music, and more. 
Anchor Component 
```kotlin
@MainThread
```class  AnchorComponent  :  Component 
The  Component  that defines a spatial anchoring relationship between entities and real-world objects. 
Anchor Entity 
```kotlin
class AnchorEntity @MainThread constructor(anchorTarget: AnchorTarget) : Entity
```
An entity extension that acts as an anchor, establishing and maintaining the pose of entities within a scene. 
Animation Resource Library Component 
```kotlin
@MainThread
```class  AnimationResourceLibraryComponent  :  Component 
AnimationResourceLibraryComponent is a component designed to manage animation resources. 
Attachment Panel Component 
```kotlin
class AttachmentPanelComponent(width: Int = WRAP_CONTENT, height: Int = WRAP_CONTENT, alignment: AttachmentPanelComponent.Alignment = Alignment.UNSPECIFIED) : Component
```
Component that attaches a 2D Android  View  to an  Entity  in spatial space. 
Audio Mixer Groups Component 
```kotlin
@MainThread
```class  AudioMixerGroupsComponent  :  Component 
A  Component  that manages audio mix groups for spatial audio processing. 
Audio Resource Library Component 
```kotlin
@MainThread
```class  AudioResourceLibraryComponent  :  Component 
A  Component  that manages audio resources as a key-value dictionary for organized audio playback. 
Blend Shape Controller Component 
```kotlin
@MainThread
```class  BlendShapeControllerComponent  :  Component 
Provides BlendShape (morph target) weight control for an Entity's model, with optional subset workflows for managing groups of BlendShapes. 
Bounding Box 
```kotlin
class BoundingBox
```
Represents the bounding box for 3D content. All measurements are expressed in meters (m). 
Channel Audio Component 
```kotlin
@MainThread
```class  ChannelAudioComponent  :  Component 
A  Component  that can be added to an entity to enable channel audio effects. 
Collision Component 
```kotlin
@MainThread
```class  CollisionComponent  :  Component 
A  Component  responsible for managing collision settings and operations, including collision detection and response. 
Component 
```kotlin
@MainThread
```open  class  Component  :  JsonModel 
The representation of a  Component  in the ECS architecture. 
Directional Light Component 
```kotlin
@MainThread
```class  DirectionalLightComponent  :  Component 
A  Component  that emits directional light along an entity's local forward (-Z) axis. 
Draw Order Group 
```kotlin
@MainThread
```class  DrawOrderGroup 
The identifier that defines a specific draw order group for rendering management. 
Draw Order Group Component 
```kotlin
@MainThread
```class  DrawOrderGroupComponent  :  Component 
The  Component  that defines a draw order group for  ModelComponent  and  ParticleComponent . 
Entity 
```kotlin
open class Entity : EventSource, SpatialCoordinateSpace
```
The base class for all entities in a scene. 
Entity Query Condition 
```kotlin
class EntityQueryCondition
```
Encapsulates conditions for querying entities. It allows checking whether an entity meets a specific condition through a condition function. 
Environment Lighting Settings Component 
```kotlin
@MainThread
```class  EnvironmentLightingSettingsComponent  :  Component 
Configures the intensity scale for environment image-based lighting (IBL). 
Event Source 
```kotlin
sealed class EventSource
```
The base class for defining sources of events. 
Extra Component Data Syncer 
```kotlin
typealias ExtraComponentDataSyncer = (ComponentType, Entity) -> Component?
```Gaussian Splatting Component 
```kotlin
@MainThread
```class  GaussianSplattingComponent  :  Component 
A  Component  that binds a  GaussianSplattingResource  to an entity for Gaussian splatting rendering. 
Ground Shadow Component 
```kotlin
@MainThread
```class  GroundShadowComponent  :  Component 
A  Component  that adds a ground shadow to the entity. 
Hover Effect Component 
```kotlin
@MainThread
```class  HoverEffectComponent  :  Component 
A  Component  that apply visual effect when user interacts with it. 
Image Based Light Component 
```kotlin
@MainThread
```class  ImageBasedLightComponent  :  Component 
A  Component  that provides localized image-based lighting (IBL) for entities with an  ImageBasedLightReceiverComponent . 
Image Based Light Receiver Component 
```kotlin
@MainThread
```class  ImageBasedLightReceiverComponent  :  Component 
A  Component  that enables an entity to receive image-based lighting (IBL) from the source entity having an  ImageBasedLightComponent . 
Image Based Light Source 
```kotlin
sealed class ImageBasedLightSource
```
Defines the source textures for image-based lighting (IBL) in a scene. 
Interactable Component 
```kotlin
@MainThread
```class  InteractableComponent  :  Component 
The  Component  that marks an entity as interactable, allowing it to receive and process input events. 
Load Type 
```kotlin
enum LoadType : Enum<LoadType>
```
Enum representing different ways of loading data. 
Look At Component 
```kotlin
@MainThread
```class  LookAtComponent  :  Component 
A  Component  that controls the "look at" behavior of entities in 3D space, allowing entities to face specific targets (such as viewers or other entities) and providing control over alignment methods and forward direction. 
Look At Forward Direction 
```kotlin
enum LookAtForwardDirection : Enum<LookAtForwardDirection>
```
Enumeration defining possible forward direction axes for the  LookAtComponent  in 3D spatial simulation. Specifies which axis an entity should use as its forward direction when implementing "look at" behavior. 
Look At Target Type 
```kotlin
enum LookAtTargetType : Enum<LookAtTargetType>
```
Enumeration defining target types for the  LookAtComponent  in 3D spatial simulation. Specifies what an entity should face when implementing "look at" behavior. 
Model Component 
```kotlin
@MainThread
```class  ModelComponent  :  Component 
A  Component  that renders 3D models. 
Model Entity 
```kotlin
class ModelEntity : Entity
```
A class for rendering a model with specified mesh and materials. 
Model Format 
```kotlin
enum ModelFormat : Enum<ModelFormat>
```
Represents supported 3D model formats. 
Object Audio Component 
```kotlin
@MainThread
```class  ObjectAudioComponent  :  Component 
A  Component  used to create spatial audio effects in the scene, such as spatial sound effects, spatial music, and so on. 
Opacity Controller Component 
```kotlin
@MainThread
```class  OpacityControllerComponent ( @ FloatRange ( from  =  0.0 ,  to  =  1.0 ) opacity :  Float  =  1.0f )  :  Component 
A Component that controls the opacity of an entity and its descendants. 
Particle Component 
```kotlin
@MainThread
```class  ParticleComponent  :  Component 
A  Component  that is used to play particle effects in the scene. 
Physics Force Component 
```kotlin
@MainThread
```class  PhysicsForceComponent  :  Component 
A  Component  that applies constant force or torque (in local coordinate space) to drive physics-based motion on an entity. Force is measured in newtons (N). Torque is measured in newton-meters (N·m). 
Physics Velocity Component 
```kotlin
@MainThread
```class  PhysicsVelocityComponent  :  Component 
A  Component  that directly sets an entity’s linear and angular velocities. 
Physics World Component 
```kotlin
@MainThread
```class  PhysicsWorldComponent  :  Component 
A  Component  that creates a new physics world for the entity and allows manipulation of physics simulation parameters including gravity,  KinematicCollisionReportMode ,  SolverIterations , and  SimulationClock . 
Point Light Component 
```kotlin
@MainThread
```class  PointLightComponent  :  Component 
A  Component  that emits omnidirectional light from the entity's position. 
Portal Component 
```kotlin
@MainThread
```class  PortalComponent  :  Component 
A  Component  that enables entity surfaces to act as portals to a target world (the targetEntity EC tree) and should be used in conjunction with PortalMaterial. 
Portal Crossable Component 
```kotlin
@MainThread
```class  PortalCrossableComponent  :  Component 
A  Component  that enables an entity (in the target world) and its descendants to traverse through a portal. This component should be utilized with  PortalComponent ,  PortalWorldComponent , and  PortalMaterial . 
Portal World Component 
```kotlin
@MainThread
```class  PortalWorldComponent  :  Component 
A  Component  that transforms an entity and its descendants into a separate world, visible only through a portal. This component should be used with  PortalComponent ,  PortalCrossableComponent , and  PortalMaterial . 
Rigid Body Component 
```kotlin
@MainThread
```class  RigidBodyComponent  :  Component 
A  Component  responsible for defining the properties of the rigid body, including its  RigidBodyMode ,  MassProperties ,  CollisionDetectionMode , linear and angular damping, gravity influence, and constraints on translation or rotation in specific directions. 
Scene 
```kotlin
class Scene : EventSource
```
Represents a scene. 
Scene Update Context 
```kotlin
class SceneUpdateContext
```
The context used to update scene. 
Sort As UIElement Component 
```kotlin
@MainThread
```class  SortAsUIElementComponent  :  Component 
Marks a 3D renderable to be sorted as a UI element. 
Spatial Coordinate Space 
```kotlin
sealed interface SpatialCoordinateSpace
```
Coordinate space for spatial objects. Describes a scene in the SpatialView using the right-handed coordinate system, with the origin described by the  origin  entity. 
Spot Light Component 
```kotlin
@MainThread
```class  SpotLightComponent  :  Component 
A  Component  that emits conical light along the entity's forward (-Z) axis. 
Stage Environment Lighting Component 
```kotlin
@MainThread
```class  StageEnvironmentLightingComponent  :  Component 
A  Component  that provides image-based environment lighting. 
System 
```kotlin
abstract class System
```
Represents a system in the Entity-Component-System (ECS) architecture. 
Transform Component 
```kotlin
@MainThread
```class  TransformComponent  :  Component 
A  Component  that manipulates the scale, rotation, and position of the entity. 
Video Component 
```kotlin
@MainThread
```class  VideoComponent  :  Component 
A  Component  that can be constructed using a provided  VideoMaterial  and  MeshResource . With the given parameters, this component can be used to render a 3D video. 
Video Player Component 
```kotlin
@MainThread
```class  VideoPlayerComponent  :  Component 
A  Component  that can be constructed with  CypressMediaPlayer ,  VideoMaterial , and  MeshResource , allowing you to render a 3D video. 
View Coordinate Space 
```kotlin
sealed interface ViewCoordinateSpace
```
Coordinate space for views, including the SpatialUI View, Standard Android View.