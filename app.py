st.markdown("""This is a quick example app for merging multiple MP3 files using the **pydub** audio library on Streamlit Cloud.
There are some issues with `ffmpeg` on Streamlit Cloud regarding temporary files and file permissions.
The quick fix is to use `libav` instead of `ffmpeg` in `packages.txt` file, because pydub prefers `libav` over `ffmpeg` if it is installed.
Therefore this example app uses `libav`.""")

uploaded_files = st.file_uploader('Upload up to 5 MP3 Files', type=['mp3'], accept_multiple_files=True)

if uploaded_files:
    merged_audio = AudioSegment.empty()
    for uploaded_file in uploaded_files:
        audio = AudioSegment.from_file(uploaded_file)
        merged_audio += audio
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
