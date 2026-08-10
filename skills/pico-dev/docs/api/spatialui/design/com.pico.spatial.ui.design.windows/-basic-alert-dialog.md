# BasicAlertDialog | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / BasicAlertDialog 
# BasicAlertDialog
```kotlin
@Composable
```fun  BasicAlertDialog ( onDismissRequest :  ( )  ->  Unit ,  properties :  DialogProperties  =  AlertDialogDefaults.DefaultAlertDialogProperties ,  cornerRadius :  Dp  =  AlertDialogDefaults.DialogCornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  dialogContent :  @ Composable ( )  ->  Unit ) 
Dialogs provide important prompts in a user flow. They can require an action, communicate information, or help users accomplish a task. 
#### Parameters
on Dismiss Request 
called when the user tries to dismiss the Dialog by clicking outside or pressing the back button. This is not called when the dismiss button is clicked. 
properties 
typically platform specific properties to further configure the dialog. 
corner Radius 
the corner radius used to clip this dialog 
follow Viewpoints 
The viewpoints to follow. 
dialog Content 
the content to display