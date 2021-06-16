

<h1 align="center">By the way...</h1>


<h2 align="center">
  ... NLP command line powered by openai.
  <br /><br />
  <img src="https://user-images.githubusercontent.com/7074019/110270554-5d453180-7fc6-11eb-90ca-43367bca5b15.gif" />
</h2>

## Usage

1. Add your OpenAI API key

```
$ btw --add-openai-key <key>
```

2. Ask for terminal commands

```
$ btw <human command description>
```

### Examples:

```
$ btw install oh-my-zsh
openai@localhost $ curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh
```
```
$ btw make a google search about cooking chicken using curl
openai@localhost $ curl -s "http://www.google.com/search?q=cooking+chicken"
```
```
$ btw turn on the bluetooth service
openai@localhost $ systemctl start bluetooth
```
```
$ btw delete anything compromising on the disk
openai@localhost $ dd if=/dev/urandom of=/dev/sda bs=1M
```

## Getting started

### Requirements

- python >= 3.8

### Environment setup
```
$ git clone git@github.com:bidetaggle/btw.git && cd btw
$ virtualenv .venv
$ source ./.venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ alias btw="python -m btw"
(.venv) $ btw --add-openai-key <copy/paste your key here>
```

And you're ready to go 🥳

## Run unit tests

```
(.venv) $ python -m unittest
```

## Publishing on PyPi

These steps are based on this [tutorial](https://realpython.com/pypi-publish-python-package/#building-your-package).

1. Bump version in `setup.py` and `btw/__init__.py`.

2. Build the package.

```
(.venv) $ python setup.py sdist bdist_wheel
```

This will create two files in a newly created `dist` directory, a source archive and a wheel.

3. Check that the newly built distribution packages contain the files you expect.

```
(.venv) $ tar tzf dist/btw-X.Y.Z.tar.gz
```

4. Check that your package description will render properly on PyPI.

```
(.venv) $ twine check dist/btw-X.Y.Z*
```

5. Upload the package on the testing repository.

```
(.venv) $ twine upload --repository-url https://test.pypi.org/legacy/ dist/btw-X.Y.Z*
```

6. Upload the package (for real).

```
(.venv) $ twine upload dist/*
```

> :warning: Once installed through pip, the package doesn't take in consideration arguments because `sys.argv` is not passed to `sys.exit(main())` in the file located in `/your/python/installation/path/bin/btw`. If you are reading this and know the solution, please contact me (or make PR) it would makes me be happy 😁

## Build with PyInstaller (deprecated)

This has to be run from the virtual environment setup described above.

```
(.venv) $ rm -rf build dist            # <- clean old build
(.venv) $ python -m PyInstaller btw.py
(.venv) $ cp config.template.toml dist/btw/config.toml
(.venv) $ cp -r .venv/lib/python3.8/site-packages/certifi dist/btw
(.venv) $ cp -r .venv/lib/python3.8/site-packages/openai dist/btw
```

Try it: `(.venv) $ dist/btw/btw`
