def score_business(row):
    try:
        rev = int(str(row["revenue"]).replace("$", "").replace(",", ""))
        cash = int(str(row["cashflow"]).replace("$", "").replace(",", ""))
        score = (cash / rev) * 100 if rev else 0
        return round(score, 2)
    except:
        return 0
