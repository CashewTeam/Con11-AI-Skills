# createTweenAnimation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / TweenAnimation / Companion / createTweenAnimation 
# createTweenAnimation
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Float ?  =  null ,  to :  Float ?  =  null ,  by :  Float ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by Float value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  FloatArray ?  =  null ,  to :  FloatArray ?  =  null ,  by :  FloatArray ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  FloatArray  value. 
This overload is primarily used with BlendShape weights targets, such as  AnimationBindTarget.bindBlendShapeWeights()  and  AnimationBindTarget.bindBlendShapeSubsetWeights(subsetName) . 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Vector2 ?  =  null ,  to :  Vector2 ?  =  null ,  by :  Vector2 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Vector2  value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Vector3 ?  =  null ,  to :  Vector3 ?  =  null ,  by :  Vector3 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Vector3  value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Vector4 ?  =  null ,  to :  Vector4 ?  =  null ,  by :  Vector4 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Vector4  value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Transform ?  =  null ,  to :  Transform ?  =  null ,  by :  Transform ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Transform  value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Quat ?  =  null ,  to :  Quat ?  =  null ,  by :  Quat ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Quat  value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  EulerAngles ?  =  null ,  to :  EulerAngles ?  =  null ,  by :  EulerAngles ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  EulerAngles  value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Color4 ?  =  null ,  to :  Color4 ?  =  null ,  by :  Color4 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Color4  value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
```kotlin
@JvmStatic
```fun  createTweenAnimation ( name :  String  =  "" ,  bindTarget :  AnimationBindTarget ?  =  null ,  from :  Color3 ?  =  null ,  to :  Color3 ?  =  null ,  by :  Color3 ?  =  null ,  duration :  Float  =  1.0f ,  delay :  Float  =  0.0f ,  repeatMode :  RepeatMode  =  RepeatMode.NONE ,  repeatCount :  Int  =  0 ,  easeType :  EaseType  =  EaseType.LINEAR ,  offset :  Float  =  0.0f ,  speed :  Float  =  1.0f ,  additive :  Boolean  =  false ,  trimStart :  Float ?  =  null ,  trimEnd :  Float ?  =  null ,  trimDuration :  Float ?  =  null ) :  TweenAnimation 
Creates a tween animation by  Color3  value. 
#### Return
The created  TweenAnimation . 
#### Parameters
name 
The name of the animation, no more than 63 ascii characters. The default value is an empty string "". 
bind Target 
The target to be animated. Default is null. 
from 
The initial value of the animation. Default is null. 
to 
The target value of the animation. Default is null. 
by 
The relative change value of the animation. Default is null. 
duration 
The total playback duration of the animation, in seconds. Must be greater than 0. The default value is 1F (1 second). 
delay 
The amount of seconds the animation delays before starting to be played. Must be greater than or equal to 0. The default value is 0F (0 second). 
repeat Mode 
How an animation behaves when it reaches the end of one playback. An animation's  repeatCount  must be set to a positive integer or '-1' for this property to work. The Default value is  RepeatMode.NONE . 
repeat Count 
How many times an animation is repeated. Use  INFINITE  to repeat indefinitely, or a non-negative integer. For example, a value of  1  means that the animation is repeated once after the initial playback ends, so the animation plays a total of two times. The default value is  0 , which means no repetition. 
ease Type 
The ease type of the animation. The default value is  EaseType.LINEAR . 
offset 
The offset for the start time of the animation's playback, in seconds. Must be greater than or equal to 0. The default value is 0F (0 second). 
speed 
A factor that increases or decreases the animation’s playback speed. Must be greater than 0. The default value is 1F (1x speed). 
additive 
Whether to add the data of this animation to the animation that is currently playing. The default value is  false . 
trim Start 
The start time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim End 
The end time of the trimmed animation segment, in seconds. Must be greater than or equal to 0 if specified. The default value is null. 
trim Duration 
The duration of the animation to trim, in seconds. Must be greater than or equal to 0 if specified. The default value is null.