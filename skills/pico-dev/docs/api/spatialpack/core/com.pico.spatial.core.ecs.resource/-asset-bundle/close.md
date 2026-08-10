# close | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / close 
# close
```kotlin
open override fun close()
```
Closes an  AssetBundle  and releases the resources occupied by it. 
This function overrides the close method to ensure that, even if the  AssetBundle  is destroyed, it does not affect resources that are currently in use. However, the  AssetBundle  itself becomes unavailable and the strong reference to any loaded resource is released. This is crucial for preventing memory leaks and ensuring that resources no longer needed are properly disposed of, while still allowing currently used resources to remain functional. 
Closing an  AssetBundle  does not affect resources currently in use, but makes the  AssetBundle  itself unavailable and releases strong references to its loaded resources. This helps prevent memory leaks and ensures unused resources are properly disposed while allowing active resources to remain functional.