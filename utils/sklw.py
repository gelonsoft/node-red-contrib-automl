#SciKit-Learn models' wrapper

import pickle
import os
import json
import numpy as np
class NumpyEncoder(json.JSONEncoder):
	""" Special json encoder for numpy types """
	def default(self, obj):
		if isinstance(obj, np.integer):
			return int(obj)
		elif isinstance(obj, np.floating):
			return float(obj)
		elif isinstance(obj, np.ndarray):
			return obj.tolist()
		return json.JSONEncoder.default(self, obj)
class SKLW:
	def __init__(self, path, model=None):
		self.path = path
		if model is not None:
			self.model = model
		else:
			self.last = os.stat(self.path).st_mtime
			self.model = pickle.load(open(self.path, "rb"))

	def fit(self, x, y=None):
		if y is not None:
			self.model.fit(x, y)
		else:
			self.model.fit(x)

		dir = os.path.dirname(self.path)
		if not os.path.isdir(dir):
			os.makedirs(dir, exist_ok=True)

		pickle.dump(self.model, open(self.path, "wb"))

	def predict(self, x):
		return self.model.predict(x) #.tolist()

	def fit_predict(self, x, roles):
		self.model.fit_predict(x,roles=roles)
		dir = os.path.dirname(self.path)
		if not os.path.isdir(dir):
			os.makedirs(dir, exist_ok=True)

		pickle.dump(self.model, open(self.path, "wb"))

	def update(self):
		modified = os.stat(self.path).st_mtime
		if(modified > self.last):
			self.last = modified
			self.model = pickle.load(open(self.path, "rb"))