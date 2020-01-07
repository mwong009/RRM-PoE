# RRM-PoE
An example of a product of experts (PoE) choice model using BIOGEME

## File description 
Model files: 
- ```rrm-poe.py``` Product of Experts model to calculate a random regret model
- ```rrm-poe2.py``` alternative variant of the PoE model
- ```rrm2010.py``` original formulation of the regret function (RRM2010 paper)
- ```logit.py``` standard MNL model
- ```mixedlogit.py``` mixed logit model
 
HTML files: model estimation results

### Dataset
```biogeme_trh.csv```

Dataset tech report: [Sp_TrainHotel_Draft 5_Oct 27.2016.pdf](https://github.com/LiTrans/RRM-PoE/blob/master/Sp_TrainHotel_Draft%205_Oct%2027.2016.pdf)

## Getting started
To run, use ```python3 rrm-poe.py```.
Optionally, to test the dataset on different models, replace ```rrm-poe.py``` with the appropriate python script.

```rrm-poe2.py``` uses a different mathematical function to calculate the product utility function. Theoretically it should result in the same expression and estimated parameters. However, due to the internal optimization calculation, it may or may not produce the same result as ```rrm-poe.py```.

### Prerequisites
Python 3.5+ (with pip3), PythonBiogeme **Version 2.5** [download](https://biogeme.epfl.ch/archives.html)

Note: PandasBiogeme is not supported yet

## Versioning
0.1 Inital version

## Authors
Melvin Wong ([Github](https://github.com/mwong009))

## Licence
See [LICENCE](https://github.com/LiTrans/RRM-PoE/blob/master/LICENSE) for details
