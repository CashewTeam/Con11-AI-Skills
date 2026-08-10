本文介绍 Shader Graph 的用户界面。
**Shader Graph** 标签页位于 PICO Spatial Editor 的最下方，包括 **Input Node** 面板、工作区和 **Shader Graph Inspector** 窗口。
## Input Node 面板
在 **Shader Graph** 标签页的最左侧，你可以添加输入节点（Input Node）。

Shader Graph 支持以下类型的输入节点。
| **输入类型** | **端口颜色** | **连线颜色** |
| --- | --- | --- |
| Integer |  |  |
| Float |  |  |
| Boolean |  |  |
| Vector2 |  |  |
| Vector3 |  |  |
| Vector4 |  |  |
| Color3 |  |  |
| Color4 |  |  |
| Filename |  |  |
| Matrix3 |  |  |
| Matrix4 |  |  |
## 工作区
在 **Shader Graph** 标签页中间的工作区，你可以为 Shader Graph 添加处理节点，连接输入节点、处理节点和输出节点。

### 打开节点创建页面
你可以通过以下任意一种方式打开节点创建页面。

* 点击右上方**➕New Node**。
* 在空白区域双击鼠标左键。
* 单击输入或输出端口。

### 右键快捷菜单
在工作区，你可以使用鼠标右键快捷菜单实现创建便签、创建或取消节点组、缩放自适应、自动排列节点、合成或拆分 node graph 节点、常量节点与输入节点之间的转换、以及对节点的拷贝、粘贴、删除等操作。

| **选项** | **说明** |
| --- | --- |
| Create Sticky Note | 创建便签。 |
| Create Group | 把当前节点加入节点组。 |
| Ungroup | 解散节点组，或将节点从分组中移除（只有节点组或加入节点组的节点有该选项）。 |
| Zoom Fit | 缩放自适应，快捷键为 F。 |
| Auto Layout | 自动排列节点。 |
| Compose Node Graph | 将所选节点合成一个 Node Graph 节点。 |
| Decompose Node Graph | 将所选的 Node Graph 节点拆分成多个节点（只有 Node Graph 节点有该选项）。 |
| Create Node Graph Instance | 创建 Node Graph 节点的实例（只有 Node Graph 节点有该选项）。 |
| Convert to Input | 将常量节点转换为输入节点（只有常量节点有该选项）。 |
| Convert to Constant | 将输入节点转换为常量节点（只有输入节点有该选项）。 |
| Cut | 剪切，快捷键 Command/Ctrl+X。 |
| Copy | 拷贝，快捷键 Command/Ctrl+C。 |
| Paste | 粘贴，快捷键 Command/Ctrl+V。 |
| Duplicate | 复制，快捷键 Command/Ctrl+D。 |
| Delete | 删除，快捷键 Backspace/Delete。 |
## Shader Graph Inspector 窗口
在 **Shader Graph** 标签页的最右侧，你可以通过 **Shader Graph Inspector** 设置已选中节点的属性。

你在新建 Shader Graph 时，系统会自动创建一个 PreviewSurface 节点和一个输出节点（Outputs 节点）。

