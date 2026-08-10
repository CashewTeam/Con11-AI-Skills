# writeStreamData | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamPlayerController / writeStreamData 
# writeStreamData
```kotlin
@Synchronized
```fun  writeStreamData ( buffer :  ByteBuffer ,  frameCount :  Int ,  blocking :  Boolean ) :  Long 
Writes pcm audio data in push mode operation, which is suitable for real-time audio,the buffer must be direct buffer and the owner of the buffer must be the caller, and the buffer must be released after no longer needed. 
Note: This method only supports writing raw PCM audio data. Any audio file format headers must be removed before writing. In order to get smooth playback experience， the best practice is to write audio data in IO thread with coroutines, please call  writeStreamData  in IO thread, don't call it in main thread or UI thread. 
## Buffer Lifecycle Rules
- 
Ownership : 
- 
Caller retains ownership of the buffer. 
- 
Caller is responsible for allocation and deallocation. 
- 
Release Timing ： 
- 
After write completion: Safe to reuse when: a) Blocking mode: After method returns. b)       Non-blocking: After buffer is fully consumed (check via position). 
- 
After controller close: Must release all associated buffers. 
#### Return
Returns the number of audio frames successfully written (positive value) if the operation succeeds; otherwise, returns a negative error code indicating the specific failure reason. The error codes are based on the standard Linux/Unix  errno.h  definitions: 
- 
EPERM  (-1): Operation not permitted. 
- 
ENOENT  (-2): No such file or directory. 
- 
ESRCH  (-3): No such process. 
- 
EINTR  (-4): Interrupted system call. 
- 
EIO  (-5): I/O error. 
- 
ENXIO  (-6): No such device or address. 
- 
E2BIG  (-7): Argument list too long. 
- 
ENOEXEC  (-8): Exec format error. 
- 
EBADF  (-9): Bad file number. 
- 
ECHILD  (-10): No child processes. 
- 
EAGAIN  (-11): Try again (resource temporarily unavailable). 
- 
ENOMEM  (-12): Out of memory. 
- 
EACCES  (-13): Permission denied. 
- 
EFAULT  (-14): Bad address. 
- 
EBUSY  (-16): Device or resource busy. 
- 
EEXIST  (-17): File exists. 
- 
ENODEV  (-19): No such device. 
- 
ENOTDIR  (-20): Not a directory. 
- 
EISDIR  (-21): Is a directory. 
- 
EINVAL  (-22): Invalid argument. 
#### Parameters
buffer 
PCM audio data buffer (must be direct buffer). 
frame Count 
Number of audio frames to write. 
blocking 
Whether to wait for buffer consumption.