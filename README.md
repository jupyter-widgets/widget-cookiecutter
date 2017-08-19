# widget-cookiecutter
#### A cookiecutter template for creating a custom Jupyter widget project

[![Documentation Status](https://readthedocs.org/projects/ipywidgets/badge/?version=latest)](https://ipywidgets.readthedocs.io/en/latest/?badge=latest)
[![Join the chat at https://gitter.im/jupyter-widgets/Lobby](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jupyter-widgets/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for a custom
Jupyter widget project.

## What is widget-cookiecutter?

With **widget-cookiecutter** you can create a custom Jupyter interactive
widget project with sensible defaults. widget-cookiecutter helps custom widget
authors get started with best practices for the packaging and distribution
of a custom Jupyter interactive widget library.

## Who uses widget-cookiecutter

Popular widget libraries such as
[bqplot](https://github.com/bloomberg/bqplot),
[pythreejs](https://github.com/jovyan/pythreejs) and
[ipyleaflet](https://github.com/ellisonbg/ipyleaflet)
 can serve as advanced examples of usage of the
Jupyter widget infrastructure.

## Usage

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    $ pip install cookiecutter

After installing cookiecutter, use the widget-cookiecutter:

    $ cookiecutter https://github.com/jupyter/widget-cookiecutter.git

As widget-cookiecutter runs, you will be asked for basic information about
your custom Jupyter widget project. You will be prompted for the following
information:

- `author_name`: your name or the name of your organization,
- `author_email`: your project's contact email,
- `github_project_name`: name of your custom Jupyter widget's GitHub repository,
- `github_organization_name`: name of your custom Jupyter widget's GitHub user or organization,
- `python_package_name`: name of the Python "back-end" package used in your custom widget.
- `npm_package_name`: name for the npm "front-end" package holding the JavaScript
  implementation used in your custom widget.
- `project_short_description` : a short description for your project that will
  be used for both the "back-end" and "front-end" packages.
  
After this, you will have a directory containing files used for creating a
custom Jupyter widget. You will now be able to easily package and distribute
your custom Jupyter widget.

## More information

- [Documentation of Jupyter widgets](https://ipywidgets.readthedocs.io/en/latest/)
- Ask questions about using widget-cookiecutter on the Gitter channel
- If you find an issue with widget-cookiecutter or would like to contribute an
  enhancement, [file an issue](https://github.com/jupyter/widget-cookiecutter/issues/new)
  at the widget-cookiecutter GitHub repo.
