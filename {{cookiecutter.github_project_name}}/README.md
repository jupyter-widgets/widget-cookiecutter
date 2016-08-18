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
    $ cd {{ cookiecutter.github_project_name }}
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix {{ cookiecutter.python_package_name }}
    $ jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name }}
