import numpy as np
import matplotlib.pyplot as plt
y = np.array([15, 31, 41, 7])
mylabels = ["Candy", "Fruits", "Cereal", "Vegetables"]
mycolors = ["orange", "blue", "pink", "black"]
plt.pie(y, labels=mylabels, colors=mycolors)
plt.show()
