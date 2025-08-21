### Data Storage (Stage 5)

**Folders (from `.env`):**
- `DATA_DIR_RAW = data/raw` → CSV (as-ingested)
- `DATA_DIR_PROCESSED = data/processed` → Parquet (typed, smaller, faster I/O)

**Why CSV + Parquet:**
- CSV = universal/portable
- Parquet = efficient columnar format (smaller files, faster reads/writes)

**How the code reads/writes (env-driven):**
- Paths are loaded from `.env` using `dotenv` and anchored to the repo
- Save examples (timestamped):
  - CSV: `RAW / f"sample_{ts()}.csv"`
  - Parquet: `PRO / f"sample_{ts()}.parquet"`
- Utilities:
  - `write_df(df, path)` / `read_df(path)` route by suffix (`.csv` / `.parquet`) and create missing folders
  - Parquet is handled with `pyarrow`/`fastparquet`; errors are caught with a clear message if the engine is missing

**Validation performed after reload:**
- Shapes/columns match the source DataFrame
- `date` remains datetime (when present)
- Numeric columns remain numeric

**.env**
- `.env` is at repo root and **not committed** (ignored via `.gitignore`)
