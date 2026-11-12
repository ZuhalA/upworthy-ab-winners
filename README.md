# Upworthy: Are A/B test winners in Upworthy really winners?
# Are A/B test winners really winners?

Kind of. About half of a winner's lead is luck.

I used the [Upworthy Research Archive](https://upworthy.natematias.com/about-the-archive), which has thousands of real headline tests with views and clicks for each version, to see if a test's winner still wins when you check it again.

## how I did it

In each test I ranked the packages by click rate. The winner's lead is its click rate minus the runner-up's, in percentage points (pp).

Then I split every package's visitors into two random halves. I picked the winner on one half (the selection half) and measured the same two packages on the other (the validation half). The validation half had no say in who won, so the luck that got the winner picked can't show up there.

The winner's curse is the selection lead minus the validation lead, averaged over 200 random splits and all tests. For the 95% range I redrew the tests at random 2,000 times and took the middle 95% of the results.

I built this on 3,823 exploratory tests, then ran it once on 17,836 confirmatory tests I hadn't touched.

## what I found

Winners are real, but the test makes them look better than they are. On the selection half the winner leads by about 0.32 pp. On fresh visitors the same two packages are about 0.16 pp apart. Half the edge was luck. The confirmatory tests say the same thing.

So if a test says B beats A by 0.3 points, plan on about 0.15.

## numbers

| Row | Exploratory | Confirmatory |
|---|---:|---:|
| Tests | 3,823 | 17,836 |
| Lead, selection half (pp) | 0.319 | 0.324 |
| Lead, validation half (pp) | 0.160 | 0.162 |
| Winner's curse (pp) | 0.158 | 0.163 |
| 95% range of the curse (pp) | 0.152 to 0.164 | 0.160 to 0.166 |

pp = percentage points, the plain difference between two percentages (a 2.5% click rate vs 2.2% is a 0.3 pp lead). Leads are rounded; the curse is worked out before rounding, so the differences can be off by 0.001.

Each half only has half the visitors, so on full-size tests the curse is probably smaller. I didn't test a fix for it, and I didn't check the method on fake data.
Data: Upworthy Research Archive (Matias, Munger, Aubin Le Quere, Ebersole, 2021), https://osf.io/jd64p/.
PS. Claude was used as an advisor for this project.