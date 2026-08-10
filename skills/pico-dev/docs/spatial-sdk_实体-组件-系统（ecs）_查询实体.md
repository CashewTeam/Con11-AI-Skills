实体以树的方式维护其层级结构。你可以使用 PICO Spatial SDK 提供的函数来快速查询目标实体。
## 实现方法
### 使用 scene.queryEntity
通过 `scene.queryEntity(EntityQueryCondition)`，你可以查找到符合条件的所有实体。该函数会将这些实体返回为一个列表。

* **按组件查询**
   筛选挂载了特定组件的实体。例如，筛选带有 `ModelComponent` 的实体：
   ```Kotlin
   val hasComponentsCondition =
       EntityQueryCondition.hasComponent(ModelComponent::class.java)
   val entities = entity.scene!!.queryEntity(hasComponentsCondition)
   ```

* **按自定义条件查询**
   使用 lambda 函数传入自定义查询条件。例如，查询名字为 `"PICO"` 的实体：
   ```Kotlin
   val customCondition =
       EntityQueryCondition.customCondition { it.getName() == "PICO" }
   val entities = entity.scene!!.queryEntity(customCondition)
   ```

* **按组合条件查询**
   你可以使用 `and` 或者 `or` 随意组合不同的 `EntityQueryCondition`，从而形成一个最终的查询条件，传递给 `scene.queryEntity()`。例如，筛选同时带有 `ModelComponent` 和 `InteractableComponent` 的实体：
   ```Kotlin
   val hasComponentsCondition =
       EntityQueryCondition.hasComponent(ModelComponent::class.java)
           .and(EntityQueryCondition.hasComponent(InteractableComponent::class.java))
   val entities = entity.scene!!.queryEntity(hasComponentsCondition)
   ```

   你也可以直接在 `scene.queryEntity()` 中传入多个条件（用 `,` 分隔）。但建议尽量将条件合并，而不要传入过多的单个条件。
   ```Kotlin
   // 查询同时带有 ModelComponent 和 InteractableComponent，且名字为“PICO”的 Entity
   val entities = entity.scene!!.queryEntity(hasComponentsCondition, customCondition)
   
   // 查询同时带有 ModelComponent 和 InteractableComponent，且名字不为“PICO”的 Entity
   val entities = entity.scene!!.queryEntity(hasComponentsCondition, !customCondition)
   ```


在自定义 `System` 中，通过 `content: SceneUpdateContext` 的 `scene` 查询实体（例如 `context.scene.queryEntity(condition)`）时，查询范围限定在当前 `SpatialContainer` 内，会返回该容器范围中的实体。

### 使用 entity.findEntity(name)
如果你已知目标实体的名称，则可以通过 `entity.findEntity(name)` 在当前实体的层级结构中查询对应的实体。
### 使用 entity.getChildren
你可以通过 `entity.getChildren()` 获取当前实体的所有子实体，并结合广度优先搜索（BFS）或深度优先搜索（DFS）遍历整个实体树，在遍历过程中判断每个实体是否为目标实体。
## API 参考
`EntityQueryCondition` 类中提供了用于查询实体的接口，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)
