# com.pico.spatial.ui.design.text | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.text 
# Package-level declarations
Types Functions 
## Types
Text Field Feed Back Option Action 
```kotlin
typealias TextFieldFeedBackOptionAction = (TextFieldFeedBackOption) -> Unit
```
## Functions
Text Selection And Toolbar Provider 
```kotlin
@Composable
```fun  TextSelectionAndToolbarProvider ( toolbar :  TextToolbar  =  TextToolbarAndSelectionDefaults.textToolbar() ,  colors :  TextSelectionColors  =  TextToolbarAndSelectionDefaults.textSelectionColors() ,  content :  @ Composable ( )  ->  Unit ) 
A helper composable to provide  TextSelectionColors  and  TextToolbar