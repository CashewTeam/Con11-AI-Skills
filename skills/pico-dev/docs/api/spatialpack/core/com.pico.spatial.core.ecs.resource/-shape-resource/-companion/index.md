# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShapeResource / Companion 
# Companion
```kotlin
object Companion
```
Static functions for  ShapeResource  generator. 
Members 
## Functions
create Box 
```kotlin
@JvmStatic
```fun  createBox ( size :  Vector3 ) :  ShapeResource 
Creates a box-shaped  ShapeResource  with the specified dimensions. 
create Capsule 
```kotlin
@JvmStatic
```fun  createCapsule ( height :  Float ,  radius :  Float ) :  ShapeResource 
Creates a capsule-shaped  ShapeResource  with the specified height and radius. 
create Convex Mesh 
```kotlin
@JvmStatic
```fun  createConvexMesh ( mesh :  MeshResource ) :  ShapeResource 
Creates a convex mesh-shaped  ShapeResource  from the given mesh. 
create Sphere 
```kotlin
@JvmStatic
```fun  createSphere ( radius :  Float ) :  ShapeResource 
Creates a sphere-shaped  ShapeResource  with the specified radius. 
create Static Mesh 
```kotlin
@JvmStatic
```fun  createStaticMesh ( mesh :  MeshResource ) :  ShapeResource 
Creates a static mesh-shaped  ShapeResource  from the given mesh.