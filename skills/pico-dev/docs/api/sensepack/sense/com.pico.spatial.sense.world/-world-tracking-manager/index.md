# WorldTrackingManager | PICO Spatial SDK

sense / com.pico.spatial.sense.world / WorldTrackingManager 
# WorldTrackingManager
```kotlin
@RequiredFullSpace
```object  WorldTrackingManager 
Provides world tracking functionalities, including managing and updating anchors. 
WorldTrackingManager  is responsible for asynchronously creating, loading, and removing anchors. It facilitates the management of anchors in a 3D space by enabling you to do the following: 
- 
Create : You can create a new anchor by providing a specific transform (position and orientation) and an optional name. This operation returns a deferred result containing the created  WorldAnchor , allowing for asynchronous handling. 
- 
Load : Existing anchors can be loaded using their UUIDs. This is useful for persisting anchor states across sessions. This operation returns a deferred result containing an array of loaded  WorldAnchors . 
- 
Remove : Anchors that are no longer needed can be removed by specifying their UUIDs. This ensures efficient resource management and prevents unnecessary memory usage. This operation returns a deferred result indicating the success or failure of the removal. 
Additionally,  WorldTrackingManager  manages anchor update events, enabling subscribers to register and receive updates when anchors change. This is implemented through a listener mechanism that notifies registered subscribers of any anchor updates. 
### Code sample
The following code sample demonstrates how to use  WorldTrackingManager : 

```
runBlocking {    // Subscribe to anchor update events    val subscription = WorldTrackingManager.subscribeAnchorUpdate { event ->        when (event.anchorUpdateEvent) {            AnchorUpdate.Event.ADDED -> println("Anchor added: ${event.anchorUUID}")            AnchorUpdate.Event.LOADED -> println("Anchor loaded: ${event.anchorUUID}")            AnchorUpdate.Event.REMOVED -> println("Anchor removed: ${event.anchorUUID}")        }    }    // Create a new anchor    val createResult = WorldTrackingManager         .createAnchor(Vector3(0F, 0F, 0F), EulerAngles(0F, 0F, 0F), "exampleAnchor")    val anchor = when (createResult) {        is WorldTrackingResult.Success -> {            println("Anchor created successfully: ${createResult.data.name}")            createResult.data        }        is WorldTrackingResult.Error -> {            println("Failed to create anchor: ${createResult.errorMessage}")            null        }    }    // Load existing anchors    val loadResult = WorldTrackingManager.loadAnchor()    when (loadResult) {        is WorldTrackingResult.Success -> {            println("Loaded anchors: ${loadResult.data.map { it.name }}")        }        is WorldTrackingResult.Error -> {            println("Failed to load anchors: ${loadResult.errorMessage}")        }    }    // Remove the created anchor    anchor?.let {        val removeResult = WorldTrackingManager.removeAnchor(it.anchorUUID)        when (removeResult) {            is WorldTrackingResult.Success -> println("Anchor removed successfully: ${it.name}")            is WorldTrackingResult.Error -> println("Failed to remove anchor: ${removeResult.errorMessage}")        }    }    // Unsubscribe from anchor update events    subscription.cancel()}
```Members 
## Functions
create Anchor 
```kotlin
suspend fun createAnchor(position: Vector3, rotation: EulerAngles, name: String = ""): WorldTrackingResult<WorldAnchor>
```
Asynchronously creates a new anchor with a specified position, rotation, and name. 
load Anchor 
```kotlin
suspend fun loadAnchor(uuids: Array<UUID> = arrayOf()): WorldTrackingResult<Array<WorldAnchor>>
```
Asynchronously loads anchors with the specified UUIDs. 
remove Anchor 
```kotlin
suspend fun removeAnchor(uuid: UUID): WorldTrackingResult<Unit>
```
Asynchronously removes an anchor with the specified UUID. 
subscribe Anchor Update 
```kotlin
fun subscribeAnchorUpdate(subscriber: AnchorUpdateSubscriber<WorldAnchor>): Cancellable
```
Subscribes to anchor update events.