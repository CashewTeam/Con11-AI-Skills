本文介绍如何管理实体之间的层级。
## 实现方法
`Entity` 之间可以构成父子层级（场景树）。常见功能的实现方式如下：
| **功能** | **相关接口** |
| --- | --- |
| 将实体添加为子实体 | `addChild`/`setParent` |
| 从父节点移除 | `removeFromParent`/`removeChild`/`removeAllChildren` |
| 遍历子节点 | `getChildren`/`getChildrenCount` |
| 在当前子树内按名称查找 | `findEntity` |
## 示例代码
以下代码展示了如何在 `SpatialView` 中把实体加入到内容里，并建立父子关系。
```Kotlin
SpatialView(modifier = Modifier.size(100.dp, 100.dp)) { content, _ ->
    content.addEntity(viewModel.windowContainerEntity)
    viewModel.windowContainerEntity.addChild(viewModel.entityForMoving)
}
```

以下代码展示了如何给关键实体设置名字，并在实体子树中按名字查找节点。
```Kotlin
val entityForMoving =
    BoxEntity().apply {
        setName("CrossingWindowContainerEntity")
        color(Color.Blue)
    }
```

```Kotlin
val timelineEntity = entity.findEntity("CrossingWindowContainerEntity")
timelineEntity?.playTimeline()
```

## 注意事项

* `findEntity(name)` 会在当前实体及其整棵子树中按名称进行深度搜索。如果存在多个同名实体，将只返回第一个匹配项。
* `setName(name)` 对名称有明确约束：长度不得超过 2048 个字符，且只能包含字母、数字和下划线 (`a-zA-Z0-9_`)。建议你为关键实体设置唯一的名称，以方便调试和自动化测试。

## API 参考
对于`Entity` 类中有关实体层级的函数，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)
