# ImageBasedLightReceiverComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ImageBasedLightReceiverComponent 
# ImageBasedLightReceiverComponent
```kotlin
@MainThread
```class  ImageBasedLightReceiverComponent  :  Component 
A  Component  that enables an entity to receive image-based lighting (IBL) from the source entity having an  ImageBasedLightComponent . 
This component enables an entity to be affected by localized environment lighting and have realistic material responses. 
Members 
## Constructors
Image Based Light Receiver Component 
```kotlin
constructor(source: Entity)
```
## Properties
source 
```kotlin
var source: Entity?
```
The source entity which has an  ImageBasedLightComponent . 
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