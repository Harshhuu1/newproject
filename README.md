# 🤖 CapBot: AI-Powered Acquisition Target Finder

CapBot is a smart, AI-enhanced tool that helps private equity and venture teams evaluate small online businesses for acquisition. It automatically scores listings, generates investor-ready summaries, and presents everything in a clean, interactive Streamlit dashboard.

---

## 🎯 Goal

Build a tool that:
- ✅ Collects and filters business listings
- ✅ Scores them based on financials
- ✅ Generates a 1-paragraph investment pitch using AI
- ✅ Provides an interactive UI for exploration and export

---

## 🧠 How It Works

CapBot simulates the workflow of an early-stage investment analyst:

| Step            | What It Does                                                                 |
|------------------|------------------------------------------------------------------------------|
| Data Collection   | Loads curated business listings from a CSV file (can be replaced with live scraping) |
| Financial Scoring | Calculates profitability score based on revenue and cashflow               |
| AI Summarization  | Uses Hugging Face + LangChain to generate investment pitches                |
| Frontend UI       | Streamlit dashboard with search, view, and CSV export capabilities         |

---

## ⚠️ Disclaimer

> 🚨 **Note**: For demonstration purposes, CapBot uses a curated CSV dataset of 500+ realistic startup listings.  
> Real-time scraping (from Flippa, IndieHackers, BizBuySell, etc.) was not implemented due to rate limits, JavaScript rendering, and ethical scraping guidelines — but the scraper module is modular and can be extended.

---

## 🗂 Folder Structure

capbot/
├── app.py ← Streamlit UI
├── scraper.py ← Loads business listings from CSV
├── scorer.py ← Calculates profitability score
├── generator.py ← AI-powered pitch generator using Hugging Face + LangChain
├── scraped_500_plus.csv ← Curated listing dataset (500+ rows)
├── requirements.txt ← Python dependencies
├── .env ← Stores Hugging Face API key (ignored in Git)
├── .gitignore ← Ensures clean commits
├── README.md ← You're reading it :)


---

## 📊 Scoring Logic

Each business is scored using a simple but effective formula:

Score = (cashflow / revenue) × 100


This allows quick comparison of business health and profitability.

---

## 🧠 Sample Pitch (AI-Generated)

> "This AI SaaS business shows strong operational leverage with a 42% profit margin and automated lead-gen features. A great opportunity for bolt-on acquisition or scaled growth."

---

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/capbot.git
cd capbot

python -m venv venv
venv\Scripts\activate  # on Windows

pip install -r requirements.txt

Create a .env file:

HUGGINGFACEHUB_API_TOKEN=your_token_here
⚠️ Keep this file local — it is ignored by Git for safety.

💻 Run the Streamlit App

streamlit run app.py

🙋 Author
Built with 💻 and 🧠 by
Harsh Yadav
GitHub: @Harshhuu1


