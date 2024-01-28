# app.py
import streamlit as st
from pydub import AudioSegment
import os

# Specify the path to the FFmpeg executable
AudioSegment.ffmpeg = "/usr/bin/ffmpeg"

def merge_mp3(files, output_filename):
    audio = AudioSegment.silent(duration=0)

    for file in files:
        audio += AudioSegment.from_mp3(file)

    audio.export(output_filename, format="mp3")

def main():
    st.title("MP3 Merger App")

    st.write("Upload the MP3 files you want to merge:")
    input_files = st.file_uploader("Choose MP3 Files", type=["mp3"], accept_multiple_files=True)

    if input_files:
        st.write("Files to be merged:")
        for file in input_files:
            st.write(file.name)

        # Save uploaded files to a temporary directory
        temp_dir = "temp"
        os.makedirs(temp_dir, exist_ok=True)
        temp_files = [os.path.join(temp_dir, file.name) for file in input_files]

        for i, file in enumerate(input_files):
            with open(temp_files[i], "wb") as f:
                f.write(file.read())

        if st.button("Merge Files"):
            output_filename = "output.mp3"
            merge_mp3(temp_files, output_filename)
            st.success(f"Files merged successfully. Output file: {output_filename}")

            # Remove temporary files
            for temp_file in temp_files:
                os.remove(temp_file)

if __name__ == "__main__":
    main()
