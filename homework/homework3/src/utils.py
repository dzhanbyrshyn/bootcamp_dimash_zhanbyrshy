import pandas as pd

def get_summary_stats(df, category_col):
    return df.groupby(category_col).mean(numeric_only=True).reset_index()