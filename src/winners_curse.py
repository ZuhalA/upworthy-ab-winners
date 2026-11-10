import numpy as np

def split_halves(clicks, impressions, rng):
    clicks = np.asarray(clicks)
    impressions = np.asarray(impressions)
    n_sel = impressions // 2
    n_val = impressions - n_sel
    clicks_sel = rng.hypergeometric(clicks, impressions - clicks, n_sel)
    clicks_val = clicks - clicks_sel
    return clicks_sel, n_sel, clicks_val, n_val