# rigidBodyMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs / RigidBodyComponent / rigidBodyMode 
# rigidBodyMode
```kotlin
var rigidBodyMode: RigidBodyMode
```
Defines what will influence the motion of the object. 
- 
RigidBodyMode.KINEMATIC : The object's motion is only affected by direct velocity changes; and its motion will not be affected by forces. 
- 
RigidBodyMode.DYNAMIC : The object's motion is affected not only by direct velocity changes, but also by forces, such as gravity or collisions. 
By default, when a  RigidBodyComponent  is added to an  Entity , it's  RigidBodyMode  is set to  RigidBodyMode.DYNAMIC . To disable force-based motion, change the  RigidBodyMode  to  RigidBodyMode.KINEMATIC . If you want the object's  RigidBodyMode  to be STATIC, i.e., the object does not move, do not attach a  RigidBodyComponent  to the  Entity .