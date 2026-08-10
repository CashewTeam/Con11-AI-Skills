# OrbitAnimation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / OrbitAnimation 
# OrbitAnimation
```kotlin
class OrbitAnimation : SpatialAnimation
```
OrbitAnimation describes an orbital (revolution) animation of an object moving around a given axis. 
It moves an object, starting from  startTransform , along a circular path whose plane normal is defined by  axis . Over the configured duration (from the factory method or parent class), the object completes  rotationCount  full revolutions (1.0 = 360°, 2.0 = 720°, etc.). 
Runtime behavior: 
- 
The orbit radius equals the magnitude of the component of  startTransform.position  that is     perpendicular to  axis . 
- 
The plane of motion is perpendicular to  axis  (axis is normalized internally). 
- 
rotationCount  determines how many full circles are completed within the animation's total     duration. 
- 
If  orientToPath  = true, the object's forward direction will continuously align to the     tangent of the path (i.e., "faces travel direction"). Otherwise, only position changes. 
- 
spinClockwise  toggles the direction of revolution (exact visual interpretation depends on     your engine's handedness). 
Typical use cases: 
- 
Planet / satellite orbit visualization 
- 
Camera orbiting around a focus object 
- 
Decorative circular motion in UI / 3D scenes 
Value & behavior notes: 
- 
rotationCount = 1f -> one full revolution (360°). 
- 
rotationCount = 2.5f -> two and a half revolutions (900°). 
- 
rotationCount = 0f usually means "no orbit" (unless your framework gives it special meaning). 
- 
A zero vector axis (0,0,0) is invalid—avoid it. 
Example: Suppose you want a model (a "satellite") starting at position (2, 0, 0) to revolve counter-clockwise around the Y axis, completing 2 full orbits over 4 seconds, always facing along its path, with a 0.5s start delay, looping: 

```
val orbit = OrbitAnimation.createOrbitAnimation(    name = "SatelliteOrbit",    duration = 4f,                      // 4 seconds total    axis = Vector3(0f, 1f, 0f),         // Orbit around Y axis    startTransform = Transform(        position = Vector3(2f, 0f, 0f)  // Radius ≈ 2    ),    spinClockwise = false,              // Counter‑clockwise (depends on coordinate system)    orientToPath = true,                // Face travel direction    rotationCount = 2f,                 // Two full revolutions (720°)    delay = 0.5f,                       // Start after 0.5s    repeatMode = RepeatMode.RESTART,    // Loop from beginning    repeatCount = -1                    // Loop indefinitely)val resource = AnimationResource.generate(orbit)// Effect: The object circles the origin on the XZ plane twice in 4s, reorients to tangent,// then restarts, creating a continuous orbital loop.
```Members 
## Types
Companion 
```kotlin
object Companion
```
The companion of  OrbitAnimation . 
## Properties
axis 
```kotlin
var axis: Vector3
```
Direction vector of the revolution axis (normalized internally). Example: Vector3(0f, 1f, 0f) -> orbit around the world Y axis. Avoid using (0,0,0). 
orient To Path 
```kotlin
var orientToPath: Boolean
```
If true, the object's orientation continuously aligns to the tangent of its orbital path (i.e., faces direction of motion). If false, orientation is left unchanged (allowing external rotation or "free facing"). 
rotation Count 
```kotlin
var rotationCount: Float
```
Number of full revolutions during the entire animation duration. 1f = 360°, 2f = 720°, fractional values allowed (0.5f = 180°). 0f typically means no rotation (unless defined otherwise by the framework). 
spin Clockwise 
```kotlin
var spinClockwise: Boolean
```
Whether the orbit proceeds in a clockwise direction true = clockwise, false = counter‑clockwise. 
start Transform 
```kotlin
var startTransform: Transform
```
The object's initial transform (position / rotation / scale) at animation start. The distance from the orbit center to this position defines the orbit radius. Changing this changes both the starting point and the radius. 
## Functions
axis 
```kotlin
fun axis(axis: Vector3): OrbitAnimation
```
Set the axis of the animation. 
delay 
```kotlin
fun delay(delay: Float): OrbitAnimation
```
Set the delay of the animation. 
duration 
```kotlin
fun duration(duration: Float): OrbitAnimation
```
Set the duration of the animation. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```name 
```kotlin
fun name(name: String): OrbitAnimation
```
Set the name of the animation. 
offset 
```kotlin
fun offset(offset: Float): OrbitAnimation
```
Set the offset of the animation. 
orient To Path 
```kotlin
fun orientToPath(orientToPath: Boolean): OrbitAnimation
```
Set the orient to path of the animation. 
repeat Count 
```kotlin
fun repeatCount(repeatCount: Int): OrbitAnimation
```
Set the repeat count of the animation. 
repeat Mode 
```kotlin
fun repeatMode(repeatMode: RepeatMode): OrbitAnimation
```
Set the repeat mode of the animation. 
rotation Count 
```kotlin
fun rotationCount(rotationCount: Float): OrbitAnimation
```
Set the rotation count of the animation. 
speed 
```kotlin
fun speed(speed: Float): OrbitAnimation
```
Set the speed of the animation. 
spin Clockwise 
```kotlin
fun spinClockwise(spinClockwise: Boolean): OrbitAnimation
```
Set the spin clockwise of the animation. 
start Transform 
```kotlin
fun startTransform(startTransform: Transform): OrbitAnimation
```
Set the start transform of the animation. 
to String 
```kotlin
open override fun toString(): String
```trim Duration 
```kotlin
fun trimDuration(trimDuration: Float): OrbitAnimation
```
Set the trim duration of the animation. 
trim End 
```kotlin
fun trimEnd(trimEnd: Float): OrbitAnimation
```
Set the trim end of the animation. 
trim Start 
```kotlin
fun trimStart(trimStart: Float): OrbitAnimation
```
Set the trim start of the animation.