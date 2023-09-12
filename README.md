# node-red-contrib-automl
This module for Node-RED contains a set of nodes which offer machine learning functionalities based on LightAutoML (LAMA) - AutoML framework by Sber AI Lab.
Automatic value predictions can be performed through the use of this package.
**Tip:** For dataset creation or assessment use 

## Pre requisites
Be sure to have a working installation of [Node-RED](https://nodered.org/ "Node-RED").  
Install python and the following libraries:
* [Python](https://www.python.org/ "Python") 3.3 to 3.9.0+ (3.10+ not working due to unresolved bug in log_calls package dependency of LightAutoML)  accessible by the command 'python' (on linux 'python3')
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

This flow loads a training partition and trains a 'automl-trainer', saving the model locally.
![Training](https://i.imgur.com/yncaHql.png "Training")

This flow loads a test partition and evaluates a previously trained model.
![Evaluation](https://i.imgur.com/oMCfaBO.png "Evaluation")

Example flows available here:
```json
[
  {
    "id": "93f8e9fa7b981965",
    "type": "tab",
    "label": "Example",
    "disabled": false,
    "info": "",
    "env": []
  },
  {
    "id": "c9c2d44b4942ccf3",
    "type": "inject",
    "z": "93f8e9fa7b981965",
    "name": "Startup",
    "props": [
      {
        "p": "topic",
        "v": "",
        "vt": "date"
      }
    ],
    "repeat": "",
    "crontab": "",
    "once": true,
    "onceDelay": "0",
    "topic": "",
    "x": 120,
    "y": 180,
    "wires": [
      [
        "e1d69b6ab8bb3dbc"
      ]
    ]
  },
  {
    "id": "3d64403dbef62755",
    "type": "automl-trainer",
    "z": "93f8e9fa7b981965",
    "name": "Blank automl trainer, inititiated by income msg with config override",
    "savePath": ".",
    "saveName": "1",
    "task_name": "reg",
    "task_metric": "mse",
    "orient": "split",
    "roles": "",
    "x": 800,
    "y": 180,
    "wires": [
      [
        "900d87ab6c41ab10"
      ],
      [
        "810b6bac3f6609f0"
      ]
    ]
  },
  {
    "id": "900d87ab6c41ab10",
    "type": "switch",
    "z": "93f8e9fa7b981965",
    "name": "Check result",
    "property": "payload.state",
    "propertyType": "msg",
    "rules": [
      {
        "t": "cont",
        "v": "training complete",
        "vt": "str"
      },
      {
        "t": "cont",
        "v": "parameters applied",
        "vt": "str"
      }
    ],
    "checkall": "false",
    "repair": false,
    "outputs": 2,
    "x": 1170,
    "y": 180,
    "wires": [
      [
        "ba0eb2757966aa57"
      ],
      [
        "e70e95f3bf05810a"
      ]
    ]
  },
  {
    "id": "ba0eb2757966aa57",
    "type": "debug",
    "z": "93f8e9fa7b981965",
    "name": "Good, training complete",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload",
    "targetType": "msg",
    "statusVal": "",
    "statusType": "auto",
    "x": 1410,
    "y": 140,
    "wires": []
  },
  {
    "id": "e70e95f3bf05810a",
    "type": "debug",
    "z": "93f8e9fa7b981965",
    "name": "Parameter override complete",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload",
    "targetType": "msg",
    "statusVal": "",
    "statusType": "auto",
    "x": 1420,
    "y": 180,
    "wires": []
  },
  {
    "id": "810b6bac3f6609f0",
    "type": "debug",
    "z": "93f8e9fa7b981965",
    "name": "Something goes wrong",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload",
    "targetType": "msg",
    "statusVal": "",
    "statusType": "auto",
    "x": 1200,
    "y": 260,
    "wires": []
  },
  {
    "id": "ebbb20ee88785748",
    "type": "comment",
    "z": "93f8e9fa7b981965",
    "name": "Dynamic config override example",
    "info": "",
    "x": 170,
    "y": 80,
    "wires": []
  },
  {
    "id": "74c77439e67a576f",
    "type": "automl-predictor",
    "z": "93f8e9fa7b981965",
    "name": "",
    "modelPath": ".",
    "modelName": "example_model.pb",
    "orient": "split",
    "x": 720,
    "y": 520,
    "wires": [
      [
        "2075f007f0ccdc25"
      ],
      [
        "452afc07ae46a9fe"
      ]
    ]
  },
  {
    "id": "40b307080ba54353",
    "type": "change",
    "z": "93f8e9fa7b981965",
    "name": "Set train data",
    "rules": [
      {
        "t": "set",
        "p": "payload",
        "pt": "msg",
        "to": "{\"columns\":[\"X1\",\"X2\",\"Y\"],\"data\":[[1,2,3],[2,3,4],[3,4,5],[4,5,6],[7,8,9],[8,9,10],[9,10,11]]}",
        "tot": "json"
      }
    ],
    "action": "",
    "property": "",
    "from": "",
    "to": "",
    "reg": false,
    "x": 430,
    "y": 320,
    "wires": [
      [
        "3d64403dbef62755"
      ]
    ]
  },
  {
    "id": "e81a3288569c71d5",
    "type": "change",
    "z": "93f8e9fa7b981965",
    "name": "Set evaluate data",
    "rules": [
      {
        "t": "set",
        "p": "payload",
        "pt": "msg",
        "to": "{\"columns\":[\"X1\",\"X2\",\"Y\"],\"data\":[[1,3,3],[1.5,6,4],[2,4,5],[7,5,6],[2,8,9],[4,9,10],[1,10,11]]}",
        "tot": "json"
      }
    ],
    "action": "",
    "property": "",
    "from": "",
    "to": "",
    "reg": false,
    "x": 390,
    "y": 520,
    "wires": [
      [
        "74c77439e67a576f"
      ]
    ]
  },
  {
    "id": "2075f007f0ccdc25",
    "type": "debug",
    "z": "93f8e9fa7b981965",
    "name": "Prediction result",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload.predict",
    "targetType": "msg",
    "statusVal": "",
    "statusType": "auto",
    "x": 1000,
    "y": 500,
    "wires": []
  },
  {
    "id": "452afc07ae46a9fe",
    "type": "debug",
    "z": "93f8e9fa7b981965",
    "name": "Something goes wrong",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "true",
    "targetType": "full",
    "statusVal": "",
    "statusType": "auto",
    "x": 1020,
    "y": 580,
    "wires": []
  },
  {
    "id": "5855044829e55473",
    "type": "inject",
    "z": "93f8e9fa7b981965",
    "name": "Inject to start",
    "props": [
      {
        "p": "topic",
        "v": "",
        "vt": "date"
      }
    ],
    "repeat": "",
    "crontab": "",
    "once": false,
    "onceDelay": "",
    "topic": "",
    "x": 150,
    "y": 520,
    "wires": [
      [
        "e81a3288569c71d5"
      ]
    ]
  },
  {
    "id": "e1d69b6ab8bb3dbc",
    "type": "change",
    "z": "93f8e9fa7b981965",
    "name": "Set automl trainer params override",
    "rules": [
      {
        "t": "set",
        "p": "payload",
        "pt": "msg",
        "to": "{\"orient\":\"split\",\"savePath\":\".\",\"saveName\":\"example_model.pb\",\"roles\":\"{\\\"target\\\":\\\"Y\\\",\\\"drop\\\":[\\\"X1\\\"]}\",\"task_name\":\"reg\",\"metric\":\"mse\"}",
        "tot": "json"
      }
    ],
    "action": "",
    "property": "",
    "from": "",
    "to": "",
    "reg": false,
    "x": 360,
    "y": 180,
    "wires": [
      [
        "3d64403dbef62755"
      ]
    ]
  },
  {
    "id": "c7dbe2abda3a25f8",
    "type": "comment",
    "z": "93f8e9fa7b981965",
    "name": "Dynamic config must contain \"orient\" parameter",
    "info": "",
    "x": 260,
    "y": 140,
    "wires": []
  },
  {
    "id": "cd6faf49fcf5830e",
    "type": "comment",
    "z": "93f8e9fa7b981965",
    "name": "Click to train model",
    "info": "",
    "x": 150,
    "y": 280,
    "wires": []
  },
  {
    "id": "c9abcc8a3b09d38e",
    "type": "comment",
    "z": "93f8e9fa7b981965",
    "name": "Load model and evaluate",
    "info": "",
    "x": 730,
    "y": 480,
    "wires": []
  },
  {
    "id": "8c58368a92b4a68f",
    "type": "inject",
    "z": "93f8e9fa7b981965",
    "name": "Inject to start",
    "props": [
      {
        "p": "topic",
        "v": "",
        "vt": "date"
      }
    ],
    "repeat": "",
    "crontab": "",
    "once": true,
    "onceDelay": "0.1",
    "topic": "",
    "x": 150,
    "y": 320,
    "wires": [
      [
        "40b307080ba54353"
      ]
    ]
  },
  {
    "id": "977b6889d96be6d4",
    "type": "comment",
    "z": "93f8e9fa7b981965",
    "name": "Click to evaluate saved model",
    "info": "",
    "x": 180,
    "y": 480,
    "wires": []
  }
]
```
## Thanks
Thanks to  Gabriele Maurina for awesome nodes - [node-red-contrib-machine-learning](https://github.com/GabrieleMaurina/node-red-contrib-machine-learning "node-red-contrib-machine-learning") 