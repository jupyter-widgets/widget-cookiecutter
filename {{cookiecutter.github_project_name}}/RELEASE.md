### To release a new version of {{ cookiecutter.python_package_name  }} on PyPI:

Update _version.py (set release version, remove 'dev')
git add the _version.py file and git commit
```
python setup.py sdist upload
python setup.py bdist_wheel upload
git tag -a X.X.X -m 'comment'
```

Update _version.py (add 'dev' and increment minor)
```
git add and git commit
git push
git push --tags
```

### To release a new version of {{ cookiecutter.npm_package_name }} on NPM:

Update `js/package.json` with new npm package version

Clean out the `dist` and `node_modules` directories:
```
git clean -fdxn
git clean -fdx
```

Release new npm package (register [here](https://www.npmjs.com/)):
```
cd js
npm login
npm install
npm publish
```
