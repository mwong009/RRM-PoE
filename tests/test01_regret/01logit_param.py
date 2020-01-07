# This file has automatically been generated
# biogeme 2.6a [Mon May 14 17:32:05 EDT 2018]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Fri Jun  1 15:46:30 2018</p>
#
ASC_CAR = Beta('ASC_CAR',-1.63264,-10,10,0,'Car cte.' )

B_COST = Beta('B_COST',-0.185909,-10,10,0,'Travel cost' )

B_TIME = Beta('B_TIME',-0.0231764,-10,10,0,'Travel time' )

B_RELIB = Beta('B_RELIB',0.108234,-10,10,0,'Travel reliability' )

ASC_CARRENTAL = Beta('ASC_CARRENTAL',-3.41027,-10,10,0,'Car Rental cte.' )

ASC_BUS = Beta('ASC_BUS',-2.85593,-10,10,0,'Bus cte.' )

ASC_PLANE = Beta('ASC_PLANE',-2.31911,-10,10,0,'Plane cte.' )

ASC_TRAIN = Beta('ASC_TRAIN',-2.00373,-10,10,0,'Train cte.' )

ASC_TRH = Beta('ASC_TRH',0,-10,10,1,'TrH cte.' )


## Code for the sensitivity analysis
names = ['ASC_BUS','ASC_CAR','ASC_CARRENTAL','ASC_PLANE','ASC_TRAIN','B_COST','B_RELIB','B_TIME']
values = [[0.0229326,0.00814544,0.00276302,-0.000726108,0.0096313,0.00259645,0.012586,-2.11388e-05],[0.00814544,0.0205113,0.0180945,0.0216301,0.00766634,0.000111728,0.00642815,0.000708949],[0.00276302,0.0180945,0.0491342,0.0304268,0.00376194,-0.00227544,0.00571194,0.000906364],[-0.000726108,0.0216301,0.0304268,0.0527067,0.00212077,-0.00431755,0.00592864,0.00123132],[0.0096313,0.00766634,0.00376194,0.00212077,0.0174536,0.00187094,0.00755315,7.66835e-05],[0.00259645,0.000111728,-0.00227544,-0.00431755,0.00187094,0.00118127,0.000150025,-9.21573e-05],[0.012586,0.00642815,0.00571194,0.00592864,0.00755315,0.000150025,0.0268674,-1.008e-05],[-2.11388e-05,0.000708949,0.000906364,0.00123132,7.66835e-05,-9.21573e-05,-1.008e-05,4.02124e-05]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
