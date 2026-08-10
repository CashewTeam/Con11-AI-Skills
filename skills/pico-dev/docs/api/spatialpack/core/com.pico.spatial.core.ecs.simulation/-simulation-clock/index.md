# SimulationClock | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / SimulationClock 
# SimulationClock
```kotlin
class SimulationClock
```
A custom clock that drives the physics simulation. By default, the engine clock is used. 
Members 
## Constructors
Simulation Clock 
```kotlin
constructor(fixedTimeStep: Float = 0.02f, maxTimeStep: Float = 0.33f, timeSpeed: Float = 1.0f)
```
```kotlin
constructor(other: SimulationClock)
```
Constructs a  SimulationClock  instance with another instance. 
## Properties
fixed Time Step 
```kotlin
val fixedTimeStep: Float
```
The fixed interval (in seconds) that determines how often physics calculations will be performed. 
max Time Step 
```kotlin
val maxTimeStep: Float
```
The fixed interval (in seconds) that determines the maximum time step allowed for physics calculations. 
time Speed 
```kotlin
val timeSpeed: Float
```
The speed at which time progresses. A value of 1 means real-time. A value of 0.5 means half speed. 
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