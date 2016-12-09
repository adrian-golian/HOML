from sklearn import datasets, metrics
import numpy as np
from es00_clusteringalgorithm import HOMLClusterAlgo
from HOML_evaluation import clustering_precision_recall

digits = datasets.load_digits()

threshold = 0.9
minsamp = 1200
maxsamp = 1300

clf = HOMLClusterAlgo(cluster_labels = None, min_sim = threshold, num_seeds=10)

clf.fit(digits.data[minsamp:maxsamp])

print clustering_precision_recall(digits.target[minsamp:maxsamp],clf.cluster_labels[:])

#predicted_digits = list(clf.predict(digits.data[1300:]))
#expected_digits = list(digits.target[1300:])

#print predicted_digits
#print expected_digits

# Now let's see a quantitative measure of the classifier's performance
#comparison = [predicted_digits[i] == expected_digits[i] for i in xrange(min(len(predicted_digits), len(expected_digits)))]
#print sum(comparison) / float(len(comparison))

# We can also take advantage of the library's 'metrics'
#print metrics.confusion_matrix(expected_digits, predicted_digits)
