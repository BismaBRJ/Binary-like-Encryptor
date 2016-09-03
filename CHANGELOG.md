#Legend:
- (+) Additions
- (-) Removed features
- (*) Improvements
- (#) Notes
- (!) Known bugs
- (;) Bug fixing

Date format is in DD/MM/YY, and the project is no longer under development.

#0.2.1 (23/11/2015)
- (*) Edited Changelog to prevent confusion

#0.2.0 (08/11/2015)
- (+) Added a menu for the application
  - (#) Menu has 3 cascades (plus the Window cascade for OS X): File, Edit, and Help.
  - (+) Added short Docs. Can be accessed through Help > Binary-like Encryptor Docs.
- (+) Added status bar
  - (#) Errors show up here
- (+) Added a size grip, letting the GUI be resized
  - (#) It can also be resized manually, or be set to zoomed mode
- (*) Invalid encryptions no longer clear the output

#0.1.4 (10/10/2015)
- (;) Fixed 0.1.0#2-07/10/2015

#0.1.3 (10/10/2015)
- (;) Fixed 0.1.0#4-08/10/2015

#0.1.2 (08/10/2015)
- (;) Fixed 0.1.0#1-07/10/2015
- (;) Fixed 0.1.0#3-07/10/2015

#0.1.1 (05/10/2015)
- (*) GUI now suits the operating system it is ran on

#0.1.0 (04/10/2015)
- (+) Added simple GUI
  - (#) [OS X] Menu is automatically set up by OS X. The application will have its own menu starting from 0.2.0
  - (!) (0.1.0#2-07/10/2015) Application properties are blank
- (+) Added encryption and decryption functionality
  - (#) Handles invalid encryptions by emptying the output
  - (!) (0.1.0#1-07/10/2015) Upon decrypting: spaces, backspaces, tabs, and newlines are considered part of the encryption and therefore makes empty output
  - (!) (0.1.0#3-07/10/2015) Upon decrypting, the last character outputted may not be correct
  - (!) (0.1.0#4-08/10/2015) Upon decrypting, sometimes the application may not be able to handle invalid encryptions and therefore doesn’t change the output
