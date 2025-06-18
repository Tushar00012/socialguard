# 🛡️ Social Guard  
### *Preventing the Spread of Misinformation using AI & ML*

---

## 🚀 Overview  
**Social Guard** is an **AI-powered misinformation detection system** that proactively analyzes and flags potentially harmful digital content across platforms like **YouTube, Facebook, and Twitter**. By combining **web scraping**, **NLP**, and **machine learning**, it identifies suspicious content, classifies it, and automates takedown workflows, thereby enhancing **digital trust and safety**.

---

## 🎯 Problem Statement  
With the rise of **social media**, misinformation is spreading **faster than ever** — influencing public opinion, triggering unrest, and spreading fake news. Manual fact-checking is slow, unscalable, and often too late. **Social Guard** addresses this challenge through **automated, intelligent misinformation detection and mitigation**.

---

## 🔑 Key Features  
- ✅ **Interactive Dashboard:** Monitor flagged content and accounts in real-time  
- ✅ **YouTube Scraper:** Automatically fetches videos based on keywords or region  
- ✅ **Metadata Analyzer:** Evaluates content age, user activity, and engagement  
- ✅ **Automated Takedown Requests:** Sends notifications for content removal  
- ✅ **NLP-Powered Transcription:** Transcribes multilingual audio to text and verifies against trustworthy news  
- ✅ **AI Classification Model:** Labels content as:
  - 🟢 Green (Safe)
  - 🟡 Yellow (Suspicious)
  - 🔴 Red (Fake/Malicious)

---

## 🧠 Methodology  
![kcash - Execute 4 0 (1)](https://github.com/user-attachments/assets/78b76a27-f9a6-4248-85cd-241f06824f20)


---

## 📐 Low-Level Design (LLD)
![kcash - Execute 4 0](https://github.com/user-attachments/assets/68fe3b6f-aa03-452e-981d-0aab1525d6da)


---

## 🛠️ Tech Stack  
- **Frontend:** Streamlit  
- **Database:** MySQL  
- **Web Scraping:** BeautifulSoup  
- **Machine Learning:** LLaMA 38B, Scikit-learn, TensorFlow  
- **APIs:** YouTube API, Facebook Graph API  
- **NLP:** spaCy, NLTK, Google Speech-to-Text
  ![9](https://github.com/user-attachments/assets/453ac1ba-03db-4485-9c4e-838e72a5fa14)


---

## 🖼️ Working Images  

![10](https://github.com/user-attachments/assets/47201aef-b79d-4fd3-b93d-527997c8cfd3)


![11](https://github.com/user-attachments/assets/ffaa5d04-03f6-488a-8beb-4ee6a8245d53)



---

## 📈 Potential Applications  
- 📰 **Digital Literacy Tool** for journalists, students, and educators  
- 🎥 Helps **creators** avoid spreading misinformation unknowingly  
- 🏛️ Useful for **government agencies** to detect and counter propaganda  
- 🌐 Integrates with **social media platforms** to enhance moderation  

---

## 🚀 Future Enhancements  
- 🌍 Expand to **WhatsApp, Telegram, X, Reddit**  
- 🔎 Implement **real-time misinformation heatmaps**  
- 🧬 Detect **bot-driven activity** and fake accounts using behavioral data  
- 🤝 Collaborate with **regulatory authorities** and fact-checking orgs  

---

## 📌 How to Run Locally  
```bash
# Clone the repository
git clone https://github.com/Tushar00012/socialguard.git
cd socialguard

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run Dashboard.py
