# SpatialAudioTrackExtension | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension 
# SpatialAudioTrackExtension
```kotlin
class SpatialAudioTrackExtension
```
Provides spatial audio extensions for Android  AudioTrack . 
This extension enables third-party players (e.g., video players) to leverage spatial audio rendering capabilities while continuing to use standard Android AudioTrack APIs. 
## API Structure

```
SpatialAudioTrackExtension├── attachToEntity              (Bind spatial audio to an Entity's position)│   ├── withBuilder             (Configure and bind before AudioTrack creation)│   └── withAudioTrack          (Bind after AudioTrack creation)└── attachToContainer           (Bind spatial audio at container/window level)    ├── withBuilder             (Configure and bind before AudioTrack creation)    └── withAudioTrack          (Bind after AudioTrack creation)
```
## Choosing the Right Method
withBuilder vs withAudioTrack: 
- 
Use  withBuilder  methods when you have access to the  AudioTrack.Builder  before calling  build() . This is the typical case when you control the AudioTrack creation pipeline. 
- 
Use  withAudioTrack  methods when the  AudioTrack  is already created by an external framework (e.g., ExoPlayer, MediaPlayer) and handed to you after instantiation. 
Entity vs Container: 
- 
Use  attachToEntity  when the audio should follow a specific 3D object's position in the scene (e.g., a video panel entity). 
- 
Use  attachToContainer  when the audio only needs to follow the window/container position (e.g., fixed background music). 
## Usage Examples
### Entity + Builder (recommended for custom players)

```
val extension = SpatialAudioTrackExtension()extension.spatialAudioTrackExtensionConfig(    mode = SpatialAudioMode.OBJECT,    isAmbisonic = false,    builder = audioTrackBuilder)extension.attachToEntityWithBuilder(targetEntity, audioTrackBuilder)val audioTrack = audioTrackBuilder.build()
```
### Entity + AudioTrack (for third-party frameworks)

```
val extension = SpatialAudioTrackExtension()extension.spatialAudioTrackExtensionConfig(    mode = SpatialAudioMode.OBJECT,    isAmbisonic = false,    builder = audioTrackBuilder)val audioTrack = audioTrackBuilder.build() // created by frameworkextension.attachToEntityWithAudioTrack(targetEntity, audioTrack)
```
### Container + Builder (window-level audio)

```
val extension = SpatialAudioTrackExtension()extension.spatialAudioTrackExtensionConfig(    mode = SpatialAudioMode.AMBIENT,    isAmbisonic = false,    builder = audioTrackBuilder)extension.attachToContainerWithBuilder(context, audioTrackBuilder)val audioTrack = audioTrackBuilder.build()
```
### Container + AudioTrack

```
val extension = SpatialAudioTrackExtension()extension.spatialAudioTrackExtensionConfig(    mode = SpatialAudioMode.AMBIENT,    isAmbisonic = false,    builder = audioTrackBuilder)val audioTrack = audioTrackBuilder.build()extension.attachToContainerWithAudioTrack(context, audioTrack)
```
#### See also
Spatial Audio Track Extension. Spatial Audio Mode 
for available spatialization modes. 
Members 
## Constructors
Spatial Audio Track Extension 
```kotlin
constructor()
```
## Types
Spatial Audio Mode 
```kotlin
enum SpatialAudioMode : Enum<SpatialAudioTrackExtension.SpatialAudioMode>
```
Spatial audio rendering mode. 
## Functions
attach To Container With Audio Track 
```kotlin
fun attachToContainerWithAudioTrack(currentContext: Context, audioTrack: AudioTrack)
```
Attaches spatial audio to a Container/Context using an already-created  AudioTrack . 
attach To Container With Builder 
```kotlin
fun attachToContainerWithBuilder(currentContext: Context, builder: AudioTrack.Builder)
```
Attaches spatial audio to a Container/Context using a pre-configured  AudioTrack.Builder . 
attach To Entity With Audio Track 
```kotlin
@MainThread
```fun  attachToEntityWithAudioTrack ( entityToAttach :  Entity ,  audioTrack :  AudioTrack ) 
Attaches spatial audio to an Entity using an already-created  AudioTrack . 
attach To Entity With Builder 
```kotlin
@MainThread
```fun  attachToEntityWithBuilder ( entityToAttach :  Entity ,  builder :  AudioTrack.Builder ) 
Attaches spatial audio to an Entity using a pre-configured  AudioTrack.Builder . 
enable Spatial Audio 
```kotlin
fun enableSpatialAudio(enable: Boolean, audioTrack: AudioTrack): Boolean
```
Enables or disables spatial audio processing for the given  AudioTrack . 
release 
```kotlin
@MainThread
```fun  release ( ) 
Releases all resources associated with this spatial audio extension. 
spatial Audio Track Extension Config 
```kotlin
fun spatialAudioTrackExtensionConfig(mode: SpatialAudioTrackExtension.SpatialAudioMode = SpatialAudioMode.AMBIENT, isAmbisonic: Boolean = false, builder: AudioTrack.Builder)
```
Configures spatial audio parameters on the  AudioTrack.Builder .