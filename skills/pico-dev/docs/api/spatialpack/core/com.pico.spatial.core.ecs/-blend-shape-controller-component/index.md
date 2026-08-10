# BlendShapeControllerComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / BlendShapeControllerComponent 
# BlendShapeControllerComponent
```kotlin
@MainThread
```class  BlendShapeControllerComponent  :  Component 
Provides BlendShape (morph target) weight control for an Entity's model, with optional subset workflows for managing groups of BlendShapes. 
This component lets you: 
- 
Read weights : Get a single BlendShape weight by  index  or  name , or read all weights. 
- 
Write weights : Set a single weight or set all weights in batch. 
- 
Control subsets : Define a named subset (by indices or names) and then get/set that group as a whole, which is convenient for high-level controls such as "Mouth", "Brows", or "Eyes". 
## ECS Preconditions (Very Important)
- 
Attach to any Entity : You can add this component to any Entity in the ECS system. 
- 
Model requirement : The Entity must have a  ModelComponent  attached. 
- 
BlendShape data requirement : The  ModelComponent 's mesh must contain BlendShape data (for example,  mesh.getBlendShapeNames()  is not null or empty). 
When any of these preconditions is not satisfied, all APIs behave as invalid / no-op: 
- 
Getter behavior : Single-value getters return  null ; list getters return an empty list. 
- 
Setter behavior : Setter functions return  false  and do not modify any weights. 
## Content Authoring Notes
- 
Author in DCC tools first : Create and tune BlendShapes in a DCC tool such as Maya or Blender, and verify the visual effect of different weights there. 
- 
Preserve channels on export : Make sure the exported asset keeps all BlendShape channels so that the runtime mesh exposes the same names. 
- 
Match names and indices : Use the names and index order from the imported mesh when calling the APIs of this component. 
## Weight Semantics
- 
Value type : Weights are  Float  values. 
- 
Typical range : Many pipelines use a normalized range like  [0.0f .. 1.0f] , but the effective range is content-dependent. The component itself does not clamp. 
- 
Index rules : BlendShape indices are zero-based and must fall inside the mesh's BlendShape list. 
- 
Name rules : Name matching is exact and case-sensitive; use the same spelling as in the imported mesh. 
- 
Performance : Each successful write may schedule graphics work. Prefer batch functions such as  setBlendShapeWeights  over many single-weight calls in a tight loop. 
## Subset Workflow
Subsets are developer-defined logical groups of BlendShapes stored internally under a  subsetName . They let you control several related shapes with a single higher-level slider or animation channel. 
- 
Create by indices : Use  createBlendShapeSubset(subsetName, indices)  when you know the mesh index layout. 
- 
Create by names : Use  createBlendShapeSubset(subsetName, blendShapeNames)  when indices may change; this is usually more robust. 
- 
Ordering : The order of indices or names you pass defines the order of weights returned by  getBlendShapeWeights(subsetName)  and expected by  setBlendShapeWeights(subsetName, weights) . 
- 
Duplicates : You may include the same BlendShape multiple times in a subset, but this is discouraged. When setting weights for such a subset, later entries for the same target override earlier ones. 
- 
Missing subsets : If a subset does not exist, subset getters return an empty list and subset setters return  false . 
## Mesh Replacement (Must Re-add This Component)
Changing the mesh on the  ModelComponent  (for example, swapping heads, changing LODs, or switching to a different skinned mesh) typically changes the BlendShape layout. To keep the mapping between this component and the runtime mesh consistent: 
- 
After changing the mesh : 
- 
Remove this component from the Entity. 
- 
Add a new  BlendShapeControllerComponent  to the same Entity. 
- 
Re-create subsets : Any previously defined subsets are not guaranteed to stay valid after a mesh change. Rebuild subsets for the new mesh before driving them again. 
Members 
## Constructors
Blend Shape Controller Component 
```kotlin
constructor()
```
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
create Blend Shape Subset By Indices 
```kotlin
fun createBlendShapeSubsetByIndices(subsetName: String, indices: List<Int>): Boolean
```
Create a BlendShape subset by indices. 
create Blend Shape Subset By Names 
```kotlin
fun createBlendShapeSubsetByNames(subsetName: String, blendShapeNames: List<String>): Boolean
```
Create a BlendShape subset by names. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get Blend Shape Weight 
```kotlin
fun getBlendShapeWeight(index: Int): Float?
```
Get the weight of a BlendShape by its index. 
```kotlin
fun getBlendShapeWeight(blendShapeName: String): Float?
```
Get the weight of a BlendShape by its name. 
get Blend Shape Weights 
```kotlin
fun getBlendShapeWeights(): List<Float>
```
Get the weights of all BlendShapes. 
```kotlin
fun getBlendShapeWeights(subsetName: String): List<Float>
```
Gets the weights of a BlendShape subset by its name. 
hash Code 
```kotlin
open override fun hashCode(): Int
```remove Blend Shape Subset 
```kotlin
fun removeBlendShapeSubset(subsetName: String)
```
Remove a BlendShape subset by its name. 
set Blend Shape Weight 
```kotlin
fun setBlendShapeWeight(index: Int, weight: Float): Boolean
```
Set the weight of a BlendShape by its index. 
```kotlin
fun setBlendShapeWeight(blendShapeName: String, weight: Float): Boolean
```
Set the weight of a BlendShape by its name. 
set Blend Shape Weights 
```kotlin
fun setBlendShapeWeights(weights: List<Float>): Boolean
```
Set the weights of all BlendShapes. 
```kotlin
fun setBlendShapeWeights(subsetName: String, weights: List<Float>): Boolean
```
Set the weights of a BlendShape subset by its name. 
to String 
```kotlin
open override fun toString(): String
```