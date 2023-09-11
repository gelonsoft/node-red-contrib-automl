import json
import pickle
import pandas
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../utils')
from sklw import SKLW

REG_DETECTORS = ['automl-trainer']

#read configurations
config = json.loads(input())
save = config['save']

while True:
	#read request
	data = input()
	try:
		#load data from request
		df = pandas.read_json(data, orient=config['orient'])
	except:
		#lead file specified in the request
		df = pandas.read_csv(json.loads(data)['file'], header=None)

	if config['automl'] in REG_DETECTORS:
		x = df

	automl = None

	if config['automl'] == 'automl-trainer':
		from lightautoml.automl.presets.tabular_presets import TabularAutoML
		from lightautoml.tasks import Task

		automl = SKLW(path=save, model=TabularAutoML(task = Task(**config['kwargs']))) #name = 'reg',#metric = config['metric']))

	try:
		#train model
		automl.fit_predict(x,config['roles'])
	except Exception as e:
		print(e)
		raise()

	print(config['automl'] + ': training completed.')
