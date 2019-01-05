import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

label_font = {
    'color': 'c',
    'size': 10,
}


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 准备数据
r=100/2
R=267.4/2
deta1=5
deta2=5
G=1
afa1=30
L=15
theta=range(0,360,1)
x=map(lambda p:r*math.cos(p/180*3.1415),theta)
y=map(lambda p:r*math.sin(p/180*3.1415),theta)
z=map(lambda p:math.sqrt(R*R-r*r*math.sin(p/180*3.1415)*math.sin(p/180*3.1415)),theta)

x1=map(lambda p:(r-deta2)*math.cos(p/180*3.1415),theta)
y1=map(lambda p:(r-deta2)*math.sin(p/180*3.1415),theta)
z1=map(lambda p:math.sqrt(R*R-(r-deta2)*(r-deta2)*math.sin(p/180*3.1415)*math.sin(p/180*3.1415)),theta)

x2=map(lambda p:(r-deta2)*math.cos(p/180*3.1415),theta)
y2=map(lambda p:(r-deta2)*math.sin(p/180*3.1415),theta)
z2=map(lambda p:math.sqrt(R*R-(r-deta2)*(r-deta2)*math.sin(p/180*3.1415)*math.sin(p/180*3.1415))+G,theta)

x3=map(lambda p:r*math.cos(p/180*3.1415),theta)
y3=map(lambda p:r*math.sin(p/180*3.1415),theta)
z3=map(lambda p:math.sqrt(R*R-(r-deta2)*(r-deta2)*math.sin(p/180*3.1415)*math.sin(p/180*3.1415))+G+deta2*math.tan(afa1*3.1415/180),theta)

x4=map(lambda p:(r+L)*math.cos(p/180*3.1415),theta)
y4=map(lambda p:(r+L)*math.sin(p/180*3.1415),theta)
z4=map(lambda p:math.sqrt(R*R-(r+L)*(r+L)*math.sin(p/180*3.1415)*math.sin(p/180*3.1415)),theta)

# 用5个颜色画了5圈曲线

ax.scatter(list(x), list(y), list(z), c='r')
ax.scatter(list(x1),list(y1),list(z1),c='b')
ax.scatter(list(x2),list(y2),list(z2),c='g')
ax.scatter(list(x3),list(y3),list(z3),c='y')
ax.scatter(list(x4),list(y4),list(z4),c='violet')

ax.set_xlabel("X axis", fontdict=label_font)
ax.set_ylabel("Y axis", fontdict=label_font)
ax.set_zlabel("Z axis", fontdict=label_font)
ax.set_title("Renyuan", alpha=0.6, color="b", size=10)
ax.legend(loc="upper left")

plt.show()