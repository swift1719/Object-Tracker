import random
from matplotlib import pyplot as plt
#Histograms
#A histogram is a representation of distribution of values of a dataset.

#data = []
#for x in range(10):
#    data.append(random.randint(1,10))
# data = [1, 1, 1, 1, 1, 4, 5, 6, 10, 9, 9, 9]

data = [random.randint(1,10) for x in range(100)]
print(data)

#make a histogram having 10 bins (intervals) representing values in range 1-10
plt.hist(data, 10, [1,10])
#render the histogram
plt.show()
