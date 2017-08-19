import ipywidgets as widgets
from traitlets import Unicode

@widgets.register
class HelloWorld(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('HelloView').tag(sync=True)
    _model_name = Unicode('HelloModel').tag(sync=True)
    _view_module = Unicode('{{ cookiecutter.npm_package_name }}').tag(sync=True)
    _model_module = Unicode('{{ cookiecutter.npm_package_name }}').tag(sync=True)
    _view_module_version = Unicode('^{{ cookiecutter.npm_package_version }}').tag(sync=True)
    _model_module_version = Unicode('^{{ cookiecutter.npm_package_version }}').tag(sync=True)
    value = Unicode('Hello World!').tag(sync=True)
