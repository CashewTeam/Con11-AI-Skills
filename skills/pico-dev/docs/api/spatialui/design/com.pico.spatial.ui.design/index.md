# com.pico.spatial.ui.design | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design 
# Package-level declarations
Types Functions Properties 
## Types
Badge Colors 
```kotlin
@Immutable
```class  BadgeColors ( val  backgroundColor :  Color ,  val  contentColor :  Color ) 
Color defs for badge 
Badge Defaults 
```kotlin
object BadgeDefaults
```
The default values for the  Badge  component. 
Badge Size 
```kotlin
@Stable
```class  BadgeSize 
BadgeSize 
Button Colors 
```kotlin
@Immutable
```class  ButtonColors 
Holds colors used by  Button 
Button Defaults 
```kotlin
object ButtonDefaults
```
Object holding default values used by buttons 
Button Size 
```kotlin
@Stable
```class  ButtonSize 
Presents sizes used by  Button . Holds pre-defined sizes used by styled buttons like  Button . Each size has related  PaddingValues , Shape  and  TextStyle . 
Checkbox Color 
```kotlin
@Immutable
```class  CheckboxColor 
colors wrapper for  Checkbox 
Checkbox Content Size 
```kotlin
@JvmInline
```@ Immutable value  class  CheckboxContentSize ( value :  Dp ) 
Defines box content size. Means the circle diameter 
Check Box Defaults 
```kotlin
object CheckBoxDefaults
```
Contains the default values used by CheckBox 
Chip Colors 
```kotlin
@Immutable
```open  class  ChipColors 
colors for  Chip 
Chips Defaults 
```kotlin
object ChipsDefaults
```
the default values for chips. 
Chip Size 
```kotlin
@JvmInline
```value  class  ChipSize 
size for  Chip 
Circular Progress Defaults 
```kotlin
object CircularProgressDefaults
```
Default values for  CircularProgressIndicator 
Circular Progress Size 
```kotlin
@JvmInline
```value  class  CircularProgressSize 
define size spec for circular indicator 
Color Scheme 
```kotlin
@Immutable
```class  ColorScheme ( val  fillPrimary :  Color ,  val  fillSecondary :  Color ,  val  fillTertiary :  Color ,  val  fillLight :  Color ,  val  labelPrimaryLight :  Color ,  val  labelPrimary :  Color ,  val  labelSecondary :  Color ,  val  labelTertiary :  Color ,  val  labelQuaternary :  Color ,  val  lightenHover :  Color ,  val  lightenPressed :  Color ,  val  error :  Color ,  val  alert :  Color ,  val  passable :  Color ,  val  interaction :  Color ,  val  dividerLine :  Color ) 
A color scheme holds all the named color roles parameters for PICO design system. 
Date Picker Colors 
```kotlin
@Immutable
```class  DatePickerColors 
colors for  DatePicker 
Date Picker Defaults 
```kotlin
object DatePickerDefaults
```
Contains default values used by the  DatePicker . 
Date Picker Formatter 
```kotlin
interface DatePickerFormatter
```
A date formatter interface used by  DatePicker . 
Date Picker State 
```kotlin
@Stable
```interface  DatePickerState 
A state object that can be hoisted to observe the date picker state. See  rememberDatePickerState . 
Date Range Picker State 
```kotlin
@Stable
```interface  DateRangePickerState 
A state object that can be hoisted to observe the date range picker state. See  rememberDateRangePickerState . 
Divider Defaults 
```kotlin
object DividerDefaults
```
The default values for the  Divider  component. 
Header Style 
```kotlin
sealed class HeaderStyle
```
Define header style for  DatePicker . 
Icon Button Defaults 
```kotlin
object IconButtonDefaults
```
Holding IconButton default values. 
Linear Progress Defaults 
```kotlin
object LinearProgressDefaults
```
Default values for  LinearProgressIndicator 
Linear Progress Height 
```kotlin
@JvmInline
```value  class  LinearProgressHeight 
Defines height for  LinearProgressIndicator 
Link Defaults 
```kotlin
object LinkDefaults
```
Holds the default values used by  Link . 
List Item Colors 
```kotlin
@Immutable
```class  ListItemColors 
Represents the container and content colors used in a list item in different states. 
List Item Defaults 
```kotlin
object ListItemDefaults
```
Object hold default values used by  ListItem 
Number Field Colors 
```kotlin
@Immutable
```class  NumberFieldColors 
The colors for  NumberField . 
Number Field Defaults 
```kotlin
object NumberFieldDefaults
```
Object that containing default values for  NumberField . 
Number Field Size 
```kotlin
@JvmInline
```value  class  NumberFieldSize 
The size for  NumberField . 
Option Colors 
```kotlin
@Immutable
```class  OptionColors 
The colors used by  Option 
Option Defaults 
```kotlin
object OptionDefaults
```
hold default values for  Option 
Overflow 
```kotlin
enum Overflow : Enum<Overflow>
```
Number badge overflow style 
Page Control Colors 
```kotlin
@Immutable
```class  PageControlColors 
The colors of  PageControl . 
Page Control Defaults 
```kotlin
object PageControlDefaults
```
The default values of  PageControl . 
Page Control Spec 
```kotlin
@Stable
```class  PageControlSpec 
that defines the appearance of a page control. 
Pico Indication 
```kotlin
class PicoIndication(pressedColorProducer: () -> Color) : IndicationNodeFactory
```
Default state indication of PICO design. will draw a color behind content when pressed. Hover effect is support by spatialHoverEffect modifier. 
Pico Theme 
```kotlin
object PicoTheme
```
Holds getter to access the current theme values provided at the call site's position in the hierarchy. 
Progress Colors 
```kotlin
@Immutable
```open  class  ProgressColors 
defines colors for progress indicator 
Progress Indicator Edge Style 
```kotlin
enum ProgressIndicatorEdgeStyle : Enum<ProgressIndicatorEdgeStyle>
```
define edge style 
Scroll Indicator Colors 
```kotlin
@Immutable
```class  ScrollIndicatorColors ( val  trackColor :  Color ,  val  indicatorColor :  Color ,  val  scrollMarksColor :  Color ,  val  backgroundColor :  Color ) 
Colors for  ScrollIndicator . 
Scroll Indicator Defaults 
```kotlin
object ScrollIndicatorDefaults
```
Hold default configs for  ScrollIndicator 
Scroll Indicator State 
```kotlin
@Stable
```interface  ScrollIndicatorState 
State for a scroll indicator. 
Search Field Defaults 
```kotlin
object SearchFieldDefaults
```
SearchFieldDefaults 
Segment Control Colors 
```kotlin
@Immutable
```class  SegmentControlColors 
The colors used in the segment control. 
Segment Control Defaults 
```kotlin
object SegmentControlDefaults
```
Provides default values for the  SegmentControl  composable function. 
Segment Control Size 
```kotlin
@JvmInline
```value  class  SegmentControlSize 
The size of the segment control. 
Side Navigation Item Colors 
```kotlin
@Stable
```class  SideNavigationItemColors 
Holds the colors used by  SideNavigationItem . 
Side Navigation Item Defaults 
```kotlin
object SideNavigationItemDefaults
```
Contains default values used in  SideNavigationItem  components. 
Slider Colors 
```kotlin
@Immutable
```class  SliderColors 
Colors for  Slider 
Slider Defaults 
```kotlin
object SliderDefaults
```
Object hold default values used by sliders 
Slider Spec 
```kotlin
@Stable
```class  SliderSpec 
slider size wrapper 
Spatial UIProvider 
```kotlin
class SpatialUIProvider : ContentProvider
```
SpatialUI use Content Provider to access application context 
Stepper Icon Style 
```kotlin
sealed class StepperIconStyle
```
default icon style 
Switch Colors 
```kotlin
@Immutable
```class  SwitchColors 
Represents the colors used by a  Switch  in different states 
Switch Defaults 
```kotlin
object SwitchDefaults
```
Contains the default values used by  Switch 
Switch Size 
```kotlin
class SwitchSize
```
define switch size. 
Text Field Colors 
```kotlin
@Immutable
```class  TextFieldColors 
Defines  TextField  color theme 
Text Field Defaults 
```kotlin
object TextFieldDefaults
```
TextFieldDefaults 
Timepicker Config 
```kotlin
@Stable
```class  TimepickerConfig 
Wrapper for Set of  TimepickerElement  for stability 
Timepicker Element 
```kotlin
@Stable
```class  TimepickerElement 
Used by  Timepicker  to determinate which element should be shown 
Title Alignment 
```kotlin
enum TitleAlignment : Enum<TitleAlignment>
```
Define how to place title in  TitleBar 
Title Bar Colors 
```kotlin
@Immutable
```class  TitleBarColors 
The colors of  TitleBar . 
Title Bar Defaults 
```kotlin
object TitleBarDefaults
```
The default values of  TitleBar . 
Toggleable Chip Colors 
```kotlin
@Immutable
```class  ToggleableChipColors  :  ChipColors 
colors for  ToggleableChip 
Toggle Button Colors 
```kotlin
@Stable
```class  ToggleButtonColors ( checkedContainerColor :  Color ,  checkedContentColor :  Color ,  uncheckedContainerColor :  Color ,  uncheckedContentColor :  Color ) 
Holds the colors used by  ToggleButton 
Toggle Button Defaults 
```kotlin
object ToggleButtonDefaults
```
Contains the default values used by  ToggleButton 
Toggle Icon Button Defaults 
```kotlin
object ToggleIconButtonDefaults
```
Holding ToggleIconButton default values. 
Typography 
```kotlin
@Immutable
```class  Typography ( val  bodyLarge :  TextStyle ,  val  bodyLargeMultiline :  TextStyle ,  val  bodyMedium :  TextStyle ,  val  bodyMediumMultiline :  TextStyle ,  val  bodySmall :  TextStyle ,  val  bodyTiny :  TextStyle ,  val  displayLarge :  TextStyle ,  val  displayMedium :  TextStyle ,  val  displaySmall :  TextStyle ,  val  headlineLarge :  TextStyle ,  val  headlineMedium :  TextStyle ,  val  headlineSmall :  TextStyle ,  val  labelLarge :  TextStyle ,  val  labelMedium :  TextStyle ,  val  labelSmall :  TextStyle ,  val  titleLarge :  TextStyle ,  val  titleMedium :  TextStyle ,  val  titleSmall :  TextStyle ) 
Typography used by PICO Design 
Wheel Picker Colors 
```kotlin
@Immutable
```class  WheelPickerColors 
Define colors for  WheelPicker 
Wheel Picker Defaults 
```kotlin
object WheelPickerDefaults
```
Object that contains default values for  WheelPicker 
## Properties
Local Content Color 
```kotlin
val LocalContentColor: ProvidableCompositionLocal<Color>
```
CompositionLocal containing the preferred content color for a given position in the hierarchy. 
Local Disable Alpha 
```kotlin
val LocalDisableAlpha: ProvidableCompositionLocal<Float>
```
CompositionLocal containing the alpha value for component's disabled state 
Local Text Style 
```kotlin
val LocalTextStyle: ProvidableCompositionLocal<TextStyle>
```
CompositionLocal provides  TextStyle  used by  Text  components by default. To set the value of this CompositionLocal, see  ProvideTextStyle . 
## Functions
Badge 
```kotlin
@Composable
```fun  Badge ( modifier :  Modifier  =  Modifier ,  badgeColor :  BadgeColors  =  BadgeDefaults.badgeColors() ,  badgeSize :  BadgeSize  =  BadgeDefaults.Small ,  radius :  Dp  =  badgeSize.badgeRadius() ,  contentPadding :  PaddingValues  =  badgeSize.badgePadding() ,  textStyle :  TextStyle  =  PicoTheme.typography.bodySmall ,  content :  @ Composable RowScope . ( )  ->  Unit ?  =  null ) 
Badge is a component that can contain dynamic information, such as the presence of a new notification or a number of pending requests. Badges can be icon only or contain short text. 
badge Padding 
```kotlin
@Composable
```fun  BadgeSize . badgePadding ( ) :  PaddingValues 
Calculates the inner padding values for a badge based on its size. 
badge Radius 
```kotlin
fun BadgeSize.badgeRadius(): Dp
```
Calculates the corner radius for a badge. This function determines the appropriate radius based on the badge size. 
Basic Scroll Indicator 
```kotlin
@Composable
```fun  BasicScrollIndicator ( state :  ScrollIndicatorState ,  modifier :  Modifier  =  Modifier ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.ZeroPadding ,  contentPadding :  PaddingValues  =  ScrollIndicatorDefaults.TrackPadding ) 
Basic implementation of scroll indicator. Different to  ScrollIndicator  with  BoxScope , this implementation can be placed anywhere in the tree. And it's always visible. 
Button 
```kotlin
@Composable
```fun  Button ( onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  size :  ButtonSize  =  ButtonDefaults.Regular ,  colors :  ButtonColors  =  ButtonDefaults.buttonColors() ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  contentPadding :  PaddingValues  =  ButtonDefaults.paddingForButtonSize(
            size,
            haveIcon = leadingIcon != null || trailingIcon != null,
        ) ,  shape :  Shape  =  ButtonDefaults.shapeForButtonSize(size) ,  gap :  Dp  =  ButtonDefaults.gapForButtonSize(
            size,
            haveIcon = leadingIcon != null || trailingIcon != null,
        ) ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
A stylized button component defined by PICO design which can be easily used by passing pre-defined  ButtonSize  and  ButtonColors . Each pre-defined  ButtonSize  has related  PaddingValues , Shape , gap  and  TextStyle . 
Button Chip 
```kotlin
@Composable
```fun  ButtonChip ( label :  @ Composable ( )  ->  Unit ,  onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  chipSize :  ChipSize  =  ChipsDefaults.Small ,  colors :  ChipColors  =  ChipsDefaults.chipColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Button-like Chip 
Checkbox 
```kotlin
@Composable
```fun  Checkbox ( checked :  Boolean ,  onCheckedChange :  ( Boolean )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  contentSize :  CheckboxContentSize  =  CheckBoxDefaults.Regular ,  colors :  CheckboxColor  =  CheckBoxDefaults.checkboxColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Checkboxes allow users to select one or more items from a set. Checkboxes can turn an option on or off. 
Chip 
```kotlin
@Composable
```fun  Chip ( label :  @ Composable ( )  ->  Unit ,  onClick :  ( )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  colors :  ChipColors  =  ChipsDefaults.chipColors() ,  chipSize :  ChipSize  =  ChipsDefaults.Small ,  contentPadding :  PaddingValues  =  chipSize.contentPadding(leading = leadingIcon != null) ,  contentGap :  Dp  =  chipSize.contentGap() ,  shape :  Shape  =  RoundedCornerShape(chipSize.cornerRadius()) ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Basic chip. 
Circular Progress Indicator 
```kotlin
@Composable
```fun  CircularProgressIndicator ( modifier :  Modifier  =  Modifier ,  color :  Color  =  PicoTheme.colorScheme.labelPrimaryLight ,  progressSize :  CircularProgressSize  =  CircularProgressDefaults.Small ,  strokeWidth :  Dp  =  progressSize.strokeWidth() ) 
Progress indicators express an unspecified wait time, such as loading. 
```kotlin
@Composable
```fun  CircularProgressIndicator ( progress :  ( )  ->  Float ,  modifier :  Modifier  =  Modifier ,  colors :  ProgressColors  =  CircularProgressDefaults.circleProgressColors() ,  edgeStyle :  ProgressIndicatorEdgeStyle  =  ProgressIndicatorEdgeStyle.RoundCorner ,  progressSize :  CircularProgressSize  =  CircularProgressDefaults.Small ,  strokeWidth :  Dp  =  progressSize.strokeWidth() ) 
Progress indicators display the length of a process. 
container Corner Radius 
```kotlin
fun SegmentControlSize.containerCornerRadius(): Dp
```
The corner radius of the segment control. 
content Gap 
```kotlin
fun ChipSize.contentGap(): Dp
```
Calculates the content gap for a given  ChipSize . 
content Padding 
```kotlin
fun ChipSize.contentPadding(leading: Boolean = false): PaddingValues
```
Calculates the content padding for a given  ChipSize . 
corner Radius 
```kotlin
fun ChipSize.cornerRadius(): Dp
```
Calculates the corner radius for a given  ChipSize . 
Date Picker 
```kotlin
@Composable
```fun  DatePicker ( onDateSelected :  ( selectedDateMillis :  Long )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  state :  DatePickerState  =  rememberDatePickerState() ,  dateFormatter :  DatePickerFormatter  =  remember { DatePickerDefaults.dateFormatter() } ,  colors :  DatePickerColors  =  DatePickerDefaults.datePickerColors() ,  headerStyle :  HeaderStyle  =  HeaderStyle.Navigation(true) ) 
DatePicker is a component that allows users to select a date. 
Date Range Picker 
```kotlin
@Composable
```fun  DateRangePicker ( onStartSelected :  ( startDateInMillis :  Long )  ->  Unit ,  onEndSelected :  ( endDateInMillis :  Long ? )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  state :  DateRangePickerState  =  rememberDateRangePickerState() ,  dateFormatter :  DatePickerFormatter  =  remember { DatePickerDefaults.dateFormatter() } ,  colors :  DatePickerColors  =  DatePickerDefaults.datePickerColors() ,  headerStyle :  HeaderStyle  =  HeaderStyle.Navigation(true) ) 
Date range pickers let people select a range of dates and can be embedded into Dialogs. 
default Color Scheme 
```kotlin
fun defaultColorScheme(fillPrimary: Color = ColorTokens.Default.FillDarkerAlpha, fillSecondary: Color = ColorTokens.Default.FillSemilightAlpha, fillTertiary: Color = ColorTokens.Default.FillNeutralAlpha, fillLight: Color = ColorTokens.Default.FillLightAlpha, labelPrimaryLight: Color = ColorTokens.Default.SubWhite100, labelPrimary: Color = ColorTokens.Default.LabelDarkestAlpha, labelSecondary: Color = ColorTokens.Default.LabelUltradarkAlpha, labelTertiary: Color = ColorTokens.Default.LabelSemidarkAlpha, labelQuaternary: Color = ColorTokens.Default.LabelDarkAlpha, lightenHover: Color = ColorTokens.Default.FillSemilightAlpha, lightenPressed: Color = ColorTokens.Default.FillSemilightAlpha, error: Color = ColorTokens.Default.SubRed100, alert: Color = ColorTokens.Default.SubOrange100, passable: Color = ColorTokens.Default.SubGreen100, interaction: Color = ColorTokens.Default.SubBlue100, dividerLine: Color = ColorTokens.Default.SubBlack12): ColorScheme
```
The default color scheme that does not use vibrant colors. 
Divider 
```kotlin
@Composable
```fun  Divider ( modifier :  Modifier  =  Modifier ,  color :  Color  =  DividerDefaults.color ,  thickness :  Dp  =  DividerDefaults.thickness ,  orientation :  Orientation  =  Orientation.Horizontal ) 
A divider is a thin line that groups content in lists and layouts. 
Dot Badge 
```kotlin
@Composable
```fun  DotBadge ( modifier :  Modifier  =  Modifier ,  color :  Color  =  BadgeDefaults.DotColor ) 
Dot badge 
Horizontal Divider 
```kotlin
@Composable
```fun  HorizontalDivider ( modifier :  Modifier  =  Modifier ,  color :  Color  =  DividerDefaults.color ,  thickness :  Dp  =  DividerDefaults.thickness ) 
A divider is a thin line that groups content in lists and layouts. 
Icon 
```kotlin
@Composable
```fun  Icon ( bitmap :  ImageBitmap ,  contentDescription :  String ? ,  modifier :  Modifier  =  Modifier ,  tint :  Color  =  LocalContentColor.current ) 
A PICO design icon component that draws  bitmap  using  tint , with a default value of  LocalContentColor . If  bitmap  has no intrinsic size, this component uses the recommended default size. Icon is an opinionated component designed to be used with single-color icons so that they can be tinted correctly for the component they are placed in. For multicolored icons and icons that should not be tinted, use  Color.Unspecified  for  tint . For generic images that should not be tinted, and do not follow the recommended icon size, use the generic  androidx.compose.foundation.Image  instead. For a clickable icon, see  IconButton . 
```kotlin
@Composable
```fun  Icon ( painter :  Painter ,  contentDescription :  String ? ,  modifier :  Modifier  =  Modifier ,  tint :  Color  =  LocalContentColor.current ) 
A PICO design icon component that draws  painter  using  tint , with a default value of  LocalContentColor . If  painter  has no intrinsic size, this component uses the recommended default size. Icon is an opinionated component designed to be used with single-color icons so that they can be tinted correctly for the component they are placed in. For multicolored icons and icons that should not be tinted, use  Color.Unspecified  for  tint . For generic images that should not be tinted, and do not follow the recommended icon size, use the generic  androidx.compose.foundation.Image  instead. For a clickable icon, see  IconButton . 
```kotlin
@Composable
```fun  Icon ( imageVector :  ImageVector ,  contentDescription :  String ? ,  modifier :  Modifier  =  Modifier ,  tint :  Color  =  LocalContentColor.current ) 
A PICO design icon component that draws  imageVector  using  tint , with a default value of  LocalContentColor . If  imageVector  has no intrinsic size, this component uses the recommended default size. Icon is an opinionated component designed to be used with single-color icons so that they can be tinted correctly for the component they are placed in. For multicolored icons and icons that should not be tinted, use  Color.Unspecified  for  tint . For generic images that should not be tinted, and do not follow the recommended icon size, use the generic  androidx.compose.foundation.Image  instead. For a clickable icon, see  IconButton . 
Icon Button 
```kotlin
@Composable
```fun  IconButton ( onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  colors :  ButtonColors  =  IconButtonDefaults.iconButtonColors() ,  size :  ButtonSize  =  IconButtonDefaults.Regular ,  shape :  Shape  =  IconButtonDefaults.DefaultShape ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable ( )  ->  Unit ) 
Icon button defined by PICO design 
item Content Padding 
```kotlin
fun SegmentControlSize.itemContentPadding(): PaddingValues
```
The content padding of the segment control item. 
Linear Progress Indicator 
```kotlin
@Composable
```fun  LinearProgressIndicator ( progress :  ( )  ->  Float ,  modifier :  Modifier  =  Modifier ,  colors :  ProgressColors  =  LinearProgressDefaults.linearProgressColors() ,  edgeStyle :  ProgressIndicatorEdgeStyle  =  ProgressIndicatorEdgeStyle.RoundCorner ,  height :  LinearProgressHeight  =  LinearProgressDefaults.Small ) 
Progress indicators express an unspecified wait time or display the length of a process. By default there is no animation between  progress  values. 
Link 
```kotlin
@Composable
```fun  Link ( onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  size :  ButtonSize  =  LinkDefaults.Regular ,  shape :  Shape  =  size.shapeForLink() ,  colors :  ButtonColors  =  LinkDefaults.defaultColors() ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  semanticsContent :  String ?  =  null ,  contentPadding :  PaddingValues  =  size.paddingForLink(trailingIcon != null) ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
A  Link  is a text button with a optional trailing icon. 
List Item 
```kotlin
@Composable
```fun  ListItem ( headlineContent :  @ Composable ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  supportingContent :  @ Composable ( )  ->  Unit ?  =  null ,  leadingContent :  @ Composable BoxScope . ( )  ->  Unit ?  =  null ,  trailingContent :  @ Composable BoxScope . ( )  ->  Unit ?  =  null ,  colors :  ListItemColors  =  ListItemDefaults.listItemColors() ,  padding :  PaddingValues  =  ListItemDefaults.DefaultPadding ,  shape :  Shape  =  ListItemDefaults.shape ) 
This component can be used to achieve the list item templates existing in the spec. 
Number Badge 
```kotlin
@Composable
```fun  NumberBadge ( modifier :  Modifier  =  Modifier ,  number :  Int ,  threshold :  Int  =  BadgeDefaults.OverflowThreshold ,  overflow :  Overflow  =  Overflow.Plus ,  textStyle :  TextStyle  =  BadgeDefaults.NumberTextStyle ,  badgeSize :  BadgeSize  =  BadgeDefaults.NumberSmall ,  badgeColor :  BadgeColors  =  BadgeDefaults.numberBadgeColors() ,  contentPadding :  PaddingValues  =  badgeSize.badgePadding() ) 
A  Badge  that is used to show numbers 
Number Field 
```kotlin
@Composable
```fun  NumberField ( value :  Int ,  onValueChange :  ( Int )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  increaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultIncreaseIcon() ,  decreaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultDecreaseIcon() ,  stepLength :  Int  =  1 ,  valueRange :  IntRange  =  NumberFieldDefaults.DefaultRange ,  colors :  NumberFieldColors  =  NumberFieldDefaults.numberFieldColors() ,  size :  NumberFieldSize  =  NumberFieldDefaults.defaultSize() ,  cornerSize :  Dp  =  size.height.cornerSize() ,  gap :  Dp  =  NumberFieldDefaults.DefaultGap ,  enabled :  Boolean  =  true ,  editable :  Boolean  =  true ,  textStyle :  TextStyle  =  NumberFieldDefaults.defaultTextStyle(size.height) ,  keyboardOptions :  KeyboardOptions  =  NumberFieldDefaults.DefaultKeyboardOptions ,  unit :  String ?  =  null ,  spacerWidth :  Dp  =  NumberFieldDefaults.DefaultSpacerWidth ) 
```kotlin
@Composable
```fun  NumberField ( value :  Double ,  onValueChange :  ( Double )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  increaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultIncreaseIcon() ,  decreaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultDecreaseIcon() ,  stepLength :  Double  =  1.0 ,  valueRange :  ClosedFloatingPointRange < Double >  =  NumberFieldDefaults.DefaultDoubleRange ,  colors :  NumberFieldColors  =  NumberFieldDefaults.numberFieldColors() ,  size :  NumberFieldSize  =  NumberFieldDefaults.defaultSize() ,  cornerSize :  Dp  =  size.height.cornerSize() ,  gap :  Dp  =  NumberFieldDefaults.DefaultGap ,  enabled :  Boolean  =  true ,  editable :  Boolean  =  true ,  textStyle :  TextStyle  =  NumberFieldDefaults.defaultTextStyle(size.height) ,  keyboardOptions :  KeyboardOptions  =  NumberFieldDefaults.DefaultKeyboardOptions ,  unit :  String ?  =  null ,  spacerWidth :  Dp  =  NumberFieldDefaults.DefaultSpacerWidth ,  fractionDigits :  Int  =  1 ) 
```kotlin
@Composable
```fun  NumberField ( value :  Float ,  onValueChange :  ( Float )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  increaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultIncreaseIcon() ,  decreaseIcon :  @ Composable ( )  ->  Unit  =  NumberFieldDefaults.defaultDecreaseIcon() ,  stepLength :  Float  =  1.0f ,  valueRange :  ClosedFloatingPointRange < Float >  =  NumberFieldDefaults.DefaultFloatRange ,  colors :  NumberFieldColors  =  NumberFieldDefaults.numberFieldColors() ,  size :  NumberFieldSize  =  NumberFieldDefaults.defaultSize() ,  cornerSize :  Dp  =  size.height.cornerSize() ,  gap :  Dp  =  NumberFieldDefaults.DefaultGap ,  enabled :  Boolean  =  true ,  editable :  Boolean  =  true ,  textStyle :  TextStyle  =  NumberFieldDefaults.defaultTextStyle(size.height) ,  keyboardOptions :  KeyboardOptions  =  NumberFieldDefaults.DefaultKeyboardOptions ,  unit :  String ?  =  null ,  spacerWidth :  Dp  =  NumberFieldDefaults.DefaultSpacerWidth ,  fractionDigits :  Int  =  1 ) 
NumberField  is used to create a number input field with increase and decrease buttons. 
Option 
```kotlin
@Composable
```fun  Option ( selected :  Boolean ,  onSelectChange :  ( selected :  Boolean )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  icon :  @ Composable ( )  ->  Unit ?  =  null ,  colors :  OptionColors  =  OptionDefaults.optionColors() ,  enabled :  Boolean  =  true ,  gap :  Dp  =  OptionDefaults.Gap ,  shape :  Shape  =  OptionDefaults.Shape ,  contentPadding :  PaddingValues  =  OptionDefaults.ContentPadding ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable ( )  ->  Unit ) 
Option is a stylized button component defined by PICO design witch has a  selected  state. And usually has a  Text  and optional leading  icon . 
Page Control 
```kotlin
@Composable
```fun  PageControl ( currentIndex :  Int ,  onClickAction :  ( Int )  ->  Unit ,  @ IntRange ( from  =  0 ) totalDots :  Int ,  modifier :  Modifier  =  Modifier ,  colors :  PageControlColors  =  PageControlDefaults.pageControlColors() ,  selectIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  maxDisplayCount :  Int  =  PageControlDefaults.NormalMax ,  pageControlSpec :  PageControlSpec  =  PageControlDefaults.Spec ) 
PageControl used to create a page indicator. 
Pico Theme 
```kotlin
@Composable
```fun  PicoTheme ( colorScheme :  ColorScheme  =  systemColorScheme(LocalContext.current) ,  typography :  Typography ?  =  null ,  content :  @ Composable ( )  ->  Unit ) 
Provides PICO theme values. 
Progress Page Control 
```kotlin
@Composable
```fun  ProgressPageControl ( currentIndex :  Int ,  onClickAction :  ( Int )  ->  Unit ,  @ IntRange ( from  =  0 ) totalDots :  Int ,  currentProgress :  ( )  ->  Float ,  modifier :  Modifier  =  Modifier ,  colors :  PageControlColors  =  PageControlDefaults.pageControlColors() ,  enabled :  Boolean  =  true ,  maxDisplayCount :  Int  =  PageControlDefaults.ProgressMax ,  pageControlSpec :  PageControlSpec  =  PageControlDefaults.Spec ) 
ProgressPageControl used to create a page indicator, each dot has a progress indicator. 
Provide Text Style 
```kotlin
@Composable
```fun  ProvideTextStyle ( textStyle :  TextStyle ,  content :  @ Composable ( )  ->  Unit ) 
This function will merge the given style values with current values for any missing attributes. Any  Text  included in this component will be styled with the merged style by default. 
remember Date Picker State 
```kotlin
@Composable
```fun  rememberDatePickerState ( initialSelectedDateMillis :  Long ?  =  null ,  initialDisplayedMonthMillis :  Long ?  =  initialSelectedDateMillis ) :  DatePickerState 
Creates a  DatePickerState  for a  DatePicker  that is remembered across compositions. 
remember Date Range Picker State 
```kotlin
@Composable
```fun  rememberDateRangePickerState ( initialSelectedStartDateMillis :  Long ?  =  null ,  initialSelectedEndDateMillis :  Long ?  =  null ,  initialDisplayedMonthMillis :  Long ?  =  initialSelectedStartDateMillis ) :  DateRangePickerState 
Creates a  DateRangePickerState  for a  DateRangePicker  that is remembered across compositions. 
remember Scroll Indicator State 
```kotlin
@Composable
```fun  rememberScrollIndicatorState ( state :  LazyListState ) :  ScrollIndicatorState 
Create a  ScrollIndicatorState  for  LazyListState . 
```kotlin
@Composable
```fun  rememberScrollIndicatorState ( state :  LazyGridState ) :  ScrollIndicatorState 
Create a  ScrollIndicatorState  for  LazyGridState . 
```kotlin
@Composable
```fun  rememberScrollIndicatorState ( state :  LazyStaggeredGridState ) :  ScrollIndicatorState 
Create a  ScrollIndicatorState  for  LazyStaggeredGridState . 
```kotlin
@Composable
```fun  rememberScrollIndicatorState ( orientation :  Orientation ,  state :  ScrollState ) :  ScrollIndicatorState 
Create a  ScrollIndicatorState  for  ScrollState . 
remember Wheel State 
```kotlin
@Composable
```fun  rememberWheelState ( vararg  inputs :  Any ? ,  initialFirstVisibleItemIndex :  Int  =  0 ,  initialFirstVisibleItemScrollOffset :  Int  =  0 ) :  LazyListState 
state for  WheelPicker 
Removable Chip 
```kotlin
@Composable
```fun  RemovableChip ( label :  @ Composable ( )  ->  Unit ,  onLeadingClick :  ( )  ->  Unit ,  onTrailingRemoveClick :  ( )  ->  Unit ,  visible :  Boolean ,  modifier :  Modifier  =  Modifier ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  colors :  ChipColors  =  ChipsDefaults.chipColors() ,  chipSize :  ChipSize  =  ChipsDefaults.Small ,  contentPadding :  PaddingValues  =  chipSize.removeChipPadding(leadingIcon != null) ,  contentGap :  Dp  =  chipSize.contentGap() ,  shape :  Shape  =  RoundedCornerShape(chipSize.cornerRadius()) ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
A chip which is removable 
remove Chip Icon Size 
```kotlin
fun ChipSize.removeChipIconSize(): Dp
```
Calculates the icon size for a given  ChipSize  in  RemovableChip . 
remove Chip Padding 
```kotlin
fun ChipSize.removeChipPadding(leading: Boolean = false): PaddingValues
```
Calculates the padding for a given  ChipSize  in  RemovableChip . 
Scroll Indicator 
```kotlin
@Composable
```fun  BoxScope . ScrollIndicator ( state :  LazyListState ,  modifier :  Modifier  =  Modifier ,  alignment :  Alignment  =  if (state.layoutInfo.orientation == Orientation.Vertical) Alignment.CenterEnd
        else Alignment.BottomCenter ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.defaultHotAreaPadding(state.layoutInfo.orientation, alignment) ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  minVisibleSize :  Dp  =  ScrollIndicatorDefaults.MinSize ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  dismissAfter :  Long  =  3000 ) 
Scroll indicator is used to indicate scrolling progress of a list view, just like  LazyColumn  or  LazyRow . You can also drag the indicator to scroll the content of list view. 
```kotlin
@Composable
```fun  BoxScope . ScrollIndicator ( state :  LazyGridState ,  modifier :  Modifier  =  Modifier ,  alignment :  Alignment  =  if (state.layoutInfo.orientation == Orientation.Vertical) Alignment.CenterEnd
        else Alignment.BottomCenter ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.defaultHotAreaPadding(
            orientation = state.layoutInfo.orientation,
            alignment = alignment,
        ) ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  minVisibleSize :  Dp  =  ScrollIndicatorDefaults.MinSize ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  dismissAfter :  Long  =  3000 ) 
Scroll indicator is used to indicate scrolling progress of a grid view, just like  LazyHorizontalGrid  or  LazyVerticalGrid . You can also drag the indicator to scroll the content of grid view. 
```kotlin
@Composable
```fun  BoxScope . ScrollIndicator ( state :  LazyStaggeredGridState ,  modifier :  Modifier  =  Modifier ,  alignment :  Alignment  =  if (state.layoutInfo.orientation == Orientation.Vertical) Alignment.CenterEnd
        else Alignment.BottomCenter ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.defaultHotAreaPadding(
            orientation = state.layoutInfo.orientation,
            alignment = alignment,
        ) ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  minVisibleSize :  Dp  =  ScrollIndicatorDefaults.MinSize ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  dismissAfter :  Long  =  3000 ) 
Scroll indicator is used to indicate scrolling progress of a staggered grid view, just like  LazyHorizontalStaggeredGrid  or  LazyVerticalStaggeredGrid . You can also drag the indicator to scroll the content of grid view. 
```kotlin
@Composable
```fun  BoxScope . ScrollIndicator ( state :  ScrollState ,  orientation :  Orientation ,  modifier :  Modifier  =  Modifier ,  alignment :  Alignment  =  if (orientation == Orientation.Vertical) Alignment.CenterEnd else Alignment.BottomCenter ,  paddingForInteraction :  PaddingValues  =  ScrollIndicatorDefaults.defaultHotAreaPadding(orientation, alignment) ,  colors :  ScrollIndicatorColors  =  ScrollIndicatorDefaults.scrollIndicatorColors() ,  minVisibleSize :  Dp  =  ScrollIndicatorDefaults.MinSize ,  scrollingMarkSize :  Dp  =  ScrollIndicatorDefaults.ScrollingMarkSize ,  dismissAfter :  Long  =  3000 ) 
Scroll indicator is used to indicate scrolling progress of a scrollable view with Modifier.verticalScroll or Modifier.horizontalScroll, like  Column  or  Row . You can also drag the indicator to scroll the content of scrollable view. 
Search Field 
```kotlin
@Composable
```fun  SearchField ( value :  String ,  onValueChange :  ( String )  ->  Unit ,  onSearch :  ( String )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  leadingContent :  @ Composable ( )  ->  Unit  =  SearchFieldDefaults.searchIcon() ,  enabled :  Boolean  =  true ,  textStyle :  TextStyle  =  SearchFieldDefaults.DefaultTextStyle ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  100.dp ,  colors :  TextFieldColors  =  SearchFieldDefaults.searchFieldColors() ) 
Search field allows users to input text, and trigger a search action either by pressing the search button on the keyboard or other means. 
Segment Control 
```kotlin
@Composable
```fun  SegmentControl ( modifier :  Modifier  =  Modifier ,  backgroundColor :  Color  =  SegmentControlDefaults.backgroundColor ,  itemSpace :  Dp  =  SegmentControlDefaults.ItemSpace ,  contentPadding :  Dp  =  SegmentControlDefaults.ContainerPadding ,  cornerRadius :  Dp  =  SegmentControlDefaults.Small.containerCornerRadius() ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
Segment control with Texts or Icons 
Segment Item 
```kotlin
@Composable
```fun  RowScope . SegmentItem ( selected :  Boolean ,  onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  textStyle :  TextStyle  =  SegmentControlDefaults.Small.textStyle() ,  colors :  SegmentControlColors  =  SegmentControlDefaults.colors() ,  title :  @ Composable ( )  ->  Unit ?  =  null ,  icon :  @ Composable ( )  ->  Unit ?  =  null ,  contentPadding :  PaddingValues  =  SegmentControlDefaults.Small.itemContentPadding() ,  gap :  Dp  =  SegmentControlDefaults.ItemGap ) 
A composable function that creates a basic segment item. The segment item can be used as a building block for creating the text and icon segment controls. 
Segment Slider 
```kotlin
@Composable
```fun  SegmentSlider ( initialStep :  Int ,  segmentCount :  Int ,  onStepChange :  ( newStep :  Int )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  sliderSpec :  SliderSpec  =  SliderDefaults.Regular ,  colors :  SliderColors  =  SliderDefaults.sliderColors() ) 
Sliders allow users to make selections range from 0 to  segmentCount 
Side Navigation 
```kotlin
@Composable
```fun  SideNavigation ( modifier :  Modifier  =  Modifier ,  scrollState :  ScrollState  =  rememberScrollState() ,  contentPadding :  PaddingValues  =  SideNavigationDefaults.DefaultContentPadding ,  headerColor :  Color  =  SideNavigationDefaults.headerColor ,  header :  @ Composable BoxScope . ( )  ->  Unit ?  =  null ,  content :  @ Composable ColumnScope . ( )  ->  Unit ) 
A vertical navigation component typically used for primary navigation patterns. 
Side Navigation Item 
```kotlin
@Composable
```fun  SideNavigationItem ( selected :  Boolean ,  modifier :  Modifier  =  Modifier ,  horizontalArrangement :  Arrangement.Horizontal  =  SideNavigationItemDefaults.HorizontalArrangement ,  shape :  Shape  =  SideNavigationItemDefaults.Shape ,  contentPadding :  PaddingValues  =  SideNavigationItemDefaults.ContentPadding ,  colors :  SideNavigationItemColors  =  SideNavigationItemDefaults.colors() ,  leading :  @ Composable BoxScope . ( )  ->  Unit ?  =  null ,  trailing :  @ Composable BoxScope . ( )  ->  Unit ?  =  null ,  content :  @ Composable BoxScope . ( )  ->  Unit ) 
A single navigation item within a  SideNavigation  or  SideNavigationSection . 
Side Navigation Section 
```kotlin
@Composable
```fun  SideNavigationSection ( modifier :  Modifier  =  Modifier ,  contentPadding :  PaddingValues  =  SideNavigationDefaults.DefaultSectionContentPadding ,  titlePadding :  PaddingValues  =  SideNavigationDefaults.DefaultSectionTitlePadding ,  sectionColor :  Color  =  SideNavigationDefaults.sectionColor ,  title :  @ Composable BoxScope . ( )  ->  Unit ,  content :  @ Composable ColumnScope . ( )  ->  Unit ) 
A section within a  SideNavigation  that groups related navigation items. 
Slider 
```kotlin
@Composable
```fun  Slider ( value :  Float ,  onValueChange :  ( newValue :  Float )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  valueRange :  ClosedFloatingPointRange < Float >  =  0f..1f ,  onValueChangeFinished :  ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  sliderSpec :  SliderSpec  =  SliderDefaults.Regular ,  colors :  SliderColors  =  SliderDefaults.sliderColors() ) 
Continuous sliders allow users to make selections in valueRange 
Stepper 
```kotlin
@Composable
```fun  Stepper ( value :  String ,  onStep :  ( step :  Int )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  decreaseIcon :  @ Composable ( )  ->  Unit  =  StepperIconStyle.MinusAndAdd.iconDecrease() ,  increaseIcon :  @ Composable ( )  ->  Unit  =  StepperIconStyle.MinusAndAdd.iconIncrease() ,  stepLength :  Int  =  1 ,  increasable :  Boolean  =  true ,  decreasable :  Boolean  =  true ,  onEdited :  ( newValue :  String )  ->  Unit ?  =  null ,  editable :  Boolean  =  onEdited != null ,  textStyle :  TextStyle  =  PicoTheme.typography.titleMedium.copy(fontWeight = FontWeight.Normal) ,  textColor :  Color  =  PicoTheme.colorScheme.labelPrimary ,  paddingValues :  PaddingValues  =  PaddingValues(defaultPadding) ,  backgroundShape :  Shape  =  RoundedCornerShape(10.dp) ,  backgroundColor :  Color  =  PicoTheme.colorScheme.fillTertiary ,  cursorBrush :  Brush  =  SolidColor(PicoTheme.colorScheme.fillPrimary) ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ) 
Basic implement of a stepper. 
Switch 
```kotlin
@Composable
```fun  Switch ( checked :  Boolean ,  onCheckedChange :  ( Boolean )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  enabled :  Boolean  =  true ,  colors :  SwitchColors  =  SwitchDefaults.switchColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Switches toggle the state of a single item on or off. 
Symbolic Circular Progress Indicator 
```kotlin
@Composable
```fun  SymbolicCircularProgressIndicator ( progress :  ( )  ->  Float ,  progressSymbol :  @ Composable ( )  ->  Unit ? ,  modifier :  Modifier  =  Modifier ,  colors :  ProgressColors  =  CircularProgressDefaults.circleProgressColors() ,  progressSize :  CircularProgressSize  =  CircularProgressDefaults.Small ,  strokeWidth :  Dp  =  progressSize.strokeWidth() ,  edgeStyle :  ProgressIndicatorEdgeStyle  =  ProgressIndicatorEdgeStyle.RoundCorner ) 
Progress indicators display the length of a process. When  progress  is 1.0f, a complete animation will be display. A  progressSymbol  is optional for you to display the progress details 
Symbol Slider 
```kotlin
@Composable
```fun  SymbolSlider ( value :  Float ,  onValueChange :  ( newValue :  Float )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  valueRange :  ClosedFloatingPointRange < Float >  =  0f..1f ,  icon :  @ Composable ( )  ->  Unit ,  onValueChangeFinished :  ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  sliderSpec :  SliderSpec  =  SliderDefaults.Regular ,  colors :  SliderColors  =  SliderDefaults.sliderColors() ) 
Continuous sliders allow users to make selections in  valueRange . 
system Color Scheme 
```kotlin
fun systemColorScheme(context: Context): ColorScheme
```
The colors will be load from system resources. 
Text 
```kotlin
@Composable
```fun  Text ( text :  String ,  modifier :  Modifier  =  Modifier ,  color :  Color  =  Color.Unspecified ,  autoSize :  TextAutoSize ?  =  null ,  fontSize :  TextUnit  =  TextUnit.Unspecified ,  fontStyle :  FontStyle ?  =  null ,  fontWeight :  FontWeight ?  =  null ,  fontFamily :  FontFamily ?  =  null ,  letterSpacing :  TextUnit  =  TextUnit.Unspecified ,  textDecoration :  TextDecoration ?  =  null ,  textAlign :  TextAlign  =  TextAlign.Unspecified ,  lineHeight :  TextUnit  =  TextUnit.Unspecified ,  overflow :  TextOverflow  =  TextOverflow.Clip ,  softWrap :  Boolean  =  true ,  maxLines :  Int  =  Int.MAX_VALUE ,  minLines :  Int  =  1 ,  onTextLayout :  ( TextLayoutResult )  ->  Unit ?  =  null ,  style :  TextStyle  =  LocalTextStyle.current ) 
```kotlin
@Composable
```fun  Text ( text :  AnnotatedString ,  modifier :  Modifier  =  Modifier ,  color :  Color  =  Color.Unspecified ,  autoSize :  TextAutoSize ?  =  null ,  fontSize :  TextUnit  =  TextUnit.Unspecified ,  fontStyle :  FontStyle ?  =  null ,  fontWeight :  FontWeight ?  =  null ,  fontFamily :  FontFamily ?  =  null ,  letterSpacing :  TextUnit  =  TextUnit.Unspecified ,  textDecoration :  TextDecoration ?  =  null ,  textAlign :  TextAlign  =  TextAlign.Unspecified ,  lineHeight :  TextUnit  =  TextUnit.Unspecified ,  overflow :  TextOverflow  =  TextOverflow.Clip ,  softWrap :  Boolean  =  true ,  maxLines :  Int  =  Int.MAX_VALUE ,  minLines :  Int  =  1 ,  inlineContent :  Map < String ,  InlineTextContent >  =  mapOf() ,  onTextLayout :  ( TextLayoutResult )  ->  Unit ?  =  null ,  style :  TextStyle  =  LocalTextStyle.current ) 
High level PICO design component to display text. 
Text Area 
```kotlin
@Composable
```fun  TextArea ( value :  TextFieldValue ,  onValueChange :  ( TextFieldValue )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  supportingText :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  readOnly :  Boolean  =  false ,  textStyle :  TextStyle  =  TextFieldDefaults.DefaultTextStyle ,  isError :  Boolean  =  false ,  visualTransformation :  VisualTransformation  =  VisualTransformation.None ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ,  keyboardActions :  KeyboardActions  =  KeyboardActions.Default ,  maxLines :  Int  =  Int.MAX_VALUE ,  minLines :  Int  =  1 ,  showScrollIndicator :  Boolean  =  false ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  TextFieldDefaults.CornerRadius ,  colors :  TextFieldColors  =  TextFieldDefaults.textFieldColors() ) 
Multi line text input 
```kotlin
@Composable
```fun  TextArea ( value :  String ,  onValueChange :  ( String )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  supportingText :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  readOnly :  Boolean  =  false ,  textStyle :  TextStyle  =  TextFieldDefaults.DefaultTextStyle ,  isError :  Boolean  =  false ,  visualTransformation :  VisualTransformation  =  VisualTransformation.None ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ,  keyboardActions :  KeyboardActions  =  KeyboardActions.Default ,  maxLines :  Int  =  Int.MAX_VALUE ,  minLines :  Int  =  1 ,  showScrollIndicator :  Boolean  =  false ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  TextFieldDefaults.CornerRadius ,  colors :  TextFieldColors  =  TextFieldDefaults.textFieldColors() ) 
Multi-line text input 
Text Field 
```kotlin
@Composable
```fun  TextField ( value :  TextFieldValue ,  onValueChange :  ( TextFieldValue )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  leadingContent :  @ Composable ( )  ->  Unit ?  =  null ,  trailingContent :  @ Composable ( )  ->  Unit ?  =  null ,  supportingText :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  readOnly :  Boolean  =  false ,  textStyle :  TextStyle  =  TextFieldDefaults.DefaultTextStyle ,  isError :  Boolean  =  false ,  visualTransformation :  VisualTransformation  =  VisualTransformation.None ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ,  keyboardActions :  KeyboardActions  =  KeyboardActions.Default ,  singleLine :  Boolean  =  true ,  maxLines :  Int  =  if (singleLine) 1 else Int.MAX_VALUE ,  minLines :  Int  =  1 ,  showScrollIndicator :  Boolean  =  false ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  TextFieldDefaults.CornerRadius ,  colors :  TextFieldColors  =  TextFieldDefaults.textFieldColors() ,  clearable :  Boolean  =  true ) 
```kotlin
@Composable
```fun  TextField ( value :  String ,  onValueChange :  ( String )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  placeholder :  @ Composable ( )  ->  Unit ?  =  null ,  leadingContent :  @ Composable ( )  ->  Unit ?  =  null ,  trailingContent :  @ Composable ( )  ->  Unit ?  =  null ,  supportingText :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  readOnly :  Boolean  =  false ,  textStyle :  TextStyle  =  TextFieldDefaults.DefaultTextStyle ,  isError :  Boolean  =  false ,  visualTransformation :  VisualTransformation  =  VisualTransformation.None ,  keyboardOptions :  KeyboardOptions  =  KeyboardOptions.Default ,  keyboardActions :  KeyboardActions  =  KeyboardActions.Default ,  singleLine :  Boolean  =  true ,  maxLines :  Int  =  if (singleLine) 1 else Int.MAX_VALUE ,  minLines :  Int  =  1 ,  showScrollIndicator :  Boolean  =  false ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  cornerRadius :  Dp  =  TextFieldDefaults.CornerRadius ,  colors :  TextFieldColors  =  TextFieldDefaults.textFieldColors() ,  clearable :  Boolean  =  true ) 
Text fields allow users to enter text into a UI. 
text Style 
```kotlin
@Composable
```fun  ChipSize . textStyle ( ) :  TextStyle 
Calculates the text style for a given  ChipSize . 
```kotlin
@Composable
```fun  SegmentControlSize . textStyle ( ) :  TextStyle 
The text style of the segment control item. 
Timepicker 
```kotlin
@Composable
```fun  Timepicker ( modifier :  Modifier  =  Modifier ,  config :  TimepickerConfig  =  TimepickerConfig.create(
            hour = TimepickerElement.hours(),
            minute = TimepickerElement.minutes(),
            second = TimepickerElement.seconds(),
        ) ,  onHoursChanged :  ( Int )  ->  Unit  =  {} ,  onMinutesChanged :  ( Int )  ->  Unit  =  {} ,  onSecondsChanged :  ( Int )  ->  Unit  =  {} ,  gap :  Dp  =  TimepickerDefaults.DefaultGap ,  colors :  WheelPickerColors  =  WheelPickerDefaults.wheelPickerColors() ) 
A components for choose hours/minutes/seconds based on  WheelPicker 
Title Bar 
```kotlin
@Composable
```fun  TitleBar ( title :  @ Composable BoxScope . ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  leadingActions :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  trailingActions :  @ Composable RowScope . ( )  ->  Unit ?  =  null ,  contentPadding :  PaddingValues  =  TitleBarDefaults.HorizontalPadding ,  leadingGap :  Dp  =  TitleBarDefaults.ActionsGap ,  trailingGap :  Dp  =  TitleBarDefaults.ActionsGap ,  titleAlignment :  TitleAlignment  =  TitleAlignment.Center ,  colors :  TitleBarColors  =  TitleBarDefaults.titleBarColors() ) 
app title bar 
Toggleable Chip 
```kotlin
@Composable
```fun  ToggleableChip ( label :  @ Composable ( )  ->  Unit ,  isToggleOn :  Boolean ,  onClick :  ( )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  chipSize :  ChipSize  =  ChipsDefaults.Small ,  colors :  ToggleableChipColors  =  ChipsDefaults.toggleableChipColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Chip that is toggleable 
Toggle Button 
```kotlin
@Composable
```fun  ToggleButton ( checked :  Boolean ,  onCheckedChange :  ( Boolean )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  colors :  ToggleButtonColors  =  ToggleButtonDefaults.toggleButtonColors() ,  size :  ButtonSize  =  ToggleButtonDefaults.Min ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  leadingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  trailingIcon :  @ Composable ( )  ->  Unit ?  =  null ,  contentPadding :  PaddingValues  =  ButtonDefaults.paddingForButtonSize(
            size,
            haveIcon = leadingIcon != null || trailingIcon != null,
        ) ,  shape :  Shape  =  ButtonDefaults.shapeForButtonSize(size) ,  gap :  Dp  =  ButtonDefaults.gapForButtonSize(
            size,
            haveIcon = leadingIcon != null || trailingIcon != null,
        ) ,  content :  @ Composable RowScope . ( )  ->  Unit ) 
A stylized toggleable button component defined by PICO design which could be used easily by pass pre-defined  ButtonSize  and  ToggleButtonColors . Each pre-defined  ButtonSize  has related  PaddingValues , Shape , gap  and  TextStyle . 
Toggle Icon Button 
```kotlin
@Composable
```fun  ToggleIconButton ( checked :  Boolean ,  onCheckedChange :  ( Boolean )  ->  Unit ,  modifier :  Modifier  =  Modifier ,  colors :  ToggleButtonColors  =  ToggleIconButtonDefaults.toggleIconButtonColors() ,  size :  ButtonSize  =  ToggleIconButtonDefaults.Min ,  shape :  Shape  =  ToggleIconButtonDefaults.DefaultShape ,  enabled :  Boolean  =  true ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ,  content :  @ Composable ( )  ->  Unit ) 
Toggleable icon button defined by PICO design 
Tri State Checkbox 
```kotlin
@Composable
```fun  TriStateCheckbox ( state :  ToggleableState ,  modifier :  Modifier  =  Modifier ,  onClick :  ( )  ->  Unit ?  =  null ,  enabled :  Boolean  =  true ,  contentSize :  CheckboxContentSize  =  CheckBoxDefaults.Regular ,  colors :  CheckboxColor  =  CheckBoxDefaults.checkboxColors() ,  interactionSource :  MutableInteractionSource  =  remember { MutableInteractionSource() } ) 
Checkboxes can have a parent-child relationship with other checkboxes. When the parent checkbox is checked, all child checkboxes are checked. If a parent checkbox is unchecked, all child checkboxes are unchecked. If some, but not all, child checkboxes are checked, the parent checkbox becomes an indeterminate checkbox. 
Vertical Divider 
```kotlin
@Composable
```fun  VerticalDivider ( modifier :  Modifier  =  Modifier ,  color :  Color  =  DividerDefaults.color ,  thickness :  Dp  =  DividerDefaults.thickness ) 
A divider is a thin line that groups content in horizontal lists and layouts. 
vibrant Color Scheme 
```kotlin
fun vibrantColorScheme(fillPrimary: Color = Color.Vibrant.withVibrant(Vibrant.Darker), fillSecondary: Color = Color.Vibrant.withVibrant(Vibrant.SemiLight), fillTertiary: Color = Color.Vibrant.withVibrant(Vibrant.Neutral), fillLight: Color = Color.Vibrant.withVibrant(Vibrant.Light), labelPrimaryLight: Color = ColorTokens.Default.SubWhite100.withVibrant(Vibrant.None), labelPrimary: Color = Color.Vibrant.withVibrant(Vibrant.Darkest), labelSecondary: Color = Color.Vibrant.withVibrant(Vibrant.UltraDark), labelTertiary: Color = Color.Vibrant.withVibrant(Vibrant.Semidark), labelQuaternary: Color = Color.Vibrant.withVibrant(Vibrant.Dark), lightenHover: Color = Color.Vibrant.withVibrant(Vibrant.SemiLight), lightenPressed: Color = Color.Vibrant.withVibrant(Vibrant.SemiLight), error: Color = ColorTokens.Default.SubRed100.withVibrant(Vibrant.None), alert: Color = ColorTokens.Default.SubOrange100.withVibrant(Vibrant.None), passable: Color = ColorTokens.Default.SubGreen100.withVibrant(Vibrant.None), interaction: Color = ColorTokens.Default.SubBlue100.withVibrant(Vibrant.None), dividerLine: Color = ColorTokens.Default.SubBlack12.withVibrant(Vibrant.None)): ColorScheme
```
A vibrant color scheme. 
Wheel Picker 
```kotlin
@Composable
```fun  WheelPicker ( count :  Int ,  getItemText :  ( Int )  ->  String ,  modifier :  Modifier  =  Modifier ,  itemHeight :  Dp  =  WheelPickerDefaults.DefaultItemHeight ,  itemMargin :  Dp  =  WheelPickerDefaults.defaultItemMargin ,  rowNumber :  Int  =  7 ,  onSelectedChange :  ( Int )  ->  Unit ?  =  null ,  semanticsContent :  String ?  =  null ,  colors :  WheelPickerColors  =  WheelPickerDefaults.wheelPickerColors() ,  initialSelectedIndex :  Int  =  rowNumber / 2 ,  indicatorBackgroundShape :  Shape  =  WheelPickerDefaults.DefaultIndicatorShape ,  indicatorCenterTextStyle :  TextStyle  =  PicoTheme.typography.headlineLarge ,  isInfinite :  Boolean  =  false ,  leftText :  @ Composable ( )  ->  Unit ?  =  null ,  rightText :  @ Composable ( )  ->  Unit ?  =  null ,  state :  LazyListState  =  with(count) {
            check(this > 0) { "count must lager than 0" }
            rememberWheelState(
                count,
                rowNumber,
                initialFirstVisibleItemIndex = initialSelectedIndex % this,
            )
        } ) 
A common picker widget defined by PICO Design.