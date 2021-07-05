#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:55:47 2021

@author: matteo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./data/JJsim.csv')  

hyd = df['HYD']
irr = df['IRR']
env = df['ENV']

#%%

fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)


### HYDROPOWER ###

# RCP26
v0 = ax1.violinplot(hyd[df['RCP']==26],positions=[1],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#0D72BA')
    b.set_edgecolor('black')
    b.set_alpha(.8)

v1 = ax1.violinplot(hyd[(df['RCP']==26)&(df['MODEL']==1)],positions=[1],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax1.violinplot(hyd[(df['RCP']==26)&(df['MODEL']==2)],positions=[1],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax1.violinplot(hyd[(df['RCP']==26)&(df['MODEL']==3)],positions=[1],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
# RCP45
v0 = ax1.violinplot(hyd[df['RCP']==45],positions=[2],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#76AC42')
    b.set_edgecolor('black')
    b.set_alpha(.8)

v1 = ax1.violinplot(hyd[(df['RCP']==45)&(df['MODEL']==1)],positions=[2],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax1.violinplot(hyd[(df['RCP']==45)&(df['MODEL']==2)],positions=[2],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax1.violinplot(hyd[(df['RCP']==45)&(df['MODEL']==3)],positions=[2],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
# RCP85
v0 = ax1.violinplot(hyd[df['RCP']==85],positions=[3],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#A21D31')
    b.set_edgecolor('black')
    b.set_alpha(.8)
    
v1 = ax1.violinplot(hyd[(df['RCP']==85)&(df['MODEL']==1)],positions=[3],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax1.violinplot(hyd[(df['RCP']==85)&(df['MODEL']==2)],positions=[3],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax1.violinplot(hyd[(df['RCP']==85)&(df['MODEL']==3)],positions=[3],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)

# add medians
m26 = np.percentile(hyd[df['RCP']==26], 50)
m45 = np.percentile(hyd[df['RCP']==45], 50)
m85 = np.percentile(hyd[df['RCP']==85], 50)
ax1.scatter([1,2,3], [m26, m45, m85], marker='o', color='black', edgecolor='black', s=75, zorder=3)

### IRRIGATION ###

# RCP26
v0 = ax2.violinplot(irr[df['RCP']==26],positions=[1],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#0D72BA')
    b.set_edgecolor('black')
    b.set_alpha(.8)

v1 = ax2.violinplot(irr[(df['RCP']==26)&(df['MODEL']==1)],positions=[1],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax2.violinplot(irr[(df['RCP']==26)&(df['MODEL']==2)],positions=[1],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax2.violinplot(irr[(df['RCP']==26)&(df['MODEL']==3)],positions=[1],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
# RCP45
v0 = ax2.violinplot(irr[df['RCP']==45],positions=[2],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#76AC42')
    b.set_edgecolor('black')
    b.set_alpha(.8)

v1 = ax2.violinplot(irr[(df['RCP']==45)&(df['MODEL']==1)],positions=[2],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax2.violinplot(irr[(df['RCP']==45)&(df['MODEL']==2)],positions=[2],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax2.violinplot(irr[(df['RCP']==45)&(df['MODEL']==3)],positions=[2],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
# RCP85
v0 = ax2.violinplot(irr[df['RCP']==85],positions=[3],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#A21D31')
    b.set_edgecolor('black')
    b.set_alpha(.8)
    
v1 = ax2.violinplot(irr[(df['RCP']==85)&(df['MODEL']==1)],positions=[3],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax2.violinplot(irr[(df['RCP']==85)&(df['MODEL']==2)],positions=[3],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax2.violinplot(irr[(df['RCP']==85)&(df['MODEL']==3)],positions=[3],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
# add medians
m26 = np.percentile(irr[df['RCP']==26], 50)
m45 = np.percentile(irr[df['RCP']==45], 50)
m85 = np.percentile(irr[df['RCP']==85], 50)
ax2.scatter([1,2,3], [m26, m45, m85], marker='o', color='black', edgecolor='black', s=75, zorder=3)

   
### ENVIRONMENT ###

# RCP26
v0 = ax3.violinplot(env[df['RCP']==26],positions=[1],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#0D72BA')
    b.set_edgecolor('black')
    b.set_alpha(.8)

v1 = ax3.violinplot(env[(df['RCP']==26)&(df['MODEL']==1)],positions=[1],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax3.violinplot(env[(df['RCP']==26)&(df['MODEL']==2)],positions=[1],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax3.violinplot(env[(df['RCP']==26)&(df['MODEL']==3)],positions=[1],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
# RCP45
v0 = ax3.violinplot(env[df['RCP']==45],positions=[2],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#76AC42')
    b.set_edgecolor('black')
    b.set_alpha(.8)

v1 = ax3.violinplot(env[(df['RCP']==45)&(df['MODEL']==1)],positions=[2],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax3.violinplot(env[(df['RCP']==45)&(df['MODEL']==2)],positions=[2],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax3.violinplot(env[(df['RCP']==45)&(df['MODEL']==3)],positions=[2],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
# RCP85
v0 = ax3.violinplot(env[df['RCP']==85],positions=[3],showextrema=False)
for b in v0['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further right than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], -np.inf, m)
    b.set_color('#A21D31')
    b.set_edgecolor('black')
    b.set_alpha(.8)
    
v1 = ax3.violinplot(env[(df['RCP']==85)&(df['MODEL']==1)],positions=[3],showextrema=False)
for b in v1['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('peru')
    b.set_edgecolor('black')
    b.set_alpha(.4)

v2 = ax3.violinplot(env[(df['RCP']==85)&(df['MODEL']==2)],positions=[3],showextrema=False)
for b in v2['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('turquoise')
    b.set_edgecolor('black')
    b.set_alpha(.4)
    
v3 = ax3.violinplot(env[(df['RCP']==85)&(df['MODEL']==3)],positions=[3],showextrema=False)
for b in v3['bodies']:
    # get the center
    m = np.mean(b.get_paths()[0].vertices[:, 0])
    # modify the paths to not go further left than the center
    b.get_paths()[0].vertices[:, 0] = np.clip(b.get_paths()[0].vertices[:, 0], m, np.inf)
    b.set_color('slateblue')
    b.set_edgecolor('black')
    b.set_alpha(.4)

# add medians
m26 = np.percentile(env[df['RCP']==26], 50)
m45 = np.percentile(env[df['RCP']==45], 50)
m85 = np.percentile(env[df['RCP']==85], 50)
ax3.scatter([1,2,3], [m26, m45, m85], marker='o', color='black', edgecolor='black', s=75, zorder=3)


# set labels, legend
ax1.set_ylabel('hydropower production (TWh/y)')
ax2.set_ylabel('irrigation deficit (m3/s)')
ax3.set_ylabel('environmental deficit (m3/s)')

ax1.set_axisbelow(True)
ax2.set_axisbelow(True)
ax3.set_axisbelow(True)
ax1.grid(zorder=0)
ax2.grid(zorder=0)
ax3.grid(zorder=0)


plt.setp(ax1, xticks=[1, 2, 3], xticklabels=['RCP2.6', 'RCP4.5', 'RCP8.5'])
plt.setp(ax2, xticks=[1, 2, 3], xticklabels=['RCP2.6', 'RCP4.5', 'RCP8.5'])
plt.setp(ax3, xticks=[1, 2, 3], xticklabels=['RCP2.6', 'RCP4.5', 'RCP8.5'])

ax3.legend([v0['bodies'][0],v1['bodies'][0],v2['bodies'][0],v3['bodies'][0]],\
           ['ALL','MPI-ESM-LR + RCA4','ICHEC-EC-EARTH + RCA4','ICHEC-EC-EARTH + RACMO'])
    

plt.savefig('./violinsMC.svg')

plt.show()    





