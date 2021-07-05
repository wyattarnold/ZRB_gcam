# ZRB_gcam

This repository contains the code and results used to generate Figures 2-3-4 of the following paper:
```
Giuliani, M., J. Lamontagne, M.I. Hejazi, P.M. Reed, and A. Castelletti, Exploring the unintended 
consequences of climate change mitigation for African river basins (submitted)
```

`plot_figure2.py` uses violin plots to show the uncertain attainment of the local objectives estimated via simulation of the modeled historical Zambezi Watercourse operations over the ensemble of interdependent climate and socio-economic scenarios. In the data folder, the JJsim.csv file contains the objectives values (the columns correspond to hydropower production, irrigation deficit, environmental deficit) for different Representative Concentration Pathways (4th column) and Global-Regional Climate Models combinations (1 = MPI-ESM-LR + RCA4, 2 = ICHEC-EC-EARTH + RCA4, 3 = ICHEC-EC-EARTH + RACMO)

`plot_figure3.py` in the figures folder generates a scatterplot of 2100 forcing vs Southern Africa irrigation demand growth (left) and a scatterplot of global vs Southern Africa irrigation demand growth. Colors represent alternative policies of Land Use Change (LUC) emission price: gray points are scenarios with no emission price, green with globally uniform LUC price, and yellow with regionally differentiated LUC price (i.e., wealthy countries pay a higher LUC emission price than developing ones due to their strong attempts to curb LUC emission). In the data folder, the GCAM_demands.csv file contains the 2100 forcing and irrigation demand growth produced by the GCAM simulations in [Lamontagne et al. (2018)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017EF000701).

`plot_figure4.py` in the figures folder generates a map of African countries colored according to the ratio of average 2005-2100 irrigation demands projected by GCAM for scenarios with fragmented LUC price over the one of scenarios with universal LUC price. The white circles indicate the locations of future hydropower reservoirs and dams extracted from [Zarfl et al. (2015)](http://globaldamwatch.org/fhred/). In the data folder, the GCAM_regions.csv file specifies for each country on the rows the demand change ratio as well as the corresponding GCAM region; the FHReD_2015_africa.csv file contains the data about hydropower reservoirs and dams for the African continent; the world.shp file is a shapefile with world countries data.
