# {{ cookiecutter.github_project_name }}

{{ cookiecutter.project_short_description }}

## Installation

To install use pip:

    $ pip install {{ cookiecutter.python_package_name }}

For a development installation (requires [Node.js](https://nodejs.org) and [Yarn version 1](https://classic.yarnpkg.com/)),

    $ git clone https://github.com/{{ cookiecutter.github_organization_name  }}/{{ cookiecutter.github_project_name }}.git
    $ cd {{ cookiecutter.github_project_name }}
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --overwrite --sys-prefix {{ cookiecutter.python_package_name }}
    $ jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name }}

When actively developing your extension for JupyterLab, run the command:

    $ jupyter labextension develop --overwrite {{ cookiecutter.python_package_name  }}

Then you need to rebuild the JS when you make a code change:

    $ cd js
    $ yarn run build

You then need to refresh the JupyterLab page when your javascript changes.
