newMachine = [42.1, 41.0, 41.3, 41.8, 42.4, 42.8, 43.2, 42.3, 41.8, 42.7]
oldMachine = [42.7, 43.6, 43.8, 43.3, 42.5, 43.5, 43.1, 41.7, 44.0, 44.1]


# H0: mu1 = mu2
# H1: mu1 != mu2

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Question 1
# check if the data is normal distributed
data = np.array(newMachine)
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q-Q Plot")
plt.show()

data = np.array(oldMachine)
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q-Q Plot")
plt.show()

# Perform a t-test to compare the means of the two machines
tStat, pValue = stats.ttest_ind(newMachine, oldMachine, alternative='less')

# Results
print(tStat, pValue)
data = np.array(newMachine)

if pValue < 0.05:
    print("Reject null hypothesis. ")
else:
    print("Accept null hypothesis")

before = np.array([210, 205, 193, 182, 259, 239, 164, 197, 222, 211, 187, 175, 186, 243, 246])
after = np.array([197, 195, 191, 174, 236, 226, 157, 196, 201, 196, 181, 164, 181, 229, 231])

# Question 2
# H0: mu1 = mu2
# H1: mu1 != mu2

tStat, pValue = stats.ttest_rel(before, after)

# Results
print(tStat, pValue)

if pValue < 0.05:
    print("Reject null hypothesis. ")
else:
    print("Accept null hypothesis")

# Question 3
constantSound = np.array([7,4,6,8,6,6,2,9])
randomSound = np.array([5,5,3,4,4,7,2,2])
noSound = np.array([2,4,7,1,2,1,5,5])

fStat, pValue = stats.f_oneway(constantSound, randomSound, noSound)

print(fStat, pValue)

labels = np.array(['Group1'] * len(constantSound) + ['Group2'] * len(randomSound) + ['Group3'] * len(noSound))
# Combine the groups into a single data array
data = np.concatenate([constantSound, randomSound, noSound])
# Perform Tukey's HSD test
tukeyResults = pairwise_tukeyhsd(endog=data, groups=labels, alpha=0.05)

# Print the results
print(tukeyResults)

# Question 4
demo = [138, 83, 64]
rep = [64, 67, 84]

# perform a chi-square test
chi2, p, dof, expected = stats.chi2_contingency([demo, rep])
print("\nChi-square Test:")
# Results
print(chi2, p, dof, expected)

if p < 0.05:
    print("Reject null hypothesis. ")
else:
    print("Accept null hypothesis")