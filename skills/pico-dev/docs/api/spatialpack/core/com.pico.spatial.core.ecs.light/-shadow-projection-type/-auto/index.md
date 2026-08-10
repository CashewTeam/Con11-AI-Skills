# Auto | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowProjectionType / Auto 
# Auto
```kotlin
class Auto(val maximumDistance: Float = 5.0f) : ShadowProjectionType
```
Automatically determines the shadow projection based on the current camera configuration, constrained by a maximum distance. 
Members 
## Constructors
Auto 
```kotlin
constructor(maximumDistance: Float = 5.0f)
```
## Properties
maximum Distance 
```kotlin
val maximumDistance: Float
```
The maximum distance used when fitting the shadow projection. 
## Functions
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