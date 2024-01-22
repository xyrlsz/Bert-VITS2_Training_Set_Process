import yaml

from audio_slicer import audio_slice
from short_audio_transcribe import short_audio_transcribe
from load_wav_file_list import get_wav_file_list

print("正在加载配置文件")
try:
    with open("config/config.yaml", mode="r", encoding="utf-8") as f:
        configyl = yaml.load(f, Loader=yaml.FullLoader)
except Exception as e:
    print(f"配置文件加载失败：{e}")

print("配置文件加载成功")

print("开始读取音频")

wav_file_list = get_wav_file_list()

print("音频读取完成")

print("开始切割音频")

count = 0

for i in range(len(wav_file_list)):
    tmp = audio_slice(
        input_dir=wav_file_list[i],
        model_name=configyl["model_name"],
        output_dir="./output/data/" + configyl["model_name"] + "/raw/",
        start_index=count,
    )
    count = tmp + 1

print("切割音频完成")

print("开始生成标签文本")

short_audio_transcribe(
    model_name=configyl["model_name"],
    output_dir="./output/data/" + configyl["model_name"] + "/raw/",
    languages=configyl["languages"],
    whisper_size=configyl["whisper_size"],
    use_GPU=configyl["use_GPU"],
    is_simplified=configyl["is_simplified"],
)

print("标签文本生成完成")
