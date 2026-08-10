# PortalWorldComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PortalWorldComponent 
# PortalWorldComponent
```kotlin
@MainThread
```class  PortalWorldComponent  :  Component 
A  Component  that transforms an entity and its descendants into a separate world, visible only through a portal. This component should be used with  PortalComponent ,  PortalCrossableComponent , and  PortalMaterial . 
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
#### See also
Portal Component Portal Crossable Component Portal Material Members 
## Constructors
Portal World Component 
```kotlin
constructor()
```
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Clones a new instance of the  PortalWorldComponent . 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```