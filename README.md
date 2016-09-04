# About Binary-like-Encryptor
An abandoned project which is a text encryptor using a method I made on my own to make the encryption look like binary. It has been compiled for Windows and Mac, and is portable.

# Where do I find the compiled applications?
## Windows
Go to `Binary-like-Encryptor/(Version)/Windows Distribution`, and open `Binary-like Encryptor.exe`. Be sure to move the entire folder when you want to move the application to another directory.

## Mac
Go to `Binary-like-Encryptor/(Version)/Mac OS X Distribution`, and do one of the following:
- Open `Binary-like-Encryptor.app` from the `Files` folder.
- Unzip the zip file (ends with `.zip`).
- Open the Disk Image file (ends with `.dmg`) from the `Installer` folder and "install" the application.

# How can I manually compile from source code?
## Windows
1. Check the latest available version of Python 3 that can use cx_Freeze from [the Python Package Index](https://pypi.python.org/pypi/cx_Freeze).
2. Download and install the latest version of Python 3 that can use cx_Freeze from [Python's official site](https://www.python.org/downloads/windows/).
3. Download and install the latest version of cx_Freeze from [the Python Package Index](https://pypi.python.org/pypi/cx_Freeze).
4. Grab all the files that end in `.py` from `Binary-like-Encryptor/(Version)` as well as `Binary-like-Encryptor/(Version)/Windows Distribution` to an empty directory.
5. Open the Commnad Prompt in the new directory. You can also open the Command Prompt then manually navigate to the new directory using the `cd` command.
6. To compile, after following all the steps above, run the following command in the already-open Command Prompt: `python setup.py build`.
7. After compiling has finished, your compiled files can be found under the `build` folder.

## Mac
1. Download and install the latest version of Python 3 from [Python's official site](https://www.python.org/downloads/mac-osx).
2. After Python 3 has finished installing, open Terminal, make sure your Internet connection is stable enough, and run the following command: `pip install -U py2app`.
3. After py2app has finished installing, grab alll the files that end in `.py` from `Binary-like-Encryptor/(Version)` as well as `Binary-like-Encryptor/(Version)/Mac OS X Distribution` to an empty directory.
4. Open Terminal in the new directory. You can also open the Command Prompt then manually navigate to the new directory using the `cd` command.
5. To compile, run the following command in the already-open Terminal: `python setup.py py2app`.
6. After compiling has finished, the compiled application can be found under the `dist` folder.

## Other
Unfortnately, the developer currently does not know how to compile for other operating systems. However, the source code can be found at `Binary-like-Encryptor/(Version)`, which all end in `.py`, the main file being `Binary-like Encryptor.py` if not, it might be in `Binary-like-Encryptor/(Version)/Windows Distribution` or `Binary-like-Encryptor/(Version)/Mac OS X Distribution`, but note that `setup.py` is a script used to compile the application for the specified operating system, not part of the application itself.
