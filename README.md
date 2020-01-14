# Hardware Parts Manager

Desktop CRUD GUI application to manage customer computer parts with Python, the Tkinter library and Sqlite3 to store data.

## Demo

![app](https://user-images.githubusercontent.com/34337622/72211392-efd56800-34ca-11ea-9a0f-dae1d0306fd0.gif)

## Technologies

-   Python 3.7
-   Tkinter
-   SQLite3

## Prerequisites

-   [Python](https://www.python.org/downloads/)
-   [pip](https://pip.pypa.io/en/stable/installing/)
-   [pipenv](https://pipenv.readthedocs.io/en/latest/install/#make-sure-you-ve-got-python-pip)

## Installation

-   [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo to your local machine using:

```
$ git clone https://github.com/tarnowski-git/Hardware_Parts_Manager.git
```

-   Setup your [local environement](https://www.youtube.com/watch?v=K2fNEoZfuy8):

```
# Spawn a shell with the virtualenv activated
$ pipenv shell

# Install dependencies
$ pipenv install

# Run script into local environment
$ pipenv run python hardware_parts_manager.py
```

-   Compile with Pyinstaller to exectutable file:

```
# Windows
pyinstaller --onefile --windowed hardware_parts_manager.py
```

## Sources

This application is based on [Traversy Media](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA) Tutorial.

## License

This project is licensed under the terms of the [**MIT**](https://github.com/tarnowski-git/Hardware_Parts_Manager/blob/master/LICENSE) license.
