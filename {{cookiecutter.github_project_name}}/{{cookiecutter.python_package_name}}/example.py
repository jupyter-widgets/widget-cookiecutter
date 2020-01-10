import ipywidgets as widgets
""" Widget properties are defined as traitlets. This allows automatic
syncing of properties between kernel and front-end. These properties are
accessible in front-end using model.get('property name') with use of
Backbone.js based widget front-end models.
"""
from traitlets import Unicode

""" Declare widget class and register to widget registry """
@widgets.register
class HelloWorld(widgets.DOMWidget):
    """An example widget."""
    """ Name of the widget view class in front-end """
    _view_name = Unicode('HelloView').tag(sync=True)
    """ Name of the widget model class in front-end """
    _model_name = Unicode('HelloModel').tag(sync=True)
    """ Name of the front-end module containing widget view """
    _view_module = Unicode('{{ cookiecutter.npm_package_name }}').tag(sync=True)
    """ Name of the front-end module containing widget model """
    _model_module = Unicode('{{ cookiecutter.npm_package_name }}').tag(sync=True)
    """ Version of the front-end module containing widget view """
    _view_module_version = Unicode('^{{ cookiecutter.npm_package_version }}').tag(sync=True)
    """ Version of the front-end module containing widget model """
    _model_module_version = Unicode('^{{ cookiecutter.npm_package_version }}').tag(sync=True)
    """ Widget specific property """
    value = Unicode('Hello World!').tag(sync=True)
