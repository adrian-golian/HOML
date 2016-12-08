import numpy as np

class HOMLClusterAlgo(object):
	"""
		This is a template for a clustering model class.
		Build the functions required.
	"""
	"""
		initialize 1st cluster (put first vector into cluster)
		update aux cluster

		do rest of the samples
			do for all aux cluster
				check distance and cosine values
				assign a value that shows the fitting of the cluster
				if pass threshold # modify for solution 1
					mark this cluster eligible

			if eligible cluster is = 0
				create new cluster
				add vector to cluster
				label cluster
				update aux cluster
			else if eligible cluster is = 1
				put vector into that cluster
				update aux cluster
			else (if eligible cluster is > 1)
				find the highest fitting values (max)
				put vector into that cluster
				update aux cluster
			#if cluster number is > 15 # add for solution 2
			#	combine cluster

		print number of clusters
		combine cluster # original idea


		# optimization option
		# generative clustering may be heavy as cluster increases
		# solution 1: create a lower threshold values
		#	less clusters, but le3ss accurate
		# solution 2: combine cluster when cluster reaches x (say 15)
		#	quicker, less accurate, but not as bad as solution 1

		---
		def update aux cluster
			aux cluster = add all vectors in cluster/number of cluster
		---
		def combine cluster
			while cluster number is > 10
				find the highest/last cluster
				do rest of aux cluster
					check distances and cosine values
					find highest number of of fitting
				combine cluster to highest fit cluster
				update aux cluster




	"""

	def __init__(self, *args, **kwargs):
		self.k_clusters = k_clusters # Remove if your algo discovers k
		self.cluster_labels = None
		pass

	def fit(self, feature_vectors):
		"""
			This method receives the objects to cluster
			and finds the assigned cluster labels.

			--- Explain any function arguments ---

		"""

		# Typecheck the input data
		if not isinstance(feature_vectors, (np.ndarray, list)):
			raise TypeError("Feature vectors not numpy arrays.")

		self.cluster_labels = [0] * len(feature_vectors) # Replace this with actual computation
		return self
