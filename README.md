Cookiecutter template for custom Jupyter widget project
=======================================================

[![Documentation Status](https://readthedocs.org/projects/ipywidgets/badge/?version=latest)](http://ipywidgets.readthedocs.org/en/latest/?badge=latest)
[![Join the chat at https://gitter.im/ipython/ipywidgets](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ipython/ipywidgets?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for a custom
Jupyter widget project.

Goals
-----

This project is meant to help custom widget authors get started with the
packaging and the distribution of Jupyter interactive widgets.

It produces a project for a Jupyter interactive widget library following the
current best practices for using interactive widgets. An implementation for a
placeholder "Hello World" widget is provided.

More Advanced Examples
----------------------

Popular widget libraries such as
[bqplot](https://github.com/bloomberg/bqplot),
[pythreejs](https://github.com/jovyan/pythreejs) and
[ipyleaflet](https://github.com/ellisonbg/ipyleaflet)
follow exactly the same template and directory structure. They can serve as
more advanced examples of usage of the Jupyter widget infrastructure.

Usage
-----

You first need to get cookiecutter

    $ pip install cookiecutter

Then you can run

    $ cookiecutter https://github.com/jupyter/widget-cookiecutter.git

You will be asked for basic information about your project. The required fields
are:

- `author_name`: your name or the name of your organization,
- `author_email`: the contact email for the project,
- `github_project_name`: name of the GitHub repository,
- `github_organization_name`: name of the GitHub user or organization holding
  the repository,
- `python_package_name`: name of the Python backend package.
- `npm_package_name`: name for the npm package holding the JavaScript
  implementation.
- `project_short_description` : a short description for the project that will
  be used for both the back-end and front-end packages.
