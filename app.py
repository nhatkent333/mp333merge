import io
import pathlib

import streamlit as st
from pydub import AudioSegment

st.title('MP3 Merger')

st.markdown("""This is a quick example app for merging two MP3 files using the **pydub** audio library on Streamlit Cloud.
There are some issues with `ffmpeg` on Streamlit Cloud regarding temporary files and file permissions.
The quick fix is to use `libav` instead of `ffmpeg` in `packages.txt` file, because pydub prefers `libav` over `ffmpeg` if it is installed.
Therefore this example app uses `libav`.""")

uploaded_mp3_file1 = st.file_uploader('Upload Your First MP3 File', type=['mp3'])
uploaded_mp3_file2 = st.file_uploader('Upload Your Second MP3 File', type=['mp3'])

if uploaded_mp3_file1 and uploaded_mp3_file2:
    audio1 = AudioSegment.from_file(uploaded_mp3_file1)
    audio2 = AudioSegment.from_file(uploaded_mp3_file2)
    merged_audio = audio1 + audio2
    merged_audio.export("merged.mp3", format='mp3')
    st.success('Files merged successfully!')

    # Add download button
    with open("merged.mp3", "rb") as f:
        bytes = f.read()
    st.download_button(
        label="Download merged file",
        data=bytes,
        file_name="merged.mp3",
        mime="audio/mpeg",
    )
