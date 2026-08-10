# clone | PICO Spatial SDK

core / com.pico.spatial.core.ecs / OpacityControllerComponent / clone 
# clone
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
### Code sample:

```
class CustomComponent : Component() {    var index = 0    var name = ""    override fun clone(): Component {        val cloneComponent = CustomComponent()        cloneComponent.index = this.index        cloneComponent.name = this.name        return cloneComponent    }}
```
#### Return
A new  Component  instance that is a clone of this one.