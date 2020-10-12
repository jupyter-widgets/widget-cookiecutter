from __future__ import print_function
from setuptools import setup, find_packages
import os
from os.path import join as pjoin
from distutils import log

from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
    get_version,
)


here = os.path.dirname(os.path.abspath(__file__))

log.set_verbosity(log.DEBUG)
log.info('setup.py entered')
log.info('$PATH=%s' % os.environ['PATH'])

name = '{{ cookiecutter.python_package_name  }}'
LONG_DESCRIPTION = '{{ cookiecutter.project_short_description }}'

# Get {{ cookiecutter.python_package_name  }} version
version = get_version(pjoin(name, '_version.py'))

js_dir = pjoin(here, 'js')

# Representative files that should exist after a successful build
jstargets = [
    pjoin(js_dir, 'dist', 'index.js'),
]

data_files_spec = [
    ('share/jupyter/nbextensions/{{ cookiecutter.npm_package_name }}', '{{ cookiecutter.python_package_name }}/static', '*.*'),
    ('etc/jupyter/nbconfig/notebook.d', '.', '{{ cookiecutter.npm_package_name }}.json'),
]

cmdclass = create_cmdclass('jsdeps', data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(js_dir, build_cmd='build'), ensure_targets(jstargets),
)

setup_args = dict(
    name=name,
    version=version,
    description='{{ cookiecutter.project_short_description }}',
    long_description=LONG_DESCRIPTION,
    include_package_data=True,
    install_requires=[
        'ipywidgets>=7.0.0',
    ],
    packages=find_packages(),
    zip_safe=False,
    cmdclass=cmdclass,
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='https://github.com/{{ cookiecutter.github_organization_name  }}/{{ cookiecutter.github_project_name }}',
    keywords=[
        'ipython',
        'jupyter',
        'widgets',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

setup(**setup_args)
