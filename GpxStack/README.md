# GpxStack

## Python dependencies
Some libraies can be found in the subfolder `lib`, here is the list:

- **Gpxpy** is a Python module for reading and parsing .gpx file. [More info](https://github.com/tkrajina/gpxpy)
- **Srtm** is a Python module for getting elevation data using coordinates, but it can do lot more. [More info](https://github.com/tkrajina/srtm.py).
- **Gizeh** is a vector drawing module, based on the top of *Cairocffi* , itself being a biding of the popular C library *Cairo*. [More info](https://github.com/Zulko/gizeh).
- **Cairocffi** is the Python binding for the C library *Cairo*. [More info](https://github.com/SimonSapin/cairocffi)

## Native dependencies

In order to draw shapes using *Gizeh*, some low level dependencies are required:

- The original **C library Cairo** must be installed first. More info on the [official page](http://cairographics.org/) and especially on the [download page](http://cairographics.org/download/).
- The Python module *Cairocffi* needs the library **cffi** that can be found [here](https://pypi.python.org/pypi/cffi#downloads) with some documentation [here](http://cffi.readthedocs.org/en). **cffi** can also be installed using *pip* : `pip install cffi`. The purpose of *cffi* is to ease communication between the compiled C library *Cairo* and the Python binding *Cairocffi*.

## Base
GpxStack is based on the very basic [BLANK_PI](https://github.com/jonathanlurie/BLANK_PY) project.