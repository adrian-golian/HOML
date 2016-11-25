from sklearn import metrics
from collections import defaultdict, Counter

def clustering_precision_recall(true_labels, predicted_labels):
	"""
		This function calculates precision and recall
		for the clusters discovered in classed data.
	"""

	# Find the most common (true) class present in each cluster found
	clusters = defaultdict(list)
	clusters_classes = defaultdict(list)
	for vector_index, cluster_label in enumerate(predicted_labels):
		clusters[cluster_label].append(vector_index)
		clusters_classes[cluster_label].append(true_labels[vector_index])

	cluster_label_class = {}
	for cluster_label, classes in clusters_classes.items():
		cluster_label_class[cluster_label] = Counter(classes).most_common(1)[0][0]

	# Assume the most common cluster-class as the whole cluster's label
	discovered_classes = []
	for cluster_label in predicted_labels:
		cluster_class = cluster_label_class[cluster_label]
		discovered_classes.append(cluster_class)

	# Compare the discovered classes with true classes
	precision = metrics.precision_score(true_labels, discovered_classes, average='macro')
	recall = metrics.recall_score(true_labels, discovered_classes, average='macro')

	return precision, recall
