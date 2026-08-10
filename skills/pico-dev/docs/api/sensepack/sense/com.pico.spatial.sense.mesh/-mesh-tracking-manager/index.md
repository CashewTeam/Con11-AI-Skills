# MeshTrackingManager | PICO Spatial SDK

sense / com.pico.spatial.sense.mesh / MeshTrackingManager 
# MeshTrackingManager
```kotlin
object MeshTrackingManager
```
Provides mesh tracking functionalities, including managing and updating mesh anchors. 
This singleton object is responsible for handling mesh anchor updates and providing asynchronous operations to load all mesh anchors and subscribe to anchor update events. It facilitates the management of mesh anchors in a 3D space by allowing developers to: 
- 
Subscribe to Updates : Developers can subscribe to anchor update events to receive real-time notifications whenever a mesh anchor is added, updated, or removed. This is achieved through a listener mechanism that notifies registered subscribers of any anchor updates. 
- 
Load All Anchors : Developers can load all currently tracked mesh anchors asynchronously. This operation returns a suspendable function that provides an array of  MeshAnchor  objects. 
- 
Start and Stop : The tracking manager can be started or stopped as needed. The manager needs to be in a running state to load anchors or receive updates. 
Additionally, developers can check the current state of the tracking manager to determine whether it is running or stopped. 
### Example Usage
Below is an example demonstrating how to use  MeshTrackingManager : 

```
runBlocking {    // Subscribe to anchor update events    val subscription = MeshTrackingManager.subscribeAnchorUpdate { event ->        when (event.anchorUpdateEvent) {            AnchorUpdate.Event.ADDED -> println("Mesh anchor added: ${event.anchor.anchorUUID}")            AnchorUpdate.Event.UPDATED -> println("Mesh anchor updated: ${event.anchor.anchorUUID}")            AnchorUpdate.Event.REMOVED -> println("Mesh anchor removed: ${event.anchor.anchorUUID}")        }    }    // Start the tracking manager    MeshTrackingManager.start()    // Check the state of the tracking manager    when (MeshTrackingManager.state) {        TrackingState.RUNNING -> {            // Only available when the tracking manager is running            // Load all currently tracked Plane anchors            val anchors = MeshTrackingManager.loadAllAnchors()            println("Loaded Plane anchors: ${anchors.map { it.anchorUUID }}")        }        TrackingState.NONE -> println("Manager not initialized yet.")        TrackingState.INITIALIZED -> println("Manager initialized but not running.")        TrackingState.PAUSED -> println("Manager is paused due to an exception " +                    "or stage transition. Resume tracking to continue.")        TrackingState.STOPPED -> println("Manager has been stopped. Restart required.")        TrackingState.INVALID -> println("Manager is in an invalid state. Functionality unavailable.")    }    // Stop the tracking manager    MeshTrackingManager.stop()    // Unsubscribe from anchor updates    subscription.cancel()}
```Members 
## Properties
state 
```kotlin
val state: TrackingState
```
Gets the current state of the tracking manager. 
## Functions
load All Anchors 
```kotlin
suspend fun loadAllAnchors(): Array<MeshAnchor>
```
Loads all mesh anchors asynchronously. 
start 
```kotlin
fun start()
```
Starts the tracking manager. 
stop 
```kotlin
fun stop()
```
Stops the tracking manager. 
subscribe Anchor Update 
```kotlin
fun subscribeAnchorUpdate(subscriber: AnchorUpdateSubscriber<MeshAnchor>): Cancellable
```
Subscribes to anchor update events.