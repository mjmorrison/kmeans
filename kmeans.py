import math

# define any needed variables
iterations_max = 0
iteration_count = 1 # iteration count set to start at 1 to account for the first iteration not counted in loop
points_num = 0
clusters_total = 0
points = []
x_values = []
y_values = []
coordinates = []
clusters = [[],[],[],[]]

# read and parse all fields from input file and initialize variables
f = open("/Users/michaelmorrison/Desktop/points.txt","r")
iterations_max = int(f.readline())
points_num = int(f.readline())
clusters_total = int(f.readline())
c1_index = int(f.readline())
c2_index = int(f.readline())
c3_index = int(f.readline())
c4_index = int(f.readline())
points = f.readlines()

# split provided coordinates into x and y values and then convert to int
for i in range(len(points)):
    split_list = points[i].split(",")
    x_values.append(int(split_list[0]))
    y_values.append(int(split_list[1]))
    coordinates.append([x_values[i],y_values[i]])

# aggregate x and y values back into a single list with all values of type int

# use the provided indicies to pull out the centroid's points from the coordinates list
centroids = [[coordinates[c1_index][0],coordinates[c1_index][1]],[coordinates[c2_index][0],coordinates[c2_index][1]],
             [coordinates[c3_index][0],coordinates[c3_index][1]],[coordinates[c4_index][0],coordinates[c4_index][1]]]

# for number of iterations in input file
for i in range(iterations_max):
    # for each point in the input file
    for j in range(len(coordinates)):
        # calculate distance between current point and all k centroids
        d_1 = (coordinates[j][0]-centroids[0][0])**2 + (coordinates[j][1]-centroids[0][1])**2
        d_1 = math.sqrt(d_1)
        d_2 = (coordinates[j][0]-centroids[1][0])**2 + (coordinates[j][1]-centroids[1][1])**2
        d_2 = math.sqrt(d_2)
        d_3 = (coordinates[j][0]-centroids[2][0])**2 + (coordinates[j][1]-centroids[2][1])**2
        d_3 = math.sqrt(d_3)
        d_4 = (coordinates[j][0]-centroids[3][0])**2 + (coordinates[j][1]-centroids[3][1])**2
        d_4 = math.sqrt(d_4)

        # assign point to the cluster with the nearest centroid
        if d_1 < d_2 and d_1 < d_3 and d_1 < d_4:
            clusters[0].append([coordinates[j][0],coordinates[j][1]])
        elif d_2 < d_1 and d_2 < d_3 and d_2 < d_4:
            clusters[1].append([coordinates[j][0],coordinates[j][1]])
        elif d_3 < d_1 and d_3 < d_2 and d_1 < d_4:
            clusters[2].append([coordinates[j][0],coordinates[j][1]])
        else:
            clusters[3].append([coordinates[j][0],coordinates[j][1]])

    # check if any points have changed clusters and update the iteration count if necessary
    if i > 0:
        if c1_prev != len(clusters[0]) or c2_prev != len(clusters[1]) or c3_prev != len(clusters[2]) or c4_prev != len(clusters[3]):
            iteration_count += 1
        else:
            pass
    else:
        pass

    # calculate cluster mean x/y and update centroid for each cluster
    for k in range(len(clusters)):
        x_values = [x[0] for x in clusters[k]]
        y_values = [x[1] for x in clusters[k]]
        x_mean = sum(x_values) / len(x_values)
        y_mean = sum(y_values) / len(y_values)
        centroids[k] = ([x_mean, y_mean])

    coordinates[c1_index] = centroids[0]
    coordinates[c2_index] = centroids[1]
    coordinates[c3_index] = centroids[2]
    coordinates[c4_index] = centroids[3]

    # save current cluster sizes (for comparison in next iteration)
    c1_prev = len(clusters[0])
    c2_prev = len(clusters[1])
    c3_prev = len(clusters[2])
    c4_prev = len(clusters[3])

    # empty clusters for re-clustering except on final iteration
    if i < iterations_max - 1:
        for i in range(clusters_total):
            clusters[i] = []
    else:
        pass

# output results in specified format
print(f"Iterations to achieve stability: {iteration_count}\nCentroid 0: {centroids[0]}\n\
Number of points in Cluster 0: {len(clusters[0])}\nCluster 0: {clusters[0]}\nCentroid 1: {centroids[1]}\n\
Number of points in Cluster 1: {len(clusters[1])}\nCluster 1: {clusters[1]}\n\
Centroid 2: {centroids[2]}\nNumber of points in Cluster 2: {len(clusters[2])}\nCluster 2: {clusters[2]}\n\
Centroid 3: {centroids[3]}\nNumber of points in Cluster 3: {len(clusters[3])}\nCluster 3: {clusters[3]}")