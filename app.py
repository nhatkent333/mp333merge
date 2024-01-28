import io
import pathlib

import streamlit as st
from pydub import AudioSegment

st.title('Ghép Nối File MP3')

st.markdown("""Công cụ ghép nối file MP3 do [Việc Làm Vui](https://vieclamvui.com/ "tìm việc làm, tuyển dụng miễn phí") phát triển. Thuộc dự án 1001 công cụ online hỗ trợ cho hơn 100 ngành nghề.""")

uploaded_files = st.file_uploader('Upload up to 5 MP3 Files', type=['mp3'], accept_multiple_files=True)

if uploaded_files:
    merged_audio = AudioSegment.empty()
    for uploaded_file in uploaded_files:
        audio = AudioSegment.from_file(uploaded_file)
        merged_audio += audio
    merged_audio.export("merged.mp3", format='mp3')
    st.success('Ghép nối các file MP3 thành công!')

    # Add download button
    with open("merged.mp3", "rb") as f:
        bytes = f.read()
    st.download_button(
        label="Download merged file",
        data=bytes,
        file_name="merged.mp3",
        mime="audio/mpeg",
    )
