// Entry point for the npmcdn bundle containing custom model definitions.
//
// It differs from the notebook bundle in that it does not need to define a
// dynamic baseURL for the static assets and may load some css that would
// already be loaded by the notebook otherwise.

// Export everything from jupyter-widget-example and the npm package version number.
module.exports = require('./jupyter-widget-example.js');
module.exports['version'] = require('../package.json').version;
