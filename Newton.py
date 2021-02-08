import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
import random

fig = plt.figure()
ax = plt.axes()

#初期条件
N=7
x=[random.uniform(-5e11,5e11) for i in range(N)]
y=[random.uniform(-5e11,5e11) for i in range(N)]
vx=[random.uniform(-2e4,2e4) for i in range(N)]
vy=[random.uniform(-2e4,2e4) for i in range(N)]
m=[10**random.uniform(20,32) for i in range(N)]
logm=[]
K=6e-11
T=1000
ax=[[] for i in range(N)]
ay=[[] for i in range(N)]
ims=[]
def dist(x1,y1,x2,y2):
    return ((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

for i in range(N):
    logm.append(math.log(m[i]))

for i in range(200000):
    for j in range(N):
        x[j]+=vx[j]*T
        y[j]+=vy[j]*T
        ax[j].append(x[j])
        ay[j].append(y[j])
    for j in range (N):
        for k in range(N):
            if(j==k):
                continue
            L=dist(x[j],y[j],x[k],y[k])
            F=m[j]*K*m[k]/L
            theta=math.atan2(y[k]-y[j],x[k]-x[j])
            vx[j]+=(x[k]-x[j])/math.sqrt(L)*(F/m[j])*T
            vy[j]+=(y[k]-y[j])/math.sqrt(L)*(F/m[j])*T

for i in range(N):
    plt.scatter(ax[i],ay[i],logm[i],marker=".")
plt.xlim(-1e13,1e13)
plt.ylim(-1e13,1e13)

plt.show()