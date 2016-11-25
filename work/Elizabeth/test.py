from sklearn import datasets, metrics
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

digits = datasets.load_digits()

feature_vectors = digits.data[:]
min_sim = 0.9


sim_list = []
counts = [0]*len(feature_vectors)
for i in range(len(feature_vectors)):
        for j in range(len(feature_vectors)):
                sim = float(cosine_similarity(feature_vectors[i].reshape(1,-1),feature_vectors[j].reshape(1,-1)))
                sim_list.append((i,j,sim))
                if sim > min_sim:
                        counts[i] += 1

# Sort counts descending from max, and returns list of indices            
s_counts = sorted(range(len(counts)), key=lambda k: counts[k], reverse=True)

s_counts_short = s_counts[:]
sim_dict = {sublist[0:2]: sublist[2] for sublist in sim_list}
seeds = s_counts[:10]

print seeds
for i in seeds:
#    for j in seeds:
#        print i, j, sim_dict[(i,j)]
    print counts[i]

incomplete = True
# Remove seeds if part of same cluster, until we have 10 "unique" seeds
while incomplete:
    for item in seeds:
        for i in range(len(seeds)):
            #print item, seeds[i], sim_dict[(item,seeds[i])]
            if sim_dict[(item,seeds[i])] > min_sim and item != seeds[i]:
                s_counts_short.remove(item)
                #print "bigger than 0.8\n"
                #seeds = s_counts_short[:i]
                break
    if seeds == s_counts_short[:10]:
        #print "false"
        incomplete = False
    else:
        seeds = s_counts_short[:10]

print seeds
for i in seeds:
    #for j in seeds:
    #    print i, j, sim_dict[(i,j)]
    print counts[i]


# Labeling clusters
cluster_labels = [0] * len(feature_vectors)
largest = 0

for i in range(len(feature_vectors)):
    for j, item in enumerate(seeds):
        if sim_dict[(item,i)] > sim_dict[(seeds[largest],i)]:
            largest = j
    cluster_labels[i] = largest


#for i in range(len(feature_vectors)):
#    for j, item in enumerate(seeds):
#        if sim_dict[(item,i)] > min_sim:
#            cluster_labels[i] = j
#            break
#        else:
#            cluster_labels[i] = 999
print cluster_labels[1300:1600]
