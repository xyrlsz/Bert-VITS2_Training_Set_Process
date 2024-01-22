import os


def get_wav_file_list(directory_path: str = "input") -> list:
    file_list = []
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath) and filename.find(".wav") != -1:
            file_list.append(directory_path + "/" + filename)
    return file_list


if __name__ == "__main__":
    directory_path = "input"
    file_list = get_wav_file_list(directory_path)

    print("Files in the directory:")
    for filename in file_list:
        print(filename)
