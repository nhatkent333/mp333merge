# app.py
import streamlit as st
from pydub import AudioSegment
import os

# Thiết lập đường dẫn của FFmpeg cho Pydub
# Trong Streamlit Cloud, FFmpeg thường đã được cài sẵn, không cần phải thiết lập đường dẫn
# Nếu cần, bạn có thể để Pydub tự tìm đường dẫn bằng cách không thiết lập giá trị này
# AudioSegment.converter = "/usr/bin/ffmpeg"  # Đường dẫn có thể thay đổi, tùy thuộc vào cài đặt cụ thể trên Streamlit Cloud

def merge_mp3(files):
    audio = AudioSegment.from_mp3(files[0])
    for file in files[1:]:
        audio += AudioSegment.from_mp3(file)
    return audio

def main():
    st.title("MP3 Merger")

    uploaded_files = st.file_uploader("Chọn các file MP3 để merge", type="mp3", accept_multiple_files=True)

    if uploaded_files:
        st.subheader("Các file đã chọn:")
        for file in uploaded_files:
            st.write(file.name)

        if st.button("Merge"):
            # Lưu các file vào thư mục tạm trên Streamlit Cloud
            tmp_folder = "/tmp/uploads"
            os.makedirs(tmp_folder, exist_ok=True)

            file_paths = [os.path.join(tmp_folder, file.name) for file in uploaded_files]

            for file_path, uploaded_file in zip(file_paths, uploaded_files):
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())

            # Thực hiện merge và lưu kết quả vào thư mục tạm
            merged_audio = merge_mp3(file_paths)
            tmp_output_path = "/tmp/merged.mp3"
            merged_audio.export(tmp_output_path, format="mp3")

            # Hiển thị link để tải file đã merge
            st.success(f"File đã merge thành công! [Tải về](sandbox:/mnt/data{tmp_output_path})")

if __name__ == "__main__":
    main()
