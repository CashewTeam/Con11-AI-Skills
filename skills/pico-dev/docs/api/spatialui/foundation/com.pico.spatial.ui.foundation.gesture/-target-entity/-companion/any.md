# any | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / TargetEntity / Companion / any 
# any
```kotlin
@Stable
```fun  any ( condition :  ( entity :  Entity )  ->  Boolean ) :  TargetEntity 
Bind a gesture to target entities which meet the  condition . 
#### Return
MeetCondition instance 
#### Parameters
condition 
Entity filter. Return  true  if gesture can bind to entity 
```kotlin
@Stable
```fun  any ( ) :  TargetEntity 
Bind a gesture to any entity 
#### Return
MeetCondition instance