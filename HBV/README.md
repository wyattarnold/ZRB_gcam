### HBV Rainfall-Runoff Model

HBV Rainfall-runoff model, based on the work by ([Bergstrom 1995](http://www.cabdirect.org/abstracts/19961904773.html)). Runs on a daily timestep and saves all states and fluxes from each day for further analysis. 

To compile and run:

* Run `make` to compile. Modify the makefile first to use a different compiler or flags.
* Run `./SimHBV ./data/<GCM-RCM>/<HBV_input>.txt my_output_file.txt < ./data/<param_file>.txt` to perform simulation

Arguments:
* `<GCM-RCM>`: Global-Regional Climate Models combination, namely MPI-ESM-LR + RCA4, ICHEC-EC-EARTH + RCA4, ICHEC-EC-EARTH + RACMO (corresponding to three different subfolders)
* `<HBV_input>.txt`: input data for Ithezi-thezi (IT), Victoria Falls (VF), and Luangwa (GRE) sub-basins under three Representative Concentration Pathways, i.e. RCP2.6-4.5-8.5
* `my_output_file.txt`: name of file to output the simulated discharge
* `<param_file>.txt`: parameter sets to be used for the model's simulation (param_IT, param_VF, param_GRE); the order of parameters to be read in can be modified at `hbv_model.cpp:309`


Based on work from the following paper:
Herman, J.D., P.M. Reed, and T. Wagener (2013), Time-varying sensitivity analysis clarifies the effects of watershed model formulation on model behavior, Water Resour. Res., 49, doi:10.1002/wrcr.20124.
([Link to Paper](http://onlinelibrary.wiley.com/doi/10.1002/wrcr.20124/abstract))

Copyright (C) 2010-2017 Matteo Giuliani, Josh Kollat, Jon Herman, and others.

HBV is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

HBV is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with HBV.  If not, see <http://www.gnu.org/licenses/>.
