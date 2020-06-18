{{ cookiecutter.github_project_name }}
===============================

{{ cookiecutter.project_short_description }}

Installation
------------

To install use pip:

    $ pip install {{ cookiecutter.python_package_name }}
    $ jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name  }}

To install for jupyterlab

    $ jupyter labextension install {{ cookiecutter.python_package_name  }}

For a development installation (requires npm),

    $ git clone https://github.com/{{ cookiecutter.github_organization_name  }}/{{ cookiecutter.github_project_name }}.git
    $ cd {{ cookiecutter.github_project_name }}
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix {{ cookiecutter.python_package_name }}
    $ jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name }}
    $ jupyter labextension install js

When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch

This takes a minute or so to get started, but then automatically rebuilds JupyterLab when your javascript changes.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

