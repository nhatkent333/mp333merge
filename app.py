# Import necessary libraries
from pydub import AudioSegment
import os
import streamlit as st
from io import BytesIO

def merge_mp3(files):
    audio = AudioSegment.silent(duration=0)

    for file in files:
        audio += AudioSegment.from_file(file, format="mp3")

    return audio

# Create a Streamlit app
st.title("MP3 Merger App")

# Upload MP3 files
st.write("Upload the MP3 files you want to merge:")
uploaded_files = st.file_uploader("Choose MP3 files", type=["mp3"], accept_multiple_files=True)

if uploaded_files:
    # Process the uploaded files
    file_names = [file.name for file in uploaded_files]
    st.write(f"Files to be merged: {file_names}")

    # Merge MP3 files
    merged_audio = merge_mp3([BytesIO(file.read()) for file in uploaded_files])

    # Export the merged audio
    st.audio(merged_audio.export(format="mp3").read(), format="audio/mp3", start_time=0)

    # Download button for the merged file
    st.download_button(label="Download Merged File", data=merged_audio.export(format="mp3").read(),
                       file_name="output.mp3", key="download_button")

# Display a footer or any additional information
st.write("This app allows you to merge multiple MP3 files.")

