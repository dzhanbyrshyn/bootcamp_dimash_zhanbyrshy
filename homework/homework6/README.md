## Cleaning Strategy

- **Missingness:** drop rows that are >50% missing (after optionally dropping heavily-missing columns). Fill remaining numeric features with **median**
- **Features vs non-features:** only scale true numeric feature columns; skip IDs/ZIP/binary/constant columns
- **Normalization:** min–max scaling to [0, 1] (or z-score), after imputation
- **I/O & Reproducibility:** raw data loaded from `data/raw/`; cleaned dataset saved to `data/processed/`
- **Validation:** notebook compares original vs cleaned (shape, NA%, dtypes, basic stats)
