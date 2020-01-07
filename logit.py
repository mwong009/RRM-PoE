########################################
#
# @file 01logit.py
# @author: Michel Bierlaire, EPFL
# @date: Wed Dec 21 13:23:27 2011
#
#######################################

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

#Parameters to be estimated
# Arguments:
#   - 1  Name for report; Typically, the same as the variable.
#   - 2  Starting value.
#   - 3  Lower bound.
#   - 4  Upper bound.
#   - 5  0: estimate the parameter, 1: keep it fixed.
#
ASC_CAR = Beta('ASC_CAR', 0, -10, 10, 0, 'Car cte.')
ASC_CARRENTAL = Beta('ASC_CARRENTAL', 0, -10, 10, 0, 'Car Rental cte.')
ASC_BUS = Beta('ASC_BUS', 0, -10, 10, 0, 'Bus cte.')
ASC_PLANE = Beta('ASC_PLANE', 0, -10, 10, 0, 'Plane cte.')
ASC_TRAIN = Beta('ASC_TRAIN', 0, -10, 10, 0, 'Train cte.')
ASC_TRH = Beta('ASC_TRH', 0, -10, 10, 1, 'TrH cte.')
B_TIME = Beta('B_TIME', 0, -10, 10, 0, 'Travel time')
B_COST = Beta('B_COST', 0, -10, 10, 0, 'Travel cost')
B_RELIB = Beta('B_RELIB', 0, -10, 10, 0, 'Travel reliability')

# Utility functions
V0 = ASC_CAR + B_TIME * Car_Cost + B_COST * Car_TT + B_RELIB * CarRelib
V1 = ASC_CARRENTAL + B_TIME * CarRental_Cost + B_COST * CarRental_TT + B_RELIB * CarRentalRelib
V2 = ASC_BUS + B_TIME * Bus_Cost + B_COST * Bus_TT + B_RELIB * BusRelib
V3 = ASC_PLANE + B_TIME * Plane_Cost + B_COST * Plane_TT + B_RELIB * PlaneRelib
V4 = ASC_TRAIN + B_TIME * Train_Cost + B_COST * Train_TT + B_RELIB * TrainRelib
V5 = ASC_TRH + B_TIME * TrH_Cost + B_COST * TrH_TT + B_RELIB * TrHRelib


# Associate utility functions with the numbering of alternatives
V = {0: V0,
     1: V1,
     2: V2,
     3: V3,
     4: V4,
     5: V5}

# Associate the availability conditions with the alternatives

av = {0: AV_Car,
      1: AV_CarRental,
      2: AV_Bus,
      3: AV_Plane,
      4: AV_Train,
      5: AV_TrH}

# The choice model is a logit, with availability conditions
logprob = bioLogLogit(V, av, Choice)

# Defines an itertor on the data
rowIterator('obsIter')

# DEfine the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(logprob,'obsIter')

# All observations verifying the following expression will not be
# considered for estimation
# The modeler here has developed the model only for work trips.
# Observations such that the dependent variable CHOICE is 0 are also removed.
# exclude = (( PURPOSE != 1 ) * (  PURPOSE   !=  3  ) + ( CHOICE == 0 )) > 0
# BIOGEME_OBJECT.EXCLUDE = exclude

# Statistics
nullLoglikelihood(av,'obsIter')
choiceSet = [0,1,2,3,4,5]
cteLoglikelihood(choiceSet,Choice,'obsIter')
availabilityStatistics(av,'obsIter')


BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"

# BIOGEME_OBJECT.FORMULAS['Train utility'] = V1
# BIOGEME_OBJECT.FORMULAS['Swissmetro utility'] = V2
# BIOGEME_OBJECT.FORMULAS['Car utility'] = V3
