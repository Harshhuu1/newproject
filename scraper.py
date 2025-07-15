import pandas as pd

def scrape_bizbuysell(keyword=""):
    df = pd.read_csv("scraped_500_plus.csv")
    if keyword:
        keyword = keyword.lower()
        df = df[df["title"].str.lower().str.contains(keyword) | df["description"].str.lower().str.contains(keyword)]
    return df.reset_index(drop=True)

