# com.pico.spatial.ui.design.windows | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows 
# Package-level declarations
Types Functions Properties 
## Types
Coachmark Defaults 
```kotlin
object CoachmarkDefaults
```
Holds default values for Coachmark. 
Coachmark Direction 
```kotlin
enum CoachmarkDirection : Enum<CoachmarkDirection>
```
CoachmarkDirection is used to specify the direction of the coachmark. 
Coachmark Scope 
```kotlin
interface CoachmarkScope
```
Scope for coachmark content. 
Date Picker Dialog Defaults 
```kotlin
object DatePickerDialogDefaults
```
Object that contains the default values for  DatePickerDialog 
Snackbar Action 
```kotlin
interface SnackbarAction
```
Represents an action that can be performed in a snack. 
Snackbar Duration 
```kotlin
@JvmInline
```@ Immutable value  class  SnackbarDuration 
Represents the duration for which a snack should be displayed. 
Snackbar Host State 
```kotlin
@Stable
```interface  SnackbarHostState 
State of the  SnackbarHost , can be retrieved by  LocalSnackbarHostState  inside composable function 
Snackbar Result 
```kotlin
sealed class SnackbarResult
```
Possible results of the  SnackbarHostState.show  call 
Spatial Popup Defaults 
```kotlin
object SpatialPopupDefaults
```
hold the default values for  SpatialPopup 
Subwindow Placement 
```kotlin
enum SubwindowPlacement : Enum<SubwindowPlacement>
```
Determines the placement of the subwindow. 
Tab Bar Defaults 
```kotlin
object TabBarDefaults
```
TabBarDefaults contains the default values used by TabBar. 
Tab Bar Scope 
```kotlin
interface TabBarScope
```
TabBarScope is the scope for TabBar. It defines the interface for adding items to the TabBar. 
Toolbar Defaults 
```kotlin
object ToolbarDefaults
```
The default values of  Toolbar . 
Toolbar Segment Configuration 
```kotlin
@Immutable
```class  ToolbarSegmentConfiguration 
Configuration for a single toolbar segment. 
## Properties
Local Snackbar Host State 
```kotlin
val LocalSnackbarHostState: ProvidableCompositionLocal<SnackbarHostState>
```
Provides  SnackbarHostState 
## Functions
Alert Dialog 
```kotlin
@Composable
```fun  AlertDialog ( modifier :  Modifier  =  Modifier ,  cornerRadius :  Dp  =  AlertDialogDefaults.DialogCornerRadius ,  properties :  DialogProperties  =  AlertDialogDefaults.DefaultAlertDialogProperties ,  onDismissRequest :  ( )  ->  Unit ?  =  null ,  icon :  @ Composable ( )  ->  Unit ?  =  null ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  content :  @ Composable ( )  ->  Unit ?  =  null ,  buttons :  @ Composable ( )  ->  Unit ?  =  null ,  orientation :  Orientation  =  Orientation.Horizontal ,  padding :  PaddingValues  =  AlertDialogDefaults.DialogPadding ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ) 
Dialogs provide important prompts in a user flow. They can require an action, communicate information, or help users accomplish a task. 
Basic Alert Dialog 
```kotlin
@Composable
```fun  BasicAlertDialog ( onDismissRequest :  ( )  ->  Unit ,  properties :  DialogProperties  =  AlertDialogDefaults.DefaultAlertDialogProperties ,  cornerRadius :  Dp  =  AlertDialogDefaults.DialogCornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  dialogContent :  @ Composable ( )  ->  Unit ) 
Dialogs provide important prompts in a user flow. They can require an action, communicate information, or help users accomplish a task. 
Basic Sheet 
```kotlin
@Composable
```fun  BasicSheet ( onDismissRequest :  ( )  ->  Unit ,  properties :  DialogProperties  =  SheetDefaults.DefaultSheetsProperties ,  cornerRadius :  Dp  =  SheetDefaults.CornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  sheetContent :  @ Composable ( )  ->  Unit ) 
A basic sheet, can be used to show a sheet with custom content. usually used when the design is different from the default sheet, likes  Sheet 、 HeadImageSheet . 
Coachmark Box 
```kotlin
@Composable
```fun  CoachmarkBox ( coachmark :  @ Composable CoachmarkScope . ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  showCoachmark :  Boolean  =  true ,  direction :  CoachmarkDirection  =  CoachmarkDirection.ToEnd ,  gap :  Dp  =  CoachmarkDefaults.DefaultGap ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
CoachmarkBox  is a container for displaying a coachmark. 
Date Picker Dialog 
```kotlin
@Composable
```fun  DatePickerDialog ( onDismissRequest :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  positiveButton :  @ Composable ( )  ->  Unit ?  =  null ,  negativeButton :  @ Composable ( )  ->  Unit ?  =  null ,  properties :  DialogProperties  =  DatePickerDialogDefaults.DefaultDialogProperties ,  cornerRadius :  Dp  =  LocalTokensBearer.current.dimension.RadiusLarge ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  content :  @ Composable ( )  ->  Unit ) 
A dialog for displaying a  DatePicker  and  DateRangePicker . Date pickers let people select a date. 
Head Image Sheet 
```kotlin
@Composable
```fun  HeadImageSheet ( headerImage :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  properties :  DialogProperties  =  SheetDefaults.DefaultSheetsProperties ,  onDismissRequest :  ( )  ->  Unit ?  =  null ,  cornerRadius :  Dp  =  SheetDefaults.CornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  contentPadding :  PaddingValues  =  SheetDefaults.ContentPadding ,  contentSpace :  Dp  =  SheetDefaults.ContentSpace ,  closeIcon :  @ Composable ( )  ->  Unit  =  {
        HeadImageSheetCloseIconButton { onDismissRequest?.invoke() }
    } ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  bottom :  @ Composable ( )  ->  Unit ?  =  null ,  content :  @ Composable ( )  ->  Unit ) 
A sheet. It includes a head image, a title, a content body, and a bottom area. Only provides basic layout, you can customize it by passing  headerImage ,  title ,  content  and  bottom . The  headerImage  will be shown at the top, the  title  will be shown at the bottom of head image, the  content  will be shown in the middle of sheet, the  bottom  will be shown at the bottom of sheet. The  closeIcon  will be shown at top leading corner of sheet. 
Image Coachmark 
```kotlin
@Composable
```fun  CoachmarkScope . ImageCoachmark ( image :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  button :  @ Composable ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  LocalTokensBearer.current.dimension.RadiusLarge ,  padding :  Dp  =  ImagePadding ) 
ImageCoachmark  usually used to display image for anchor UI. It typically contains an image and an optional button. 
remember Spatial Popup Position Provider 
```kotlin
@Composable
```fun  rememberSpatialPopupPositionProvider ( horizontalPlacement :  HorizontalPlacement  =  HorizontalPlacement.alignStart() ,  verticalPlacement :  VerticalPlacement  =  VerticalPlacement.above(offset = MenuDefaults.DefaultMenuOffset) ) :  PopupPositionProvider 
Provides a  SpatialPositionProvider  that places the  SpatialPopup  relative to it's anchor view. 
Rich Coachmark 
```kotlin
@Composable
```fun  CoachmarkScope . RichCoachmark ( modifier :  Modifier  =  Modifier ,  image :  @ Composable ( )  ->  Unit ?  =  null ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  buttons :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  if (image != null) LocalTokensBearer.current.dimension.RadiusLarge
        else LocalTokensBearer.current.dimension.RadiusMedium ,  content :  @ Composable ( )  ->  Unit ) 
ImageCoachmark  usually used to display rich message for anchor UI. It typically contains an optional image, title, content and buttons. 
Sheet 
```kotlin
@Composable
```fun  Sheet ( modifier :  Modifier  =  Modifier ,  properties :  DialogProperties  =  SheetDefaults.DefaultSheetsProperties ,  onDismissRequest :  ( )  ->  Unit ?  =  null ,  cornerRadius :  Dp  =  SheetDefaults.CornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  contentPadding :  PaddingValues  =  SheetDefaults.ContentPadding ,  contentSpace :  Dp  =  SheetDefaults.ContentSpace ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  leadingAction :  @ Composable ( )  ->  Unit ?  =  {
        DefaultCloseIconButton(onClick = { onDismissRequest?.invoke() })
    } ,  trailingAction :  @ Composable ( )  ->  Unit ?  =  null ,  bottom :  @ Composable ( )  ->  Unit ?  =  null ,  content :  @ Composable ( )  ->  Unit ) 
A sheet. It includes a title, a content body, and a bottom area. Only provides basic layout, you can customize it by passing  title ,  content  and  bottom . In the title area, you can customize the leading action and trailing action. 
Simple Coachmark 
```kotlin
@Composable
```fun  CoachmarkScope . SimpleCoachmark ( text :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  button :  @ Composable ( )  ->  Unit ?  =  null ,  backgroundColor :  Color  =  CoachmarkDefaults.DefaultBackgroundColor ,  cornerSize :  Dp  =  LocalTokensBearer.current.dimension.RadiusMedium ) 
SimpleCoachmark  usually used to display brevity message for anchor UI. It typically contains text and an optional button. 
Snackbar Host 
```kotlin
@Composable
```fun  SnackbarHost ( content :  @ Composable ( )  ->  Unit ) 
A host of snack, provides  SnackbarHostState  for content to use 
Spatial Popup 
```kotlin
@Composable
```fun  SpatialPopup ( onDismissRequest :  ( )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  popupPositionProvider :  PopupPositionProvider  =  rememberSpatialPopupPositionProvider() ,  cornerRadius :  Dp  =  SpatialPopupDefaults.CornerRadius ,  defaultMinWidth :  Dp  =  SpatialPopupDefaults.DefaultWidth ,  defaultMinHeight :  Dp  =  SpatialPopupDefaults.DefaultHeight ,  properties :  PopupProperties  =  SpatialPopupDefaults.DefaultPopupProperties ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
Opens a popup with the given content. 
Subwindow 
```kotlin
@Composable
```fun  Subwindow ( rotation3D :  Rotation3D ?  =  null ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  placement :  SubwindowPlacement  =  SubwindowPlacement.Default ,  offset :  DpOffset3D  =  getGap(getLayoutDirection(placement)) ,  focusable :  Boolean  =  true ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
Subwindow is a component shown at left or right side of the window container. and it's height always fill the height of the window container. 
Tab Bar 
```kotlin
@Composable
```fun  TabBar ( followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  focusable :  Boolean  =  true ,  extraContentHeight :  Dp  =  TabBarDefaults.ExpandedContentHeight ,  content :  TabBarScope . ( )  ->  Unit ) 
TabBar is floating window will be placed at center Top of WindowContainer It is used to navigate between different views or pages for WindowContainer. It supports different item content by  TabBarScope . In  TabBarScope , you can define the item main content by MainContent which can be any image, text, or any other content. and the item label by SupportContent which is optional, badge used to show the unread count and some other information to alert the user. 
Toolbar 
```kotlin
@Composable
```fun  Toolbar ( cornerSize :  Dp  =  ToolbarDefaults.CornerRadius ,  followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  focusable :  Boolean  =  true ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
Toolbar is floating window will be placed at center bottom of WindowContainer. 
```kotlin
@Composable
```fun  Toolbar ( followViewpoints :  Set < ViewPoint >  =  ViewPoint.All ,  focusable :  Boolean  =  true ,  contentConfiguration :  ToolbarSegmentConfiguration  =  ToolbarDefaults.contentConfiguration() ,  supportingConfiguration :  ToolbarSegmentConfiguration  =  ToolbarDefaults.supportingConfiguration() ,  supportingContent :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
Segmented Toolbar overload.