# PortalComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PortalComponent 
# PortalComponent
```kotlin
@MainThread
```class  PortalComponent  :  Component 
A  Component  that enables entity surfaces to act as portals to a target world (the targetEntity EC tree) and should be used in conjunction with PortalMaterial. 
Terminologies: 
- 
PortalEntity: An entity that the  PortalComponent  is added to. 
- 
PortalWorldEntity: An entity that the  PortalWorldComponent  is added to. 
- 
PortalCrossableEntity: An entity that the  PortalCrossableComponent  is added to. 
To achieve the desired portal effect, you should adhere to the following design principles: 
- 
PortalEntity should have a  PortalMaterial  linked to its  ModelComponent . 
- 
PortalEntity must be either a sibling or parent node to PortalWorldEntity, not a child. 
- 
PortalCrossableEntity must be a child node within a PortalWorldEntity and cannot be isolated outside of it. 
- 
The system can display up to 8 pairs of Portal-World relationships simultaneously. This supports up to 8 such pairs. 
## Background Settings
The portal background can be configured with  panelColor  and  backgroundMode : 
- 
PortalBackgroundMode.SOLID_COLOR : Displays a solid color background (default). The color is controlled by  panelColor . 
- 
PortalBackgroundMode.PASSTHROUGH : Shows the real world (passthrough) behind the portal. 
These properties are experimental and require  ExperimentalSpatialApi  to be enabled. 
## Usage Example

```
// Create world entity and crossing entityval worldEntity = Entity()worldEntity.components.set(PortalWorldComponent())val willCrossingEntity = Entity()willCrossingEntity.components.set(PortalCrossableComponent())worldEntity.addChild(willCrossingEntity)// Create portal entityval portalEntity = Entity()portalEntity.components.set(    PortalComponent(        targetEntity = worldEntity,        allowClipping = true,        doubleSide = false,        allowEntityCrossing = true    ))// Attach required visual componentsportalEntity.components.set(ModelComponent(mesh, PortalMaterial()))
```
#### See also
Portal World Component Portal Crossable Component Portal Material Portal Background Mode Members 
## Constructors
Portal Component 
```kotlin
constructor(targetEntity: Entity, enable: Boolean = true, doubleSide: Boolean = false, allowClipping: Boolean = true, allowEntityCrossing: Boolean = true)
```
Constructs a  PortalComponent  with the specified parameters. 
```kotlin
@ExperimentalSpatialApi
```constructor ( targetEntity :  Entity ,  enable :  Boolean  =  true ,  doubleSide :  Boolean  =  false ,  allowClipping :  Boolean  =  true ,  allowEntityCrossing :  Boolean  =  true ,  panelColor :  Color3  =  Color3(0f, 0f, 0f) ,  backgroundMode :  PortalBackgroundMode  =  PortalBackgroundMode.SOLID_COLOR ) 
Constructs a  PortalComponent  with the specified parameters, including experimental background settings. 
## Properties
allow Clipping 
```kotlin
var allowClipping: Boolean
```
Whether clipping is allowed for the  PortalComponent . The default value is  true . 
allow Entity Crossing 
```kotlin
var allowEntityCrossing: Boolean
```
Whether entities are allowed to cross through the  PortalComponent . The default value is  true . 
background Mode 
```kotlin
@ExperimentalSpatialApi
```var  backgroundMode :  PortalBackgroundMode 
The background mode of the portal. The default value is  PortalBackgroundMode.SOLID_COLOR . 
double Side 
```kotlin
var doubleSide: Boolean
```
Whether both sides (forward and backward) of the  PortalComponent  are rendered. The default value is  false . 
enable 
```kotlin
var enable: Boolean
```
The enabled state of the  PortalComponent . The default value is  true , indicating enabled. 
panel Color 
```kotlin
@ExperimentalSpatialApi
```var  panelColor :  Color3 
The color of the portal panel. The default value is black (0, 0, 0). The panel color is used when  backgroundMode  is set to  PortalBackgroundMode.SOLID_COLOR . 
target Entity 
```kotlin
var targetEntity: Entity?
```
The target entity representing the world visible through the portal. If  targetEntity  is  null , the portal will not be rendered. To render the portal correctly, set  targetEntity  to a valid  Entity  object. 
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