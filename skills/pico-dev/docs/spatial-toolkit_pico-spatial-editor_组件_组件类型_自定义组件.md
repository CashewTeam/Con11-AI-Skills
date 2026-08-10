本文介绍 PICO Spatial Editor（Spatial Editor）中的自定义组件。
## 什么是自定义组件
自定义组件用于存储特定功能的数据，从而扩展系统能力。详情参阅 [自定义系统和组件](./spatial-sdk_实体-组件-系统（ecs）_自定义系统和组件.md)。你可以在 Android Studio 中为 Spatial Editor 项目创建、更新或删除自定义组件，也可以在 PICO Spatial Editor（Spatial Editor）中为 Spatial Editor 项目创建自定义组件。详情参阅 [管理自定义组件](/use-custom-components)。

* 你在 Android Studio 中对自定义组件的创建、更新或删除操作会自动同步到 Spatial Editor 中。
* 你在 Spatial Editor 中对自定义组件的创建操作也会自动同步到 Android Studio 中。但是，你只能在 Android Studio 中更新或删除自定义组件。

### 创建自定义组件
参考下面的步骤在 Spatial Editor 中为 Spatial Editor 项目创建自定义组件。Spatial Editor 不支持更新或删除自定义组件。你需要在 Android Studio 中更新或删除自定义组件。详情参阅 [在 Android Studio 中管理自定义组件](/editor/use-custom-components)。

1. 在 Spatial Editor 的 **Inspector** 窗口，单击 **Add Component**。

2. 在弹出的菜单中双击 **New Component**。

3. 在 **Enter a name for your new Component** 窗口，输入自定义组件的名称（例如 MyComponent），然后单击 **Create**。

   你可以在 **Inspector** 中看到创建的自定义组件。

