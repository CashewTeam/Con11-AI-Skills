# Instance | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource / Instance 
# Instance
```kotlin
class Instance
```
Represents a single instance with an ID and a transform. 
Members 
## Constructors
Instance 
```kotlin
constructor(id: String, transform: Transform)
```
Creates an instance with the specified unique ID and transform. 
```kotlin
constructor(id: String, transform: Transform, customFloatData: FloatArray)
```
Creates an instance with the specified unique ID, transform and custom float data. 
## Properties
custom Float Data 
```kotlin
val customFloatData: FloatArray
```
The custom float data attached to this instance. 
id 
```kotlin
val id: String
```
The ID of the instance. 
transform 
```kotlin
val transform: Transform
```
The transform matrix defining the position, rotation, and scale of the instance. 
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