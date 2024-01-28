import streamlit as st
import pydub

# Define the function to merge the MP3 files
def merge_mp3(files):
    # Create a new empty MP3 file
    out = pydub.AudioSegment.empty()

    # Iterate over the input files
    for f in files:
        # Read the input file
        audio = pydub.AudioSegment.from_file(f)

        # Append the audio to the output file
        out += audio

    # Write the output file
    out.export("output.mp3")

# Set the title of the app
st.title("Merge MP3 Files")

# Create a file input widget
files = st.file_uploader("Select the MP3 files to merge", multiple=True)

# Check if any files were uploaded
if files is not None:
    # Merge the files
    merge_mp3(files)

    # Display a success message
    st.success("The MP3 files have been merged successfully.")
