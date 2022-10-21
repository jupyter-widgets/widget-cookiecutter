import { DOMWidgetModel, DOMWidgetView } from '@jupyter-widgets/base';

// See example.py for the kernel counterpart to this file.

// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be serialized.

export class HelloModel extends DOMWidgetModel {
    defaults() {
      return {
        ...super.defaults(),
        _model_name : 'HelloModel',
        _view_name : 'HelloView',
        _model_module : '{{ cookiecutter.npm_package_name }}',
        _view_module : '{{ cookiecutter.npm_package_name }}',
        _model_module_version : '{{ cookiecutter.npm_package_version }}',
        _view_module_version : '{{ cookiecutter.npm_package_version }}',
        value : 'Hello World!'
      };
    }
  }

export class HelloView extends DOMWidgetView {
    render() {
        this.value_changed();

        // Observe and act on future changes to the value attribute
        this.model.on('change:value', this.value_changed, this);
    }

    value_changed() {
        this.el.textContent = this.model.get('value');
    }
}
