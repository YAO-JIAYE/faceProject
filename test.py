import os
import subprocess
from ncmdump.core import dump

def convert_wav_to_flac(wav_path, flac_path):
    subprocess.run(['ffmpeg', '-i', wav_path, '-c:a', 'flac', flac_path])

def main(ncm_folder_path, flac_folder_path):
    # 确保输出文件夹存在
    if not os.path.exists(flac_folder_path):
        os.makedirs(flac_folder_path)

    # 遍历文件夹中的所有文件
    for file_name in os.listdir(ncm_folder_path):
        if file_name.endswith('.ncm'):
            ncm_file_path = os.path.join(ncm_folder_path, file_name)
            temp_wav_path = os.path.join(flac_folder_path, file_name.replace('.ncm', '.wav'))
            flac_file_path = os.path.join(flac_folder_path, file_name.replace('.ncm', '.flac'))

            dump(ncm_file_path, temp_wav_path, skip=False)  # 使用 dump 方法解密并保存为 wav 文件
            convert_wav_to_flac(temp_wav_path, flac_file_path)
            os.remove(temp_wav_path)

if __name__ == "__main__":
    # 替换为你的ncm文件夹路径
    ncm_folder_path = './ncm_files'
    # 替换为你希望保存flac文件的文件夹路径
    flac_folder_path = './flac_files'
    main(ncm_folder_path, flac_folder_path)
