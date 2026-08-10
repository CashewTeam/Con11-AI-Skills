# setName | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / setName 
# setName
```kotlin
@MainThread
```fun  setName ( name :  String ) 
Sets the name of the current entity. 
#### Parameters
name 
The name of the current entity. The name must meet the following requirements: 
- 
The length of the name should not exceed 2048 characters. 
- 
The name should only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_). 
- 
For the convenience of debugging or automatic testing, it is recommended to set names for essential entities and ensure that each name is unique.