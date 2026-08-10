# TOP_AND_DOWN | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / VideoDimensionMode / TOP_AND_DOWN 
# TOP_AND_DOWN
```kotlin
TOP_AND_DOWN
```
TOP_AND_DOWN indicates the video dimension mode is vertically structured into two parts. For example, if the decoded image resolution is 3840 x 1920, both the left and right eye images have a resolution of 3840 x 960. This mode supports 2D top and bottom, 3D 180 top and bottom, and 3D 360 top and bottom videos. 
- 
2D top and bottom mode is a special video format where 2D images are arranged vertically, with the upper and lower halves displayed separately. 
- 
3D 180 top and bottom mode is a 3D 180-degree video format where the left and right eye images are vertically compressed into a single image, with the left eye image on the upper half and the right eye image on the lower half. 
- 
3D 360 top and bottom mode is a 3D 360-degree video format following the same vertical compression, with the left eye image on top and the right eye image at the bottom.