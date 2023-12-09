from matplotlib import pyplot as plt
from numpy.random import normal
from numpy import mean, std
from scipy.stats import norm

sample = normal(loc = 50, scale = 5, size = 1000)
sample_mean = mean(sample)
sample_Std = std(sample)
print('Mean=%.3F \n Standard Deviation=%.3F' % (sample_mean, sample_Std))

dist = norm(sample_mean, sample_Std)

values = [value for value in range(30,70)]
probabilities = [dist.pdf(value) for value in values]

plt.figure(figsize=(5,4))
plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilities)
plt.show()
    