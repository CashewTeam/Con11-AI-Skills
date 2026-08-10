# dec | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / dec 
# dec
```kotlin
operator fun dec(): Vector2
```
Overloads the unary decrement operator ( -- ). 
This operator creates and returns a new  Vector2  where both the  x  and  y  components of the original vector are decremented by  1.0f . 
Note: This function implements the  dec  operator, which means it returns a  new Vector2  instance. If you use it in a statement like  var v = Vector2(1f, 1f); v--; ,  v  will be reassigned to the new  Vector2(0f, 0f) . It does not modify the original  Vector2  instance in place if the class is immutable. 
Usage: 

```
var myVector = Vector2(3.0f, 4.0f)// Postfix decrement as a statementmyVector--// myVector is now Vector2(2.0f, 3.0f)// Postfix decrement used in an assignment// myVector is currently Vector2(2.0f, 3.0f)val newVector = myVector--// newVector gets the value of myVector *before* the decrement: Vector2(2.0f, 3.0f)// myVector is then decremented: myVector becomes Vector2(1.0f, 2.0f)// Prefix decrement used in an assignment// myVector is currently Vector2(1.0f, 2.0f)val anotherVector = --myVector// myVector is first decremented: myVector becomes Vector2(0.0f, 1.0f)// anotherVector gets the value of myVector *after* the decrement: Vector2(0.0f, 1.0f)
```
#### Return
A new  Vector2  instance with its  x  and  y  components each decremented by  1.0f .