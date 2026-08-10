# Companion | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / TargetEntity / Companion 
# Companion
```kotlin
object Companion
```
companion 
Members 
## Functions
any 
```kotlin
@Stable
```fun  any ( ) :  TargetEntity 
Bind a gesture to any entity 
```kotlin
@Stable
```fun  any ( condition :  ( entity :  Entity )  ->  Boolean ) :  TargetEntity 
Bind a gesture to target entities which meet the  condition . 
hit 
```kotlin
@Stable
```fun  hit ( entity :  Entity ) :  TargetEntity 
Bind a gesture to target an entity or a descendant of entity.