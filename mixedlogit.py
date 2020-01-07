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

import numpy as np

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

B_TIME_S = Beta('B_TIME_S', 0, -10, 10, 0, 'Travel time S')
B_COST_S = Beta('B_COST_S', 0, -10, 10, 0, 'Travel cost S')
B_RELIB_S = Beta('B_RELIB_S', 0, -10, 10, 0, 'Travel reliability S')

# Define an error component, normally distirbuted, designed to be used
# for Monte-Carlo simulation.
# Note that draws a generated for
# individuals, and are the same for all observcations of the same
# individuals. Individuals are identified by the variable ID.

B_TIME_RND = B_TIME + B_TIME_S * bioDraws('B_TIME_RND')
B_COST_RND = B_COST + B_COST_S * bioDraws('B_COST_RND')
B_RELIB_RND = B_RELIB + B_RELIB_S * bioDraws('B_RELIB_RND')

# Variables
asc = np.asarray(
	[ASC_CAR, ASC_CARRENTAL, ASC_BUS, ASC_PLANE, ASC_TRAIN, ASC_TRH])
cost = np.asarray(
	[Car_Cost, CarRental_Cost, Bus_Cost, Plane_Cost, Train_Cost, TrH_Cost])
time = np.asarray(
	[Car_TT, CarRental_TT, Bus_TT, Plane_TT, Train_TT, TrH_TT])
relib = np.asarray(
	[CarRelib, CarRentalRelib, BusRelib, PlaneRelib, TrainRelib, TrHRelib])
avail = np.array(
    [AV_Car, AV_CarRental, AV_Bus, AV_Plane, AV_Train, AV_TrH])
    
# Utility functions
V = {i: asc[i] for i in range(len(asc))}
av = {j: avail[j] for j in range(len(avail))}

for i in range(len(asc)):
    V[i] += B_TIME_RND * cost[i] + B_COST_RND * time[i] + B_RELIB_RND * relib[i]

# The choice model is a logit, with availability conditions
prob = bioLogit(V,av,Choice)
l = mixedloglikelihood(prob)

# Defines an itertor on the data
rowIterator('obsIter') 

# Define the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(l,'obsIter')

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

BIOGEME_OBJECT.PARAMETERS['NbrOfDraws'] = "500"
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"
BIOGEME_OBJECT.PARAMETERS['numberOfThreads'] = "4"

BIOGEME_OBJECT.DRAWS = { 'B_TIME_RND': 'NORMAL',
                         'B_COST_RND': 'NORMAL',
                         'B_RELIB_RND': 'NORMAL' }

# BIOGEME_OBJECT.FORMULAS['Train utility'] = V1
# BIOGEME_OBJECT.FORMULAS['Swissmetro utility'] = V2
# BIOGEME_OBJECT.FORMULAS['Car utility'] = V3
