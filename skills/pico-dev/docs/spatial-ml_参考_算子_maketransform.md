由平移、旋转、缩放等独立分量构造一个 4×4 变换矩阵。当姿态的各个组成部分以张量形式给出，而不是现成的矩阵时，可用它来组合出场景实体的姿态。
## 签名
```text
Pipeline.makeTransform(
    rotationVec: Tensor?,
    translationVec: Tensor?,
    scaleVec: Tensor?,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `rotationVec` | 输入 | 可选的旋转分量（旋转向量）。传入 `null` 可跳过。 |
| `translationVec` | 输入 | 可选的平移分量。传入 `null` 可跳过。 |
| `scaleVec` | 输入 | 可选的缩放分量。传入 `null` 可跳过。 |
| `result` | 结果 | 形状为 `[4, 4]` 的 `FLOAT32` 变换矩阵。 |
## 空间模式说明

* 得到的矩阵可配合 [Transform.LocalMatrix](zh-reference-tensor-types-and-enums#scenegraphproperty) 属性传给 [updateSceneGraphProperty](zh-reference-operators-update-scene-graph-property)，用于放置实体。
* 当姿态来自视觉算法时，可与 [solvePnP](zh-reference-operators-solve-pnp) / [uvTo3DInCameraSpace](zh-reference-operators-uv-to-3d-in-camera-space) 结合使用，也可以直接由计算得到的张量构造。

## 相关算子

* [updateSceneGraphProperty](zh-reference-operators-update-scene-graph-property) — 将变换应用到实体上。
* [solvePnP](zh-reference-operators-solve-pnp) — 从对应点估计姿态。
* [驱动场景图输出](zh-workflows-drive-scene-graph-output)

