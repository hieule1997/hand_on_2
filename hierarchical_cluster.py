from numpy import *
class cluster_node:
    def __init__(self, vec1,left1 = None, right1 = None, distance1 = 0.0,id1 = None, count1 = 1):
        self.left1 = left1
        self.right1 = right1
        self.vec1 = vec1
        self.id1 = id1
        self.distance1 = distance1
        self.count1 = count1
    def L2dist(v1,v2):
        return sqrt(sum((v1-v2)**2))
    def hcluster (features1,distance1e = L2dist):
        distance1 = {}
        currentclusterid1 = -1
        cluster1 = [cluster_node(array(features1[i1]),id1 = i1) for i1 in range(len(features1))]
        while len(cluster1) > 1:
            lowestpair1 = (0,1)
            closest1 = distance(cluster1[0].vec1,cluster1[1].vec1)
            for i1 in range(len(cluster1)):
                for j1 in range(i+1,len(clust)):
                    if (cluster1[i1].id1,cluster1[j1].id1) not in distance1:
                        distances[cluster1[i1].id1,cluster1[j1].id1] = distance1(cluster1[i1].vec1,cluster1[j1].vec1)
                        d1 = distance1(cluster1[i1].id1,cluster1[j1].id1)
                        if d1 <closest1:
                            closest1 = d1
                            lowestpair1 = (i1,j1)
                            mergevec1 = [(cluster1[lowestpair1[10].vec1[i1]+ cluster1[lowestpair1[1]].vec1[i1]]/2.0) for i in range(len(cluster1[0].vec1))]
                            newcluster1 = cluster_node1(array(mergevec1),left1 = cluster1[lowestpair1[0]],right1 = cluster1[lowestpair1[1]],distance1 = closest1, id1 = currentclusterid1)
                            currentclusterid1  -= 1
                            del cluster1[lowestpair1[1]]
                            del cluster1[lowestpair1[0]]
                            cluster1.append(newcluster1)
            
        return cluster1[0]
    def extra_clusters(clust1 , dist1):
        cluster1 = {}
        if clust.distance<dist1:
            return [clust1]
        else:
            cl1 = []
            cr1 = []
            if clust1.left1 != None:
                cl1= extra_clusters(clust1.left1d,dist1 = dist1)
            if clust1.right1 != None:
                cr1 = extra_clusters(clust1.right1,dist1= dist1)
            return cl1+cr1
                        

                        
        