import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import scipy
from math import hypot
from numpy.linalg import norm
from scipy.spatial import distance

class HOMLClusterAlgo(object):
		# Algorithm for Clustering
		# initialize 1st cluster (put first vector into cluster)
		# update aux cluster
		#
		# do rest of the samples
		# 	do for all aux cluster
		# 		check cosine values ONLY
		#		check dist solved, now what to do
		# 		assign a value that shows the fitting of the cluster
		#		if cos is higher than threshold
		#
		# print number of clusters
		# combine cluster # original idea
		#
		#
		# # optimization option
		# # generative clustering may be heavy as cluster increases
		# # solution 1: create a lower threshold value
		# #	less clusters, but less accurate
		# # solution 2: combine cluster when cluster reaches x (say 15)
		# #	quicker, less accurate, but not as bad as solution 1



	def __init__(self, cluster_labels, num_class, threshold_value):
		self.cluster_labels = None				# cluster labels
		self.num_class = num_class				# number of classifier
		self.threshold_value = threshold_value 	# threshold_value
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
		aux_cluster = [0] * len(feature_vectors)
		aux_cluster[0] = feature_vectors[0] # 1st aux cluster is 1st vector

		for i in range(1,len(feature_vectors)): # do all vector from 1
			new_tres = 0
			print "feature_vectors length", len(feature_vectors)
			print "Doing feature_vectors",i,"out of",len(feature_vectors)
			for j in range(len(aux_cluster)):	# do all current aux cluster

				print "Doing aux cluster",j,"out of",len(aux_cluster)
				if np.all(aux_cluster[j] == 0) :
					print "There are no more aux cluster! Break!"
					break # no more aux cluster to compare
				aux_cls_hld = np.asarray(aux_cluster[j])

				# this is for checking cosine
				sim_cos = float(cosine_similarity(feature_vectors[i].reshape(1,-1),aux_cls_hld.reshape(1,-1))) # check cosine
				# this is for checking distance
				real_dist = np.sqrt(np.abs(np.sum((feature_vectors[i].__sub__(aux_cls_hld)))))
				sim_dist = np.sqrt(np.abs(np.sum(aux_cluster[j])))
				sim_dist = (sim_dist - real_dist)/(sim_dist)
				# mean of both similarity score
				sim_score = np.mean([sim_cos,sim_dist])
				print "Distance similarity", sim_dist
				print "Cosine similarity", sim_cos
				print "Average similarity", sim_score
				print ("-")*10

				if sim_score >= self.threshold_value:
					if sim_score > new_tres: self.cluster_labels[i]=j
					new_tres = sim_score
				else:
					add_aux = 0
					for k in range(len(aux_cluster)):
						add_aux += k
						if np.all(aux_cluster[k] == 0): break
					print add_aux
					aux_cluster[add_aux] = feature_vectors[i]

			print self.cluster_labels[i]

		return self
