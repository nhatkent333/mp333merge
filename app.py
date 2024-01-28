from pydub import AudioSegment
import os

def merge_mp3(files, output_filename):
    audio = AudioSegment.silent(duration=0)

    for file in files:
        audio += AudioSegment.from_mp3(file)

    audio.export(output_filename, format="mp3")

# Thay thế 'file1.mp3', 'file2.mp3',... bằng đường dẫn thực sự của các file MP3 bạn muốn nối lại.
input_files = ['/content/1t.mp3', '/content/2t.mp3', 'file3.mp3']

# Thay thế 'output.mp3' bằng tên file MP3 đầu ra mong muốn.
output_filename = 'output.mp3'

# Nối các file MP3
merge_mp3(input_files, output_filename)

print(f"Files merged successfully. Output file: {output_filename}")
