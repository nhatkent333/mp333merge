import streamlit as st
from pydub import AudioSegment

def merge_mp3_files(file1, file2):
    audio1 = AudioSegment.from_file(file1)
    audio2 = AudioSegment.from_file(file2)
    combined = audio1 + audio2
    combined.export("merged.mp3", format='mp3')

st.title('MP3 Merger')

uploaded_file1 = st.file_uploader("Choose a MP3 file", type="mp3")
if uploaded_file1 is not None:
    file_details = {"FileName":uploaded_file1.name,"FileType":uploaded_file1.type,"FileSize":uploaded_file1.size}
    st.write(file_details)

uploaded_file2 = st.file_uploader("Choose another MP3 file", type="mp3")
if uploaded_file2 is not None:
    file_details = {"FileName":uploaded_file2.name,"FileType":uploaded_file2.type,"FileSize":uploaded_file2.size}
    st.write(file_details)

if st.button('Merge MP3 Files'):
    if uploaded_file1 is not None and uploaded_file2 is not None:
        merge_mp3_files(uploaded_file1, uploaded_file2)
        st.success('Files merged successfully!')
    else:
        st.error('Please upload two MP3 files.')
