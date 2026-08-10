本文介绍 Spatial Editor 支持的 3D 模型格式。
Spatial Editor 仅支持 USD（Universal Scene Description）作为 3D 模型的导入格式。USD 包含两个核心概念：Prim（最小逻辑容器单位）和 Reference（Prim 的复用机制），二者共同构成 USD 高效管理 3D 场景的基础。
## 什么是 USD
[USD](https://openusd.org/release/index.html) 是 Pixar 开发的开源 3D 场景描述格式。USD 以 Prim 构建层级结构，通过 Reference 实现跨文件资源复用，从而灵活组织、高效编辑复杂场景并支持团队协作。USD 包含以下四种文件格式，均围绕 Prim 与 Reference 机制设计：

* .usd：可以包含人类可读的文本格式（ASCII）或二进制格式的数据。
* .usda：一种人类可读的文本格式（ASCII），适合进行编辑和版本控制。在 Spatial Editor 中，场景（Scene）以 .usda 文件的格式存储。
* .usdz：单文件打包格式，集成模型、贴图等资源，适合 AR 场景分发，其内部仍以 Prim 层级存储数据。
* .usdc：二进制格式，体积紧凑、加载高效，不含外部资源引用，Prim 数据以二进制编码存储，适合高性能生产环境。

## USD 的基本容器：Prim
Prim 是 USD 的最小逻辑容器单位，既是 USD 层级结构的节点，也是 Reference 操作的对象（类似文件系统的文件夹或面向对象编程的实例）。Prim 的作用如下：

* Prim 构成 USD 场景的树状结构。Prim 可包含子 Prim，形成如 `/World/Characters/Hero` 的路径标识（SdfPath）。这种层级通过 Reference 可跨文件扩展，例如将外部 “角色.usd” 中的 `/Character` Prim 引用为 `/World/Characters` 的子节点。
* Prim 可表示任意 3D 场景实体，包括：
   * 具体场景元素：直接构成场景视觉或物理属性的实体，包括几何体（Mesh、Cube）、光源（SphereLight）、摄像机（UsdGeomCamera）等。
   * 抽象结构：用于组织和变换场景实体的逻辑容器，包括 Xform 和 Scope：
      * Xform：带变换属性（平移、旋转、缩放）的 Prim，通过 Reference 引用后可独立调整空间位置，实现多实例布局。例如将同一把椅子的 Xform Prim 引用 4 次，放置在桌子四周。
      * Scope：纯逻辑分组 Prim，无变换属性，适合通过 Reference 整合多个无空间变换需求的 Prim。例如将 “道具集.usd” 中的 `/Props` Scope Prim 引用为 `/World` 的子节点。
   * 支持组件：为场景实体提供外观或动画能力的功能性实体，包括材质（UsdPreviewSurface）、骨骼（Skeleton）等。

Prim 通过以下定义行为与关联：

* 属性（Attributes）：存储数值数据（如尺寸、颜色），支持动画关键帧。
* 关系（Relationships）：建立 Prim 间逻辑连接，Reference 本质是一种指向外部 Prim 的特殊关系（如将 `/Chair` Prim 引用为 `/Table` 的子节点）。
* 元数据（Metadata）：控制 Prim 行为的附加信息，如 `active`（是否激活）、`hidden`（是否隐藏）。

## USD 的复用机制：Reference
Reference 通过非破坏性方式将外部 USD 文件中的 Prim 组合到当前空间容器，用于连接分散的 Prim 资源。Reference 的作用如下：

* 通过 Reference 可将一个或多个 USD 文件中的 Prim 引用到当前空间容器的任意层级下，实现资源复用。例如：将 “椅子.usd” 中的 `/Chair` Prim 引用 4 次，快速构建 “一桌四椅” 场景，每个引用的 Prim 保持独立可编辑性。
* 引用的 Prim 数据可在当前层（或更强优先级的层）中覆写（override），如修改位置、材质或动画，而不影响原始 USD 文件。这使得同一 Prim 引用可生成多个变体实例（如 “红色椅子” “蓝色椅子”）。

Reference 具有以下特性：

* 灵活的引用数量：一个 Prim 可以不包含任何引用，也可以同时引用一个或多个外部 Prim。你可以随时添加、删除或修改这些引用，从而动态调整场景的构成。
* 内存与性能优化：当你多次引用同一个 USD 文件时，其内容在内存中仅加载一次，以节省资源。同时，每个引用实例都是独立的，因此修改其中一个实例（例如，改变四把椅子中一把的颜色）不会影响其他实例。
* 循环引用安全：USD 的设计可以防止产生循环依赖。例如，一个场景可以包含 A 引用 B、B 引用 C 的结构，但系统会阻止 A 引用 B 的同时 B 又引用 A 这样的循环。

## 应用场景
USD 的应用场景如下：

* 大型场景装配：将建筑、车辆、植被等独立 USD 资源（含 Prim）通过 Reference 引用，快速搭建开放世界环境。
* 多实例资源管理：对同一辆车做脏旧、干净两种外观版本，只需在 Reference 之上覆写材质，即可得到多实例、可变体效果。
* 跨部门协同：布局、模型、动画部门基于同一套 Prim 引用工作，非破坏性修改互不干扰，提升协作效率。

