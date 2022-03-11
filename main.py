import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.exponential(scale=10 size=100)

print(x)

#x = np.random.poisson(lam=5, size=100)
#print(x)
#sns.distplot(x, kde=False)
#plt.show()

#x = np.random.binomial(n=5, p=0.3, size = 6)
#print (x)
#mylabels = ["Zero Wins", "One Win", "Two Wins", "Three Wins", "Four Wins", "Five Wins"]
#plt.pie(x, labels=mylabels)
#plt.show()

#marks = np.array([23,37,45,49,56,63,63,70,72,82])

#mean_mark = marks.mean()

#print(f"Mean:{mean_mark}")

#difference_from_mean = np.array([])

#for mark in marks:
  #difference =  mark - mean_mark
  #difference_from_mean = np.insert(difference_from_mean,0,difference)
#print(f"difference from mean:{difference_from_mean}")

#variance = np.square(difference_from_mean).mean()
#print(f"variance:{variance}")

#standard_deviation = np.sqrt(variance)
#print(f"standard_deviation:{standard_deviation}")

#sns.distplot(marks, hist=False)

#plt.show()



#scores = np.array([62, 90])
#standard_deviations = 2

#x = np.random.normal(loc = scores.mean(), scale = standard_deviations, size = 1000)

#print(x)

#sns.distplot(x, hist = False)
#plt.show()