import streamlit as st
from pydub import AudioSegment

def merge_mp3_files(mp3_files):
    combined = AudioSegment.empty()
    for mp3_file in mp3_files:
        audio = AudioSegment.from_file(mp3_file, format="mp3")
        combined += audio
    return combined

st.title("Ứng dụng ghép các tệp MP3")
st.write("Sử dụng ứng dụng này để ghép các tệp MP3 lại với nhau.")

uploaded_files = st.file_uploader("Chọn các tệp MP3 để ghép lại", accept_multiple_files=True, type="mp3")

if uploaded_files:
    st.write("Các tệp MP3 đã chọn:")
    for uploaded_file in uploaded_files:
        st.write(uploaded_file.name)
    if st.button("Ghép các tệp MP3"):
        mp3_files = [uploaded_file.name for uploaded_file in uploaded_files]
        merged_audio = merge_mp3_files(mp3_files)
        st.write("Tệp MP3 đã được ghép lại!")
        st.audio(merged_audio.export("merged.mp3", format="mp3"), format="audio/mp3")
