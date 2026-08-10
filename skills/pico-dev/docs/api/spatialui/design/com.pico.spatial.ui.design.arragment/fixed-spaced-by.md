# fixedSpacedBy | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.arragment / fixedSpacedBy 
# fixedSpacedBy
```kotlin
@Stable
```fun  Arrangement . fixedSpacedBy ( space :  Dp ) :  Arrangement.HorizontalOrVertical 
Place children such that each two adjacent ones are spaced by a fixed  space  distance across the main axis. The spacing will be subtracted from the available space that the children can occupy. The  space  can be negative, in which case children will overlap. 
To change alignment of the spaced children horizontally or vertically, use spacedBy overloads with  alignment  parameter. 
#### Return
A new  Arrangement  instance. 
#### Parameters
space 
The space between adjacent children. 
```kotlin
@Stable
```fun  Arrangement . fixedSpacedBy ( space :  Dp ,  alignment :  Alignment.Horizontal ) :  Arrangement.Horizontal 
Place children horizontally such that each two adjacent ones are spaced by a fixed  space  distance. The spacing will be subtracted from the available width that the children can occupy. An  alignment  can be specified to align the spaced children horizontally inside the parent, in case there is empty width remaining. The  space  can be negative, in which case children will overlap. 
#### Return
A new  Arrangement  instance. 
#### Parameters
space 
The space between adjacent children. 
alignment 
The alignment of the spaced children inside the parent.