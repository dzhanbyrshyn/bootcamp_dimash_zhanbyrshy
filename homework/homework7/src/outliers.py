import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Return boolean mask for IQR-based outliers.
    Assumptions: distribution reasonably summarized by quartiles; k controls strictness.
    """
    # make sure it's numeric + keep original index
    s = pd.to_numeric(series, errors="coerce")

    # compute quartiles on finite values only (avoid NaN/±inf messing bounds)
    s_finite = s[np.isfinite(s)]
    if s_finite.empty:
        # nothing to compute on -> no finite outliers
        return pd.Series(False, index=series.index)

    q1 = s_finite.quantile(0.25)
    q3 = s_finite.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr

    # flag strict outside of (lower, upper) + NaNs -> False
    mask = (s < lower) | (s > upper)

    # treat +-inf as outliers explicitly
    mask = mask.fillna(False) | (~np.isfinite(s))
    return mask


def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Return boolean mask for Z-score outliers where |z| > threshold.
    Assumptions: roughly normal distribution; sensitive to heavy tails.
    """
    # numeric + preserve index
    s = pd.to_numeric(series, errors="coerce")

    # mean/std computed on finite values only
    s_finite = s[np.isfinite(s)]
    if s_finite.empty:
        return pd.Series(False, index=series.index)

    mu = s_finite.mean()
    sigma = s_finite.std(ddof=0)  # keep ddof=0 as in starter

    # avoid dividing by 0; if sigma==0, no (finite) value is "far"
    if not np.isfinite(sigma) or sigma == 0:
        z = pd.Series(0.0, index=s.index)
    else:
        z = (s - mu) / sigma

    mask = z.abs() > threshold

    # 3) NaNs -> False ; +-inf -> True
    mask = mask.fillna(False) | (~np.isfinite(s))
    return mask

def winsorize_series(series: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:
    # basic guard rails
    if not (0.0 <= lower < upper <= 1.0):
        raise ValueError("lower/upper must satisfy 0 <= lower < upper <= 1.")

    # numeric view (preserve index), NaNs kept as NaN
    s = pd.to_numeric(series, errors="coerce")

    # compute quantiles on finite values only (avoid +-inf/NaN messing cutoffs)
    s_finite = s[np.isfinite(s)]
    if s_finite.empty:
        # nothing to winsorize -> return a copy as-is
        return series.copy()

    lo = s_finite.quantile(lower)
    hi = s_finite.quantile(upper)

    # clip to (lo, hi) + keeps index
    out = s.clip(lower=lo, upper=hi)
    out.name = getattr(series, "name", None)
    return out