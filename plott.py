import csv
import matplotlib.pyplot as plt

import sys
import numpy as np
import pandas as pd

global today
global minchisq
today = 0



def openFileAll(f):
    global today
    y = 0
    with open(f) as fi:
        reader = csv.reader(fi)
#        y = reader
        next(reader)

        for row in reader:
            if today==0:
                today = len(row)
                y = np.zeros(today)
            for (i,v) in enumerate(row):
                if i>=2:
                    y[i] = float(y[i]) + float(v)
 #               columns[i].append(v)
    return y

def openFileCountry(f,name):
    global today
    y = 0
    with open(f) as fi:
        reader = csv.reader(fi)
#        y = reader
        next(reader)

        for row in reader:
            if today==0:
                today = len(row)
                y = np.zeros(today)
            if (name in row[1]):
                for (i,v) in enumerate(row):
                    if i>=2:
                        y[i] = float(y[i]) + float(v)
 #               columns[i].append(v)
    return y



def calcChisq(d,yy):
    c = 0
    for i in range(len(d)):
        if (i>30):
            c+= pow(d[i]-yy[i],2)
    return c/len(d)/10000000000

start = 0
if len(sys.argv)!=2:
    print("Usage: covidkun.sh [ Country name or 'world' ] ")
    exit(1)
#print 'Number of arguments:', len(sys.argv), 'arguments.'
if (sys.argv[1]=="world"):
    y = openFileAll('data.txt')
    start = 70000

else:
    y = openFileCountry('data.txt',sys.argv[1])

#print(y)
N = today
x = np.linspace(0,N,N)
#y = np.empty(N)    
y2 = np.zeros(N)    


a = 10.3
b=0.14

a = 1

winnerB = 0
winnerS = 0

s = -1.0
b=0.178
#y2 = start + a*np.exp(x*b-s)

SX = 100

BB = np.linspace(0.01,0.80,SX)
SS = np.linspace(-15.0, 10.0,SX)



minchisq = 10000000


for b in BB:
    for s in SS:
        y2 = start + a*np.exp(x*b-s)
        chisq = calcChisq(y,y2)
#        print(str(chisq) + " , " + str(b) + " , "+str(s))
        if (chisq<minchisq):
            winnerB = b
            winnerS = s
            minchisq = chisq
#            print(str(b) + " , " +str(s)+ " : " + str(chisq))

print("Winner: s = "+str(winnerS) + " , b = "+str(winnerB))



y2 = np.zeros(N)    

y2 = start + np.exp(x*winnerB-winnerS)


plt.plot(x,y)
plt.plot(x,y2)
plt.ylabel('Time')
plt.show()

N = 200
x = np.linspace(0,N,N)
y2 = start + np.exp(x*winnerB-winnerS)


for i in range(32):
    print("In "+str(i)+" days: "+str(int(y2[today+i])))


