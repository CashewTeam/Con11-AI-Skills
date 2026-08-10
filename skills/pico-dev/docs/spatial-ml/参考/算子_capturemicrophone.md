采集麦克风的 PCM 音频并写入张量，供计算图内的音频处理或模型推理使用。
## 签名
```text
// interleaved stereo into a single track
Pipeline.captureMicrophone(
    sampleRate: Int,
    stereoTrackResult: Tensor,
    timestampResult: Tensor? = null,
)

// split left/right tracks (supply at least one)
Pipeline.captureMicrophone(
    sampleRate: Int,
    leftTrackResult: Tensor? = null,
    rightTrackResult: Tensor? = null,
    timestampResult: Tensor? = null,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `sampleRate` | 输入 | 采集采样率，单位 Hz，范围 `8000`–`96000`。 |
| `stereoTrackResult` | 结果 | 交织存储的立体声 PCM 音轨。 |
| `leftTrackResult` / `rightTrackResult` | 结果 | 按声道分离的 PCM 音轨（分离重载版本）；至少需提供其中一个。 |
| `timestampResult` | 结果 | 可选的采集时间戳张量。 |
## 空间模式说明

* 在运行时内部生成音频数据，遵循与传感器算子相同的结果张量模式。
* 常与 [outputSounds](zh-reference-operators-output-sounds) 搭配，构建“采集—处理—播放”计算图，或将结果送入 [runModelInference](zh-reference-operators-run-model-inference) 供音频模型使用。
* 麦克风采集受应用音频权限的限制。

## 相关算子

* [outputSounds](zh-reference-operators-output-sounds) —— 播放处理后的音频。
* [runModelInference](zh-reference-operators-run-model-inference) —— 运行音频模型。

