# DataProvider | PICO Spatial SDK

tracking / com.pico.spatial.tracking / DataProvider 
# DataProvider
```kotlin
@RequiredFullSpace
```interface  DataProvider < T > 
Generic data provider for various types of tracking data. 
Usage: 
- 
Call  start  to begin providing data and  stop  when data is no longer needed. Make sure to call  stop  to avoid potential memory leaks. 
- 
Check if the current data type is available via  supportState . 
- 
Get the latest data via  latestData , register a  DataListener  via  addListener  to receive data, or get data from  dataFlow . 
#### Parameters
T 
The type of tracking data. 
#### Inheritors
BodyTrackingProvider ControllerTrackingProvider EyeTrackingProvider HandTrackingProvider HMDTrackingProvider MotionTrackingProvider Members 
## Types
Data Listener 
```kotlin
fun interface DataListener<T>
```
The listener for receiving data from a  DataProvider . 
Start Result 
```kotlin
enum StartResult : Enum<DataProvider.StartResult>
```
The result of  start , represent the state when  start  is called. 
State 
```kotlin
enum State : Enum<DataProvider.State>
```
Represents the state of the current  DataProvider . 
Support State 
```kotlin
enum SupportState : Enum<DataProvider.SupportState>
```
Indicates whether the current type of data is supported now. 
## Properties
data Flow 
```kotlin
abstract val dataFlow: SharedFlow<T>
```
The  SharedFlow  of tracking data. This flow is a hot flow with no replay. 
latest Data 
```kotlin
abstract val latestData: T
```
The latest tracking data. 
state 
```kotlin
abstract val state: DataProvider.State
```
The state of the current  DataProvider . 
support State 
```kotlin
abstract val supportState: DataProvider.SupportState
```
The support state of the data type. 
## Functions
add Listener 
```kotlin
abstract fun addListener(listener: DataProvider.DataListener<T>)
```
Adds a  DataListener  to receive data. 
remove Listener 
```kotlin
abstract fun removeListener(listener: DataProvider.DataListener<T>)
```
Removes a  DataListener  to stop receiving data. 
start 
```kotlin
abstract fun start(): DataProvider.StartResult
```
Starts providing tracking data. 
stop 
```kotlin
abstract fun stop()
```
Stops providing tracking data.