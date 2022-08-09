# Release

Before doing a release, check to see if there are any outstanding changes or untracked files:

```
git status
git clean -fdxn
```

Commit changes, and make sure that any untracked files can be deleted. Then clean the repository:

```
git clean -fdx # actually delete untracked files
```

## Javascript release

To release a new version of {{ cookiecutter.npm_package_name }} on NPM, first register for an NPM account [here](https://www.npmjs.com/), then log in with `yarn login`. Then:

1. Update `js/package.json` with the new npm package version
2. Build and publish the npm package inside the `js/` directory:

   ```
   cd js/
   yarn install
   yarn publish
   cd ..
   ```

## Python release

To release a new version of {{ cookiecutter.python_package_name  }} on PyPI, first make sure that the `build` package is installed: `pip install build`.

1. Update `{{ cookiecutter.python_package_name  }}/_version.py`:
   - Update `__version__`
   - Update `NPM_PACKAGE_RANGE` if necessary
2. Commit changes to `_version.py` and tag the release
   ```
   git add {{ cookiecutter.python_package_name  }}/_version.py
   git tag -a X.X.X -m 'comment'
   ```
3. Generate Python packages and upload to PyPI:
   ```
   python -m build
   twine check dist/*
   twine upload dist/*
   ```
4. Update `_version.py` (add 'dev' and increment minor)
   ```
   git commit -a -m 'Back to dev'
   git push
   git push --tags
   ```
