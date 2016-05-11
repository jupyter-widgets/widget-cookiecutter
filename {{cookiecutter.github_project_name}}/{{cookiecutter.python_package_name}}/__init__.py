from ._version import version_info, __version__

from .example import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': '{{ cookiecutter.npm_package_name}}',
        'require': '{{ cookiecutter.npm_package_name }}/extension'
    }]
