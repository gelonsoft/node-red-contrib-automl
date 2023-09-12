module.exports = function(RED){
	function rFCNode(config){
		const path = require('path')
		const utils = require('../../../utils/utils')

		const node = this;

		//set configurations
		node.file = __dirname +  '/../trainer.py'
		node.config = {
			automl: 'automl-trainer',
			save: path.join(config.savePath, config.saveName),
			orient: config.orient || 'split',
			kwargs: {
				name: config.task_name || 'reg',
				metric: config.task_metric || 'mse'
			},
			roles: JSON.parse(config.roles||"{}")
		}

		utils.run(RED, node, config)
	}
	RED.nodes.registerType("automl-trainer", rFCNode);
}
