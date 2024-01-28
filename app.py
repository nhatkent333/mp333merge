# app.py
import streamlit as st
import os
import soundfile as sf
import librosa
import tempfile

def merge_mp3(files):
    # Tạo thư mục tạm trên Streamlit Cloud
    tmp_folder = tempfile.mkdtemp()

    # Tên file output
    output_path = os.path.join(tmp_folder, "merged.wav")

    # Đọc và ghi file âm thanh sử dụng librosa và soundfile
    audio, _ = librosa.load(files[0], sr=None)
    for file in files[1:]:
        audio += librosa.load(file, sr=None)[0]

    sf.write(output_path, audio, 44100)

    return output_path

def main():
    st.title("MP3 Merger")

    uploaded_files = st.file_uploader("Chọn các file MP3 để merge", type="mp3", accept_multiple_files=True)

    if uploaded_files:
        st.subheader("Các file đã chọn:")
        for file in uploaded_files:
            st.write(file.name)

        if st.button("Merge"):
            # Thực hiện merge và lưu kết quả vào thư mục tạm
            merged_audio_path = merge_mp3([file.name for file in uploaded_files])

            # Hiển thị link để tải file đã merge
            st.success(f"File đã merge thành công! [Tải về](sandbox:/mnt/data{merged_audio_path})")

if __name__ == "__main__":
    main()
