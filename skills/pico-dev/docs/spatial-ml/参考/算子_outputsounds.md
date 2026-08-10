播放在计算图内部生成或处理过的 PCM 音频。
## 签名
```text
Pipeline.outputSounds(
    sampleRate: Int,
    audioTrack: Tensor,
)
```

## 参数
| 参数 | 说明 |
| --- | --- |
| `sampleRate` | 播放采样率，单位 Hz。 |
| `audioTrack` | 存放待播放 PCM 采样数据的张量。 |
## 空间模式说明

* 是 [captureMicrophone](zh-reference-operators-capture-microphone) 在音频输出方向的对应算子。
* 可用它在运行时内部完整地闭合“采集 → 处理 → 播放”循环，或播放由计算图合成/选取的音频。

## 相关算子

* [captureMicrophone](zh-reference-operators-capture-microphone) —— 将 PCM 采集到计算图中。
* [runModelInference](zh-reference-operators-run-model-inference) —— 使用模型生成或变换音频。

