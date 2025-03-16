import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Social Content Report", layout="wide")

st.title("📊 Social Content Report")

# ✅ **Cache data loading for performance optimization**
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("video_data.csv")

        # Ensure required columns exist
        required_columns = {"Published At", "Views", "Channel Title"}
        if not required_columns.issubset(df.columns):
            st.error(f"⚠ Missing required columns: {required_columns - set(df.columns)}")
            return pd.DataFrame()  # Return empty DataFrame on error

        # Convert "Published At" column to datetime format
        df["Published At"] = pd.to_datetime(df["Published At"], errors="coerce")

        # Handle missing or invalid dates
        df = df.dropna(subset=["Published At"])  

        return df

    except FileNotFoundError:
        st.error("❌ File `video_data.csv` not found. Please upload a valid file.")
        return pd.DataFrame()

# Load data
df = load_data()

# ✅ **Display Data if Available**
if df.empty:
    st.warning("⚠ No valid data available. Please check the CSV file.")
    st.stop()  # Stop execution if no valid data

st.write("📌 **Dataset Overview**")
st.dataframe(df)  # Interactive table view

# ✅ **Multi-select for filtering channels**
selected_channels = st.multiselect("🎥 Select Channels", df["Channel Title"].unique(), [])

# ✅ **Filter Data by Selected Channels**
if selected_channels:
    df = df[df["Channel Title"].isin(selected_channels)]

# ✅ **Ensure Non-Empty Data After Filtering**
if df.empty:
    st.warning("⚠ No data available for the selected channels.")
    st.stop()

# ✅ **Prepare Data for Visualization**
plot_data = df.groupby(df["Published At"].dt.date)["Views"].sum().reset_index()
plot_data["Published At"] = pd.to_datetime(plot_data["Published At"])

# ✅ **Create Altair Chart**
chart = (
    alt.Chart(plot_data)
    .mark_line(color="steelblue", size=3)
    .encode(
        x=alt.X("Published At:T", title="📅 Published Date"),
        y=alt.Y("Views:Q", title="👀 Total Views"),
        tooltip=["Published At:T", "Views:Q"]
    )
    .properties(
        width=900,
        height=450,
        title="📈 Views Over Time for Published Videos"
    )
)

# ✅ **Display Chart**
st.altair_chart(chart, use_container_width=True)

st.success("✅ Analysis Completed Successfully!")
