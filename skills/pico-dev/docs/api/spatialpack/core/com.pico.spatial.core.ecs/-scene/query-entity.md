# queryEntity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Scene / queryEntity 
# queryEntity
```kotlin
@MainThread
```fun  queryEntity ( vararg  conditions :  EntityQueryCondition ) :  List < Entity > 
Queries a list of entities based on one or more conditions. 
This function filters the entities and returns those that meet all the specified conditions. All conditions are treated as part of an  AND  relationship, meaning an entity must satisfy all conditions to be included in the result. 
### Best practices:
- 
Combine component queries into a single condition : For better performance, group all component-related queries (for example,  hasComponent ,  !hasComponent ) into a single condition. For example, to find entities that have both  MyComponent  and  AnotherComponent :  `` val componentCondition =   EntityQueryCondition.hasComponent(MyComponent::class.java).and(   EntityQueryCondition.hasComponent(AnotherComponent::class.java)) val result =   queryEntity(componentCondition) ``  This ensures the system can handle component filtering   more efficiently. 
- 
Use separate conditions for custom logic or  or  queries : Place custom queries or  or    conditions into a separate condition for clarity and maintainability. For example, to find   entities with a specific name or a specific tag:  `` val customCondition =   EntityQueryCondition.custom { entity -> entity.name == "Player" }.or(   EntityQueryCondition.custom { entity -> entity.hasParent() }) val result =   queryEntity(componentCondition, customCondition) ``  This separates component filtering   from more complex logic, improving both readability and performance. 
- 
Avoid overusing complex combined conditions : While combining conditions is powerful,   overly complex conditions can impact readability and debugging. Break them into smaller,   reusable conditions when possible. 
@param conditions One or more conditions to filter the entities by. @return A list of entities that meet the specified conditions.