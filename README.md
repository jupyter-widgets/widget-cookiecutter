Jupyter Widget Example
======================

This repository is an example project for a custom widget library.
It implements a very simple interactive widget, but also contains all the
information about

 - packaging
 - distribution (pypi, npm, cdn)
 - dealing with URL prefixes

It is meant to serve as a template for custom widget authors.

Installation
------------

At the moment, the example only contains an implementation for the Python
backend. It can be installed with pip.

```
$ pip install ipywidgetexample
$ jupyter nbextension enable --py ipywidgetexample
```

For a development installation (requires npm),

```
$ git clone https://github.com/jupyter/jupyter-widget-example.git
$ cd ipywidgetexample
$ pip install -e .
$ jupyter nbextension install --py --symlink --user ipywidgetexample
$ jupyter nbextension enable --py --user ipywidgetexample
```

Note for developers: the `--symlink` argument on Linux or OS X allows one to
modify the JavaScript code in-place. This feature is not available
with Windows.


