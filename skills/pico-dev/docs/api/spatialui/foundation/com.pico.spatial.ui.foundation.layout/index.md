# com.pico.spatial.ui.foundation.layout | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout 
# Package-level declarations
Types Functions Properties 
## Types
Box3DScope 
```kotlin
@Immutable
```interface  Box3DScope 
Scope for  Box3D 's content 
Depth Alignment 
```kotlin
@Stable
```interface  DepthAlignment 
Depth alignment defines how an element is aligned along the depth axis (usually the Z-axis) of a three-dimensional coordinate system, and determines the offset applied to the element in that axis. 
Int Size3D 
```kotlin
@Stable
```class  IntSize3D ( val  width :  Int ,  val  height :  Int ,  val  depth :  Int ) 
The 3D size of a layout. 
## Properties
depth 
```kotlin
val LayoutCoordinates.depth: Int
```
The depth of this layout in the 3D coordinates space. when monitor the layout depth change, the depth will be updated. get the current depth in 3D coordinates space. 
size In3D 
```kotlin
val LayoutCoordinates.sizeIn3D: IntSize3D
```
The 3D size of this layout in the 3D coordinates space. when monitor the layout size change, the size will be updated. get the current size in 3D coordinates space. 
## Functions
align Depth 
```kotlin
@Stable
```fun  Modifier . alignDepth ( alignment :  DepthAlignment  =  DepthAlignment.DepthCenter ) :  Modifier 
Modifier to align the element along the depth axis (usually the Z-axis) of a three-dimensional coordinate system. the default alignment is  DepthAlignment.DepthCenter 
Box3D 
```kotlin
@Composable
```fun  Box3D ( modifier :  Modifier  =  Modifier ,  depthAlignment :  DepthAlignment  =  DepthAlignment.DepthCenter ,  propagateMinConstraints :  Boolean  =  false ,  content :  @ Composable Box3DScope . ( )  ->  Unit ) 
A layout composable that arranges its children in a 3D space. The  Box3D  will size itself to fit the content, subject to the incoming constraints. For the alignments of the children layouts in the xy plane, you need to use the  Box3DScope.align  modifier. By default, the content will be measured without the  Box3D 's incoming min constraints, unless  propagateMinConstraints  is  true . As an example, setting  propagateMinConstraints  to  true  can be useful when the  Box3D  has content on which modifiers cannot be specified directly and setting a min size on the content of the  Box3D  is needed. If  propagateMinConstraints  is set to  true , the min size set on the  Box3D  will also be applied to the content, whereas otherwise the min size will only apply to the  Box3D . When the content has more than one layout child, the layout children will be stacked one on top of the other (positioned as explained above) in the composition order. 
depth 
```kotlin
@Stable
```fun  Modifier . depth ( depth :  Dp  =  Dp.Unspecified ) :  Modifier 
Declare the preferred depth of the content to be exactly  depth dp. The incoming measurement  Constraints3D  may override this value, forcing the content to be either smaller or larger. 
depth In 
```kotlin
@Stable
```fun  Modifier . depthIn ( min :  Dp  =  Dp.Unspecified ,  max :  Dp  =  Dp.Unspecified ) :  Modifier 
Constrain the depth of the content to be between  min dp and  max dp as permitted by the incoming measurement  Constraints3D . If the incoming constraints are more restrictive the requested size will obey the incoming constraints and attempt to be as close as possible to the preferred size. 
layout3D 
```kotlin
fun Modifier.layout3D(measure: MeasureScope.(Measurable, Constraints3D) -> MeasureResult): Modifier
```
This is a convenience API of creating a custom  LayoutModifierNode  modifier which implements 3D measurement, without having to create a class or an object that implements the  LayoutModifierNode  interface. 
offset 
```kotlin
@Stable
```fun  Modifier . offset ( z :  Dp ) :  Modifier 
Offset content by  z  dp 
padding3D 
```kotlin
@Stable
```fun  Modifier . padding3D ( all :  Dp ) :  Modifier 
Apply  all  dp of additional space along each edge of the content, left, top, right, bottom, back and front. Padding is applied before content measurement and takes precedence; content may only be as large as the remaining space. Negative padding is not permitted — it will cause IllegalArgumentException. See Modifier.offset. 
```kotlin
@Stable
```fun  Modifier . padding3D ( horizontal :  Dp  =  0.dp ,  vertical :  Dp  =  0.dp ,  thicknessPadding :  Dp  =  0.dp ) :  Modifier 
Apply  horizontal  dp space along the left and right edges of the content, and  vertical  dp space along the top and bottom edges, and  thicknessPadding  dp space along the back and front edges. 
```kotlin
@Stable
```fun  Modifier . padding3D ( start :  Dp  =  0.dp ,  top :  Dp  =  0.dp ,  end :  Dp  =  0.dp ,  bottom :  Dp  =  0.dp ,  back :  Dp  =  0.dp ,  front :  Dp  =  0.dp ) :  Modifier 
Apply additional space along each edge of the content in Dp: start, top, end, bottom, back, and front. The start and end edges will be determined by the current LayoutDirection. Padding is applied before content measurement and takes precedence; content may only be as large as the remaining space. Negative padding is not permitted — it will cause IllegalArgumentException. See Modifier.offset. 
required Depth 
```kotlin
@Stable
```fun  Modifier . requiredDepth ( depth :  Dp ) :  Modifier 
Declare the depth of the content to be exactly  depth dp. The incoming measurement  Constraints3D  will not override this value. If the content chooses a size that does not satisfy the incoming  Constraints3D , the parent layout will be reported a size coerced in the  Constraints3D , and the position of the content will be automatically offset to be centered on the space assigned to the child by the parent layout under the assumption that  Constraints3D  were respected. 
required Depth In 
```kotlin
@Stable
```fun  Modifier . requiredDepthIn ( min :  Dp  =  Dp.Unspecified ,  max :  Dp  =  Dp.Unspecified ) :  Modifier 
Constrain the depth of the content to be between  min dp and  max dp. If the content chooses a size that does not satisfy the incoming  Constraints3D , the parent layout will be reported a size coerced in the  Constraints3D , and the position of the content will be automatically offset to be centered on the space assigned to the child by the parent layout under the assumption that  Constraints3D  were respected. 
z Offset 
```kotlin
fun Modifier.zOffset(offset: Density.() -> Float): Modifier
```
Offset content by  offset  px