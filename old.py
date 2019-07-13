import json
import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure(figsize=(12, 12))
ax = fig.gca()

with open("c:/Users/rcjcyoo/Downloads/skorea-provinces-2018-geo.json", encoding='utf-8') as json_file:
    jdata = json_file.read()
    geoJSON = json.loads(jdata)

pts=[]
for  feature in geoJSON['features']:
    if feature['geometry']['type']=='Polygon':
        pts.extend(feature['geometry']['coordinates'][0])    
        pts.append([None, None])
        
    elif feature['geometry']['type']=='MultiPolygon':
        for polyg in feature['geometry']['coordinates']:
            pts.extend(polyg[0])
            pts.append([None, None])
    else: raise ValueError("geometry type irrelevant for map")  

x = [i for i,j in pts]
y = [j for i,j in pts]
ax.plot(x,y)

# sidos = 서울, 부산, 대구, 인천, 광주, 
#           대전, 울산, 세종, 경기, 강원, 
#           충북, 충남, 전북, 전남, 경북, 
#           경남, 제주

old_age = [36.6, 41.0, 39.7, 37.8, 36.6, 36.4, 37.0, 27.8, 35.3, 45.0, 40.6, 40.0, 43.9, 46.8, 45.4, 41.4, 36.6]
sidos = [[127.2, 37.8], [129.35, 35], [128.5, 36.15], [126.2, 37.5], [126.7, 35],
           [127.2, 36.3], [129.6, 35.5], [127, 36.7], [127.3, 37.25], [128.3, 37.8],
           [127.75, 36.8], [126.1, 36.5], [127.2, 35.7], [126.6, 34.6], [129, 36.5],
           [128.1, 35.4], [126.5, 33.7]]

for s, sido  in enumerate(sidos):
    cx, cy = sido
    ratios = []
    ratios.append(old_age[s]/100.0)
    ratios.append(1.0-old_age[s]/100.0)
    start = 0.25
    for i, ratio in enumerate(ratios):
        x = np.add(np.multiply(np.cos(np.linspace(2*math.pi*start,2*math.pi*(start+ratio), 30)), 0.25), cx)
        x1 = [cx] + x.tolist()
        y = np.add(np.multiply(np.sin(np.linspace(2*math.pi*start,2*math.pi*(start+ratio), 30)), 0.2), cy)
        y1 = [cy] + y.tolist()
        ax.fill(x1,y1, color=colors[i], facecolor=colors[i], alpha=1.0)
        start += ratio
        
plt.show()
#plt.savefig("old_age.png")