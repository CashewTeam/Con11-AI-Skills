欢迎来到 PICO Spatial SDK 的《在空间应用中实现 3D 物体的交互》系列教程。
在空间应用中，用户与 3D 物体的交互是必不可少的。如何自然地与 3D 空间中的物体进行交互，是提升空间应用体验的核心。通过这个系列教程，你将学习到如何通过 PICO Spatial SDK 为 3D 物体赋予全新的生命力，循序渐进地体验从“可见”到“可触”，再到“自然交互”的完整过程。
完成整个系列教程后，你将能够：

* 为 3D 物体添加碰撞体（`CollisionComponent`）、可交互组件（`InteractableComponent`）和高亮反馈（`HoverEffectComponent`），让"可见"的物体变得"可触"。
* 使用 `detectSpatialDragGesture()` 与 `detectSpatialScaleGesture()` 实现单手拖拽与双手缩放等基础交互。
* 通过 `TargetEntity.hit()` / `TargetEntity.any()` 精确控制可被交互的物体范围，并通过多个 `Modifier.pointerInput` 组合实现复合交互。
* 通过 `InteractionKind` 区分捏合、拨动等不同的交互触发方式，并据此分发差异化的业务逻辑。
* 通过 `RigidBodyComponent` 与 `PhysicsVelocityComponent` 让物体具备惯性、阻尼等真实物理表现，实现接近现实世界的自然交互。

本系列教程包含以下三个阶段：

* [第一阶段：让 3D 物体可以被交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第一阶段：让-3d-物体可以被交互.md)
   在空间应用中展示一个地球模型，并且和它进行最基本的交互。
* [第二阶段：从基础交互到复合交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第二阶段：从基础交互到复合交互.md)
   在空间应用中展示 8 大行星的模型，并且和其中的任意一个行星进行交互。
* [第三阶段：实现更自然的交互](./spatial-tutorial_在空间应用中实现-3d-物体的交互_第三阶段：实现更自然的交互.md)
   添加交互逻辑，单手拨动行星，让它自然地旋转，实现接近真实世界中的交互体验。

