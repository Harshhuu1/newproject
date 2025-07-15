# CapBot – AI-Powered Acquisition Target Finder

**Author:** Harsh Yadav  
**Challenge:** Caprae Capital Internship Submission  
**Link:** [GitHub Repo](https://github.com/Harshhuu1/newproject)

---

## ✅ Objective

CapBot is an AI-assisted tool designed to help acquisition analysts filter and evaluate small businesses efficiently. It loads startup listings, scores them based on financials, and generates acquisition pitches using a language model — all within a Streamlit dashboard.

---

## 🔍 Approach & Architecture

- **Modular Design:** Divided into scraper, scorer, generator, and app modules.
- **Dataset:** A curated CSV file of 500+ realistic small business listings (`scraped_500_plus.csv`) with title, location, revenue, cashflow, and description.
- **Scoring Logic:** Businesses are scored using a formula:
=score = (cashflow / revenue) × 100

- **Frontend:** Built using `Streamlit` to allow search, sort, and CSV export.

---

## 🧠 AI Model & Usage

- **Model:** `mistralai/Mistral-7B-Instruct-v0.3` from Hugging Face
- **Library:** Used `LangChain` with `HuggingFaceEndpoint` wrapper
- **Prompt Engineering:** Structured input to generate a 1-paragraph investor pitch per business
- **Integration:** AI summarization triggered per row in the dataset (batch-capable)

---

## 🧹 Data Handling & Preprocessing

- Cleaned revenue and cashflow (removed `$`, `,`)
- Removed rows with missing financials
- Generated scores numerically before passing to LLM
- CSV outputs handled using `pandas`, no database required

---

## 📈 Performance & Evaluation

- **Output Quality:** Pitches generated are short, grammatically clean, and investor-facing
- **Scalability:** Can handle 500+ rows; model call is modular
- **Extendable:** Real-time scraping and deal pipeline export can be added easily

---

## ✅ Rationale

While real-time scraping was avoided to reduce ethical/legal risk, the core logic was designed to simulate real acquisition workflows. LangChain + Hugging Face was chosen to show strong LLM integration and modular reasoning logic, while Streamlit was used to provide a fast demo-ready interface.

---

