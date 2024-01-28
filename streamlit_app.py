# streamlit_app.py
import streamlit as st
import requests

st.title("MP3 Merger")

uploaded_files = st.file_uploader("Choose MP3 files to merge", type="mp3", accept_multiple_files=True)

if st.button("Merge"):
    if len(uploaded_files) < 2:
        st.warning("Please upload at least two MP3 files.")
    else:
        # Upload files to Flask server
        files = {'files[]': uploaded_files}
        response = requests.post("http://127.0.0.1:5000/merge", files=files)

        if response.status_code == 200:
            st.success("Merge successful! Download the merged file below.")
            st.download_button("Download Merged File", response.content, file_name="merged_output.mp3")
        else:
            st.error("Merge failed. Please try again.")
