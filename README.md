# node-red-contrib-automl
This module for Node-RED contains a set of nodes which offer machine learning functionalities based on LightAutoML (LAMA) - AutoML framework by Sber AI Lab.
Automatic value predictions can be performed through the use of this package.
**Tip:** For dataset creation or assessment use 

## Pre requisites
Be sure to have a working installation of [Node-RED](https://nodered.org/ "Node-RED").  
Install python and the following libraries:
* [Python](https://www.python.org/ "Python") 3.6.4 or higher accessible by the command 'python' (on linux 'python3')
* [Numpy](http://www.numpy.org/ "Numpy")
* [Pandas](https://pandas.pydata.org/ "Pandas")
* [SciKit-Learn](http://scikit-learn.org "SciKit-Learn")
* [LightAutoML](https://github.com/sberbank-ai-lab/LightAutoML "LightAutoML")

## Install
To install the latest version use the Menu - Manage palette option and search for node-red-contrib-automl, or run the following command in your Node-RED user directory (typically ~/.node-red):

    npm i node-red-contrib-automl

## Usage
These flows create a dataset, train a model and then evaluate it. Models, after training, can be use in real scenarios to make predictions.

Flows and test datasets are available in the 'test' folder. Make sure that the paths specified inside nodes' configurations are correct before trying to execute the program.  
**Tip:** you can run 'node-red' (or 'sudo node-red' if you are using linux) from the folder '.node-red/node-modules/node-red-contrib-automl' and the paths will be automatically correct.

This flow loads a training partition and trains a 'decision tree classifier', saving the model locally.
![Training](https://i.imgur.com/yncaHql.png "Training")

This flow loads a test partition and evaluates a previously trained model.
![Evaluation](https://i.imgur.com/oMCfaBO.png "Evaluation")

This flow shows how to use a trained model during deploymnet. Data is received via mqtt, predictions are made and then sent back.  
![Deployment](https://i.imgur.com/an7FwAC.png "Deployment")

Example flows available here:
```json
[]
```
## Thanks
Thanks to  Gabriele Maurina for package base - [node-red-contrib-machine-learning](https://github.com/GabrieleMaurina/node-red-contrib-machine-learning "node-red-contrib-machine-learning") 