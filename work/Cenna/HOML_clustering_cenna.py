import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class HOMLClusterAlgo(object):
		# This is a template for a clustering model class.
		# Build the functions required.


		# initialize 1st cluster (put first vector into cluster)
		# update aux cluster

		# do rest of the samples
		# 	do for all aux cluster
				# check distance and cosine values
				# assign a value that shows the fitting of the cluster
				# if pass threshold # modify for solution 1
					# mark this cluster eligible

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






	def __init__(self, *args, **kwargs):
		self.cluster_labels = None			# cluster labels
		self.aux_cluster = aux_cluster 		# average of cluster member
		self.sim_score = sim_score			# similarity score for comparison
		self.eligibility = eligibility		# eligibility statement
		pass

	def fit(self, feature_vectors):
		# """
		# 	This method receives the objects to cluster
		# 	and finds the assigned cluster labels.
		#
		# 	--- Explain any function arguments ---
		#
		# """

		# Typecheck the input data
		if not isinstance(feature_vectors, (np.ndarray, list)):
			raise TypeError("Feature vectors not numpy arrays.")


		self.cluster_labels = [0] * len(feature_vectors) # label all cluster [0]

		self.cluster_labels[0] = [0]	# label 1st cluster
		self.aux_cluster = feature_vectors[1] # 1st aux cluster is 1st vector
		self.sim_score = [0]
		threshold_value = 0.8
		for i in range(2,len(feature_vectors)): # do all vector from 2
			eligible_cluster = 0
			for j in range(len(self.aux_cluster)):	# do all current aux cluster
				sim_cos = float(cosine_similarity( \
				feature_vectors[i].reshape(1,-1),
				self.aux_cluster[j].reshape(1,-1))) # check cosine
				# sim_dist = abs(float(feature_vectors[i] - /
				# self.aux_cluster[j])) # check distance
				sim_dist = float(hypot(feature_vectors[i],
				self.aux_cluster[j])) # check distance via hypot
				self.sim_score[j] = np.mean(sim_cos, sim_dist) # similarity
				if self.sim_score[j] > threshold_value: # check eligibility
					eligible_cluster += 1
					self.eligibility[j] = True

			if eligible_cluster = 0: # create new cluster
				self.cluster_labels[len(self.aux_cluster) + 1 ] = \
				len(self.aux_cluster) + 1
				self.aux_cluster[len(self.aux_cluster) + 1 ] = \
				feature_vectors[i]
			elif eligible_cluster = 1: # add vector to cluster
				ok_cluster = self.eligibility.index(True)
				self.aux_cluster[ok_cluster] = sum(self.aux_cluster,
				feature_vectors[i]) / 2
			else eligible_cluster > 1: # pick highest score, add to that cluster
				 hi_sim = max(self.sim_score) # highest similarity






		return self


	def update_aux(self, aux_cluster):
		pass
