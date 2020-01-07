# This file has automatically been generated
# biogeme 2.6a [Mon May 14 17:32:05 EDT 2018]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Mon Jun  4 13:57:03 2018</p>
#
ASC_CAR = Beta('ASC_CAR',-1.64275,-10,10,0,'Car cte.' )

B_COST = Beta('B_COST',-0.180929,-10,10,0,'Travel cost' )

B_TIME = Beta('B_TIME',-0.0232704,-10,10,0,'Travel time' )

B_RELIB = Beta('B_RELIB',0.0860714,-10,10,0,'Travel reliability' )

ASC_CARRENTAL = Beta('ASC_CARRENTAL',-3.43973,-10,10,0,'Car Rental cte.' )

ASC_BUS = Beta('ASC_BUS',-2.875,-10,10,0,'Bus cte.' )

ASC_PLANE = Beta('ASC_PLANE',-2.36068,-10,10,0,'Plane cte.' )

ASC_TRAIN = Beta('ASC_TRAIN',-2.0106,-10,10,0,'Train cte.' )

ASC_TRH = Beta('ASC_TRH',0,-10,10,1,'TrH cte.' )


## Code for the sensitivity analysis
names = ['ASC_BUS','ASC_CAR','ASC_CARRENTAL','ASC_PLANE','ASC_TRAIN','B_COST','B_RELIB','B_TIME']
values = [[0.0222299,0.00778935,0.00263632,-0.000888164,0.00902636,0.0024049,0.0105436,-4.32583e-05],[0.00778935,0.0199112,0.0178978,0.0215904,0.0071847,-7.05174e-05,0.00508875,0.000675359],[0.00263632,0.0178978,0.0491379,0.0305725,0.003541,-0.00235489,0.00445526,0.000886736],[-0.000888164,0.0215904,0.0305725,0.0530497,0.00189364,-0.0043733,0.00427259,0.0012203],[0.00902636,0.0071847,0.003541,0.00189364,0.0169265,0.00171577,0.00605909,5.53087e-05],[0.0024049,-7.05174e-05,-0.00235489,-0.0043733,0.00171577,0.00113907,-0.000122535,-9.52213e-05],[0.0105436,0.00508875,0.00445526,0.00427259,0.00605909,-0.000122535,0.0223307,-7.38437e-05],[-4.32583e-05,0.000675359,0.000886736,0.0012203,5.53087e-05,-9.52213e-05,-7.38437e-05,3.91556e-05]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
