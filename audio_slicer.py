import librosa  # Optional. Use any library you like to read audio files.
import soundfile  # Optional. Use any library you like to write audio files.

import os


import os


model_name = "ada"
from slicer2 import Slicer

_input_dir = f"./input/{model_name}.wav"
_output_dir = f"./output/data/{model_name}/raw/"


def audio_slice(
    input_dir: str = _input_dir,
    output_dir=_output_dir,
    model_name="ada",
    start_index=0,
):
    # 检查目录是否存在
    if not os.path.exists(output_dir):
        # 如果不存在，创建目录
        os.makedirs(output_dir)
        print(f"目录 '{output_dir}' 已创建.")
    else:
        print(f"目录 '{output_dir}' 已存在.")

    audio, sr = librosa.load(
        input_dir, sr=None, mono=False
    )  # Load an audio file with librosa.
    slicer = Slicer(
        sr=sr,
        threshold=-40,
        min_length=2000,
        min_interval=300,
        hop_size=10,
        max_sil_kept=500,
    )
    chunks = slicer.slice(audio)
    curr_index = 0
    for i, chunk in enumerate(chunks):
        if len(chunk.shape) > 1:
            chunk = chunk.T  # Swap axes if the audio is stereo.
        curr_index = start_index + i
        soundfile.write(
            output_dir + f"{model_name}_{start_index+i}.wav", chunk, sr
        )  # Save sliced audio files with soundfile.

        print("正在写入" + f"{model_name}_{start_index+i}.wav")

    if os.path.exists(input_dir):  # 如果文件存在
        # os.remove(f"./Data/{model_name}/raw/{model_name}.wav")
        pass
    return curr_index


if __name__ == "__main__":
    audio_slice()
