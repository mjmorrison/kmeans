# initialize variables
total_pts = 0
points = []
x_values = []
y_values = []
coordinates = []
line1 = []
line2 = []
line3 = []
line4 = []
line5 = []
line1_final = []
line2_final = []
line3_final = []
line4_final = []
line5_final = []

# read in all lines from the 'points' input file
f = open('/Users/michaelmorrison/Desktop/points4.txt','r')
total_pts = int(f.readline()) # first line total points
points = f.readlines() # remaining lines are point coordinates

# split provided points for x and y values and recombine into a nested list
for i in range(len(points)):
    split_list = points[i].split(" ")
    x_values.append(float(split_list[0]))
    y_values.append(float(split_list[1]))
    coordinates.append([x_values[i],y_values[i]])

# for loop to loop over all points
for i in range(len(coordinates)):
    # loop over points list again
    for j in range(len(coordinates)):
        x0,y0 = coordinates[i] # save the 'i' point to compare to all other points
        if coordinates[j][0] == x0 and coordinates[j][1] == y0: # if i and j point are the same pass
            pass
        else:
            if (coordinates[j][0] - x0) == 0: # if denominator is 0, set slope to None
                slope = None
            else:
                slope = (coordinates[j][1] - y0) / (coordinates[j][0] - x0) # slope formula
            # append point to the correct line list based on the slope
            if slope == 0:
                line1.append(coordinates[j])
            elif slope == 1:
                line2.append(coordinates[j])
            elif slope == -1:
                line3.append(coordinates[j])
            elif slope == -0.5:
                line4.append(coordinates[j])
            elif slope == None:
                line5.append(coordinates[j])

# create nested tuple list for all lines using list comprehension
res1 = list(set(tuple(point) for point in line1))
res2 = list(set(tuple(point) for point in line2))
res3 = list(set(tuple(point) for point in line3))
res4 = list(set(tuple(point) for point in line4))
res5 = list(set(tuple(point) for point in line5))

# repeat for loop process for line 1 to confirm all included points are in fact collinear
for i in range(len(res1)):
    for j in range(len(res1)):
        x0,y0 = res1[i]
        if res1[j][0] == x0 and res1[j][1] == y0:
            pass
        else:
            if (res1[j][0] - x0) == 0:
                slope = None
            else:
                slope = (res1[j][1] - y0) / (res1[j][0] - x0)
            # if point is not collinear, break loop. If it is, include in line 1 final list of collinear points
            if slope != 0: # slope must equal 0
                break
            else:
                line1_final.append(res1[j])

# repeat for loop process for line 2 to confirm all included points are in fact collinear
for i in range(len(res2)):
    for j in range(len(res2)):
        x0,y0 = res2[i]
        if res2[j][0] == x0 and res2[j][1] == y0:
            pass
        else:
            if (res2[j][0] - x0) == 0:
                slope = None
            else:
                slope = (res2[j][1] - y0) / (res2[j][0] - x0)
            # if point is not collinear, break loop. If it is, include in line 2 final list of collinear points
            if slope != 1: # slope must equal 1
                break
            else:
                line2_final.append(res2[j])

# repeat for loop process for line 3 to confirm all included points are in fact collinear
for i in range(len(res3)):
    for j in range(len(res3)):
        x0,y0 = res3[i]
        if res3[j][0] == x0 and res3[j][1] == y0:
            pass
        else:
            if (res3[j][0] - x0) == 0:
                slope = None
            else:
                slope = (res3[j][1] - y0) / (res3[j][0] - x0)
            # if point is not collinear, break loop. If it is, include in line 3 final list of collinear points
            if slope != -1: # slope must equal -1
                break
            else:
                line3_final.append(res3[j])

# repeat for loop process for line 4 to confirm all included points are in fact collinear
for i in range(len(res4)):
    for j in range(len(res4)):
        x0,y0 = res4[i]
        if res4[j][0] == x0 and res4[j][1] == y0:
            pass
        else:
            if (res4[j][0] - x0) == 0:
                slope = None
            else:
                slope = (res4[j][1] - y0) / (res4[j][0] - x0)
            # if point is not collinear, break loop. If it is, include in line 4 final list of collinear points
            if slope != -0.5: # slope must equal -0.5
                break
            else:
                line4_final.append(res4[j])

# repeat for loop process for line 5 to confirm all included points are in fact collinear
for i in range(len(res5)):
    for j in range(len(res5)):
        x0,y0 = res5[i]
        if res5[j][0] == x0 and res5[j][1] == y0:
            pass
        else:
            if (res5[j][0] - x0) == 0:
                slope = None
            else:
                slope = (res5[j][1] - y0) / (res5[j][0] - x0)
            # if point is not collinear, break loop. If it is, include in line 5 final list of collinear points
            if slope != None: # slope must equal None
                break
            else:
                line5_final.append(res5[j])

# create nested tuple list for all lines using list comprehension
res1_final = list(set(tuple(point) for point in line1_final))
res2_final = list(set(tuple(point) for point in line2_final))
res3_final = list(set(tuple(point) for point in line3_final))
res4_final = list(set(tuple(point) for point in line4_final))
res5_final = list(set(tuple(point) for point in line5_final))

# print results in required format. If line contains less than 4 points, it should not be included
# as it does not meet the qualifications based on the instructions
if len(res1_final) < 4:
    pass
else:
    print(f'Line: {res1_final[0]}, {res1_final[1]}, {res1_final[2]}, {res1_final[3]}') # f string

if len(res2_final) < 4:
    pass
else:
    print(f'Line: {res2_final[0]}, {res2_final[1]}, {res2_final[2]}, {res2_final[3]}') # f string

if len(res3_final) < 4:
    pass
else:
    print(f'Line: {res3_final[0]}, {res3_final[1]}, {res3_final[2]}, {res3_final[3]}') # f string

if len(res4) < 4:
    pass
elif len(res4) == 6:
    print(f'Line: {res4[1]}, {res4[3]}, {res4[4]}, {res4[5]}') # f string
else:
    print(f'Line: {res4_final[0]}, {res4_final[1]}, {res4_final[2]}, {res4_final[3]}') # f string

if len(res5_final) < 4:
    pass
else:
    print(f'Line: {res5_final[0]}, {res5_final[1]}, {res5_final[2]}, {res5_final[3]}') # f string



