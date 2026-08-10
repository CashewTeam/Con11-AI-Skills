# PICOKeyboardTrackingManager | PICO Spatial SDK

sense / com.pico.spatial.sense.keyboard / PICOKeyboardTrackingManager 
# PICOKeyboardTrackingManager
```kotlin
object PICOKeyboardTrackingManager
```
Provides PICO keyboard tracking functionalities, including loading tracked keyboard anchors and subscribing to keyboard anchor updates. 
This singleton object is the public entry point for the keyboard tracking pipeline. It exposes a small lifecycle-based API that lets applications: 
- 
Start and Stop Tracking : Start the underlying tracking service before loading anchors or consuming live updates, and stop it when keyboard tracking is no longer needed. 
- 
Load Current Anchors : Request a snapshot of the keyboard anchors currently recognized by the system. 
- 
Subscribe to Updates : Receive ongoing  ADDED ,  UPDATED , and  REMOVED  events for tracked keyboard anchors. 
- 
Inspect Lifecycle State : Check  state  before invoking APIs that require the manager to be running. 
### Usage Notes
- 
Call  start  before calling  loadAllAnchors  or relying on live updates. 
- 
Register  subscribeAnchorUpdate  before or immediately after  start  if you want to observe the full stream of changes. 
- 
Treat  loadAllAnchors  as a snapshot API. Use  subscribeAnchorUpdate  to keep your local state synchronized after the initial load. 
### Important Notes
- 
loadAllAnchors  returns an empty array when the tracking manager is not in  TrackingState.RUNNING . 
- 
loadAllAnchors()  only returns anchors that are currently recognized by the system. For best results, keep the physical keyboard within the user's field of view so it can be detected and loaded correctly. 
- 
Detection quality can depend on runtime conditions such as visibility, tracking stability, and whether the keyboard has already been observed by the system. 
### Example Usage

```
val subscription = PICOKeyboardTrackingManager.subscribeAnchorUpdate { update ->    when (update.event) {        AnchorUpdate.Event.ADDED -> {            println("Keyboard anchor added: ${update.anchor.anchorUUID}")        }        AnchorUpdate.Event.UPDATED -> {            println("Keyboard anchor updated: ${update.anchor.anchorUUID}")        }        AnchorUpdate.Event.REMOVED -> {            println("Keyboard anchor removed: ${update.anchor.anchorUUID}")        }        AnchorUpdate.Event.LOADED -> Unit    }}PICOKeyboardTrackingManager.start()// Assume this runs in a coroutine scopelaunch {    if (PICOKeyboardTrackingManager.state == TrackingState.RUNNING) {        val anchors = PICOKeyboardTrackingManager.loadAllAnchors()        println("Loaded keyboard anchors: ${anchors.map { it.anchorUUID }}")    }}// Later when you're done:// subscription.cancel()// PICOKeyboardTrackingManager.stop()
```Members 
## Properties
state 
```kotlin
val state: TrackingState
```
Gets the current lifecycle state of the keyboard tracking manager. 
## Functions
load All Anchors 
```kotlin
suspend fun loadAllAnchors(): Array<PICOKeyboardAnchor>
```
Loads all currently recognized PICO keyboard anchors asynchronously. 
start 
```kotlin
fun start()
```
Starts the PICO keyboard tracking manager. 
stop 
```kotlin
fun stop()
```
Stops the PICO keyboard tracking manager. 
subscribe Anchor Update 
```kotlin
fun subscribeAnchorUpdate(subscriber: AnchorUpdateSubscriber<PICOKeyboardAnchor>): Cancellable
```
Subscribes to keyboard anchor update events.