# PortalCrossableComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PortalCrossableComponent 
# PortalCrossableComponent
```kotlin
@MainThread
```class  PortalCrossableComponent  :  Component 
A  Component  that enables an entity (in the target world) and its descendants to traverse through a portal. This component should be utilized with  PortalComponent ,  PortalWorldComponent , and  PortalMaterial . 
#### See also
Portal World Component Portal Material Portal Component Members 
## Constructors
Portal Crossable Component 
```kotlin
constructor()
```
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Clones a new instance from the  PortalCrossableComponent . 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```