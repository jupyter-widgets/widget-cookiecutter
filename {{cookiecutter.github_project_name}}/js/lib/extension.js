// This file contains the javascript that is run when the notebook is loaded.
// It contains some requirejs configuration and the `load_ipython_extension`
// which is required for any notebook extension.

// Configure requirejs
if (window.require) {
    window.require.config({
        map: {
            "*" : {
                "{{ cookiecutter.npm_package_name }}": "nbextensions/{{ cookiecutter.npm_package_name }}/index",
            }
        }
    });
}

export function load_ipython_extension() { };
