通过 `OpacityControllerComponent` 快速控制 entity 的透明度。
## 重要提示

* `OpacityControllerComponent` 会影响其所在节点及所有子节点的整体透明度。
* 若父节点与子节点都挂载了 `OpacityControllerComponent`，子节点的最终透明度为父节点和子节点的 `opacity` 值的乘积。例如，若节点 A 与节点 B 构成父子节点关系，A 的 `opacity = 0.6`，B 的 `opacity = 0.5`，则 B 的最终渲染透明度为 `0.6 × 0.5 = 0.3`。
* 对于挂载了 `OpacityControllerComponent` 的 entity，若你为该 entity 的 SpatialView 及 SpatialView 的父 view 设置了 alpha 值，则该 entity 的渲染透明度需要乘以该 alpha 值。
* `OpacityControllerComponent` 会影响粒子的透明度。
* `OpacityControllerComponent` 对 `PortalMaterial` 不生效。

## 设置 entity 的透明度
### 3D 场景：单个 entity

* 直接通过设置 `OpacityControllerComponent` 来更改 entity 的整体透明度：

   以下代码实现了一个可交互的 3D 场景界面，用户可以通过滑块实时调节并观察 3D entity 的透明度变化。
   ```Kotlin
   @Composable
   fun OpacityController3DOnly() {
       // 定义 entity 的初始透明度（半透明）
       var entityOpacity by remember { mutableFloatStateOf(0.5f) }
       
       // 垂直布局容器，用于放置 3D 视图与滑块控制
       Column(
           modifier = Modifier.fillMaxSize().backgroundMaterial(),
           horizontalAlignment = Alignment.CenterHorizontally,
           verticalArrangement = Arrangement.Center,
       ) {
           SpatialView(
               modifier = Modifier.size(300.dp, 200.dp),
               // 每次状态（例如 entityOpacity）变化时，触发更新回调
               update = { content, _ ->
                   // 获取当前场景中的第一个 entity，并为其设置 OpacityControllerComponent
                   content.entities
                       .firstOrNull()
                       ?.components
                       ?.set(OpacityControllerComponent(entityOpacity))
               },
           ) { content, _ ->
               val entity = withContext(Dispatchers.IO) {
                   Entity.load("asset://model/pico_robot_static.usdz")
               }.also {
                   it.components.get<TransformComponent>()?.scaleBy(0.3f)
               }
               content.addEntity(entity)
           }
           Spacer(modifier = Modifier.size(20.dp))        
           // 文本：展示 entity 当前的透明度数值
           Text("Slide to change entity opacity to $entityOpacity")        
           // 滑块：用于实时修改 entity 的透明度     
           Slider(value = entityOpacity, onValueChange = { entityOpacity = it })
       }
   }
   ```

* 通过 view 的透明度来控制 entity 的透明度：

   以下代码实现了一个可交互示例，用户可以通过滑块实时调整 view 的透明度，从而影响整个 3D SpatialModelView 的整体透明效果。
   ```Kotlin
   @Composable
   fun EntityOpacityAffectedByViewAlpha() {
       // 使用 Compose 状态保存 view 当前的透明度（0.5），该值会实时影响 SpatialModelView 的整体透明度
       var alpha by remember { mutableFloatStateOf(0.5f) }
       
       // 垂直布局容器：负责组织 3D 视图与透明度调节控件
       Column(
           modifier = Modifier.fillMaxSize().backgroundMaterial().depth(400.dp),
           horizontalAlignment = Alignment.CenterHorizontally,
           verticalArrangement = Arrangement.Center,
       ) {
           SpatialModelView(
               // view 的大小和透明度
               modifier = Modifier.size(400.dp, 400.dp).alpha(alpha),
               resizability = Resizability.FitInside,
               source = Source.assets("model/pico_robot_static.usdz")
           )
           Spacer(modifier = Modifier.size(30.dp))        
           // 文本：展示 entity 当前的透明度数值
           Text("Slide to change view alpha to $alpha", fontSize = 28.sp, color = Color.White)        
           // 滑块：用于实时修改 entity 的透明度
           Slider(value = alpha, onValueChange = { alpha = it })
       }
   }
   ```


### 3D 场景：父子级关系的 entity
你可以分别控制两个是父子级关系的 entity 的透明度。子 entity 的实际透明度为二者透明度的乘积。

以下代码实现了一个父子级 entity 的透明度控制示例，用户可分别通过滑块调节父 entity 和子 entity 的透明度，并观察它们在场景中的最终显示效果。
```Kotlin
@Composable
fun OpacityTimesInEntityTree() {
    // 定义父 entity 和子 entity 的初始透明度（完全不透明）
    var parentOpacity by remember { mutableFloatStateOf(1.0f) }
    var childOpacity by remember { mutableFloatStateOf(1.0f) }
    
    // 使用 Column 布局居中显示 3D 视图与透明度控制滑块
    Column(
        modifier = Modifier.fillMaxSize().backgroundMaterial(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
    ) {
        SpatialView(
            modifier = Modifier.size(300.dp, 200.dp),
            update = { content, _ ->
                // 获取父 entity
                val parent = content.entities
                    .firstOrNull()
                // 获取名为 "child" 的子 entity
                val child = parent?.getChildren()?.firstOrNull {it.getName() == "child"}
                // 为父 entity 设置 OpacityControllerComponent
                parent?.components
                    ?.set(OpacityControllerComponent(parentOpacity))
                // 为子 entity 设置 OpacityControllerComponent
                child?.components
                    ?.set(OpacityControllerComponent(childOpacity))
            },
        ) { content, _ ->
            val entity = withContext(Dispatchers.IO) {
                Entity.load("asset://model/pico_robot_static.usdz")
            }.also {
                it.components.get<TransformComponent>()?.scaleBy(0.3f)
            }
            // 从父 entity 中克隆出一个完整 entity，并将其作为父 entity 的子 entity
            entity.clone(Entity.CloneOptions(recursive = true))?.also {
                it.setName("child") 
                it.components.set(TransformComponent().apply {
                    position = Vector3(0.6f, 0f, 0f)
                })
                entity.addChild(it)
            }
            // 将父 entity 添加进渲染内容中
            content.addEntity(entity)
        }
        Spacer(modifier = Modifier.size(20.dp))
        // 文本：展示父 entity 当前的透明度数值
        Text("Slide to change parent opacity to $parentOpacity", fontSize = 28.sp, color = Color.White)
        // 滑块：用于控制父 entity 的透明度
        Slider(value = parentOpacity, onValueChange = { parentOpacity = it })
        Spacer(modifier = Modifier.size(20.dp))
        // 文本：展示子 entity 当前的透明度数值
        Text("Slide to change child opacity to $childOpacity", fontSize = 28.sp, color = Color.White)
        // 滑块：用于控制子 entity 的透明度
        Slider(value = childOpacity, onValueChange = { childOpacity = it })
    }
}
```

### 2D&3D 混合场景
对于挂载了 `OpacityControllerComponent` 的 entity，若你为该 entity 的 SpatialView 及 SpatialView 的父 View 设置了 alpha 值，则该 entity 的渲染透明度需要乘以该 alpha 值。
从以下例子可以观察到，随着 view 的青色背景越来越透明，机器人模型也越来越透明，高于其自身设置的透明度。

以下代码实现了一个 2D 和 3D 混合场景的透明度控制示例，用户可分别通过滑块调节 3D 模型自身的透明度与整个视图的透明度，从而观察两者叠加后的最终显示效果（entity opacity × view alpha）。
```Kotlin
@Composable
fun EntityOpacityTimesViewAlpha() {
    // 定义 entity 的初始透明度（完全不透明）
    var entityOpacity by remember { mutableFloatStateOf(1.0f) }
    // 定义 view 的初始透明度（完全不透明）
    var viewOpacity by remember { mutableFloatStateOf(1.0f) }
    // 布局容器，用于垂直排列 view 与两个透明度控制滑块
    Column(
        modifier = Modifier.fillMaxSize().backgroundMaterial(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
    ) {
        SpatialView(
            // 设置 view 的大小、透明度、背景色
            modifier = Modifier.size(300.dp, 200.dp).alpha(viewOpacity).background(Color.Cyan),
            update = { content, _ ->
                content.entities
                    // 获取当前场景中第一个 entity
                    .firstOrNull()
                    ?.components
                    // 为该 entity 设置 OpacityControllerComponent
                    ?.set(OpacityControllerComponent(entityOpacity))
            },
        ) { content, _ ->
            val entity = withContext(Dispatchers.IO) {
                Entity.load("asset://model/pico_robot_static.usdz")
            }.also {
                it.components.get<TransformComponent>()?.scaleBy(0.3f)
            }
            content.addEntity(entity)
        }
        Spacer(modifier = Modifier.size(20.dp))
        // 文本：展示 entity 当前的透明度数值
        Text("Slide to change entity opacity to $entityOpacity", fontSize = 28.sp, color = Color.White)
        // 滑块：用于控制 entity 透明度
        Slider(value = entityOpacity, onValueChange = { entityOpacity = it })
        Spacer(modifier = Modifier.size(20.dp))
        // 文本：展示 view 当前的透明度数值
        Text("Slide to change view opacity to $viewOpacity", fontSize = 28.sp, color = Color.White)
        // 滑块：用于控制 view 的透明度
        Slider(value = viewOpacity, onValueChange = { viewOpacity = it })
    }
}
```

## 对粒子透明度的影响
场景中的粒子系统作为一个 entity，其透明度也可以通过 `OpacityControllerComponent` 控制。

以下代码实现了一个可交互示例，用户可以通过滑块实时调节粒子系统 entity 的透明度，并在场景中查看效果。
```Kotlin
@Composable
fun OpacityControllerAndParticle() {
    // 定义 entity 的初始透明度（完全不透明）
    var entityOpacity by remember { mutableFloatStateOf(1.0f) }
    
    // 使用 Column 布局居中放置 3D 视图与控制滑块
    Column(
        modifier = Modifier
            .fillMaxSize()
            .backgroundMaterial(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
    ) {
        // SpatialView：用于在 Compose 中显示 3D entity（此处为粒子系统）
        SpatialView(
            modifier = Modifier.size(300.dp, 300.dp),
            // update 回调：当 entityOpacity 变化时触发
            update = { content, _ ->
                // 获取当前场景中的第一个 entity（即粒子系统）
                content.entities
                    .firstOrNull()
                    ?.components
                    // 为该 entity 设置 OpacityControllerComponent
                    ?.set(OpacityControllerComponent(entityOpacity))
            },
        ) { content, _ ->
            withContext(Dispatchers.IO) {
                AssetBundle.load("asset://${Configs.BUNDLE_NAME}.bundle")
                    .loadModel("SimpleParticle")
            }.also {
                // 将 entity 添加为 SpatialView 的渲染内容
                content.addEntity(it)
            }
        }
        Spacer(modifier = Modifier.size(20.dp))
        // 文本：展示粒子当前的透明度数值
        Text(
            "Slide to change particle opacity to $entityOpacity",
            fontSize = 28.sp,
            color = Color.White
        )
        // 滑块：用于控制粒子的透明度
        Slider(value = entityOpacity, onValueChange = { entityOpacity = it })
    }
}
```

## API 参考
`OpacityControllerComponent` 类提供了用于控制 entity 透明度的属性和函数，详情参阅 API 参考。根据你所处的地理位置选择合适的文档链接：

* 中国大陆：[https://developer-cn.picoxr.com/spatial-api/index.html](https://developer-cn.picoxr.com/spatial-api/index.html)
* 非中国大陆：[https://developer.picoxr.com/spatial-api/index.html](https://developer.picoxr.com/spatial-api/index.html)
