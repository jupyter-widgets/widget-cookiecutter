var extension = require('./index');
var base = require('@jupyter-widgets/base');

/**
 * Register the widget.
 */
module.exports = {
  id: '{{ cookiecutter.npm_package_name }}',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: '{{ cookiecutter.npm_package_name }}',
          version: extension.version,
          exports: extension
      });
    },
  autoStart: true
};
