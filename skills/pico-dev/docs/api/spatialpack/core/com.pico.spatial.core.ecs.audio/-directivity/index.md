# Directivity | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / Directivity 
# Directivity
```kotlin
class Directivity
```
Defines how sound is emitted from an audio source and perceived within the spatial environment. 
Audio directivity is essential in spatial audio design, defining both the direction and dispersion of sound. It is primarily controlled by two parameters: 
- 
Pattern  – Determines the overall shape of the sound projection. 
- 
Sharpness  – Controls the focus of the sound beam. 
Properly tuning directivity helps achieve desired acoustic effects while ensuring optimal sound clarity and coverage. 
Members 
## Constructors
Directivity 
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) pattern: Float = 0.0f, @FloatRange(from = 0.0) sharpness: Float = 0.0f)
```
Constructor of audio directivity. 
## Properties
pattern 
```kotlin
var pattern: Float
```
The pattern of audio directivity, which refers to the shape of the sound projection. It determines how focused or dispersed the sound is. 
sharpness 
```kotlin
var sharpness: Float
```
The sharpness of audio directivity, which determines how focused or dispersed the sound is. Higher sharpness results in a more focused sound; lower sharpness produces a wider, more diffuse sound. 
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