# TabBarScope | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / TabBarScope 
# TabBarScope
```kotlin
interface TabBarScope
```
TabBarScope is the scope for TabBar. It defines the interface for adding items to the TabBar. 
Members 
## Functions
item 
```kotlin
abstract fun item(selected: Boolean, onClick: () -> Unit, mainContent: @Composable () -> Unit, modifier: Modifier = Modifier, badge: @Composable () -> Unit? = null, supportContent: @Composable () -> Unit? = null, extraContent: @Composable () -> Unit? = null)
```
Add an item to the TabBar.