from setuptools import setup
from os import path

from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
)

HERE = path.dirname(path.abspath(__file__))

js_dir = path.join(HERE, 'js')

# Representative files that should exist after a successful build
jstargets = [path.join(js_dir, 'dist', 'index.js')]

data_files_spec = [
    ('share/jupyter/nbextensions/{{ cookiecutter.npm_package_name }}', '{{ cookiecutter.python_package_name }}/nbextension', '*.*'),
    ('share/jupyter/labextensions/{{ cookiecutter.npm_package_name }}', '{{ cookiecutter.python_package_name }}/labextension', "**"),
    ("share/jupyter/labextensions/{{ cookiecutter.npm_package_name }}", '.', "install.json"),
    ('etc/jupyter/nbconfig/notebook.d', '.', '{{ cookiecutter.npm_package_name }}.json'),
]

cmdclass = create_cmdclass('jsdeps', data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(js_dir, npm=['yarn'], build_cmd='build:prod'),
    ensure_targets(jstargets),
)

setup(cmdclass=cmdclass)
