# TitleBarDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / TitleBarDefaults 
# TitleBarDefaults
```kotlin
object TitleBarDefaults
```
The default values of  TitleBar . 
Members 
## Properties
Actions Gap 
```kotlin
val ActionsGap: Dp
```
The default gap between actions. 
Height 
```kotlin
val Height: Dp
```
The default height of  TitleBar . 
Horizontal Padding 
```kotlin
val HorizontalPadding: PaddingValues
```
The default horizontal padding of  TitleBar . 
Title Content Padding 
```kotlin
val TitleContentPadding: Dp
```
The default padding of title content. 
## Functions
title Bar Colors 
```kotlin
@Composable
```fun  titleBarColors ( ) :  TitleBarColors 
The default colors used for  TitleBar 
```kotlin
@Composable
```fun  titleBarColors ( titleColor :  Color  =  Color.Unspecified ,  leadingColor :  Color  =  Color.Unspecified ,  trailingColor :  Color  =  Color.Unspecified ) :  TitleBarColors 
custom colors for linear progress indicator