# BLANK_PY
## What is it?
It provides a simple super-basic framework for making a Python app. I created this framework because I was all the time making the same architecture from scratch, for all my Python apps. Now it's a bit faster.

## What's inside?
It contains several folders and files, among them:

**Files:**

- `launcher.sh` a double click on it will launch your app, with the entry point in `src/main.py`. It also load  the local  `lib/`folder in `PYTHONPATH`.
- `settings.ini` a config file to be used with the `ConfigParser` module.
- `README.md` the readme, using markdown syntax.

**Folders:**

- `src` must contain your python source files.
- `lib` contains the external Python modules (from Pypi, Github...)
- `test` you can place your test sources there

## How does it work?
When your code is in the `src` folder with `main.py`as entry point and your external module in the `lib` folder, just double click on `launcher.sh` to start the program.


## Platform
It was developped on **OSX** but should work without any problem on any **UNIX** platform.