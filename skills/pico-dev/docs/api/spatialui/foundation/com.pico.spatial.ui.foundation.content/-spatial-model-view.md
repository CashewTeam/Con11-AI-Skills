# SpatialModelView | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.content / SpatialModelView 
# SpatialModelView
```kotlin
@Composable
```fun  SpatialModelView ( source :  Source < * > ,  modifier :  Modifier  =  Modifier ,  resizability :  Resizability  =  Resizability.None ,  onLoad :  ( )  ->  Unit ?  =  null ,  onError :  ( String )  ->  Unit ?  =  null ,  onSuccess :  ( LoadedModel )  ->  Unit ?  =  null ,  content :  @ Composable SpatialModelScope . ( )  ->  Unit  =  {} ) 
A view that asynchronously loads and displays a 3D model from  source , while exposing the load lifecycle through callbacks. 
This overload is intended for observing the loading lifecycle or triggering side effects. If you need to render different UI for different states based on the load state, use the  SpatialModelView  overload that exposes  ModelLoadingState  in  content . 
#### Parameters
source 
The data source of a 3D model. For example, you can load a model file located in android assets directory to this SpatialModelView. 
modifier 
The modifier to be applied to SpatialModelView. 
resizability 
An enum value which indicates whether the loaded model should resize to fit the SpatialModelView size. 
on Load 
Callback invoked when the loading state enters  ModelLoadingState.Loading . 
on Error 
Callback invoked after the loading state changes to  ModelLoadingState.Error . The callback parameter is the failure reason. 
on Success 
Callback invoked after the loading state changes to  ModelLoadingState.Success . The callback parameter is the loaded model. 
content 
A composable function displayed inside the view while the load callbacks are being observed. The default implementation renders no content. 
```kotlin
@Composable
```fun  SpatialModelView ( source :  Source < * > ,  modifier :  Modifier  =  Modifier ,  resizability :  Resizability  =  Resizability.None ,  content :  @ Composable SpatialModelScope . ( state :  ModelLoadingState )  ->  Unit  =  { state ->
        if (state is ModelLoadingState.Success) {
            Model(state.model)
        }
    } ) 
A view that asynchronously loads and displays a 3D model from  source . 
#### Parameters
source 
The data source of a 3D model. For example, you can load a model file located in android assets directory to this SpatialModelView. 
modifier 
The modifier to be applied to SpatialModelView. 
resizability 
An enum value which indicates whether the loaded model should resize to fit the SpatialModelView size. 
content 
A composable function takes the load state as an input. So you can determine what to show according to the state. For example, you can display a loading view as place holder. when state is  ModelLoadingState.Loading , and when the model loaded successfully, which means the state is  ModelLoadingState.Success , you can display the model by  Model  function.