在设备里可以对 **沉浸场景** 进行声音设计，对声音进行不同内容的处理，以及随机的逻辑关系，场景的分层处理，可以更好的加大代入感以及沉浸度；也可以对 **App** 的声音进行设计，可以根据自己的需求上传音频内容，不同的 App 对应的内容也不一样，工具类的内容声音更注重效率类型的音效，消费类的 App 更注重声音的娱乐类型。本文提供声音相关的设计思路以及技术标准。
## 定义声音内容
### 沉浸式场景

* 什么是空间音频
   空间音频不是一种具体的技术，而是能够提升声音沉浸感受的一系列标准。与传统音频相比，空间音频通过呈现出空间中不同的方位的声音来提升音频体验的沉浸感受。从远处城市的喧嚣声、屋顶上海鸥的鸣叫声，到现场演出中人群疯狂的原始能量。这些声音不仅仅是我们所见事物的补充，它们将我们置于风景之中，让事物充满生机，同时突显它们在我们周围的位置。
* 空间音频组成结构

   * **Spatial Audio**（对象音频）：在真实的环境内，手机来电我们可以准确的根据这个对象音频找到手机的位置。
   * **Ambient Audio**（环境音频）：在真实的户外环境，刮风了，我们可以感知到四周被风声包围。
   * **Channel Audio**（频道音频）：带上耳机，听音乐，或者自己说话听到自己的声音。
* 沉浸场景所需要的内容
   * 场景分析，拆分场景的层级关系。
   * 场景的不同关系对于声音的意义。
      * 远景：可以设计成环境氛围效果
      * 中景：可动的场景声音
      * 近景：可交互的场景内容

* 空间化场景
   * 需要更多位置信息来设计声音，对象音频（点声源）。
   * 根据场景的不同的位置，以及声音的内容来码放声音对象。
   * 点声源的动态效果与静态区分。
      * 动态效果的声音，可以具有随机性，时间随机播放与声音的随机内容、声音的可动随机。
      * 静态效果的声音，固定位置的声音。
* 场景中的声音基础参数设计（参考建议）
   * 采样频率：48KHZ
   * 量化精度：24bit
   * 响度：-13LUFS
   * 声道选择：mono/stereo
   * 存储格式：wav/mp3/ogg
* 场景中的声音资源设计
   * 根据场景的层级以及场景内容，来定义场景所需要的音频资源。
   * 根据根据资源内容来摆放声音，不同的位置定义不同的声音。
   * 沉浸式场景的声音不易过多过乱。
   * 符合画面，表达清晰即可。

#### App 应用

* 不同的 App，声音设计也是不一样的。

   * 工具类
      * 声音以简洁轻便为主，过多的复杂声音，会让声音显得更加笨重
      * 声音时长控制在 0.5 ~ 1 秒（参考建议）
      * 声音的类型根据 UI 内容来定义（无属性、玻璃、塑料等不同材质的风格属性）
   * 应用类
      * 声音可以跟随 App 属性，让声音更具有专属的类型
      * 声音时长可以根据内容来定义时长，大多定义 0.5 ~ 1.5 秒（参考建议）
      * 声音的类型，可以根据应用内容来定义
* 声音具有统一性
   * 定义基础声音，取决于 App 整体美术设计风格
   * 在不同的操作类型中，让声音更具有统一性
      * 通用音是 App 主基调
      * 消息音是主基调的升华
      * 定制音是 App 的灵魂
* 声音的听感
   * 一个好的声音，应该是清晰的、无杂音的
   * 提示音功能表达精准
   * 动效与音频相互融合不突兀
   * 音频资源风格统一

#### 不同使用场景的声音
声音可以根据不同的使用场景分成以下几类：

1. **通用操作**类例如交互事件：点击、长按、拖动、双击、双手_缩放、旋转、移动。状态反馈成功/失败；开启/关闭
2. **通用通知**，例如：通知中心-通用**、**应用通知等
3. **定制音色**，例如：定制反馈、识别手势、开机、充电、打开资源库、来电铃声、闹钟等

#### **通用操作**
依据不同的交互事件，对声音进行基础设计。时间长度可按照格式规范，设定在 0.5 ~ 1.5 秒（参考建议）。主要针对交互事件提供声音反馈，由于这些交互事件属于常规操作，因此在声音设计方面，遵循轻简的设计原则。对于状态反馈，亦采用相同的设计原则。
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0a30cc0de1cd409894a1fdec06cde59b~tplv-goo7wpa0wc-image.image" filename="通用-点击.wav" download>通用-点击.wav</a>
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d928d448f30a4578901ad69c4b743df2~tplv-goo7wpa0wc-image.image" filename="通用-反馈.wav" download>通用-反馈.wav</a>
#### 通用通知
用于系统级通知与事件提醒。与操作声音不同的是，通知音的可设置声音范围为 2 ~ 3.5 秒（参考建议）。通知音的设计需满足传达提醒信息的需求，要具备富有灵感、超凡的设计理念，能让用户感知到声音，但又不会造成干扰。声音时长的设置应能给予用户短暂的思考空间。
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2bca2bb0c95d4f79b342b3c8c9fa074f~tplv-goo7wpa0wc-image.image" filename="通知—示范01.wav" download>通知—示范01.wav</a>
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/74ccc359814e488a9058fe94e9611336~tplv-goo7wpa0wc-image.image" filename="通知-示范02.wav" download>通知-示范02.wav</a>
#### 定制音色
定制声音的每一个声音都需单独的设计，此类声音更具多样性和辨识度。此类声音的设计时长建议为 2 - 3.5 秒。定制声音需要更多表现元素，更多元素会使声音更为丰富，例如资源库的打开与关闭。
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/27fc327ad1754f27b1d66a74a44bc9ba~tplv-goo7wpa0wc-image.image" filename="资源库打开.wav" download>资源库打开.wav</a>
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/86fb6f67bec4493cbfe81e29f39c57ca~tplv-goo7wpa0wc-image.image" filename="资源库关闭.wav" download>资源库关闭.wav</a>
### 声音设计原则
好的声音设计是需要我们用耳朵去聆听，不同的声音设计，给我带来的体验也是不一样的。我们从以下一些声音内容中，感受不一样的声音体验。
#### 声音的属性定义

1. 轻简的设计：声音需轻盈简洁、不沉重，功能性强且避免强烈的冲击感，传递轻松与舒适。
2. 温暖的设计：声音应具有温暖、亲和的特质，让用户感到舒适和友好。
3. 自然的设计：声音需贴近自然，营造以用户为中心坐标的真实感，避免过于人工化、机械化。

#### 轻简的
根据声音的属性定义，我们可以得出，轻简的声音，可以给人们带来快速便捷的使用体验，让声音听起来更加便捷，提高工作效率。
##### **正向的声音**
我们希望听到的：
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c270551e268946c68f4fa325b2027dbd~tplv-goo7wpa0wc-image.image" filename="轻简.wav" download>轻简.wav</a>
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/575152d6dafa43ad8cd330b47b416779~tplv-goo7wpa0wc-image.image" filename="轻简02.wav" download>轻简02.wav</a>
##### **反向的声音**
我们不想听到的：
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3659b9dfb7fc4c47a1049eec37d08340~tplv-goo7wpa0wc-image.image" filename="反向设计.wav" download>反向设计.wav</a>
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0ae4208e95af4b9eb6d016ec5e1896f1~tplv-goo7wpa0wc-image.image" filename="反向设计02.wav" download>反向设计02.wav</a>
#### **温暖的**
根据声音的属性，温暖的声音会让用户更有亲和力，以及舒适感，能够提升友好度。
##### **正向的声音**
我们希望听到的：
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e3de386509e94a15abedfafae5c09240~tplv-goo7wpa0wc-image.image" filename="温暖.wav" download>温暖.wav</a>
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e8e22f6cf34c493da991e987a49c8373~tplv-goo7wpa0wc-image.image" filename="温暖02.wav" download>温暖02.wav</a>
**反向的声音**
我们不想听到的：
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/103f996b244245c38e09a03d41ca5228~tplv-goo7wpa0wc-image.image" filename="反向设计03.wav" download>反向设计03.wav</a>
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3a42de4b40fd47af91bf9c2d8ff19dac~tplv-goo7wpa0wc-image.image" filename="反向设计04.wav" download>反向设计04.wav</a>
#### 自然的
还原声音最本真的状态，常用于拟音效果，诸如键盘声响或自然界的各类声音。与我们最为贴近的声音，例如键盘的敲击声、相机的拍照声，当然，这些声音可以采用一些非常规的音频设计，但运用物理声音，能让我们对这些基础操作产生更强的代入感。
##### **正向的声音**
<a href="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/812a7570f6624b3a9d5a5f1a87b4aec1~tplv-goo7wpa0wc-image.image" filename="拍照08.wav" download>拍照08.wav</a>

