# ObjectAudioComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ObjectAudioComponent / ObjectAudioComponent 
# ObjectAudioComponent
```kotlin
constructor()
```
The default constructor for  ObjectAudioComponent  with no parameters. 
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f, directivity: Directivity = Directivity(0.0f, 0.0f), distanceAttenuationMode: DistanceAttenuationMode = DistanceAttenuationMode.INVERSE_SQUARED, reverbVolume: Float = 1.0f, soundRadiusLevel: Float = 0.1f)
```
Creates a new ObjectAudioComponent with the specified parameters. 
All parameters must be valid; otherwise an  IllegalArgumentException  is thrown. 
#### Parameters
volume 
The volume of the audio. Valid range  [0.0, 1.0] . Default  1.0f . 
directivity 
The directivity of the audio. Valid range  ([0.0, 1.0],[0.0, ∞]) . 
distance Attenuation Mode 
The distance attenuation mode for audio. Default  DistanceAttenuationMode.INVERSE_SQUARED . 
reverb Volume 
The reverb volume level. Valid range  [0.0, 1.0] . Default  1.0f . Effective only when VST (Video SeeThrough) is enabled. 
sound Radius Level 
The sound radius level of the audio. The valid value range is  [0.0, ∞] . The default value is  0.1f . This parameter controls the effective radius of the sound source for spatial audio calculations. 
#### Throws
Illegal Argument Exception 
if any parameter is outside its valid range.