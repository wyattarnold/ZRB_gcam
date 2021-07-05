/*
Copyright (C) 2010-2015 Matteo Giuliani, Josh Kollat, Jon Herman, and others.

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
*/

/****************************************************************************
C/C++ Version of HBV: Lumped model, one catchment. Uses Hamon ET and MOPEX forcing data.
*****************************************************************************/

#include "hbv_model.h"
#include "moeaframework.h"
#include "utils.h"
#include "time.h"
#include <math.h>
#include <vector>

using namespace std;

void evaluate(double* Qobs, double* Qsim, int nDays, double* objs){

    //convert observations and simulations from array to vector (one year of warmup)
    vector<double> Vobs, Vsim, Verr2, Vprod, Verr ;
    for(int i=2000; i<nDays; i++){
        Vobs.push_back( Qobs[i] );
        Vsim.push_back( Qsim[i] );
        Verr.push_back( abs(Qobs[i] - Qsim[i]) );
        Verr2.push_back( pow((Qobs[i] - Qsim[i]), 2) );
        Vprod.push_back( Qobs[i]*Qsim[i] );
    }

    // NSE vs Pearson correlation
    double NSE = 1 - ( utils::computeMean( Verr2 ) / utils::computeVariance( Vobs ) ) ;
    double PearCoeff = (utils::computeMean( Vprod ) - utils::computeMean(Vobs) * utils::computeMean(Vsim)) /
    sqrt( utils::computeVariance(Vobs) * utils::computeVariance(Vsim) );
    objs[0] = NSE;
    objs[1] = PearCoeff;
    
    // calibration using NSE decomposition from Gupta et al., 2009 
    // (see http://www.meteo.mcgill.ca/~huardda/articles/gupta09.pdf):
    // obj 1) minimize relative variability (alpha)
    // obj 2) minimize absolute value of relative bias (beta)
    // obj 3) maximize correlation coefficient (r)
    //double alpha = utils::computeStDev(Vsim) / utils::computeStDev(Vobs);
    //double beta = fabs( utils::computeMean(Vsim) - utils::computeMean(Vobs) ) / utils::computeStDev(Vobs);
    //double r = utils::computeCorr(Vsim, Vobs);
    // 3-objective calibration
    //objs[0] = alpha;
    //objs[1] = beta;
    //objs[2] = -r;
}



int main(int argc, char **argv)
{
    // read user input: single input for calibration, two inputs for simulation
    string input_file = argv[1];
    string output_file;
    if(argc>2){
        output_file = argv[2];
    }

    // hbv model
    hbv_model myHBV(input_file);

    // calibration settings
    int nobjs = 2;
    int nvars = 12;
    double objs[nobjs];
    double vars[nvars];

    clock_t start, end;
    start = clock();


    MOEA_Init(nobjs, 0);
    while (MOEA_Next_solution() == MOEA_SUCCESS) {
        MOEA_Read_doubles(nvars, vars);
        myHBV.calc_HBV(vars);
        evaluate(myHBV.getData().flow, myHBV.getFluxes().Qsim, myHBV.getData().nDays, objs);
        MOEA_Write(objs, NULL);
    }

    // save simulation results
    if(argc>2){
        //utils::logArray(myHBV.getFluxes().Qsim, myHBV.getData().nDays, output_file);
        int N = myHBV.getData().nDays;
        double flow[N];
        myHBV.getSimFlow(flow);
        utils::logArray(flow, N, output_file);
    }

    // clear HBV
    myHBV.hbv_delete(myHBV.getData().nDays);

    end = clock();
    cout << "time elapsed: " << ((end - start)/double(CLOCKS_PER_SEC)) << " seconds" << endl;


    return 0;
}
