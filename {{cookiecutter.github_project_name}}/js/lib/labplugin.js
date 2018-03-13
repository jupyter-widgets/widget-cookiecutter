var {{ cookiecutter.npm_package_name }} = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: '{{ cookiecutter.npm_package_name }}',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: '{{ cookiecutter.npm_package_name }}',
          version: {{ cookiecutter.npm_package_name }}.version,
          exports: {{ cookiecutter.npm_package_name }}
      });
  },
  autoStart: true
};

