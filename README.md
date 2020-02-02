# WinPath
[![PyPi](https://img.shields.io/pypi/v/winpath.svg)](https://pypi.python.org/pypi/winpath)
[![Build status](https://codecov.io/gh/git-albertomarin/winpath/branch/master/graph/badge.svg)](https://codecov.io/gh/git-albertomarin/winpath)
[![Coverage](https://ci.appveyor.com/api/projects/status/foncpfby5exty5e9?svg=true)](https://ci.appveyor.com/project/git-albertomarin/winpath)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://en.wikipedia.org/wiki/MIT_License)

WinPath is a python module for retrieving common Windows system paths as Unicode strings.
It is especially useful in cases where the default path to a system file has been changed by the user.
i.e When a user has changed the default path to their Documents folder.

WinPath is a fork of the original [`WinPaths`](http://ginstrom.com/code/winpaths.html)
module by Ryan Ginstrom. It includes bug fixes for issues present in the
[`WinPaths`](http://ginstrom.com/code/winpaths.html)
module and allows its inclusion in platform agnostic projects.

# Installing

Install and update using pip:

```bash
pip install -U winpath
```

# A Simple Example

WinPath can be imported and used within your own project like so.

The following example assumes that the user has chosen to sync their Documents directory with Onedrive.

```python
import sys
import winpath

if sys.platform == "win32": # WinPath will only work on Windows
    my_documents = winpath.get_my_documents()
    print(my_documents) # C:\\Users\\username\\Onedrive\\Documents
```

# Available Functions

   * `get_local_appdata`: Path to `%LOCALAPPDATA%`

   * `get_appdata`: Path to `%APPDATA%`

   * `get_desktop`: Path to the logged in user's desktop folder

   * `get_programs`: current user -> Start menu -> Programs

   * `get_admin_tools`: current user -> Start menu -> Programs -> Admin tools

   * `get_common_admin_tools`: all users -> Start menu -> Programs -> Admin tools

   * `get_common_appdata`: Path to program data folder

   * `get_common_documents`: Path to public documents folder

   * `get_cookies`: Path to internet explorer cookies folder

   * `get_history`: Path to internet explorer history folder

   * `get_internet_cache`: Path to internet explorer cache folder

   * `get_my_pictures`: Path to the logged in user's pictures folder

   * `get_my_documents`: Path to the logged in user's documents folder

   * `get_program_files`: Path to Windows program files folder

   * `get_program_files_common`: Path to Windows' program files -> common files folder

   * `get_system`: Path to Windows' System32 folder

   * `get_windows`: Path to Windows folder

   * `get_favorites`: Path to the logged in user's favorites folder

   * `get_startup`: current user -> start menu -> programs -> startup

   * `get_recent`: Path to the logged in user's recently used files folder

## License

This project is licensed under the terms of the MIT license.
