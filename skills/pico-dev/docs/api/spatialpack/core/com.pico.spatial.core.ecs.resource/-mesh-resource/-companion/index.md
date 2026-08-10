# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  MeshResource . 
Members 
## Functions
create Box 
```kotlin
@JvmStatic
```fun  createBox ( size :  Vector3 ,  cornerRadius :  Float  =  0.0f ) :  MeshResource 
Synchronously creates a box mesh resource. 
create Capsule 
```kotlin
@JvmStatic
```fun  createCapsule ( height :  Float ,  radius :  Float ) :  MeshResource 
Synchronously creates a capsule mesh resource. 
create Cone 
```kotlin
@JvmStatic
```fun  createCone ( height :  Float ,  radius :  Float ) :  MeshResource 
Synchronously creates a cone mesh resource. 
create Cylinder 
```kotlin
@JvmStatic
```fun  createCylinder ( height :  Float ,  radius :  Float ) :  MeshResource 
Synchronously creates a cylinder mesh resource. 
create Plane 
```kotlin
@JvmStatic
```fun  createPlane ( width :  Float ,  height :  Float ,  cornerRadius :  Float  =  0.0f ) :  MeshResource 
Synchronously creates a plane mesh resource. 
create Sphere 
```kotlin
@JvmStatic
```fun  createSphere ( radius :  Float ) :  MeshResource 
Synchronously creates a sphere mesh resource. 
create Torus 
```kotlin
@JvmStatic
```fun  createTorus ( outerRingRadius :  Float ,  innerRingRadius :  Float ) :  MeshResource 
Synchronously creates a torus mesh resource. 
create Video Panel 
```kotlin
@JvmStatic
```fun  createVideoPanel ( width :  Float ,  height :  Float ,  cornerRadius :  Float ) :  MeshResource 
Creates a mesh resource for a video panel. 
create With Mesh Model 
```kotlin
@JvmStatic
```fun  createWithMeshModel ( model :  MeshModel ,  bounds :  BoundingBox ?  =  null ,  name :  String ) :  MeshResource 
Creates a new  MeshResource  from a  MeshModel . 
load 
```kotlin
@JvmStatic
```fun  load ( path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ) :  MeshResource 
Loads a  MeshResource  via file path. 
load From Mesh Anchor 
```kotlin
@JvmStatic
```fun  loadFromMeshAnchor ( anchorUUID :  UUID ) :  MeshResource 
Load mesh resource from mesh anchor. 
load From Plane Anchor 
```kotlin
@JvmStatic
```fun  loadFromPlaneAnchor ( anchorUUID :  UUID ) :  MeshResource 
Load mesh resource from plane anchor.