    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:48:18 2020

@author: matteo
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


fig, (ax1, ax2) = plt.subplots(1,2)
ax1.margins()

df = pd.read_csv('../data/GCAM_demands.csv')
forcing = df.Forcing.values
SA = df.IncreaseSA2005
world = df.IncreaseWorld2005
noTax = df.LUCTaxNone
fTax = df.LUCFragmentedTax
uTax = df.LUCTaxUnifiedTax

x1 = np.linspace( world.min(), world.max() )


ax1.scatter(forcing[noTax], SA[noTax], c='#7E7E7E', marker='o', s=2)
ax1.scatter(forcing[fTax], SA[fTax], c='#ECB120', marker='o', s=2)
ax1.scatter(forcing[uTax], SA[uTax], c='#2A6246', marker='o', s=2)
ax1.set_xlabel('Forcing in 2100 (W/m2)')
ax1.set_ylabel('Southern Africa irrigation demand increase (%)')


ax2.scatter(world[noTax], SA[noTax], c='#7E7E7E', marker='o', s=2)
ax2.scatter(world[fTax], SA[fTax], c='#ECB120', marker='o', s=2)
ax2.scatter(world[uTax], SA[uTax], c='#2A6246', marker='o', s=2)
ax2.plot(x1,x1, '--k', linewidth=1.0)
ax2.set_xlabel('Global irrigation demand increase (%)')
#ax2.set_ylabel('Southern Africa irrigation demand increase (%)')

plt.savefig('./scatter.svg')
plt.show()