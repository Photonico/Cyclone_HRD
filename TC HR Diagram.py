# Name:     HR Diagram for Category 5 Tropical Cyclone: Main
# Author:   ErHai, ConAntares
# Update:   20171123

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import LinearLocator, FormatStrFormatter  
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 10))
ax = Axes3D(fig)
#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Index of Wind
Wo=100
W140=Wo
W145=W140+Wo
W150=W145+Wo
W155=W150+Wo
W160=W155+Wo
W165=W160+Wo
W170=W165+Wo
W175=W170+Wo
W180=W175+Wo
W185=W180+Wo
W190=W185+Wo
W195=W190+Wo
W200=W195+Wo

# Index of Pressure # RBG and Light
#Brown
P955='#000000'  # 000,000,000   # 00
P950='#3C281E'  # 060,040,030   # 18
P945='#643C32'  # 100,060,050   # 30
P940='#9B5F4B'  # 155,095,075   # 47
#Red
P935='#B98764'  # 185,135,100   # 61
P930='#A00000'  # 160,000,000   # 34
P925='#BE190f'  # 190,025,015   # 42
P920='#DC5028'  # 220,080,040   # 54
#Orange and Yellow
P915='#FA6E00'  # 250,110,000   # 64
P910='#FF9B00'  # 255,155,000   # 73
P905='#FFDC00'  # 255,220,000   # 89
P900='#FFFA73'  # 255,250,115   # 97
#Blue
P895='#96FAFF'  # 150,250,255   # 92
P890='#64BEDC'  # 100,190,220   # 72
P885='#3282C4'  # 050,130,196   # 52
P880='#004BA0'  # 000,075,160   # 32
#Purple and Violet
P875='#7337A0'  # 115,055,160   # 35
P870='#965FC3'  # 150,095,195   # 50
P865='#B484E1'  # 180,132,225   # 63
P860='#D2AAFF'  # 210,170,255   # 76
#White
P855='#F0DCFF'  # 240,220,255   # 90
P850='#FFFFFF'  # 255,255,255   # 100
# Credibility
C1=0.50
C2=0.75
C3=1.00

# x: CDO Radius; y: Eye Radius; z: Chara Temp

#### West Pacific Ocean
# 2013 Haiyan
ax.scatter(800,24,120,s=W190,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

#### Central Pacific Ocean
##### East Pacific Ocean
# 2015 Patricia
ax.scatter(1200,6,110,s=W185,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

##### South Pacific Ocean
##### North Indian Ocean
##### South Indian Ocean
##### North Atlantic
ax.scatter(1000,20,100,s=W160,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(1005,15,105,s=W175,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(1010,30,110,s=W140,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.view_init(15, -120)

# x-axis: Gale Radius
ax.set_xlabel(r'Gale Radius (Km)', family='serif', fontsize=16)
ax.set_xlim3d(200, 2000)
ax.set_xticks([200,400,600,800,1000,1200,1400,1600,1800,2000])
# y-axis: Eye Radius
ax.set_ylabel(r'Eye Radius (Km)', family='serif', fontsize=16)
ax.set_ylim3d(0, 50)
ax.set_yticks([0,10,20,30,40,50])
# z-axis: Temperature Difference betweem Eye and CDO
ax.set_zlabel(r'Temperature Difference (K)', family='serif', fontsize=16)
ax.set_zlim3d(80, 120)
ax.set_zticks([80,85,90,95,100,105,110,115,120])

plt.savefig('TC HR.pdf', dpi=1024)
plt.savefig('TC HR.png', dpi=1024)
plt.savefig('TC HR Small.png', dpi=64)
plt.show()