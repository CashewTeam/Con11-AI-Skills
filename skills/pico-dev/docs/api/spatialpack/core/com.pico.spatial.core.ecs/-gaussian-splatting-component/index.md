# GaussianSplattingComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / GaussianSplattingComponent 
# GaussianSplattingComponent
```kotlin
@MainThread
```class  GaussianSplattingComponent  :  Component 
A  Component  that binds a  GaussianSplattingResource  to an entity for Gaussian splatting rendering. 
Members 
## Constructors
Gaussian Splatting Component 
```kotlin
constructor()
```
## Properties
gaussian Splatting Resource 
```kotlin
var gaussianSplattingResource: GaussianSplattingResource?
```
The  GaussianSplattingResource  currently bound to this component, or  null  if unbound. 
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