# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / TweenAnimation / Companion 
# Companion
```kotlin
object Companion
```
The companion of  TweenAnimation . 
Members 
## Functions
create Tween Animation 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Color3 ?  =  null ,  to :  Color3 ?  =  null ,  by :  Color3 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Color3  value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Color4 ?  =  null ,  to :  Color4 ?  =  null ,  by :  Color4 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Color4  value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  EulerAngles ?  =  null ,  to :  EulerAngles ?  =  null ,  by :  EulerAngles ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  EulerAngles  value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Quat ?  =  null ,  to :  Quat ?  =  null ,  by :  Quat ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Quat  value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Transform ?  =  null ,  to :  Transform ?  =  null ,  by :  Transform ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Transform  value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Vector2 ?  =  null ,  to :  Vector2 ?  =  null ,  by :  Vector2 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Vector2  value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Vector3 ?  =  null ,  to :  Vector3 ?  =  null ,  by :  Vector3 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Vector3  value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Vector4 ?  =  null ,  to :  Vector4 ?  =  null ,  by :  Vector4 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Vector4  value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Float ?  =  null ,  to :  Float ?  =  null ,  by :  Float ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by Float value. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  FloatArray ?  =  null ,  to :  FloatArray ?  =  null ,  by :  FloatArray ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  FloatArray  value.