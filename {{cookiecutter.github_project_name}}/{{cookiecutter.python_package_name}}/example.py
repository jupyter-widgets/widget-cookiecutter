import ipywidgets as widgets
""
from traitlets import Unicode

""" Declare widget class and register to widget registry """
@widgets.register
class HelloWorld(widgets.DOMWidget):
    """An example widget."""

    # Name of the widget view class in front-end
    _view_name = Unicode('HelloView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('HelloModel').tag(sync=True)

    # Name of the front-end module containing widget view
    _view_module = Unicode('{{ cookiecutter.npm_package_name }}').tag(sync=True)

    # Name of the front-end module containing widget model
    _model_module = Unicode('{{ cookiecutter.npm_package_name }}').tag(sync=True)

    # Version of the front-end module containing widget view
    _view_module_version = Unicode('^{{ cookiecutter.npm_package_version }}').tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode('^{{ cookiecutter.npm_package_version }}').tag(sync=True)

    # Widget specific property.
    # Widget properties are defined as traitlets. Any property tagged with `sync=True`
    # is automatically synced to the frontend *any* time it changes. It is
    # accessible from the frontend model as `this.get("value")` and from the
    # frontend view as `this.model.get("value")`.
    value = Unicode('Hello World!').tag(sync=True)
