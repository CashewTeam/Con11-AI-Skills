# Entity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity 
# Entity
```kotlin
open class Entity : EventSource, SpatialCoordinateSpace
```
The base class for all entities in a scene. 
An  Entity  represents a distinct element within a scene. 
Note: 
- 
Each entity automatically has a  TransformComponent  added upon creation. 
- 
Multiple  Component s can be attached to an entity, but only one instance per component type. That is, an entity cannot have two components of the same type. 
- 
Components collectively define the properties and behavior of the entity within the scene. 
#### Inheritors
AnchorEntity ModelEntity Members 
## Constructors
Entity 
```kotlin
@MainThread
```constructor ( ) 
The default constructor for  Entity . 
## Types
Clone Options 
```kotlin
class CloneOptions(val recursive: Boolean = false, val shouldShareMaterialInstance: Boolean = false)
```
Represents options for cloning operations. 
Companion 
```kotlin
object Companion
```
The companion object of  Entity . 
Component Set 
```kotlin
class ComponentSet : Collection<Component>
```
A set of stored components. The set represents all the components stored on an  Entity . Each  Entity  can hold only one  Component  of any given type. 
## Properties
components 
```kotlin
val components: Entity.ComponentSet
```
A set of components that have been added to this entity. 
enabled 
```kotlin
@get:JvmName(name = "isEnabled")
```@get: MainThread @set: MainThread var  enabled :  Boolean 
Gets or sets the current entity's enabled state. The default enabled state is  true . 
id 
```kotlin
val id: Long
```
The unique ID of the entity. 
scene 
```kotlin
@Volatile
```var  scene :  Scene ? 
The  Scene  to which this entity belongs. 
valid 
```kotlin
@get:JvmName(name = "isValid")
```@get: MainThread val  valid :  Boolean 
Indicates whether the current Entity is valid (i.e., not destroyed). 
## Functions
add Child 
```kotlin
@MainThread
```fun  addChild ( entity :  Entity ) :  Boolean 
Adds a child entity to the current entity instance. 
clone 
```kotlin
@MainThread
```fun  clone ( cloneOptions :  Entity.CloneOptions  =  CloneOptions() ) :  Entity ? 
Creates and returns a copy of this entity based on the specified cloning options. 
convert Position From 
```kotlin
@MainThread
```fun  convertPositionFrom ( position :  Vector3 ,  baseEntity :  Entity ? ) :  Vector3 
Converts a position relative to a  baseEntity  to the current entity. 
convert Position To 
```kotlin
@MainThread
```fun  convertPositionTo ( position :  Vector3 ,  targetEntity :  Entity ? ) :  Vector3 
Converts a position relative to the current entity to a  targetEntity . 
convert Rotation From 
```kotlin
@MainThread
```fun  convertRotationFrom ( rotation :  Quat ,  baseEntity :  Entity ? ) :  Quat 
Converts a rotation relative to a  baseEntity  to the current entity. 
convert Rotation To 
```kotlin
@MainThread
```fun  convertRotationTo ( rotation :  Quat ,  targetEntity :  Entity ? ) :  Quat 
Converts a rotation relative to the current entity to a  targetEntity . 
convert Scale From 
```kotlin
@MainThread
```fun  convertScaleFrom ( scale :  Vector3 ,  baseEntity :  Entity ? ) :  Vector3 
Converts a scale relative to a  baseEntity  to the current entity. 
convert Scale To 
```kotlin
@MainThread
```fun  convertScaleTo ( scale :  Vector3 ,  targetEntity :  Entity ? ) :  Vector3 
Converts a scale relative to the current entity to a  targetEntity . 
convert Transform From 
```kotlin
@MainThread
```fun  convertTransformFrom ( transform :  Transform ,  baseEntity :  Entity ? ) :  Transform 
Converts a  Transform  relative to a  baseEntity  to the current entity. 
convert Transform To 
```kotlin
@MainThread
```fun  convertTransformTo ( transform :  Transform ,  targetEntity :  Entity ? ) :  Transform 
Converts a  Transform  relative to the current entity to a  targetEntity . 
destroy 
```kotlin
@MainThread
```fun  destroy ( recursively :  Boolean  =  true ) :  Boolean 
Destroys this entity and, by default, all its children recursively. 
find Entity 
```kotlin
@MainThread
```fun  findEntity ( name :  String ) :  Entity ? 
Searches for an entity by its name within the entire depth of its tree structure, including the entity itself. If there are multiple entities with the same name, only the first matching entity encountered will be returned. 
find Skinned Mesh Entity 
```kotlin
@MainThread
```fun  findSkinnedMeshEntity ( includeDisabled :  Boolean  =  false ) :  Array < Entity > 
Finds all entities with a skinned mesh component within this entity and its children. The search traverses the entire entity hierarchy starting from the current entity. 
get Animation Resources 
```kotlin
@MainThread
```fun  getAnimationResources ( ) :  Array < AnimationResource > 
Gets the animation resources associated with the current entity. 
get Children 
```kotlin
@MainThread
```fun  getChildren ( ) :  Array < Entity > 
Gets all child entities of the current entity. 
get Children Count 
```kotlin
@MainThread
```fun  getChildrenCount ( ) :  Int 
Gets the number of child entities of the current entity. 
get Name 
```kotlin
@MainThread
```fun  getName ( ) :  String 
Gets the name of the current entity. 
get Parent 
```kotlin
@MainThread
```fun  getParent ( ) :  Entity ? 
Gets the parent entity of the current entity. 
get UUID 
```kotlin
@MainThread
```fun  getUUID ( ) :  Long 
Retrieves the globally unique identifier (UUID) of this entity. 
get Visual Bounds 
```kotlin
@MainThread
```fun  getVisualBounds ( relativeTo :  Entity ? ,  recursive :  Boolean  =  true ,  enabledOnly :  Boolean  =  false ) :  BoundingBox 
Computes a bounding box for the entity in the specified space, optionally including child entities. 
has Child 
```kotlin
@MainThread
```fun  hasChild ( ) :  Boolean 
Checks if the current entity has any child entities. 
has Parent 
```kotlin
@MainThread
```fun  hasParent ( ) :  Boolean 
Checks if the current entity has a parent entity. 
is Child 
```kotlin
@MainThread
```fun  isChild ( child :  Entity ) :  Boolean 
Checks if the specified entity is a child of the current entity. 
is Parent 
```kotlin
@MainThread
```fun  isParent ( parent :  Entity ) :  Boolean 
Checks if the specified entity is the parent of the current entity. 
play Animation 
```kotlin
@MainThread
```fun  playAnimation ( animationResource :  AnimationResource ,  config :  AnimationPlayConfig  =  AnimationPlayConfig() ) :  AnimationPlaybackController 
Uses the current entity to play an animation resource. 
play Audio 
```kotlin
@MainThread
```fun  playAudio ( audioResource :  AudioAsset ) :  AudioPlayerController 
Plays the specified audio attached to the entity and returns a controller to manage audio playback. 
play Audio Stream 
```kotlin
@MainThread
```fun  playAudioStream ( config :  AudioStreamConfig ,  callback :  AudioStreamDataCallback ?  =  null ) :  AudioStreamPlayerController 
Immediately starts playing an audio stream with the specified configuration. 
play Timeline 
```kotlin
@MainThread
```fun  playTimeline ( ) :  TimelinePlayerController 
Plays a preloaded Timeline using the current entity. 
prepare Audio 
```kotlin
@MainThread
```fun  prepareAudio ( audioResource :  AudioAsset ) :  AudioPlayerController 
Prepares the specified audio attached to the entity and returns a controller to manage audio playback. 
prepare Audio Stream 
```kotlin
@MainThread
```fun  prepareAudioStream ( config :  AudioStreamConfig ,  callback :  AudioStreamDataCallback ?  =  null ) :  AudioStreamPlayerController 
Prepares an audio stream for low-latency playback with specified configuration. 
remove All Children 
```kotlin
@MainThread
```fun  removeAllChildren ( ) :  Boolean 
Removes all child entities from the current entity. 
remove Child 
```kotlin
@MainThread
```fun  removeChild ( child :  Entity ) :  Boolean 
Removes a child entity from the current entity. 
remove From Parent 
```kotlin
@MainThread
```fun  removeFromParent ( ) :  Boolean 
Removes the current entity from its parent entity. 
set Name 
```kotlin
@MainThread
```fun  setName ( name :  String ) 
Sets the name of the current entity. 
set Parent 
```kotlin
@MainThread
```fun  setParent ( newParent :  Entity ) :  Boolean 
Sets the specified entity as the parent of the current entity. 
stop All Animations 
```kotlin
@MainThread
```fun  stopAllAnimations ( ) 
Stops all animations playing on the current Entity. 
stop All Audio 
```kotlin
@MainThread
```fun  stopAllAudio ( ) 
Stops playing all audios on the current entity. 
to String 
```kotlin
open override fun toString(): String
```