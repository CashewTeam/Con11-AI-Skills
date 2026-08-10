传送门可以将某个 entity 的网格的表面转化为通往其他场景的入口，从而让用户在应用内的各个场景间自由穿梭。
## 组件和材质
传送门需要通过以下组件和材质实现：
### PortalWorldComponent
该组件可以将一个 entity 及其所有子节点转换为一个独立的世界，该世界中的内容仅能通过传送门查看。该组件应与 `PortalComponent`、`PortalCrossableComponent` 和 `PortalMaterial` 一起使用。
### PortalMaterial
一种材质，可以将某个 entity 的网格的表面变成通往其他可传送场景的传送门。该材质应与 `PortalComponent` 一起使用。若要将网格转换为传送门，需将此材质添加到 `ModelComponent` 上，并在同一个 entity 上挂载 `PortalComponent`。
### PortalComponent
该组件可使某个 entity 的网格的表面成为通向目标世界（即 `targetEntity` 的 EC 树）的传送门，应与 `PortalMaterial` 一起使用。该组件提供以下可配置的属性：
| **属性** | **描述** |
| --- | --- |
| allowClipping ;   | 当穿过传送门的物体超出传送门的边界时，是否剪裁超出边界的部分。 ;; * `true`：剪裁 ;; * `false`：不剪裁 ;      |
| allowEntityCrossing | 是否允许携带了 `PortalCrossableComponent` 的 entity 穿过该传送门。 ;; * `true`：允许 ;  * `false`：不允许 |
| doubleSide | 是否渲染该传送门的双面（正面和背面）。 ;; * `true`：从正面和背面都可以看到该传送门及其内部世界。 ;  * `false`：无法从背面看到该传送门及其内部世界。 |
| enable | 是否启用该传送门。 ;; * `true`：启用 ;  * `false`：不启用 |
| targetEntity | 目标 entity，代表传送门中可见的世界。如果 `targetEntity` 为 `null`，则不渲染传送门。为正确渲染传送门，需将 `targetEntity` 设置为有效的 `Entity` 对象。 |
### PortalCrossableComponent
该组件可以使 entity 及其子节点能够穿越传送门。该组件应与 `PortalComponent`、`PortalWorldComponent` 和 `PortalMaterial` 一起使用。
## 核心 entity
传送门由以下三类 entity 协同实现：

* `PortalEntity`：挂载了 `PortalComponent` 的 entity；
* `PortalWorldEntity`：挂载了 `PortalWorldComponent` 的 entity；
* `PortalCrossableEntity`：挂载了 `PortalCrossableComponent` 的 entity。

各 entity 间需满足以下结构关系：

* `PortalEntity` 需要是 `PortalWorldEntity` 的父节点或兄弟节点，而不能是 `PortalWorldEntity` 的子节点。

* `PortalCrossableEntity` 需要是某个 `PortalWorldEntity` 的子节点，而不能孤悬于 `PortalWorldEntity` 之外。

## 使用限制
系统支持同时维护和渲染多对 `PortalEntity` 与 `PortalWorldEntity`。需要注意的是，随着 Portal 对数的增加，系统的渲染与计算开销也会相应提升，建议根据实际场景合理控制数量，以获得最佳性能表现。
## 代码示例
以下代码实现了一个可穿越的 3D 传送门场景：在空间中放置一个 `PortalWorld` 作为传送门内部显示的另一侧的世界，再创建一个带材质与网格的 `PortalEntity` 与该世界绑定；同时加载用于表现穿越效果的模型并放入 `PortalWorld`。
```Kotlin
SpatialView { content, _ ->
    // 定义 PortalWorld（即传送门内要显示的内容的根节点）
    val world =
        Entity().apply {
        // 设置 PortalWorld 的坐标，本示例中将 PortalWorld 设置在传送门左侧
            val worldTransform = TransformComponent().apply {
            setPosition(Vector3(-0.3F, 0F, 0.2F))
            setScaleVector(Vector3(1F))
            }
            components.set(worldTransform)
            components.set(PortalWorldComponent())
        }

    // 定义传送门本体
    val portalEntity = Entity().apply {
        val material = PortalMaterial()
        val mesh = MeshResource.createPlane(1.0f, 1.0f, 0.3f)
        components.set(ModelComponent(mesh, material))
        components.set(PortalComponent(world, true, true, true, true))
        components.set(TransformComponent())
        // 设置传送门坐标，并设置一个偏转角，以便观测传送门两侧的场景
        components
            .get<TransformComponent>()!!
            .setPosition(Vector3(0F, 0F, 0.3F))
            .setEulerAngles(EulerAngles(0F, 45F, 0F))
            .setScaleVector(Vector3(0.8F))
    }

    content.addEntity(world)
    content.addEntity(portalEntity)
    
    // 定义可穿越传送门的模型
    val willCrossing = Entity.load("asset://Portal/plane.glb").apply {
    // 设置 willCrossing 模型的缩放系数和旋转偏置(根据模型实际大小进行调整，本系数仅针对本模型)，以便模型正确显示
    val transform = TransformComponent().apply {
        setPosition(Vector3(-0.3F, 0F, 0.2F))
        setScaleVector(Vector3(0.0005F))
        setRotator(Rotator(-90F, 45F, 0F))
    }
    components.set(transform)
    components.set(PortalCrossableComponent())
 }      
    world.addChild(willCrossing)
}
```

## API 参考
关于 `PortalWorldComponent`、`PortalMaterial`、`PortalComponent` 和 `PortalCrossableComponent` 的详细说明，参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)

