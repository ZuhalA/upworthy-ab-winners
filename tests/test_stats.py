import numpy as np
import pytest
from statsmodels.stats.proportion import proportion_confint, proportions_ztest
from src.stats import wilson_interval, two_prop_z, Z95

#Input for Wilson tests: (clicks, impressions, label)
#label is just names the case if it fails
WILSON_CASES = [
    # (clicks, impressions, label)
    (37, 3118, "typical package"), # 3118 is median impreesion in the dataset, 37 is median clicks which is about 1.2% click rate
    (0, 3118, "zero clicks"), # in this case normal intercal breaks
    (1, 20, "very small package"), # this is too small, so a wide interval
    (300, 3000, "high rate"), # 300 clicks out of 3000 is a 10% click rate, which is high for this dataset. The data top is %12
    (0, 13, "zero clicks, tiny package"), # 13 is the smallest impressions count in the dataset
]

# we run this test to make sure our implementation matches the statsmodels implementation, which is well-tested and widely used. We don't need to test every possible input, just a few representative cases.
@pytest.mark.parametrize("x, n, label", WILSON_CASES)
def test_wilson_matches_statsmodels(x, n, label):
    mine = wilson_interval(x, n) # my (low, high)
    ref = proportion_confint(x, n, alpha=0.05, method="wilson") # statsmodels (low, high)
    assert np.allclose(mine, ref), label # equal up to numerical precision


def test_wilson_zero_clicks_upper_bound_by_hand():
    # hand check: with x = 0 the upper bound is z^2 / (n + z^2)
    low, high = wilson_interval(0, 3118)
    assert low == pytest.approx(0.0, abs=1e-12) # with zero clicks the lower bound is always 0, but we check it anyway
    assert high == pytest.approx(Z95**2 / (3118 + Z95**2))

# Input for two-proportion z-test: (clicks_1, impressions_1, clicks_2, impressions_2, label)
Z_CASES = [
    (52, 3100, 38, 3050, "typical pair"), # two ordinary packages with visibale gap
    (10, 500, 25, 520, "small packages"), # fewer impressions, so the z-test is less confident, even though the gap is larger and noiser
    (40, 3000, 40, 3000, "identical counts"), #no difference, so z = 0 and p = 1
]


@pytest.mark.parametrize("x1, n1, x2, n2, label", Z_CASES)
def test_z_matches_statsmodels(x1, n1, x2, n2, label):
    z, p = two_prop_z(x1, n1, x2, n2) # my (z, p)

    z_ref, p_ref = proportions_ztest([x1, x2], [n1, n2], alternative="two-sided") # statsmodels (z, p)

    assert np.isclose(z, z_ref), label
    assert np.isclose(p, p_ref), label


def test_z_undefined_when_both_zero():
    # when both packages have zero clicks, the pooled click rate is 0, so the standard error is 0 and the z-test is undefined. We return (nan, nan) in this case.
    z, p = two_prop_z(0, 3000, 0, 3100)
    assert np.isnan(z) and np.isnan(p)
