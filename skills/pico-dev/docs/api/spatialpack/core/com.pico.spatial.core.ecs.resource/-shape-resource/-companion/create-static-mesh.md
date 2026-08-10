# createStaticMesh | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShapeResource / Companion / createStaticMesh 
# createStaticMesh
```kotlin
@JvmStatic
```fun  createStaticMesh ( mesh :  MeshResource ) :  ShapeResource 
Creates a static mesh-shaped  ShapeResource  from the given mesh. 
Performance Note: 
- 
Collision Detection:  Significantly more expensive than primitive shapes and  createConvexMesh  as it uses triangle-based checks. 
- 
Usage:  Should  only  be used for complex, non-moving environment geometry. 
Avoid using static meshes for dynamic objects or when primitive shapes can approximate the geometry. 
#### Return
A new  ShapeResource  representing the static mesh. 
#### Parameters
mesh 
A mesh representing the polyhedron shape.