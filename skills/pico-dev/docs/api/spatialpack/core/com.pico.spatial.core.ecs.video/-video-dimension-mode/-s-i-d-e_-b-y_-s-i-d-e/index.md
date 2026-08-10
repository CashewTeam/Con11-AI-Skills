# SIDE_BY_SIDE | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / VideoDimensionMode / SIDE_BY_SIDE 
# SIDE_BY_SIDE
```kotlin
SIDE_BY_SIDE
```
SIDE_BY_SIDE indicates the video dimension mode is horizontally structured into two parts. For example, if the decoded image resolution is 3840 x 1920, both left and right eye images have a resolution of 1920 x 1920. This mode supports 2D side by side, 3D 180 side by side, and 3D 360 side by side videos. 
- 
2D side by side mode is a special video format where 2D images are arranged side by side, with the left and right halves displayed separately. 
- 
3D 180 side by side mode is a 3D 180-degree video format where the left and right eye images are horizontally compressed into a single image, with the left eye image on the left half and the right eye image on the right half. 
- 
3D 360 side by side mode is a 3D 360-degree video format following the same horizontal compression, with the left eye image on the left and the right eye image on the right.