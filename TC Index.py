# Name:     HR Diagram for Category 5 Tropical Cyclone: Index
# Author:   ErHai, ConAntares
# Update:   20171123

import matplotlib
import numpy as np
import pylab

from matplotlib import colors
from matplotlib import pyplot as plt
from matplotlib import rc

fig, ax = plt.subplots(figsize=(12, 6))
#plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#plt.grid()

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

ax.scatter(140,950,s=W140,color=P950,alpha=C3,edgecolor="#E0E0F0",cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,950,s=W145,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,950,s=W150,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,950,s=W155,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,950,s=W160,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,950,s=W165,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,950,s=W170,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,950,s=W175,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,950,s=W180,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,950,s=W185,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,950,s=W190,color=P950,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,950,s=W195,color=P950,alpha=C3,edgecolor="#E0E0F0",cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,950,s=W200,color=P950,alpha=C3,edgecolor="#E0E0F0",cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,945,s=W140,color=P945,alpha=C3,edgecolor="#E0E0F0",cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,945,s=W145,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,945,s=W150,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,945,s=W155,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,945,s=W160,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,945,s=W165,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,945,s=W170,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,945,s=W175,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,945,s=W180,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,945,s=W185,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,945,s=W190,color=P945,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,945,s=W195,color=P945,alpha=C3,edgecolor="#E0E0F0",cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,945,s=W200,color=P945,alpha=C3,edgecolor="#E0E0F0",cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,940,s=W140,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,940,s=W145,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,940,s=W150,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,940,s=W155,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,940,s=W160,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,940,s=W165,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,940,s=W170,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,940,s=W175,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,940,s=W180,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,940,s=W185,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,940,s=W190,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,940,s=W195,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,940,s=W200,color=P940,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,935,s=W140,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,935,s=W145,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,935,s=W150,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,935,s=W155,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,935,s=W160,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,935,s=W165,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,935,s=W170,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,935,s=W175,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,935,s=W180,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,935,s=W185,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,935,s=W190,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,935,s=W195,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,935,s=W200,color=P935,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,930,s=W140,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,930,s=W145,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,930,s=W150,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,930,s=W155,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,930,s=W160,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,930,s=W165,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,930,s=W170,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,930,s=W175,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,930,s=W180,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,930,s=W185,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,930,s=W190,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,930,s=W195,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,930,s=W200,color=P930,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,925,s=W140,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,925,s=W145,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,925,s=W150,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,925,s=W155,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,925,s=W160,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,925,s=W165,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,925,s=W170,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,925,s=W175,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,925,s=W180,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,925,s=W185,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,925,s=W190,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,925,s=W195,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,925,s=W200,color=P925,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,920,s=W140,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,920,s=W145,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,920,s=W150,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,920,s=W155,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,920,s=W160,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,920,s=W165,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,920,s=W170,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,920,s=W175,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,920,s=W180,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,920,s=W185,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,920,s=W190,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,920,s=W195,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,920,s=W200,color=P920,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,915,s=W140,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,915,s=W145,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,915,s=W150,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,915,s=W155,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,915,s=W160,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,915,s=W165,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,915,s=W170,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,915,s=W175,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,915,s=W180,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,915,s=W185,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,915,s=W190,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,915,s=W195,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,915,s=W200,color=P915,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,910,s=W140,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,910,s=W145,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,910,s=W150,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,910,s=W155,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,910,s=W160,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,910,s=W165,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,910,s=W170,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,910,s=W175,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,910,s=W180,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,910,s=W185,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,910,s=W190,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,910,s=W195,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,910,s=W200,color=P910,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,905,s=W140,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,905,s=W145,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,905,s=W150,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,905,s=W155,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,905,s=W160,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,905,s=W165,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,905,s=W170,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,905,s=W175,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,905,s=W180,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,905,s=W185,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,905,s=W190,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,905,s=W195,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,905,s=W200,color=P905,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,900,s=W140,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,900,s=W145,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,900,s=W150,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,900,s=W155,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,900,s=W160,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,900,s=W165,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,900,s=W170,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,900,s=W175,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,900,s=W180,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,900,s=W185,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,900,s=W190,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,900,s=W195,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,900,s=W200,color=P900,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,895,s=W140,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,895,s=W145,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,895,s=W150,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,895,s=W155,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,895,s=W160,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,895,s=W165,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,895,s=W170,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,895,s=W175,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,895,s=W180,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,895,s=W185,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,895,s=W190,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,895,s=W195,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,895,s=W200,color=P895,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,890,s=W140,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,890,s=W145,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,890,s=W150,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,890,s=W155,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,890,s=W160,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,890,s=W165,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,890,s=W170,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,890,s=W175,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,890,s=W180,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,890,s=W185,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,890,s=W190,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,890,s=W195,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,890,s=W200,color=P890,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,885,s=W140,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,885,s=W145,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,885,s=W150,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,885,s=W155,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,885,s=W160,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,885,s=W165,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,885,s=W170,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,885,s=W175,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,885,s=W180,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,885,s=W185,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,885,s=W190,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,885,s=W195,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,885,s=W200,color=P885,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,880,s=W140,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,880,s=W145,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,880,s=W150,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,880,s=W155,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,880,s=W160,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,880,s=W165,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,880,s=W170,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,880,s=W175,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,880,s=W180,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,880,s=W185,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,880,s=W190,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,880,s=W195,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,880,s=W200,color=P880,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,875,s=W140,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,875,s=W145,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,875,s=W150,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,875,s=W155,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,875,s=W160,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,875,s=W165,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,875,s=W170,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,875,s=W175,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,875,s=W180,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,875,s=W185,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,875,s=W190,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,875,s=W195,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,875,s=W200,color=P875,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,870,s=W140,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,870,s=W145,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,870,s=W150,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,870,s=W155,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,870,s=W160,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,870,s=W165,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,870,s=W170,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,870,s=W175,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,870,s=W180,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,870,s=W185,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,870,s=W190,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,870,s=W195,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,870,s=W200,color=P870,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,865,s=W140,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,865,s=W145,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,865,s=W150,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,865,s=W155,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,865,s=W160,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,865,s=W165,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,865,s=W170,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,865,s=W175,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,865,s=W180,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,865,s=W185,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,865,s=W190,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,865,s=W195,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,865,s=W200,color=P865,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,860,s=W140,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,860,s=W145,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,860,s=W150,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,860,s=W155,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,860,s=W160,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,860,s=W165,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,860,s=W170,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,860,s=W175,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,860,s=W180,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,860,s=W185,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,860,s=W190,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,860,s=W195,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,860,s=W200,color=P860,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,855,s=W140,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,855,s=W145,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,855,s=W150,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,855,s=W155,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,855,s=W160,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,855,s=W165,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,855,s=W170,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,855,s=W175,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,855,s=W180,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,855,s=W185,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,855,s=W190,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,855,s=W195,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,855,s=W200,color=P855,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

ax.scatter(140,850,s=W140,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(145,850,s=W145,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(150,850,s=W150,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(155,850,s=W155,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(160,850,s=W160,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(165,850,s=W165,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(170,850,s=W170,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(175,850,s=W175,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(180,850,s=W180,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(185,850,s=W185,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(190,850,s=W190,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(195,850,s=W195,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')
ax.scatter(200,850,s=W200,color=P850,alpha=C3,edgecolor='#E0E0F0',cmap=1.0,norm=1.0,marker='o')

# x-axis: Wind Speed (knot)
ax.set_xlabel(r'Intensity (knot)', family='serif', fontsize=16)
ax.set_xlim(135,205)
ax.set_xticks([140,145,150,155,160,165,170,175,180,185,190,195,200])
# y-axis: Pressure (hPa)
ax.set_ylabel(r'Pressure (hPa)', family='serif', fontsize=16)
ax.set_ylim(840,960)
ax.set_yticks([850,855,860,865,870,875,880,885,890,895,900,905,910,915,920,925,930,935,940,945,950])

plt.savefig('TC Index.pdf', dpi=512)
plt.savefig('TC Index.png', dpi=512)
plt.savefig('TC Index Small.png', dpi=64)
plt.show()
