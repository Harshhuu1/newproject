import streamlit as st
import pandas as pd
from scraper import scrape_bizbuysell
from scorer import score_business
from generator import generate_pitches

st.set_page_config(page_title="CapBot: AI Acquisition Finder", layout="wide")
st.title("🤖 CapBot: AI-Powered Acquisition Target Finder")

keyword = st.text_input("Enter a keyword to search businesses (e.g. 'AI', 'SaaS', 'Ecommerce')", value="saas")

if st.button("🔍 Search & Analyze"):
    with st.spinner("Scraping businesses..."):
        df = scrape_bizbuysell(keyword)

    if df.empty:
        st.error("❌ No listings found.")
    else:
        st.success("✅ Listings scraped.")

        df["score"] = df.apply(score_business, axis=1)

        with st.spinner("Generating AI Pitches..."):
            df = generate_pitches(df)

        st.dataframe(df[["title", "location", "revenue", "cashflow", "score", "pitch"]], use_container_width=True)
        st.download_button("📥 Download CSV", df.to_csv(index=False), file_name="capbot_output.csv")
