# Androidctl

[![Build Status](https://travis-ci.org/aerogear/androidctl.png)](https://travis-ci.org/aerogear/androidctl)
[![License](https://img.shields.io/:license-Apache2-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

## Project Info

Command line interface utility that installs android sdk and its development packages.

|                 | Project Info  |
| --------------- | ------------- |
| License:        | Apache License, Version 2.0  |
| Build:          | Python  |
| Documentation:  | TBD |
| Issue tracker:  | https://issues.jboss.org/browse/AGDIGGER  |
| Mailing lists:  | [aerogear-users](http://aerogear-users.1116366.n5.nabble.com/) ([subscribe](https://lists.jboss.org/mailman/listinfo/aerogear-users))  |
|                 | [aerogear-dev](http://aerogear-dev.1069024.n5.nabble.com/) ([subscribe](https://lists.jboss.org/mailman/listinfo/aerogear-dev))  |
| IRC:            | [#aerogear](https://webchat.freenode.net/?channels=aerogear) channel in the [freenode](http://freenode.net/) network.  |

## Installation

### From source

```
python setup.py install
```

### From repository (zip archive)


```
#you can change "master" to use anoter branch
 pip install https://github.com/aerogear/androidctl/archive/master.zip
```


## Development

### Installing all dependencies:

```
pip install -U -r requirements.txt
```

### Running tests

```
py.test -s
```

## Usage

The package installs an `androidctl` command line script that manages android sdk installation and its development packages:

`androidctl sdk install`: will download and unarchive android sdk (uses ANDROID_HOME as destination path, defaults to /opt/android-sdk-linux)

`androidctl sdk uninstall`: will remove android sdk from disk based on ANDROID_HOME folder

`androidctl pkg install platforms android-25`: installs a package (format is $PKG_TYPE $PKG_NAME)

`androidctl sync file.cfg`: will install all packages based on cfg file (ini format), sample file located in examples folder.


