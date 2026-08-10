# EyeTrackingProvider | PICO Spatial SDK

tracking / com.pico.spatial.tracking.eye / EyeTrackingProvider 
# EyeTrackingProvider
```kotlin
class EyeTrackingProvider : DataProvider<EyeTrackingData>
```
Provides eye tracking data. For usage details, refer to  DataProvider . 
Eye tracking data includes a 6DoF pose of the eye gaze. You can get the pose via  EyeTrackingData.eyePose . 
Notes that the eye tracking data is only available when the user has granted the eye tracking permission. The eye tracking permission is "com.picovr.permission.EYE_TRACKING". And it is a runtime permission, you need to declare it in the AndroidManifest.xml and request it at runtime before using the eye tracking data. 
#### See also
Data Provider Eye Tracking Data Members 
## Constructors
Eye Tracking Provider 
```kotlin
constructor()
```