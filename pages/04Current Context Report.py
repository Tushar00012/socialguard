import streamlit as st
import pandas as pd
from module import nextractor as nx
from module import translate as tst

st.title("📰 Actual Context Report")

# Load video data
try:
    df = pd.read_csv("video_data.csv")
    if df.empty:
        st.warning("⚠ No data found in `video_data.csv`. Please upload a valid file.")
        st.stop()
except FileNotFoundError:
    st.error("❌ `video_data.csv` not found. Make sure the file exists in the correct location.")
    st.stop()

# Extract video titles
video_titles = df['Video Title']

# Lists to store extracted data
video_title_list = []
newslist = []

# Process each video title
for title in video_titles:
    st.subheader(f"🎥 Video Title: {title}")

    # Translate the title for better news search
    query = tst.trans(title)

    # Fetch related news
    ns = nx.get_news_list(query)

    # Display extracted news
    st.write(f"**Related News Articles Found:** {len(ns)}")
    
    if ns:
        for index, news in enumerate(ns, start=1):
            st.write(f"{index}. {news}")
    else:
        st.write("⚠ No related news found.")

    # Store results
    video_title_list.append(title)
    newslist.append(ns)

# Create and save extracted data to CSV
news_data = pd.DataFrame({
    'Video Title': video_title_list,
    'News': newslist
})

csv_filename = "news_data.csv"
news_data.to_csv(csv_filename, index=False)

st.success(f"✅ Extracted news data has been saved to `{csv_filename}`.")

