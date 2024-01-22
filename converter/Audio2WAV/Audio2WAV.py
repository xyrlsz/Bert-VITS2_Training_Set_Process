import os
from pydub import AudioSegment


def get_file_list(directory_path: str = "input") -> list:
    file_list = []
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            file_list.append(filename)
    return file_list


def replace_extension(input_str, new_extension):
    # 找到最后一个.的索引
    last_dot_index = input_str.rfind(".")

    # 如果找到了.，则进行替换
    if last_dot_index != -1:
        result_str = input_str[: last_dot_index + 1] + new_extension
        return result_str
    else:
        # 如果没有找到.，则直接返回原始字符串
        return input_str


def convert_to_wav(input_file, output_file):
    # 读取输入音频文件
    audio = AudioSegment.from_file(input_file)

    # 将音频文件转换为WAV格式
    audio.export(output_file, format="wav")


if __name__ == "__main__":
    input_dir = "input/"
    output_dir = "output/"
    Audio_list = get_file_list(input_dir)
    for i in range(len(Audio_list)):
        input_audio_file = input_dir + Audio_list[i]
        output_wav_file = output_dir + replace_extension(Audio_list[i], "wav")
        convert_to_wav(input_audio_file, output_wav_file)
