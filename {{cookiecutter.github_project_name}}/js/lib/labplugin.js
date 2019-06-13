var plugin = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: '{{ cookiecutter.npm_package_name }}',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: '{{ cookiecutter.npm_package_name }}',
          version: plugin.version,
          exports: plugin
      });
  },
  autoStart: true
};

