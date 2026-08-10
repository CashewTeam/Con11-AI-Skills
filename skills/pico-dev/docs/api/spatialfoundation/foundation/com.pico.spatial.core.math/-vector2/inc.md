# inc | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / inc 
# inc
```kotlin
operator fun inc(): Vector2
```
Overloads the unary increment operator ( ++ ). 
This operator creates and returns a new  Vector2  where both the  x  and  y  components of the original vector are incremented by  1.0f . 
Note: This function implements the  inc  operator, which means it returns a  new Vector2  instance. If you use it in a statement like  var v = Vector2(1f, 1f); v++; ,  v  will be reassigned to the new  Vector2(2f, 2f) . It does not modify the original  Vector2  instance in place if the class is immutable. 
Usage: 

```
var myVector = Vector2(2.0f, 3.0f)myVector++ // myVector is now Vector2(3.0f, 4.0f)val newVector = myVector++ // newVector is Vector2(3.0f, 4.0f), myVector becomes Vector2(4.0f, 5.0f)// (if used as postfix, newVector gets value *before* increment if not reassigned directly)// More accurately, for `val newVector = myVector++`:// 1. The original value of myVector is remembered.// 2. myVector.inc() is called, and myVector is updated to this new value.// 3. The remembered original value is assigned to newVector.// However, the typical use `myVector++` (as a statement) reassigns myVector to the incremented value.val anotherVector = ++myVector // anotherVector is Vector2(5.0f, 6.0f), myVector becomes Vector2(5.0f, 6.0f)// For `val anotherVector = ++myVector`:// 1. myVector.inc() is called, and myVector is updated to this new value.// 2. The new (incremented) value of myVector is assigned to anotherVector.
```
#### Return
A new  Vector2  instance with its  x  and  y  components each incremented by  1.0f .