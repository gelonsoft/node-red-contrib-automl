import json
import pandas
import os
import sys
import io
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../utils')
from sklw import NumpyEncoder

#read configurations
config = json.loads(input())
model=None
def load():
	try:
		from sklw import SKLW
		return SKLW(path=config['path'])
	except:
		return None

while True:
	data=input()
	if "orient" in data:
		new_config = json.loads(data)
		if new_config.get('modelPath') and new_config.get('modelName'):
			config['path']=os.path.join(new_config['modelPath'], new_config['modelName'])
		if new_config.get('orient'):
			config['orient']=new_config['orient']
		model = load()
		print(json.dumps({"state":"parameters applied","config":config}))
		continue

	#read request
	features = pandas.read_json(io.StringIO(data), orient=config['orient'])

	if model is None:
		model = load()
	if model is None:
		raise('Cannot find model.')
	model.update()
	
	print(json.dumps({"predict":model.predict(features).data.tolist()},cls=NumpyEncoder))
