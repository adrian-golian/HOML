import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class HOMLClusterAlgo(object):
#"""
#	This is a template for a clustering model class.
#	Build the functions required.
#"""

    def __init__(self, cluster_labels, min_sim, num_seeds):
        self.cluster_labels = None
        self.min_sim = min_sim
        self.num_seeds = num_seeds
        #self.exclude = exclude
        pass

    def fit(self, feature_vectors):
#	"""
#		This method receives the objects to cluster
#		and finds the assigned cluster labels.

#		--- Explain any function arguments ---

#	"""

	# Typecheck the input data
	if not isinstance(feature_vectors, (np.ndarray, list)):
		raise TypeError("Feature vectors not numpy arrays.")

	self.cluster_labels = [0] * len(feature_vectors) # Replace this with actual computation
	
	sim_list = []
	counts = [0]*len(feature_vectors)
	for i in range(len(feature_vectors)):
	    for j in range(len(feature_vectors)):
	        sim = float(cosine_similarity(feature_vectors[i].reshape(1,-1),feature_vectors[j].reshape(1,-1)))
	        sim_list.append((i,j,sim))
		if sim > self.min_sim:
		    counts[i] += 1

        # Sort counts descending from max, and returns list of indices            
        s_counts = sorted(range(len(counts)), key=lambda k: counts[k], reverse=True)

        s_counts_short = s_counts[:]
        sim_dict = {sublist[0:2]: sublist[2] for sublist in sim_list}
        seeds = s_counts[:self.num_seeds]

        # Remove seeds if part of same cluster (within min_sim), until we have 10 "unique" seeds
        incomplete = True
        while incomplete:
            for item in seeds:
                for i in range(len(seeds)):
                    if sim_dict[(item,seeds[i])] > self.min_sim and item != seeds[i]:
                        s_counts_short.remove(item)
                        break
            if seeds == s_counts_short[:self.num_seeds]:
                incomplete = False
            else:
                seeds = s_counts_short[:self.num_seeds]

        # Labeling clusters
        largest = 0

        for i in range(len(feature_vectors)):
            for j, item in enumerate(seeds):
                if sim_dict[(item,i)] > sim_dict[(seeds[largest],i)]:
                    largest = j
            self.cluster_labels[i] = largest

        return self
