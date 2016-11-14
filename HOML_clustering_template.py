import numpy as np

class HOMLClusterAlgo(object):
	"""
		This is a template for a clustering model class.
		Build the functions required.
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
