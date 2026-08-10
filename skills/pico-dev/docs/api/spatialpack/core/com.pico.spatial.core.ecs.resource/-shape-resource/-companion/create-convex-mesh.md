# createConvexMesh | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShapeResource / Companion / createConvexMesh 
# createConvexMesh
```kotlin
@JvmStatic
```fun  createConvexMesh ( mesh :  MeshResource ) :  ShapeResource 
Creates a convex mesh-shaped  ShapeResource  from the given mesh. 
Performance Note: 
- 
Creation:  Computationally expensive as it involves computing the convex hull. 
- 
Collision Detection:  Efficient for simulation (better than  createStaticMesh ), but still slower than primitive shapes ( createBox ,  createSphere ,  createCapsule ). 
Use this only when primitive shapes are insufficient and ensure the input mesh has a low vertex count. 
#### Return
A new  ShapeResource  representing the convex mesh. 
#### Parameters
mesh 
A mesh representing the convex polyhedron. Use meshes with a small number of vertices to maintain performance.