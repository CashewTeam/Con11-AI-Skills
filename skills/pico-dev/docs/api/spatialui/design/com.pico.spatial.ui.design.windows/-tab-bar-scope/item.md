# item | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / TabBarScope / item 
# item
```kotlin
abstract fun item(selected: Boolean, onClick: () -> Unit, mainContent: @Composable () -> Unit, modifier: Modifier = Modifier, badge: @Composable () -> Unit? = null, supportContent: @Composable () -> Unit? = null, extraContent: @Composable () -> Unit? = null)
```
Add an item to the TabBar. 
#### Parameters
selected 
Whether the item is selected. 
on Click 
The click event of the item. 
main Content 
The main content of the item. 
modifier 
The modifier of the item. 
badge 
The badge of the item. 
support Content 
The support content of the item. 
extra Content 
The extra content shown in the expanded area below the tab row. When the selected item's  extraContent  is non-null, the expanded area uses  TabBar 's extraContentHeight; otherwise it collapses to 0dp.