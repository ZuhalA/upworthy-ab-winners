import numpy as np
from src.winners_curse import split_halves

def test_split_halves_add_back_to_totals():
    rng = np.random.default_rng(0) # rng w/ fixed seed so test gives same result every run
    clicks = np.array([83, 76, 0, 5]) # e.g 83 of 4187 and 76 of 4140 of this and below, are the best and runner up of test 1
    impressions = np.array([4187, 4140, 3118, 13]) # 0 clicks of 3118 impression is a zero-click case with median impression. And 5 clicks out of 13 is a tiny package with just 13 impressions
    c_sel, n_sel, c_val, n_val = split_halves(clicks, impressions, rng) # runs the function and returns the click and impressions of each halves
    assert np.all(c_sel + c_val == clicks) # the clicks of 2 halves add back to original clicks and the same applies to impressions
    assert np.all(n_sel + n_val == impressions)
    assert np.all(c_sel <= n_sel) and np.all(c_val <= n_val) # a half logically should never have clicks > impressions
    assert c_sel[2] == 0 # package 2 has zero clicks so it should have 0 clicks in selection too
    