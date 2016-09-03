About_TXT = """Binary-like encryptor is self-explanatory; It encrypts text into a binary-like format.

You are running version 0.3.0 of Binary-like Encryptor."""

Changelog_TXT = """Changelog
+ Additions
- Removed features
* Improvements
# Notes
! Known bugs
; Bug fixing

0.3.0
+ Added keys
  # Keys let you modify how the program encrypts.
  # For backwards compability, set the key to 0.

0.2.1
* Edited Docs to prevent confusion

0.2.0
+ Added a menu for the application
  # Menu has 3 cascades (plus the Window cascade for OS X): File, Edit, and Help
  + Added short Docs. Can be accessed through Help > Binary-like Encryptor Docs
+ Added status bar
  # Errors show up here
+ Added a size grip, letting the GUI be resized
  # It can also be resized manually, or be set to zoomed mode
* Invalid encryptions no longer clear the output

0.1.4 (10/10/2015)
; Fixed 0.1.0#2-07/10/2015

0.1.3 (10/10/2015)
; Fixed 0.1.0#4-08/10/2015

0.1.2 (08/10/2015)
; Fixed 0.1.0#1-07/10/2015
; Fixed 0.1.0#3-07/10/2015

0.1.1 (05/10/2015)
* GUI now suits the operating system it is ran on

0.1.0 (04/10/2015)
+ Added simple GUI
  # [OS X] Menu is automatically set up by OS X. The application will have its own menu starting from 0.2.0
  ! (0.1.0#2-07/10/2015) Application properties are blank
+ Added encryption and decryption functionality
  # Handles invalid encryptions by emptying the output
  ! (0.1.0#1-07/10/2015) Upon decrypting: spaces, backspaces, tabs, and newlines are considered part of the encryption and therefore makes empty output
  ! (0.1.0#3-07/10/2015) Upon decrypting, the last character outputted may not be correct
  ! (0.1.0#4-08/10/2015) Upon decrypting, sometimes the application may not be able to handle invalid encryptions and therefore doesn't change the output"""

Help_TXT = """Note:
This is a short documentary about how to use the program.
If you are looking for information about the program, open About.
If you'd like to see how far this program has been developed, open Changelog.

Welcome to Binary-like Encryptor!

As stated in About, this is a program used to encrypt messages into a binary-like form, and decrypt them back.
This program has 2 buttons and 2 text boxes, each with their own scrollbars and labels.
Recently, this program has been able to handle errors, which is why you may see some error messages while using this program.

Input Text Box:

Insert the message/encryption here, depending on wether you want to encrypt or decrypt.

Encrypt Button:

If you have inputted a message you want to encrypt into the input text box, click this button.
It will generate the encryption you asked for in the output text box.

Decrypt Button:

If you have inputted the decryption you'd like do decrypt into the input text box, click this button.
It will generate your message in the output text box.

Output Text Box:

The encryption/message will be outputted here, depending on wether you clicked Encrypt or Decrypt.

Menus:

A few more options can be found in the menus.

File Menu:

- Close (window name): Closes selected window

Edit Menu:

- Undo: Undos action on selected text box
- Redo: Redos action on selected text box
- Cut: Copies selected text to clipboard, then deletes selected text
- Copy: Copies selected text to clipboard
- Paste: Pastes text from clipboard to selected part of text box. If any text is selected, the text is replaced
- Select All: Selects all text on the text box
- Delete Selected: Deletes selected text
- Delete All: Deletes all the text in a text box

Window Menu (OS X only):

- Minimize: Minimizes selected window
- Zoom: Toggles zoom mode
- Bring All to Front: Unminimizes all windows of the application, letting some windows of the application appear to be in front of other applications
- (window name): Toggles minimize mode for selected window

Help Menu:

- Binary-like Encryptor Docs: Opens the Binary-like Encryptor Docs

Docs:

Contains information about Binary-like Encryptor.
Currently there are 3 sections: About, Changelog, and Help (which is what you're reading).
As mentioned above, this can be accessed through Help > Binary-like Encryptor Docs.
Some menu buttons are disabled while the Docs window is selected.
This is because the functionality of those buttons cannot affect the Docs window in any way whatsoever.

Error Messages:

As stated above, there may be a few errors.
Whatever the error, they will appear at the bottom of the GUI.
Also, any error given is human-readable.
If an error is not human-readable, or comes in the form of a pop-up GUI, then it should be a bug."""
