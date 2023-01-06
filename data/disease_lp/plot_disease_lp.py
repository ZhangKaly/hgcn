import matplotlib.pyplot as plt
import csv
import sys
  
x = []
y = []

#sys.path.append("data/disease_lp/")
  
with open('disease_lp.edges.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
plt.scatter(x,y)
plt.savefig("disease_lp.jpg")