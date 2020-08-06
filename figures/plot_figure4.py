#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:27:38 2020

@author: matteo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.cm as cm
import matplotlib as mpl

fig = plt.figure()
fig.set_size_inches([8.15,17.05]) # 17.05 8.15
ax = fig.add_subplot(111)

# create map background  
m = Basemap(llcrnrlon=-20.0, llcrnrlat=-37.0, urcrnrlon=60.0,
            urcrnrlat=40.0, projection='cyl', resolution='h') 

m.drawmapboundary(fill_color='steelblue', zorder=-99)

# load GCAM African countries 
df = pd.read_csv('../data/GCAM_regions.csv')
dfC = df.ISO.values
dfD = df.DemandChange.values

#Define Colormap
norm = mpl.colors.Normalize(vmin=-.1, vmax=2.1)
cmap = cm.PRGn_r
colors=cm.ScalarMappable(norm=norm, cmap=cmap)
colors.set_array(dfD)
a = colors.to_rgba(dfD)


# river basin from shapefile
m.readshapefile('../data/world', 'countries', drawbounds=False)

for info, shape in zip(m.countries_info, m.countries):
    iso3 = info['ISO3']
    if iso3 not in dfC:
        color = 'darkgray'
    else:
        sc = np.where(dfC == iso3)
        color = a[sc]

    patches = [Polygon(np.array(shape), True)]
    pc = PatchCollection(patches)
    pc.set_facecolor(color)
    ax.add_collection(pc)


# colorbar
cb = m.colorbar(colors,'right')
cb.ax.tick_params(labelsize=14)

# rivers, countries, coastlines
m.drawrivers(color='royalblue',linewidth=.8,zorder=1)
m.drawcountries(color='k',linewidth=.5)

# load reservoir data and scatterplot (lat,lon,elev)
df = pd.read_csv('../data/FHReD_2015_africa.csv')
lons = df.Lon_Cleaned.values
lats = df.LAT_cleaned.values
#cap = df.Capacity.values

x,y = m(lons,lats)
m.scatter(x,y,c='whitesmoke', marker='o', edgecolor='k', s=40)

# saving
plt.savefig('./mapAfrica.svg')
plt.show()


