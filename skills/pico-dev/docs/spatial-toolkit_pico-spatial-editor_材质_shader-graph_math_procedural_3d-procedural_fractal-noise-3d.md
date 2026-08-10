通过叠加多个不同频率和振幅的 3D Perlin 噪声层（octave），生成一种以 0 为中心波动的 3D 分形噪声。

## 参数说明

* **Amplitude**：生成噪声的强度。振幅越高，噪声图案中的变化越明显。
* **Octaves**：节点叠加的 3D Perlin Noise 层数。默认值为 3。
* **Lacunarity**：每个 octave 之间的指数缩放系数。该值决定连续各个 octave（或 Perlin 噪声层）之间的差异程度。默认值为 **2.0**。
* **Diminish**：每个后续 octave 的振幅衰减速率。建议将此参数保持在 0.0–1.0 范围内。默认值为 0.5。
* **position**：读取数据时所使用的三维坐标，用于将纹理映射到表面上。默认情况下，使用当前的对象空间 3D 坐标。

## 节点使用说明
**Fractal Noise** **3D** 节点通过将多层（多个 octave）的 3D Perlin Noise 相加来生成输出结果。Fractal Noise 中的 octave 越多，噪声细节就越丰富、越精细。每个后续 octave 都会与前一个 octave 有所不同，而这种差异由 **Lacunarity** 和 **Diminish** 参数决定。

* **Lacunarity** 表示各个 octave 之间在频率上的差异。该值越大，生成的分形噪声通常越不均匀，也越不平滑。
* **Diminish** 表示 octave 之间振幅的变化方式。当该值为 1 时，振幅不发生变化；该值越小，不同 octave 之间的振幅衰减就越快。

下面是一个节点图示例，演示如何使用 **Fractal Noise 3D** 节点生成黑白图案。将输入的 **Position** 与一个常量 **Float** 相乘。这个 Float 会提高生成噪声的频率，因此图案会更频繁地重复。

下方示例展示了将结果纹理应用到一个立方体上的效果，并分别使用了不同的参数值。其余参数均使用默认值。

<strong>Octaves = 1</strong>

<strong>Octaves = 3</strong>

<strong>Octaves = 5</strong>

<strong>Lacunarity = 1</strong>

<strong>Lacunarity = 2</strong>

<strong>Lacunarity = 5</strong>

<strong>Diminish = 0.2</strong>

<strong>Diminish = 0.5</strong>

<strong>Diminish = 1</strong>

