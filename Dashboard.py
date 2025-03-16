import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Social-guard Dashboard", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .maintitle {
            font-size: 50px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-top: 20px;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: #34495e;
            margin-bottom: 20px;
            text-align: center;
        }
        .card {
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            background-color: #f9f9f9;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Title of the Dashboard
st.markdown('<div class="maintitle">Welcome to Social-guard!</div>', unsafe_allow_html=True)

# Introduction Text
st.write("This dashboard helps identify and combat the growing problem of fake news in misleading videos and blogs.")

# Layout for Cards
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown("### 📰 Fake News: A Growing Threat")
        st.write("Fake news videos and blogs have led to misinformation, social unrest, and a general erosion of trust in media sources.")

with col2:
    with st.container():
        st.markdown("### ⚠️ Impact of Fake News")
        st.write("The consequences are severe, affecting public opinion, political stability, and even public health.")

with col3:
    with st.container():
        st.markdown("### 🛡️ How Social-guard Helps")
        st.write("We use AI and ML to analyze content, empowering users to identify and counter fake news.")

# Navigation Button

#if st.button("Let's Start 🚀"):
#    st.switch_page("pages\01Request Analysis.py")
