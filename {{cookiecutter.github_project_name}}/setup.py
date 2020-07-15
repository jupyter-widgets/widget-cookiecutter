from __future__ import print_function
from setuptools import setup, find_packages, Command
from setuptools.command.sdist import sdist
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from subprocess import check_call
from glob import glob
import os
import json
import platform
import sys
from distutils import log

here = os.path.dirname(os.path.abspath(__file__))
node_root = os.path.join(here, 'js')
is_repo = os.path.exists(os.path.join(here, '.git'))

npm_path = os.pathsep.join([
    os.path.join(node_root, 'node_modules', '.bin'),
    os.environ.get('PATH', os.defpath),
])

log.set_verbosity(log.DEBUG)
log.info('setup.py entered')
log.info('$PATH=%s' % os.environ['PATH'])

name = '{{ cookiecutter.python_package_name  }}'
LONG_DESCRIPTION = '{{ cookiecutter.project_short_description }}'


def js_prerelease(command, strict=False):
    """Decorator for building minified js/css prior to another command."""
    class DecoratedCommand(command):
        def run(self):
            jsdeps = self.distribution.get_command_obj('jsdeps')
            if not is_repo and all(os.path.exists(t) for t in jsdeps.targets):
                # sdist, nothing to do
                command.run(self)
                return

            try:
                self.distribution.run_command('jsdeps')
            except Exception as e:
                missing = [t for t in jsdeps.targets if not os.path.exists(t)]
                if strict or missing:
                    log.warn('rebuilding js and css failed')
                    if missing:
                        log.error('missing files: %s' % missing)
                    raise e
                else:
                    log.warn('rebuilding js and css failed (not a problem)')
                    log.warn(str(e))
            command.run(self)
            update_package_data(self.distribution)
    return DecoratedCommand


def get_data_files():
    """Get the data files."""
    with open(os.path.join('js', 'package.json')) as f:
        package_json = json.load(f)
    tgz = '{{ cookiecutter.npm_package_name }}-%s.tgz' % package_json['version']

    return [
        ('share/jupyter/nbextensions/{{ cookiecutter.npm_package_name }}', glob('{{ cookiecutter.python_package_name }}/static/*')),
        ('etc/jupyter/nbconfig/notebook.d', ['{{ cookiecutter.npm_package_name }}.json']),
        ('share/jupyter/lab/extensions', ['js/' + tgz]),
    ]


def update_package_data(distribution):
    """Update package_data to catch changes during setup."""
    build_py = distribution.get_command_obj('build_py')
    distribution.data_files = get_data_files()
    # re-init build_py options which load package_data
    build_py.finalize_options()


class NPM(Command):
    description = 'install package.json dependencies using npm'

    user_options = []

    node_modules = os.path.join(node_root, 'node_modules')

    targets = [
        os.path.join(here, '{{ cookiecutter.python_package_name }}', 'static', 'extension.js'),
        os.path.join(here, '{{ cookiecutter.python_package_name }}', 'static', 'index.js')
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def get_npm_name(self):
        npm_name = 'npm'
        if platform.system() == 'Windows':
            npm_name = 'npm.cmd'

        return npm_name

    def has_npm(self):
        npm_name = self.get_npm_name()
        try:
            check_call([npm_name, '--version'])
            return True
        except:
            return False

    def should_run_npm_install(self):
        return self.has_npm()

    def run(self):
        has_npm = self.has_npm()
        if not has_npm:
            log.error("`npm` unavailable.  If you're running this command using sudo, make sure `npm` is available to sudo")

        env = os.environ.copy()
        env['PATH'] = npm_path

        if self.should_run_npm_install():
            log.info("Installing build dependencies with npm.  This may take a while...")
            npm_name = self.get_npm_name()
            check_call([npm_name, 'install'], cwd=node_root, stdout=sys.stdout, stderr=sys.stderr)
            check_call([npm_name, 'pack'], cwd=node_root, stdout=sys.stdout, stderr=sys.stderr)
            os.utime(self.node_modules, None)

        for t in self.targets:
            if not os.path.exists(t):
                msg = 'Missing file: %s' % t
                if not has_npm:
                    msg += '\nnpm is required to build a development version of a widget extension'
                raise ValueError(msg)

        # update package data in case this created new files
        update_package_data(self.distribution)

version_ns = {}
with open(os.path.join(here, '{{ cookiecutter.python_package_name  }}', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup_args = dict(
    name=name,
    version=version_ns['__version__'],
    description='{{ cookiecutter.project_short_description }}',
    long_description=LONG_DESCRIPTION,
    include_package_data=True,
    data_files=get_data_files(),
    install_requires=[
        'ipywidgets>=7.0.0',
    ],
    packages=find_packages(),
    zip_safe=False,
    cmdclass={
        'build_py': js_prerelease(build_py),
        'egg_info': js_prerelease(egg_info),
        'sdist': js_prerelease(sdist, strict=True),
        'jsdeps': NPM,
    },
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
