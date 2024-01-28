import streamlit as st
from pydub import AudioSegment

def merge_mp3(files, output_filename):
    audio = AudioSegment.silent(duration=0)

    for file in files:
        audio += AudioSegment.from_mp3(file)

    audio.export(output_filename, format="mp3")

st.title("MP3 Merger")

# Thêm nút để chọn các file MP3
uploaded_files = st.file_uploader("Choose MP3 files to merge", type=["mp3"], accept_multiple_files=True)

if uploaded_files:
    st.write("Files selected:")
    for file in uploaded_files:
        st.write(file.name)

    # Nếu người dùng nhấn nút "Merge", thực hiện quá trình nối file
    if st.button("Merge MP3"):
        # Lấy đường dẫn và tên file đầu ra từ người dùng
        output_filename = st.text_input("Output file name:", "output.mp3")

        # Chuyển đổi các đối tượng FileUploader thành đường dẫn thực tế
        input_files = [file.name for file in uploaded_files]

        # Nối các file MP3
        merge_mp3(input_files, output_filename)

        st.success(f"Files merged successfully. Output file: {output_filename}")
