from sklearn import datasets, metrics
import numpy as np
from HOML_plotting import plot_heatmap

from sklearn import svm # Support Vector Machine

digits = datasets.load_digits()

# # Show an example vector
# print(digits.data[0])
# print(np.reshape(digits.data[0], (-1, 8)))

# # Show a couple of the digits
# for i in range(10):
# 	plot_heatmap(np.reshape(digits.data[i], (-1, 8)))


clf = svm.SVC()
# # Try the above and then:
# clf = svm.LinearSVC()

clf.fit(digits.data[:1300], digits.target[:1300])

predicted_digits = list(clf.predict(digits.data[1300:]))
expected_digits = list(digits.target[1300:])

print predicted_digits
print expected_digits

# Now let's see a quantitative measure of the classifier's performance
comparison = [predicted_digits[i] == expected_digits[i] for i in xrange(min(len(predicted_digits), len(expected_digits)))]
print sum(comparison) / float(len(comparison))

# We can also take advantage of the library's 'metrics'
print metrics.confusion_matrix(expected_digits, predicted_digits)