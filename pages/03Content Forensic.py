import streamlit as st
import pandas as pd
from module import transcribe as ts

st.set_page_config(page_title="Content Forensic", layout="wide")

st.title("🕵️ Content Forensic Analysis")

# Load the CSV file
csv_file = "video_data.csv"

try:
    df = pd.read_csv(csv_file)
    if df.empty:
        st.warning("⚠ No data found in `video_data.csv`. Please upload a valid file.")
        st.stop()
except FileNotFoundError:
    st.error(f"❌ File `{csv_file}` not found. Make sure it's available.")
    st.stop()

# Extract video titles & links
video_titles = df['Video Title']
video_links = df['Video URL']

st.info(f"📌 Found {len(video_titles)} videos for analysis.")

# Progress bar
progress_bar = st.progress(0)
total_videos = len(video_links)

# Loop through each video
for index, (link, title) in enumerate(zip(video_links, video_titles), start=1):
    st.subheader(f"🎥 Video {index}: {title}")

    # Process transcript
    transcript_text = ts.transcript(link, index)

    if transcript_text:
        st.success("✅ Transcript Extracted Successfully!")

        # Display transcript in expandable text area
        st.text_area(f"📜 Transcript for {title}", transcript_text, height=200)

        # Save transcript to a file
        file_name = f"transcripts/{index}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(transcript_text)
        st.write(f"💾 Transcript saved as `{file_name}`.")
    else:
        st.warning("⚠ No transcript available for this video.")

    # Update progress bar
    progress_bar.progress(index / total_videos)

st.success("🎉 Content Forensic Analysis Completed!")
