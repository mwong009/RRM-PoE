# This file has automatically been generated
# biogeme 2.6a [Mon May 14 17:32:05 EDT 2018]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Fri Jun  1 14:07:38 2018</p>
#
ASC_CAR = Beta('ASC_CAR',-1.63537,-10,10,0,'Car cte.' )

B_TIME = Beta('B_TIME',-0.57762,-10,10,0,'Travel time' )

B_COST = Beta('B_COST',-0.0716313,-10,10,0,'Travel cost' )

B_RELIB = Beta('B_RELIB',0.315639,-10,10,0,'Travel reliability' )

ASC_CARRENTAL = Beta('ASC_CARRENTAL',-3.40929,-10,10,0,'Car Rental cte.' )

ASC_BUS = Beta('ASC_BUS',-2.86802,-10,10,0,'Bus cte.' )

ASC_PLANE = Beta('ASC_PLANE',-2.33408,-10,10,0,'Plane cte.' )

ASC_TRAIN = Beta('ASC_TRAIN',-2.02141,-10,10,0,'Train cte.' )

ASC_TRH = Beta('ASC_TRH',0,-10,10,1,'TrH cte.' )


## Code for the sensitivity analysis
names = ['ASC_BUS','ASC_CAR','ASC_CARRENTAL','ASC_PLANE','ASC_TRAIN','B_COST','B_RELIB','B_TIME']
values = [[0.0234958,0.00783879,0.00184662,-0.00189935,0.0103141,-0.00016171,0.0357296,0.00895801],[0.00783879,0.0222939,0.0203695,0.0255291,0.00775118,0.00259554,0.0183816,-0.00038709],[0.00184662,0.0203695,0.0524082,0.0357426,0.00325913,0.00334775,0.0165635,-0.00852459],[-0.00189935,0.0255291,0.0357426,0.0609206,0.00145956,0.00466718,0.0172479,-0.0154822],[0.0103141,0.00775118,0.00325913,0.00145956,0.0181797,0.000199205,0.0214094,0.00669743],[-0.00016171,0.00259554,0.00334775,0.00466718,0.000199205,0.000472745,-7.18294e-05,-0.00109432],[0.0357296,0.0183816,0.0165635,0.0172479,0.0214094,-7.18294e-05,0.227021,0.000994286],[0.00895801,-0.00038709,-0.00852459,-0.0154822,0.00669743,-0.00109432,0.000994286,0.0124602]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
