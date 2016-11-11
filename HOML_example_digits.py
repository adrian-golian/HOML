from sklearn import datasets
import numpy as np
from HOML_plotting import plot_heatmap

digits = datasets.load_digits()

print digits.data[0]
print np.reshape(digits.data[0], (-1, 8))

# Show a couple of the digits
for i in xrange(10):
	plot_heatmap(np.reshape(digits.data[i], (-1, 8)))
