# ContainerProxy | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / ContainerProxy 
# ContainerProxy
```kotlin
class ContainerProxy
```
ContainerProxy  is used to describe a window container instance. 
Members 
## Properties
id 
```kotlin
val id: String
```
The name of the window container. It is declared in window container dsl. 
state 
```kotlin
val state: SpatialContainerState
```
The state of the window container. 
tag 
```kotlin
val tag: String?
```
The tag of the window container instance when you open it. See also  SpatialNavigator.openWindowContainer 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```