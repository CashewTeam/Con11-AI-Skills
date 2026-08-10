# MULTIPLE_VIEW | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / VideoDimensionMode / MULTIPLE_VIEW 
# MULTIPLE_VIEW
```kotlin
MULTIPLE_VIEW
```
MULTIPLE_VIEW indicates the video dimension mode uses a double buffer structure, meaning there is one buffer dedicated for each eye. This mode is typically used for MV-HEVC video format. For example, if the decoded image resolution is 3840 x 1920, both the left and right eye images have a resolution of 3840 x 1920.