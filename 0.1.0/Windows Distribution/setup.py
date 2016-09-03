# Only edit the constants.
executable_name = "Binary-like Encryptor"
executable_version = "0.1.0"
executable_description = "Binary-like Encryptor"

main_script_name = "Binary-like Encryptor.py"
additional_scripts = ["encryptor"]
additional_files = []
additional_packages = []

author = "Bisma Joyosumarto"
author_email = "bismabrj@gmail.com"

# Don't do anything down here unless you know what you're doing.

from cx_Freeze import setup, Executable
import sys

if sys.platform == "win32":
    Base = "Win32GUI"
else:
    Base = None

executable_options = {"compressed" : True,
                      "create_shared_zip" : False,
                      "includes" : additional_scripts,
                      "include_files" : additional_files,
                      "packages" : additional_packages}

executable_info = Executable(script = main_script_name,
                             base = Base,
                             compress = True,
                             copyDependentFiles = True,
                             appendScriptToLibrary = False,
                             appendScriptToExe = True)

setup(name=executable_name,
      version=executable_version,
      description=executable_description,
      options = {"build_exe" : executable_options},
      executables = [executable_info],

      author = author,
      author_email = author_email)

