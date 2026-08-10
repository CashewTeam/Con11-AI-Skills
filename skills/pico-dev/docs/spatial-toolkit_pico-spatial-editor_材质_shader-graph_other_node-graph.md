可包含着色节点及其他节点图的节点。

**Node Graph** 节点用于封装可在不同材质中复用的节点图，你可以将其视为一个能包含着色节点及其他节点的容器。若你需要频繁使用某些重复的节点组合（子图），便可将其定义为一个可复用的 **Node Graph** 模块。
**Node Graph** 节点中的图与 Shader Graph 的节点图几乎完全相同。主要区别在于，在节点图中你可以定义任意数量的自定义输入和输出。你需要为每个自定义输入和输出指定名称和类型。
## 节点使用说明
### 直接添加 Node Graph 节点
你可以直接添加 Node Graph 节点，然后双击该节点并编辑节点图中的节点逻辑。

你可以按需为节点图添加输入节点和输出节点。

### 把多个节点组合成 Node Graph 节点
下面展示了如何把多个节点组合成 Node Graph 节点。
用鼠标选中需要组合的节点，右击并选中 **Compose Node Graph**。

然后，你就可以看到组合后的 Node Graph。

你可以双击该 Node Graph 查看并编辑其节点逻辑。

### 基于 Node Graph 节点创建 Node Graph 实例
你可以右击 Node Graph，然后选择 **Create Node Graph Instance** 创建一个 Node Graph 实例。

Node Graph 实例会继承原 Node Graph 的节点逻辑。 如果你修改了原 Node Graph，相关的 Node Graph 实例也会被同步更新。反过来，如果你修改了Node Graph 实例，原 Node Graph 也会被同步更新。

###

