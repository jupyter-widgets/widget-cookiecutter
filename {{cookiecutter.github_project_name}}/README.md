# {{ cookiecutter.github_project_name }}

{{ cookiecutter.project_short_description }}

## Installation

### User installation:

```bash
pip install {{ cookiecutter.python_package_name }}
jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name  }}
```

#### Install the JupyterLab extension

In order to install the JupyterLab extension, you will first need to ensure `nodejs` is available in your environment. You can install it from [the nodejs website](https://nodejs.org/en/download) or using `conda`:
```bash
conda install -c conda-forge nodejs
```

You will also need to install the Widgets Manager for JupyterLab with:

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

If you already installed the Widgets Manager previously, you need to at least run the following command in order to install the {{ cookiecutter.python_package_name  }} labextension:

```bash
jupyter lab build
```

### Development installation

```bash
git clone https://github.com/{{ cookiecutter.github_organization_name  }}/{{ cookiecutter.github_project_name }}.git
cd {{ cookiecutter.github_project_name }}
pip install -e .

# If using Jupyter Notebook
jupyter nbextension install --py --symlink --sys-prefix {{ cookiecutter.python_package_name }}
jupyter nbextension enable --py --sys-prefix {{ cookiecutter.python_package_name }}

# If using JupyterLab
jupyter labextension install @jupyter-widgets/jupyterlab-manager js
```

When actively developing your extension, build JupyterLab with the command:

```bash
jupyter lab --watch
```

This takes a minute or so to get started, but then automatically rebuilds JupyterLab when your javascript changes.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

