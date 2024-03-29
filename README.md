

# Bert-VITS2_Training_Set_Processing
<img src="https://img.shields.io/badge/python->=3.9-green">

## 简介

这个是处理Bert-VITS2训练集的代码。
参考了这个仓库：https://github.com/v3ucn/Bert-vits2-V2.3

需要使用纯人声的wav文件，需要自己处理背景音乐。

音频格式转换工具：[点我跳转](./converter_doc.md#音频转换器)

视频转WAV工具：[点我跳转](./converter_doc.md#视频转音频)

在线格式转换器：[点我跳转](https://convertfree.com/)(支持多种格式转换，免费，视频转音频也可以)

人声和音乐分离：

可以使用UVR来提取人声，[教程](https://www.bilibili.com/read/cv27499700/)


## 使用方法

理论上Windows和Linu上都能运行。

**需要安装python，ffmpeg，whisper，pytorch，cuda（pytorch是什么Compute Platform就装什么，只用cpu的话可以不用装）。** 请自行百度。

有CPU和GPU两种模式，用GPU跑的话建议用WSL或者Linux，Windows可能会有点问题，自己试试吧。

**whisper Model 选择参考**:

*选择Whisper将用于转录音频的模型*。

| 大小      | 参数 | 仅英语模型  | 多语言模型 | 所需VRAM（显存） | 相对速度 |
|-----------|------------|--------------------|--------------------|---------------|----------------|
| tiny      | 39 M       | tiny.en            | tiny               | ~1 GB         | ~32x           |
| base      | 74 M       | base.en            | base               | ~1 GB         | ~16x           |
| small     | 244 M      | small.en           | small              | ~2 GB         | ~6x            |
| medium    | 769 M      | medium.en          | medium             | ~5 GB         | ~2x            |
| large     | 1550 M     | N/A                | large              | ~10 GB        | 1x             |
| large-v2  | 1550 M     | N/A                | large              | ~10 GB        | 1x             |

### 克隆仓库
```shell
git clone https://github.com/xyrlsz/Bert-VITS2_Training_Set_Processing.git
```
### 安装依赖
pip清华换源：（可选）
~~~shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
~~~
安装依赖：
```shell
cd Bert-VITS2_Training_Set_Processing
pip install -r requirements.txt
```

如果报错了可能是网络问题，可以尝试开魔法。

### 修改配置文件

把config目录下的配置文件config_example.yaml 复制一份并重命名为.yaml，并修改相关配置

### 开始使用

#### 1. 将待处理文件放入input文件夹下

#### 2. 运行
```shell
python app.py
```

#### 3. 处理后的文件在output文件夹下