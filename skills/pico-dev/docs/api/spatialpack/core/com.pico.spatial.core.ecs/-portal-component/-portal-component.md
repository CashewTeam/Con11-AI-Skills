# PortalComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PortalComponent / PortalComponent 
# PortalComponent
```kotlin
constructor(targetEntity: Entity, enable: Boolean = true, doubleSide: Boolean = false, allowClipping: Boolean = true, allowEntityCrossing: Boolean = true)
```
Constructs a  PortalComponent  with the specified parameters. 
#### Parameters
target Entity 
The  Entity  representing the target world visible through the portal. Must be a valid  Entity  object. 
enable 
Whether the portal is enabled. The default value is  true . If  true , the portal is rendered; otherwise, it is not. 
double Side 
Whether both sides (forward and backward) of the portal are rendered. The default value is  false . If  true , both the forward and backward sides are rendered; if  false , only the forward side is rendered. 
allow Clipping 
Whether entities intersecting with the portal are clipped. The default value is  true . If  true , parts of entities in the portal world will be clipped when they intersect with the portal itself; otherwise they are not. 
allow Entity Crossing 
Whether entities are allowed to cross the portal. The default value is  true . If  true , entities crossing the portal will be rendered outside the portal; otherwise they are not. 
```kotlin
@ExperimentalSpatialApi
```constructor ( targetEntity :  Entity ,  enable :  Boolean  =  true ,  doubleSide :  Boolean  =  false ,  allowClipping :  Boolean  =  true ,  allowEntityCrossing :  Boolean  =  true ,  panelColor :  Color3  =  Color3(0f, 0f, 0f) ,  backgroundMode :  PortalBackgroundMode  =  PortalBackgroundMode.SOLID_COLOR ) 
Constructs a  PortalComponent  with the specified parameters, including experimental background settings. 
#### Parameters
target Entity 
The  Entity  representing the target world visible through the portal. Must be a valid  Entity  object. 
enable 
Whether the portal is enabled. The default value is  true . If  true , the portal is rendered; otherwise, it is not. 
double Side 
Whether both sides (forward and backward) of the portal are rendered. The default value is  false . If  true , both the forward and backward sides are rendered; if  false , only the forward side is rendered. 
allow Clipping 
Whether entities intersecting with the portal are clipped. The default value is  true . If  true , parts of entities in the portal world will be clipped when they intersect with the portal itself; otherwise they are not. 
allow Entity Crossing 
Whether entities are allowed to cross the portal. The default value is  true . If  true , entities crossing the portal will be rendered outside the portal; otherwise they are not. 
panel Color 
The color of the portal panel. Each component should be in the range 0, 1. The default value is black (0, 0, 0). The panel color is used when  backgroundMode  is set to  PortalBackgroundMode.SOLID_COLOR . 
background Mode 
The background mode of the portal. The default value is  PortalBackgroundMode.SOLID_COLOR .