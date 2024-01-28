# Thêm dòng này vào đầu file để sử dụng libav thay vì ffmpeg
import pydub
pydub.AudioSegment.ffmpeg = "libav"

from pydub import AudioSegment
import os

def merge_mp3(files, output_filename):
    audio = AudioSegment.silent(duration=0)

    for file in files:
        audio += AudioSegment.from_mp3(file)

    audio.export(output_filename, format="mp3")

# Hàm để upload file MP3
def upload_mp3():
    import streamlit as st
    uploaded = st.file_uploader("Upload các file MP3 cần nối", type=["mp3"])
    if uploaded is not None:
        return [os.path.join("user_uploaded", file.name) for file in uploaded]
    else:
        return []

# Upload các file MP3
print("Upload các file MP3 cần nối:")
input_files = upload_mp3()

# Thay thế 'output.mp3' bằng tên file MP3 đầu ra mong muốn.
output_filename = 'output.mp3'

# Nối các file MP3
merge_mp3(input_files, output_filename)

print(f"Files merged successfully. Output file: {output_filename}")
