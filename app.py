# app.py
import streamlit as st
from pydub import AudioSegment
import os

def merge_mp3(files):
    # Hàm để merge các file mp3
    audio = AudioSegment.from_mp3(files[0])
    for file in files[1:]:
        audio += AudioSegment.from_mp3(file)
    return audio

def main():
    st.title("MP3 Merger")

    uploaded_files = st.file_uploader("Chọn các file MP3 để merge", type="mp3", accept_multiple_files=True)

    if uploaded_files:
        # Tạo thư mục 'uploads' nếu chưa tồn tại
        os.makedirs("uploads", exist_ok=True)
        
        # Hiển thị danh sách các file đã chọn
        st.subheader("Các file đã chọn:")
        for file in uploaded_files:
            st.write(file.name)

        # Kiểm tra nếu người dùng bấm nút "Merge"
        if st.button("Merge"):
            # Lấy đường dẫn của các file đã tải lên
            file_paths = [file.name for file in uploaded_files]
            file_paths = [os.path.join("uploads", file) for file in file_paths]

            # Thực hiện merge và lưu kết quả vào file mới
            merged_audio = merge_mp3(file_paths)
            output_path = os.path.join("output", "merged.mp3")
            merged_audio.export(output_path, format="mp3")

            # Hiển thị link để tải file đã merge
            st.success(f"File đã merge thành công! [Tải về](sandbox:/mnt/data/{output_path})")

if __name__ == "__main__":
    main()
