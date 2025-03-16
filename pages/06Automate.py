import streamlit as st
import pandas as pd
from module import yextractor as youtube  # YouTube data extractor
from module import nextractor as nx  # News extractor
from module import transcribe as ts  # Video transcription
from module import summarize as sumz  # Summarization module
from module import translate as tst  # Translation module
from module import identifier as idefy  # Fake news validator

# File to save results
filename = "Accountreport.csv"

# Streamlit Page Title
st.title("Automated Fake News Detection")
st.write("Processing video data and analyzing its credibility...")

# Function to Load Data
@st.cache_data
def load_data():
    try:
        return pd.read_csv("video_data.csv")  # Ensure correct path
    except FileNotFoundError:
        st.error("Error: Video data file not found!")
        return None

# Load data
df = load_data()

if df is not None:
    st.subheader("Extracted Social Media Data & Metadata")
    st.write(df)

    video_titles = df['Video Title']
    video_links = df['Video URL']

    final_status_list = []
    progress_bar = st.progress(0)  # Progress bar for better UX

    for idx, (video_url, title) in enumerate(zip(video_links, video_titles)):
        st.subheader(f"Processing Video {idx + 1}: {title}")
        st.write("**************************************")

        # Step 1: Get Video Transcript
        transcript = ts.transcript(video_url, idx)
        if transcript is None:
            final_status_list.append('Yellow')
            st.warning("Transcript not available (Yellow Flag 🚩)")
            continue

        # Step 2: Display Transcript & Summary
        st.write("📜 **Video Transcript:**")
        st.write(transcript)

        video_summary = sumz.sumup(transcript)
        st.write("📌 **Summarized Content:**")
        st.write(video_summary)

        # Step 3: Fetch Related News
        query = tst.trans(title)  # Translate if needed
        related_news = nx.get_news_list(query)

        if not related_news:
            final_status_list.append('Yellow')
            st.warning("No related news found (Yellow Flag 🚩)")
            continue

        news_summary = sumz.sumup(related_news)
        st.write("📰 **Related News Summary:**")
        st.write(news_summary)

        # Step 4: Analyze and Validate Content
        st.subheader("🛠 **Content Validation Status**")
        validation_status = idefy.validator(video_summary, news_summary)
        final_status_list.append(validation_status)
        st.success(f"Analysis Result: **{validation_status}**")

        progress_bar.progress((idx + 1) / len(video_links))  # Update progress

    # Creating Final DataFrame
    results_df = pd.DataFrame({
        'Video Title': video_titles,
        'Video Link': video_links,
        'Status': final_status_list
    })

    # Save Report
    st.subheader("📊 **Final Report**")
    st.write(results_df)
    results_df.to_csv(filename, index=False)
    st.success("Report saved successfully! ✅")

else:
    st.error("No data available for processing.")
