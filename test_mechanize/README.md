# BLANK_PY
## What is it?
It provides a simple super-basic framework for making a Python app. I created this framework because I was all the time making the same architecture from scratch, for all my Python apps. Now it's a bit faster.

## What's inside?
It contains several folders and files, among them:

**Files:**

- `launcher.sh` a double click on it will launch your app, with the entry point in `src/main.py`. It also load  the local  `lib/`folder in `PYTHONPATH`.
- `src/SettingFileReader.py` for dealing with settings written in the file `settings.ini`
- `settings.ini` a config file to be used with the `ConfigParser` module.
- `README.md` the readme, using markdown syntax.

**Folders:**

- `src` must contain your python source files.
- `lib` contains the external Python modules (from Pypi, Github...)
- `test` you can place your test sources there

## How does it work?
### Entry point
When your code is in the `src` folder with `main.py`as entry point and your external module in the `lib` folder, just double click on `launcher.sh` to start the program.

### External parameters
Use the class `SettingFileReader` if you need to tune your app with some parameters. An example of using this feature is in the `main` function from `src/main.py` .   

`SettingFileReader` needs tobe used with only two functions: constructor and getter.

- **Constructor**: default is without any argument. In this case the "setting.ini" file
will be used. You can specify another file using a relative address (from the launcher) or absolute.

- **Getter** : `getSetting` returns the parameter written in "setting.ini" (by default) after casting it to float if it's a float, to int if it's an integer or to string in other cases.  
Takes two arguments:
	- `group` : the group of arguments, writen between square brackets
	- `name` : name of the argument
        

## Platform
It was developped on **OSX** but should work without any problem on any **UNIX** platform.

## TODO
- Adding a `SettingFileReader` adapter for easy setting loading.