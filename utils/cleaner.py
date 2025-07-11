# utils/cleaner.py

import pandas as pd

def clean_data(df: pd.DataFrame):
    log = []

    # Step 1: Remove duplicates safely
    original_shape = df.shape
    df = df.drop_duplicates().copy()
    log.append(f"Removed duplicates. Original shape: {original_shape}, New shape: {df.shape}")

    # Step 2: Fill missing values
    for col in df.columns:
        if df[col].isnull().any():
            if df[col].dtype == 'object':
                mode_val = df[col].mode(dropna=True)
                if not mode_val.empty:
                    df[col] = df[col].fillna(mode_val[0])
                    log.append(f"Filled missing values in column '{col}' with mode: {mode_val[0]}")
                else:
                    log.append(f"Skipped column '{col}' - mode not found.")
            else:
                mean_val = df[col].mean()
                df[col] = df[col].fillna(mean_val)
                log.append(f"Filled missing values in column '{col}' with mean: {mean_val:.2f}")

    log.append(f"Missing values filled. Columns processed: {df.columns.tolist()}")
    return df, log
