import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfinv 
import random

    

def brownianwalk2d(T):
    x = np.zeros((T))
    y = np.zeros((T))
    for t in range(0,T):
        angle = 2*np.pi*random.random()
        x[t] = np.cos(walk)+x[t-1]
        y[t] = np.sin(walk)+y[t-1]
    return x, y

def gaussianwalk2d(T):
    
   x = np.zeros((T))
   y = np.zeros((T))
   p = np.zeros((T))
   for t in range(0,T):
      phase = (1-2*random.random())
      angle = 2*np.pi*random.random()
      r=erfinv(phase)
      x[t]=r*np.cos(angle)+x[t-1]
      y[t]=r*np.sin(angle)+y[t-1]
      p[t]=r
   return x,y,p

#x, y = brownianwalk2d(1000)

def cauchywalk2d(T):
   x = np.zeros((T))
   y = np.zeros((T))
   p = np.zeros((T))
   for t in range(0,T):
      angle1 = np.pi*(1-2*random.random())
      angle2 = 2*np.pi*random.random()
      #print( angle1-angle2)
      r=np.tan(angle1)
      x[t]=r*np.cos(angle2)+x[t-1]
      y[t]=r*np.sin(angle2)+y[t-1]
      p[t]=r
   return x,y,p

#x, y = brownianwalk2d(1000)
x, y,p = cauchywalk2d(10000)
#x,y,p=gaussianwalk2d(100000)
# create a figure
fig = plt.figure()
# create a plot into the figure
ax = fig.add_subplot(111)
# plot the data
ax.plot(x,y)
plt.show()
#print(np.shape(p))

leftbin=-500
rightbin=500
bincount=10000

bins=np.linspace(leftbin,rightbin,bincount)
n,bins,patches = plt.hist(p,bins,normed=1,histtype='stepfilled')
#plt.plot(bins)
#print(bins)
y=np.zeros((bincount))
z=np.zeros((bincount))
for i in range(0,bincount):

  y[i]=1/(1+bins[i]*bins[i])/np.pi
for i in range(0,bincount):
  z[i]=1/(np.sqrt(2*np.pi))*np.exp(-bins[i]*bins[i]/2.0)

plt.plot(bins,y,'r--',linewidth=1.5)
plt.plot(bins,z,'r--',linewidth=2.5)
plt.show()
