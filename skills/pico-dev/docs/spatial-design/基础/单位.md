## 空间面板单位

* 空间面板采用 dmm 单位，Volumetric 窗口与 3D 模型采用米单位。
* 空间面板设计尺寸使用 dp 单位，系统会自动将 dp 转化成 dmm。

dmm（即与距离无关的毫米）是一种角度单位，无论用户与虚拟对象之间的距离如何，该单位始终保持不变。[dp](https://developer.android.com/training/multiscreen/screendensities?hl=zh-cn)（密度无关像素）是一种可缩放的单位，可在任何屏幕上获得一致的尺寸。它们提供了一种灵活的方式来适应跨平台的设计。
## 动态缩放
当用户拉近或推远窗口应用时，空间面板会保持相对恒定 FOV 的 dynamic scale，以确保界面 UI 信息在不同距离时都能被清晰查看与交互。但 Volumetric 窗口与 3D 模型则不会改变尺寸。
## 交互热区
交互热区 56 dp * 56 dp

