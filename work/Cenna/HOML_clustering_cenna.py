import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import scipy
from math import hypot
from numpy.linalg import norm
from scipy.spatial import distance
from collections import Counter
class HOMLClusterAlgo(object):


	def __init__(self, cluster_labels, num_class,
	threshold_value, combine_cluster):
		self.cluster_labels = None				# cluster labels
		self.num_class = num_class				# number of classifier
		self.threshold_value = threshold_value 	# threshold_value
		self.combine_cluster = combine_cluster 	# ways to combine clusters
		pass

	def fit(self, feature_vectors):
		# Here we receive the vectors and assign them to clusters

		# Typecheck the input data
		if not isinstance(feature_vectors, (np.ndarray, list)):
			raise TypeError("Feature vectors not numpy arrays.")

		# Label all vectors as the 0th cluster
		self.cluster_labels = [0] * len(feature_vectors)

		# Auxillary cluster represents the vector that represents each label
		aux_cluster = [0] * len(feature_vectors)

		# 0th aux cluster is the 0th vector
		aux_cluster[0] = feature_vectors[0]

		# This variable stores which vector is most similar
		bmatch = [0]*len(feature_vectors)

		# Check all vector from 1
		for i in range(1,len(feature_vectors)):
			new_tres = 0
			sim_top = 0.0
			# print "Doing feature_vectors",i,"out of",len(feature_vectors)

			# Compare it with all existing aux cluster (non-zero)
			for j in range(len(aux_cluster)):
				# print "Doing aux cluster",j,"out of",len(aux_cluster)

				# This will exit the loop if there are no more aux cluster
				if np.all(aux_cluster[j] == 0) :
					# print "There are no more aux cluster! Break!"
					break

				# Just a parameter to hold the aux cluster (too long to type)
				aux_cls_hld = np.asarray(aux_cluster[j])

				# This is for checking cosine
				sim_cos = float(cosine_similarity(feature_vectors[i].reshape(1,-1),
				aux_cls_hld.reshape(1,-1)))

				# This is for checking distance (normalized to aux cluster)
				real_dist = np.sqrt(np.abs(np.sum((feature_vectors[i].__sub__(aux_cls_hld)))))
				sim_dist = np.sqrt(np.abs(np.sum(aux_cluster[j])))
				sim_dist = (sim_dist - real_dist)/(sim_dist)

				# Mean of both similarity score
				sim_score = np.mean([sim_cos,sim_dist])
				# print "Average similarity	:", sim_score
				# print ("-")*10

				# This will fit the vector into the most fitting aux cluster
				if sim_score >= self.threshold_value:
					if sim_score > new_tres: self.cluster_labels[i]=j
					new_tres = sim_score

				# This will return the highest matching cluster
				if (sim_score > sim_top):
					sim_top = sim_score
					bmatch[i] = j

			# print "The best matching cluster for this vector is the",best_match,"cluster"
			# This is for vectors that does not fit in any cluster
			if (self.cluster_labels[i] == 0):

				# We now find the aux cluster that is empty
				add_aux = 0
				for k in range(len(aux_cluster)):
					if np.all(aux_cluster[k] == 0): break
					add_aux += 1

				# Create new aux cluster and label this vector using it
				aux_cluster[add_aux] = feature_vectors[i]
				self.cluster_labels[i] = add_aux

			# This is where we combine clusters

			# SuddenCombine: Whenever an extra aux cluster is created,
			# 	immidiately merge it with the most matching existing cluster
			# -----------
			# Super fast but super innacurate, as every unidentified vector
			# 	will be forced to be categorized into the first 10 vectors
			# This will work well if the first 10 vectors are "correct" and the
			#	algo is supposed to determine the rest belong to which 10 cluster

			if (self.cluster_labels[i] == (self.num_class) and self.combine_cluster == "SuddenCombine" ):
				# Average the highest cluster with the most fitting cluster
				aux_cluster[bmatch[i]] = aux_cluster[self.num_class].__add__(aux_cluster[bmatch[i]])
				aux_cluster[bmatch[i]] = np.abs(aux_cluster[bmatch[i]].__floordiv__(2))
				aux_cluster[(self.num_class)] = 0
				self.cluster_labels[i] = self.cluster_labels[bmatch[i]]

			print "This vector(",i,") is currently labeled as",self.cluster_labels[i]
		# Here we have labeled all clusters

		# FinalCombine: After all clusters has been found, merge them with the
		# 	the highest matching cluster

		if (self.combine_cluster == "FinalCombine"):

			# Find the top 10 cluster (based on frequency)
			freq = Counter(self.cluster_labels)
			freq_cluster = freq.most_common(10)
			top_cluster = [0] * (self.num_class)
			for i in (range(len(freq_cluster))):
				top_cluster[i] = freq.most_common(10)[i][0]


			# Now we compare the rest of the vector with the largest cluster
			for i in range(len(feature_vectors)):
				sim_top = 0
				bmatch[i] = 0

				for j in range(len(top_cluster)):

					# Top cluster does not need to compared to itself
					if ( j in top_cluster) : continue

					aux_cls_hld = np.asarray(aux_cluster[j])
					sim_cos = float(cosine_similarity(feature_vectors[i].reshape(1,-1),
					aux_cls_hld.reshape(1,-1)))
					real_dist = np.sqrt(np.abs(np.sum((feature_vectors[i].__sub__(aux_cls_hld)))))
					sim_dist = np.sqrt(np.abs(np.sum(aux_cluster[j])))
					sim_dist = (sim_dist - real_dist)/(sim_dist)
					sim_score = np.mean([sim_cos,sim_dist])

					# This will return the highest matching cluster
					if (sim_score > sim_top):
						sim_top = sim_score
						bmatch[i] = top_cluster[j]

				# Now we put the vector into one of the top 10 cluster
				self.cluster_labels[i] = bmatch[i]
				print "This vector (",i,") is finally labeled as",self.cluster_labels[i]
			print "Frequent cluster \n",freq_cluster
			print "Top cluster \n",top_cluster



		return self
