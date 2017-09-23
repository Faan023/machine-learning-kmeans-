import csv
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
from tabulate import tabulate
print "This is a demonstration of my implementation of the Kmeans clustering algorithm"
print "The data sets is for birthrate and life expectancy in 1953 and 2008."
         
def read_csv(csvfile):
    with open(csvfile) as readfile:
        rows = csv.reader(readfile)
        content = [row for row in rows]
        return content
inputfile = str(raw_input("Which datafile would you like to use?" + "\n"
                      "enter '1953' for data1953.csv," + "\n"
                      "enter '2008' for data2008.csv," + "\n"
                      "enter 'both' for dataBoth.csv:" + "\n"))
while inputfile not in("1953","2008","both"):
    inputfile = str(raw_input(" File not found. Please make a valid selection"))
if inputfile == "1953":
    data = read_csv("data1953.csv")
elif inputfile == "2008":
    data = read_csv("data2008.csv")
else:
    data = read_csv("dataBoth.csv")
      
data = data[1:]
points = [ i[1:] for i in data]

num = int(raw_input("Enter the amount of clusters you want: "))

num_iter = int(raw_input("How many iterations would you like to do?"))

kmeans = KMeans(n_clusters = num, max_iter = num_iter)
kmeans.fit(points)

centroid = kmeans.cluster_centers_
cluster_name = kmeans.labels_
dist = kmeans.inertia_


    
print "--------------------Centroids are:----------------------------"
print (centroid)

colors =  ['b.', 'g.', 'r.', 'c.', 'm.', 'y.', 'k.', 'w.']
for i in colors:
    while num > len(colors):
        colors.append(i) 

clust_cont = []
for i in range(len(data)):
    clust_cont.append([data[i],"clust" + str(cluster_name[i])])    
    plt.plot(data[i][1],data[i][2],colors[cluster_name[i]],markersize=10)
plt.scatter(centroid[:,0],centroid[:,1], marker = "x", s=150, linewidths = 5, zorder =10)
plt.title("Data " + str(inputfile))
plt.xlabel("Birthrate per 1000")
plt.ylabel("Life expectancy")

clustlist = []
for i in range(num):
    clustlist.append("clust" + str(i))

dct = {key:[] for key in clustlist}
            
dctitems = dct.items()

for i in dctitems:
    for j in clust_cont:
        if i[0] == j[1]:
            i[1].append(j[0])

def get_means(cluster):
    meanbr = []
    meanle = []
    for i in cluster:
        meanbr.append(i[1]) 
        meanle.append(i[2])

    meanbr = sum([float(i) for i in meanbr])/len (meanbr)
    meanle = sum([float(i) for i in meanle])/len(meanle)
    print "The average birthrate per 1000 for this cluster is: " + str(meanbr)
    print "The average life expectancy for this cluster is: " + str(meanle)    


for i in dctitems:
    print "_______________________________The counties in " + i[0] + " are:_____________________"
    print tabulate(i[1],headers = ["Countries", "Birtrate", "Life Expectancy"],tablefmt="grid")
    print "The number of counties in " + i[0] + " are: " + str(len(i[1]))
    get_means(i[1])
plt.show()
        
    
        


