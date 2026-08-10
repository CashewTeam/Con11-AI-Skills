# SolverIterations | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / SolverIterations 
# SolverIterations
```kotlin
class SolverIterations
```
Defines the iteration counts used by the physics engine when resolving position or velocity constraints. 
Members 
## Constructors
Solver Iterations 
```kotlin
constructor()
```
```kotlin
constructor(positionIterations: Int, velocityIterations: Int)
```
```kotlin
constructor(other: SolverIterations)
```
Constructs a  SolverIterations  instance with another instance. 
## Properties
position Iterations 
```kotlin
val positionIterations: Int
```
The iteration count for resolving position constraints. 
velocity Iterations 
```kotlin
val velocityIterations: Int
```
The iteration count for resolving velocity constraints. 
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