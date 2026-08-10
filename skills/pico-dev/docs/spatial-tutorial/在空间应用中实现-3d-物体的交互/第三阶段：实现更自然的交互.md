# 开始之前
本阶段在《[第二阶段：从基础交互到复合交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第二阶段：从基础交互到复合交互.md)》完成后的项目上继续开发。你的 `HomeStage.kt` 应当处于第二阶段最后一节的最终状态：包含 8 大行星场景、`enableInteraction()` 扩展函数、单手拖拽与双手缩放手势。本阶段将引入 `InteractionKind` 区分捏合与拨动，并通过 `RigidBodyComponent` / `PhysicsVelocityComponent` 实现自然的物理旋转。
## **你要实现什么**
完成本阶段教程后，你将添加一个全新的交互动作和效果：单手拨动行星，让它自然地旋转，实现接近真实世界中交互体验。

## **你将学习什么**

* 如何识别应用中的交互触发方式。
* 如何使用 `RigidBodyComponent` 和 `PhysicsVelocityComponent` 实现更自然的物理效果。

## **你将需要什么**

* 完成《[第二阶段：从基础交互到复合交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第二阶段：从基础交互到复合交互.md)》中的全部内容。
* PICO 设备或 PICO Emulator。
   PICO Emulator 暂不支持 Poke 这种交互动作。因此，你只能在 PICO 真机上测试单手拨动行星的效果。

* **预计耗时：**约 40 分钟。

# 第一步：识别交互动作
在常规开发中，你通常只需关注拖拽或缩放等手势。但在高级应用场景下，精确识别用户是如何触发这些交互的，将有助于提升应用的体验。
为此，所有以 `detectSpatial` 开头的接口（`detectSpatialPointerEvent()` 除外）都在其回调中提供了 `InteractionKind` 属性，用以明确标识当前的交互触发方式。

* **单手交互接口**：回调参数中直接包含 `interactionKind` 变量。
* **双手交互接口**：由于双手可能使用不同的交互方式，回调参数会分别提供 `leftInteractionKind`（左手）和 `rightInteractionKind`（右手）两个变量。

目前，系统支持的 `InteractionKind` 类型包括：
| **直接捏合** | **戳** | **眼睛看，手部捏合** | **手柄射线点击** | **指针** |
| --- | --- | --- | --- | --- |
|; **DirectPinch** |; **Poke** |; **GazePinch** |; **RayBasedPinch** |; **Pointer** |
通过区分不同的交互动作，你可以更精确地了解用户的意图，从而实现更自然的交互体验。
在本阶段教程中，我们将利用这一机制，为行星实现两种截然不同的交互方式：

* **单手拖拽**：实现行星的平移。
* **单手拨动**：实现行星沿 Y 轴的旋转。

你只需使用 `detectSpatialDragGesture()` 这一个函数，就能同时实现这两种操作。关键在于检查回调中的 `InteractionKind` 属性，并根据其类型为同一个手势配置差异化的响应逻辑：

* **捏合交互 (`DirectPinch`, `GazePinch`)**：当用户通过捏合手势抓住物体时，系统调用 `dragToMove()` 来实现空间平移。
* **指推交互 (`Poke`)**：当用户用手指“拨动”物体表面时，系统调用 `dragToRotate()` 来实现轴向旋转。

这种设计可以有效区分用户操作，让三维物体拥有“捏住移动，拨动旋转”的真实交互感，同时避免了功能上的冲突。
## 根据  InteractionKind 属性判断交互方式
在 `detectSpatialDragGesture()` 的回调函数中，你可以获取 `dragValue` 参数（`SpatialDragValue` 类型）。通过访问其 `interactionKind` 属性，即可精准判断用户的交互方式，并分别执行相应的业务逻辑。
你可以使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
```Kotlin
package com.pico.spatial.tutorial.interaction.content

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import com.pico.spatial.core.ecs.DirectionalLightComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.core.math.Vector3
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.toColor4
import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.HoverEffectComponent
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.ui.platform.LengthUnit
import com.pico.spatial.ui.foundation.gesture.detectSpatialScaleGesture
import com.pico.spatial.ui.foundation.gesture.data.InteractionKind


private fun Entity.enableInteraction() {
    val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
    val centerOffset = boundingBox.center
    val collisionComponent = CollisionComponent(
        collisionShape = listOf(
            ShapeResource
                .createSphere(boundingBox.size.x / 2f)
                .offsetByTranslation(centerOffset)
        ),
        physicsMaterial = PhysicsMaterialResource(),
    )
    components.set(collisionComponent)
    components.set(InteractableComponent())
    components.set(HoverEffectComponent())
}

@Composable
fun HomeStage() {
    val context = LocalContext.current
    val converter = LocalPhysicalLengthConverter.current
    val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    SpatialView(
        Modifier
            .pointerInput(Unit) {
                detectSpatialDragGesture(context) { dragValue ->
                    val offsetXInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.x.toDp(), LengthUnit.Meters)
                    }
                    val offsetYInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.y.toDp(), LengthUnit.Meters)
                    }
                    val offsetZInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.z.toDp(), LengthUnit.Meters)
                    }
                    val kind = dragValue.interactionKind
                    when (kind) {
                        InteractionKind.DirectPinch, InteractionKind.GazePinch -> {
                            dragValue.targetEntity?.apply {
                                components[TransformComponent::class.java]?.apply {
                                    setPosition(
                                        Vector3(
                                            position.x + offsetXInMeter,
                                            position.y - offsetYInMeter,
                                            position.z + offsetZInMeter,
                                        )
                                    )
                                }
                            }
                        }
                        InteractionKind.Poke -> {
                            // TODO Handle your rotate logic here.
                        }

                        else -> {
                            // TODO You can also handle other types of interactions in your own case.
                        }
                    }
                }
            }
            .pointerInput(Unit) {
            detectSpatialScaleGesture(context) { scaleValue ->
                scaleValue.targetEntity?.apply {
                    components[TransformComponent::class.java]?.apply {
                        setScaleVector(scaleVector * scaleValue.scaleValue)
                    }
                }

            }
        },
        initial = { content, attachments ->
            val bundle = withContext(Dispatchers.IO) {
                AssetBundle.load("asset://editor-planets.bundle")
            }

            val entity = Entity.loadSuspend(
                modelName = "Planets", bundle = bundle)
                .apply {
                    components[TransformComponent::class.java]?.apply {
                        scaleVector = Vector3(1f)
                        position = Vector3(0f, 1.5f, -1.5f)
                    }
                    planets.forEach {
                        findEntity(it)?.enableInteraction()
                    }
                }
            bundle.close()
            content.addEntity(entity)
            val lightEntity = Entity().apply {
                components.set(DirectionalLightComponent(
                    Color(0xFFFFFFFF).toColor4(),
                    500f))
            }
            content.addEntity(lightEntity)
        },
    )
}
```

## 实现单手拨动旋转
当用户使用“拨动”而非“抓取”手势时，让物体实时跟随手指旋转会显得不自然，并产生一种“粘滞感”。
为了提供更真实的物理反馈，我们推荐实现“延迟旋转”效果。这种方法模拟了现实中拨动地球仪的体验：当你的手指划过物体表面并抬起时，物体会根据滑动的速度和方向开始旋转，从而体现出惯性和质量感。
要实现此效果，我们不会在 `detectSpatialDragGesture()` 的回调过程中实时旋转物体，而是采用“先记录，后触发”的策略：

1. 在整个拖拽过程中，使用 `draggedOffset` 变量持续累积用户的滑动手势位移。
2. 引入一个布尔变量 `isRotated` 作为状态标记。仅当交互类型为 `Poke` 时，才将其设置为 `true`。

通过这种方式，旋转逻辑只会在 `Poke` 手势结束时被触发，从而精确模拟了“拨动”这一动作的物理反馈。
你可以使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
```Kotlin
package com.pico.spatial.tutorial.interaction.content

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import com.pico.spatial.core.ecs.DirectionalLightComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.core.math.Vector3
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.toColor4
import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.HoverEffectComponent
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.ui.platform.LengthUnit
import com.pico.spatial.ui.foundation.gesture.detectSpatialScaleGesture
import com.pico.spatial.ui.foundation.gesture.data.InteractionKind
import com.pico.spatial.ui.geometry.Offset3D
import androidx.compose.runtime.getValue


private fun Entity.enableInteraction() {
    val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
    val centerOffset = boundingBox.center
    val collisionComponent = CollisionComponent(
        collisionShape = listOf(
            ShapeResource
                .createSphere(boundingBox.size.x / 2f)
                .offsetByTranslation(centerOffset)
        ),
        physicsMaterial = PhysicsMaterialResource(),
    )
    components.set(collisionComponent)
    components.set(InteractableComponent())
    components.set(HoverEffectComponent())
}

@Composable
fun HomeStage() {
    val context = LocalContext.current
    val converter = LocalPhysicalLengthConverter.current
    val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    var isRotated by remember { mutableStateOf(false) }
    var draggedOffset by remember { mutableStateOf(Offset3D.Zero) }

    SpatialView(
        Modifier
            .pointerInput(Unit) {
                detectSpatialDragGesture(
                    context,
                    onDragStart = {
                         draggedOffset = Offset3D.Zero
                    },
                    onDragEnd = {
                        if (isRotated) {
                            // Rotate the entity by the dragged offset
                        }
                    }
                ) { dragValue ->
                    val kind = dragValue.interactionKind
                    val offsetXInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.x.toDp(), LengthUnit.Meters)
                    }
                    val offsetYInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.y.toDp(), LengthUnit.Meters)
                    }
                    val offsetZInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.z.toDp(), LengthUnit.Meters)
                    }
                    val offset3DInMeter = Offset3D(offsetXInMeter, offsetYInMeter, offsetZInMeter)

                    when (kind) {
                        InteractionKind.DirectPinch, InteractionKind.GazePinch -> {
                            dragValue.targetEntity?.apply {
                                components[TransformComponent::class.java]?.apply {
                                    setPosition(
                                        Vector3(
                                            position.x + offsetXInMeter,
                                            position.y - offsetYInMeter,
                                            position.z + offsetZInMeter,
                                        )
                                    )
                                }
                            }
                            isRotated = false
                        }

                        InteractionKind.Poke -> {
                            draggedOffset += offset3DInMeter
                            isRotated = true
                        }

                        else -> {
                            // You can also handle other types of interactions in your own case.
                            isRotated = false
                        }
                    }
                }
            }
            .pointerInput(Unit) {
            detectSpatialScaleGesture(context) { scaleValue ->
                scaleValue.targetEntity?.apply {
                    components[TransformComponent::class.java]?.apply {
                        setScaleVector(scaleVector * scaleValue.scaleValue)
                    }
                }

            }
        },
        initial = { content, attachments ->
            val bundle = withContext(Dispatchers.IO) {
                AssetBundle.load("asset://editor-planets.bundle")
            }

            val entity = Entity.loadSuspend(
                modelName = "Planets", bundle = bundle)
                .apply {
                    components[TransformComponent::class.java]?.apply {
                        scaleVector = Vector3(1f)
                        position = Vector3(0f, 1.5f, -1.5f)
                    }

                    planets.forEach {
                        findEntity(it)?.enableInteraction()
                    }

                }
            bundle.close()
            content.addEntity(entity)
            val lightEntity = Entity().apply {
                components.set(DirectionalLightComponent(
                    Color(0xFFFFFFFF).toColor4(),
                    500f))
            }
            content.addEntity(lightEntity)
        },
    )
}
```

# 第二步：实现物理旋转
在实现基本交互后，下一步是为“延迟旋转”打造理想的交互效果。
一种常见的方法是使用补间动画。你只需定义旋转的起始和目标状态，系统便会自动生成平滑的过渡动画。然而，尽管实现简单，补间动画却存在一些固有的局限性，可能导致旋转效果不自然：

* **最短路径问题**：当目标旋转角度超过 180°（例如 270°）时，动画会为了效率而选择最短路径（即反向旋转 90°），导致物体朝错误的方向转动。
* **旋转圈数丢失**：如果用户拨动的幅度超过 360°，动画只会表现出余数部分的旋转，而丢失了完整的圈数。

为了克服这些限制并创造沉浸式体验，我们推荐使用物理系统。
物理系统的核心是模拟真实的运动力学。你不再需要生硬地指定一个目标角度，而是可以将用户的滑动位移转化为物体的初始角速度。之后，物理引擎会接管后续的动力学计算，从而实现物体在受力后自然的旋转和减速效果，完美模拟真实世界中的惯性。
## 引入物理组件
要实现该物理效果，你需要为物体添加并配置以下组件：

1. **添加** `RigidBodyComponent`：为物体添加刚体组件，用于定义其物理属性，以便物理引擎能够进行模拟。
2. **锁定平移**：由于行星的位置已由拖拽逻辑控制，你应设置 `isTranslationLocked` 属性。这可以防止物理引擎改变物体的位置，确保物理模拟仅影响旋转。
3. **设置角阻尼 (**`angularDamping`**)**：此属性用于模拟摩擦力，使旋转能够自然减速。数值越高，物体停止旋转的速度就越快。建议将初始值设为 `1.0f`，你可以根据实际体验进行调整。

你可以使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
```Kotlin
package com.pico.spatial.tutorial.interaction.content

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import com.pico.spatial.core.ecs.DirectionalLightComponent
import com.pico.spatial.core.ecs.Entity
import com.pico.spatial.core.ecs.TransformComponent
import com.pico.spatial.core.ecs.resource.AssetBundle
import com.pico.spatial.core.math.Vector3
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import com.pico.spatial.ui.foundation.content.SpatialView
import com.pico.spatial.ui.foundation.content.toColor4
import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.pico.spatial.core.ecs.CollisionComponent
import com.pico.spatial.core.ecs.HoverEffectComponent
import com.pico.spatial.core.ecs.InteractableComponent
import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
import com.pico.spatial.core.ecs.resource.ShapeResource
import com.pico.spatial.ui.platform.LengthUnit
import com.pico.spatial.ui.foundation.gesture.detectSpatialScaleGesture
import com.pico.spatial.ui.foundation.gesture.data.InteractionKind
import com.pico.spatial.ui.geometry.Offset3D
import androidx.compose.runtime.getValue
import com.pico.spatial.core.ecs.RigidBodyComponent
import com.pico.spatial.core.ecs.simulation.RigidBodyMode
import com.pico.spatial.core.math.Bool3


private fun Entity.enableInteraction() {
    val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
    val centerOffset = boundingBox.center
    val collisionComponent = CollisionComponent(
        collisionShape = listOf(
            ShapeResource
                .createSphere(boundingBox.size.x / 2f)
                .offsetByTranslation(centerOffset)
        ),
        physicsMaterial = PhysicsMaterialResource(),
    )
    components.set(collisionComponent)
    components.set(InteractableComponent())
    components.set(HoverEffectComponent())
}

@Composable
fun HomeStage() {
    val context = LocalContext.current
    val converter = LocalPhysicalLengthConverter.current
    val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    var isRotated by remember { mutableStateOf(false) }
    var draggedOffset by remember { mutableStateOf(Offset3D.Zero) }

    SpatialView(
        Modifier
            .pointerInput(Unit) {
                detectSpatialDragGesture(
                    context,
                    onDragStart = {
                         draggedOffset = Offset3D.Zero

                    },
                    onDragEnd = {
                        if (isRotated) {
                            // Rotate the entity by the dragged offset
                        }
                    }
                ) { dragValue ->
                    val kind = dragValue.interactionKind
                    val offsetXInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.x.toDp(), LengthUnit.Meters)
                    }
                    val offsetYInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.y.toDp(), LengthUnit.Meters)
                    }
                    val offsetZInMeter = with(density) {
                        converter.dpToLength(dragValue.dragAmount.z.toDp(), LengthUnit.Meters)
                    }
                    val offset3DInMeter = Offset3D(offsetXInMeter, offsetYInMeter, offsetZInMeter)

                    when (kind) {
                        InteractionKind.DirectPinch, InteractionKind.GazePinch -> {
                            dragValue.targetEntity?.apply {
                                components[TransformComponent::class.java]?.apply {
                                    setPosition(
                                        Vector3(
                                            position.x + offsetXInMeter,
                                            position.y - offsetYInMeter,
                                            position.z + offsetZInMeter,
                                        )
                                    )
                                }
                            }
                            isRotated = false
                        }
                        InteractionKind.Poke -> {
                            draggedOffset += offset3DInMeter
                            isRotated = true
                        }
                        else -> {
                            // You can also handle other types of interactions in your own case.
                            isRotated = false
                        }
                    }
                }
            }
            .pointerInput(Unit) {
            detectSpatialScaleGesture(context) { scaleValue ->
                scaleValue.targetEntity?.apply {
                    components[TransformComponent::class.java]?.apply {
                        setScaleVector(scaleVector * scaleValue.scaleValue)
                    }
                }
            }
        },
        initial = { content, attachments ->
            val bundle = withContext(Dispatchers.IO) {
                AssetBundle.load("asset://editor-planets.bundle")
            }

            val entity = Entity.loadSuspend(
                modelName = "Planets", bundle = bundle)
                .apply {
                    components[TransformComponent::class.java]?.apply {
                        scaleVector = Vector3(1f)
                        position = Vector3(0f, 1.5f, -1.5f)
                    }

                    planets.forEach {
                        findEntity(it)?.enableInteraction()
                        // [Add] Enable Physics facilities
                        components.set(RigidBodyComponent().apply {
                            this.rigidBodyMode = RigidBodyMode.DYNAMIC
                            this.isTranslationLocked = Bool3(true)
                            this.angularDamping = 1f
                        })
                    }
                }
            bundle.close()
            content.addEntity(entity)
            val lightEntity = Entity().apply {
                components.set(DirectionalLightComponent(
                    Color(0xFFFFFFFF).toColor4(),
                    500f))
            }

            content.addEntity(lightEntity)
        },
    )
}
```

为行星添加 `RigidBodyComponent` 组件后，物理引擎便会接管其动态行为。如需了解该组件的详细属性配置，参阅《[添加碰撞和外部作用](./spatial-sdk_物理_添加碰撞和外部作用.md)》。
## 实现物体旋转
你可以通过配置 `PhysicsVelocityComponent` 来实现物体的旋转。

1. 创建一个 `rotateEntityByPhysics` 函数，它会根据用户的手部位移来旋转物体。
   ```Kotlin
   private fun rotateEntityByPhysics(target: Entity, offset: Offset3D) {
       val sensitivity = 7f
       val velocity = offset.x * sensitivity
   
       target.components.set(
           PhysicsVelocityComponent().apply {
               angularVelocity = Vector3(0f, velocity, 0f)
           }
       )
   }
   ```

   在 `rotateEntityByPhysics` 函数中，你可以将用户在 X 轴上的位移量映射为 `angularVelocity` 参数，从而控制物体的旋转。为了让旋转效果更符合直觉，函数引入了一个灵敏度系数 `sensitivity`。通过调整该系数，你可以平衡手势幅度与物体转速，以模拟操作真实地球仪的体验。如需深入了解 `PhysicsVelocityComponent` 的工作原理，参阅《[添加碰撞和外部作用](./spatial-sdk_物理_添加碰撞和外部作用.md)》。
2. 在 `detectSpatialDragGesture()` 的 `onDragEnd()` 回调中调用 `rotateEntityByPhysics()` 函数，即可实现行星的旋转效果。
   你可以使用下面的代码覆盖你的 Spatial 项目中`HomeStage.kt`中的内容。
   ```Kotlin
   package com.pico.spatial.tutorial.interaction.content
   
   import androidx.compose.runtime.Composable
   import androidx.compose.ui.Modifier
   import androidx.compose.ui.graphics.Color
   import androidx.compose.ui.input.pointer.pointerInput
   import androidx.compose.ui.platform.LocalContext
   import com.pico.spatial.core.ecs.DirectionalLightComponent
   import com.pico.spatial.core.ecs.Entity
   import com.pico.spatial.core.ecs.TransformComponent
   import com.pico.spatial.core.ecs.resource.AssetBundle
   import com.pico.spatial.core.math.Vector3
   import androidx.compose.runtime.mutableStateOf
   import androidx.compose.runtime.remember
   import androidx.compose.runtime.setValue
   import com.pico.spatial.ui.foundation.content.SpatialView
   import com.pico.spatial.ui.foundation.content.toColor4
   import com.pico.spatial.ui.foundation.gesture.detectSpatialDragGesture
   import com.pico.spatial.ui.platform.LocalPhysicalLengthConverter
   import kotlinx.coroutines.Dispatchers
   import kotlinx.coroutines.withContext
   import com.pico.spatial.core.ecs.CollisionComponent
   import com.pico.spatial.core.ecs.HoverEffectComponent
   import com.pico.spatial.core.ecs.InteractableComponent
   import com.pico.spatial.core.ecs.resource.PhysicsMaterialResource
   import com.pico.spatial.core.ecs.resource.ShapeResource
   import com.pico.spatial.ui.platform.LengthUnit
   import com.pico.spatial.ui.foundation.gesture.detectSpatialScaleGesture
   import com.pico.spatial.ui.foundation.gesture.data.InteractionKind
   import com.pico.spatial.ui.geometry.Offset3D
   import androidx.compose.runtime.getValue
   import com.pico.spatial.core.ecs.RigidBodyComponent
   import com.pico.spatial.core.ecs.simulation.RigidBodyMode
   import com.pico.spatial.core.math.Bool3
   import com.pico.spatial.core.ecs.PhysicsVelocityComponent
   
   // [Add] 添加 rotateEntityByPhysics 函数
   private fun rotateEntityByPhysics(target: Entity, offset: Offset3D) {
       val sensitivity = 7f
       val velocity = offset.x * sensitivity
   
       target.components.set(
           PhysicsVelocityComponent().apply {
               angularVelocity = Vector3(0f, velocity, 0f)
           }
       )
   }
   
   private fun Entity.enableInteraction() {
       val boundingBox = getVisualBounds(this, recursive = true, enabledOnly = true)
       val centerOffset = boundingBox.center
   
       // Use a sphere as collision
       val collisionComponent = CollisionComponent(
           collisionShape = listOf(
               ShapeResource
                   .createSphere(boundingBox.size.x / 2f)
                   .offsetByTranslation(centerOffset)
           ),
           physicsMaterial = PhysicsMaterialResource(),
       )
   
       components.set(collisionComponent)
   
       // Set interactable component
       components.set(InteractableComponent())
   
       // Set HoverEffect component
       components.set(HoverEffectComponent())
   }
   
   
   @Composable
   fun HomeStage() {
       val context = LocalContext.current
       val converter = LocalPhysicalLengthConverter.current
       val planets = listOf("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
   
       var isRotated by remember { mutableStateOf(false) }
       var draggedOffset by remember { mutableStateOf(Offset3D.Zero) }
       var draggedEntity by remember { mutableStateOf<Entity?>(null) }
   
       SpatialView(
           Modifier
               .pointerInput(Unit) {
                   detectSpatialDragGesture(
                       context,
                       onDragStart = {
                            draggedEntity?.components?.remove(PhysicsVelocityComponent::class.java)
                            draggedEntity = null
                            draggedOffset = Offset3D.Zero
   
                       },
                       onDragEnd = {
                           if (isRotated) {
                               draggedEntity?.let {
                                   // [Add] 调用 rotateEntityByPhysics 函数
                                   rotateEntityByPhysics(it, draggedOffset)
                               }
                           }
                       }
                   ) { dragValue ->
                       val kind = dragValue.interactionKind
                       val offsetXInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.x.toDp(), LengthUnit.Meters)
                       }
                       val offsetYInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.y.toDp(), LengthUnit.Meters)
                       }
                       val offsetZInMeter = with(density) {
                           converter.dpToLength(dragValue.dragAmount.z.toDp(), LengthUnit.Meters)
                       }
                       val offset3DInMeter = Offset3D(offsetXInMeter, offsetYInMeter, offsetZInMeter)
   
                       when (kind) {
                           InteractionKind.DirectPinch, InteractionKind.GazePinch -> {
                               dragValue.targetEntity?.apply {
                                   components[TransformComponent::class.java]?.apply {
                                       setPosition(
                                           Vector3(
                                               position.x + offsetXInMeter,
                                               position.y - offsetYInMeter,
                                               position.z + offsetZInMeter,
                                           )
                                       )
                                   }
                               }
                               isRotated = false
                           }
   
                           InteractionKind.Poke -> {
                               draggedOffset += offset3DInMeter
                               isRotated = true
                           }
   
                           else -> {
                               // You can also handle other types of interactions in your own case.
                               isRotated = false
                           }
                       }
                   }
               }
               .pointerInput(Unit) {
               detectSpatialScaleGesture(context) { scaleValue ->
                   scaleValue.targetEntity?.apply {
                       components[TransformComponent::class.java]?.apply {
                           setScaleVector(scaleVector * scaleValue.scaleValue)
                       }
                   }
               }
           },
           initial = { content, attachments ->
               val bundle = withContext(Dispatchers.IO) {
                   AssetBundle.load("asset://editor-planets.bundle")
               }
   
               val entity = Entity.loadSuspend(
                   modelName = "Planets", bundle = bundle)
                   .apply {
                       components[TransformComponent::class.java]?.apply {
                           scaleVector = Vector3(1f)
                           position = Vector3(0f, 1.5f, -1.5f)
                       }
                       planets.forEach {
                           findEntity(it)?.enableInteraction()
                           components.set(RigidBodyComponent().apply {
                               this.rigidBodyMode = RigidBodyMode.DYNAMIC
                               this.isTranslationLocked = Bool3(true)
                               this.angularDamping = 1f
                           })
                       }
                   }
               bundle.close()
               content.addEntity(entity)
               val lightEntity = Entity().apply {
                   components.set(DirectionalLightComponent(
                       Color(0xFFFFFFFF).toColor4(),
                       500f))
               }
               content.addEntity(lightEntity)
           },
       )
   }
   ```

   为了确保每次“拨动”都能正确生效，你需要用 `draggedEntity` 变量来记录被拖拽的物体。关键在于，你必须在 `onDragStart()` 回调中，及时移除该物体因上次交互而附加的 `PhysicsVelocityComponent`。
   如果不这样做，旧的物理速度会持续存在，导致系统在本次交互结束（`onDragEnd`）时无法应用新的速度。这将造成一种“锁死”状态：只有第一次拨动有效，后续所有操作都将失效。这种“先移除、后应用”的策略，能确保每一次交互都精准地捕捉并施加最新的动量。
3. 在 PICO 真机上运行应用。试着用手拨动行星，它就会自然地旋转起来。
   PICO Emulator 暂不支持 Poke 这种交互动作。因此，你只能在 PICO 真机上测试单手拨动行星的效果。

# 总结
恭喜你完成了本阶段的教程。
通过本阶段教程的学习，你学会了如何让应用更精准、更自然地响应用户的交互：

* 使用 `InteractionKind` 识别用户的具体交互方式。
* 运用 `RigidBodyComponent` 和 `PhysicsVelocityComponent` 实现更自然的物理效果。
