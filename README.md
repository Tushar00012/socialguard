
# **Social Guard**  
### Preventing the Spread of Misinformation using AI & ML  

## **🚀 Overview**  
Social Guard is an **AI-powered misinformation detection system** that helps prevent the spread of false content across platforms like **YouTube, Facebook, and Twitter**. By leveraging **machine learning, web scraping, and natural language processing (NLP)**, it analyzes video metadata, transcribes content, and verifies information against reputable news sources.

## **🎯 Problem Statement**  
In today's digital world, **misinformation spreads rapidly**, leading to social unrest, fake narratives, and even security threats. Manual fact-checking is time-consuming and ineffective at scale. **Social Guard automates misinformation detection and takedown requests**, ensuring a safer and more reliable digital space.

## **🔑 Key Features**  
✅ **Web Dashboard:** Centralized interface for managing and monitoring detected accounts in real time.  
✅ **Web Scraper:** Extracts **YouTube videos** based on location and specific criteria for analysis.  
✅ **Metadata Extractor:** Analyzes account details such as age, engagement, and activity patterns.  
✅ **Takedown Requests:** Sends removal requests to social media platforms for flagged misinformation.  
✅ **Transcription & NLP:** Converts multilingual video content to text and cross-verifies with credible news sources.  
✅ **Machine Learning Model:** Classifies accounts as **Green (Safe), Yellow (Suspicious), Red (Fake/Malicious)**.  

## **🛠️ Tech Stack**  
- **Frontend:** Streamlit  
- **Backend:** Flask  
- **Database:** MySql  
- **Web Scraping:** BeautifulSoup, Selenium  
- **Machine Learning:** LLaMA 38B, Scikit-learn, TensorFlow  
- **APIs Used:** YouTube API, Facebook Graph API  

## **🛠️ How It Works**  
1. **Fetch YouTube Videos & Channel Data** using web scraping and APIs.  
2. **Analyze Video Metadata** (upload date, engagement, account credibility).  
3. **Transcribe Video Content** using NLP and cross-check with reliable news sources.  
4. **Classify Accounts & Content** using AI-based categorization (Green, Yellow, Red).  
5. **Generate Reports & Alerts** for authorities, social platforms, and fact-checking agencies.  
6. **Automate Takedown Requests** for harmful content removal.  

## **📈 Potential & Future Upgrades**  
### **Potential Applications:**  
- Used by **journalists & students** as a **digital literacy tool**.  
- Supports **content creators** in **avoiding false copyright strikes**.  
- Helps **government agencies** track **cross-border misinformation**.  
- Assists **social media platforms** in strengthening fact-checking systems.  

### **Future Enhancements:**  
- Expand support to **more platforms (TikTok, WhatsApp, Telegram, Reddit)**.  
- Enhance **fake account detection** using behavioral analysis.  
- Implement **real-time misinformation heatmaps** for geographic tracking.  
- Collaborate with **government bodies** to regulate online misinformation.  

## **👨‍💻 Team Members**  
- **Garbhit Sharma** (Team Leader)  
- **Kashish Verma**  
- **Udit Dwivedi**  
- **Tushar Ranjan**  

## **📌 How to Run Locally**  
```bash
# Clone the repository
git clone https://github.com//GarbhitSh//socialguard.git
cd socialguard

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run Dashboard.py
```

## **📝 License**  
This project is open-source and available under the **MIT License**.  

## **⭐ Contribute**  
Feel free to **fork the repository** and submit **pull requests** to improve the system! 🚀
