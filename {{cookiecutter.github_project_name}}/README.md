{{ cookiecutter.github_project_name }}
===============================

{{ cookiecutter.project_short_description }}

Installation
------------

To install use pip:

    $ pip install {{ cookiecutter.python_package_name }}
    $ jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name  }}


For a development installation (requires npm),

    $ git clone https://github.com/{{ cookiecutter.github_organization_name  }}/{{ cookiecutter.github_project_name }}.git
    $ cd {{ cookiecutter.python_package_name  }}
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --user {{ cookiecutter.python_package_name }}
    $ jupyter nbextension enable --py --user {{ cookiecutter.python_package_name }}

The project also contains a conda recipe. The resulting conda package can be
installed with the `conda install` command. Unlike when installing from pypi,
the notebook extension is automatically enabled.
