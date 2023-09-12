import json
import pickle
import pandas
import os
import io
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
	if "orient" in data:
		new_config = json.loads(data)
		if new_config.get('savePath') and new_config.get('saveName'):
			config['save']=os.path.join(new_config['savePath'], new_config['saveName'])
		if new_config.get('orient'):
			config['orient']=new_config['orient']
		if new_config.get('task_name') and new_config.get('task_metric'):
			config['kwargs']={
				"name": new_config['task_name'],
				"metric": new_config['task_metric']
			}
		if new_config.get('roles'):
			config['roles']=json.loads(new_config['roles'])

		save = config['save']
		print(json.dumps({"state":"parameters applied","config":config}))
		continue

	try:
		#load data from request
		df = pandas.read_json(io.StringIO(data), orient=config['orient'])
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
	print(json.dumps({"state":"training completed","automl":config['automl']}))
