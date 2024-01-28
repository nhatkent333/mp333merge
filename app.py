from pydub import AudioSegment

def merge_mp3_files(mp3_files):
    combined = AudioSegment.empty()
    for mp3_file in mp3_files:
        audio = AudioSegment.from_file(mp3_file, format="mp3")
        combined += audio
    return combined

# Example usage
mp3_files = ["file1.mp3", "file2.mp3", "file3.mp3"]
merged_audio = merge_mp3_files(mp3_files)
merged_audio.export("merged.mp3", format="mp3")
