import encryptor
import text_strings
from sys import platform
import datetime
from tkinter import *
from tkinter.ttk import *

# Application Constants

VERSION = "0.2.0"

# Window

window = Tk()
window.resizable(True, True)
window.title("Binary-like Encryptor")

# Check Operating System

WINDOWS = "win32"
OS_X = "darwin"
NOT_SUPPORTED = "Not supported"
NO_OS_SUPPORT_WARNING = "Warning: Binary-like Encryptor doesn't support your operating system."

if platform.lower() == WINDOWS:
    operating_system = WINDOWS
    window.geometry("500x295")
    window.minsize(370, 200)
    AccDict = {"Close" : "Ctrl+Q",
               "Undo" : "Ctrl+Z",
               "Redo" : "Ctrl+Shift+Z",
               "Cut" : "Ctrl+X",
               "Copy" : "Ctrl+C",
               "Paste" : "Ctrl+V",
               "Select All" : "Ctrl+A"}
elif platform.lower() == OS_X:
    operating_system = OS_X
    window.geometry("445x290")
    window.minsize(355, 200)
    AccDict = {"Close" : "Command-W",
               "Undo" : "Command-Z",
               "Redo" : "Command-Shift-Z",
               "Cut" : "Command-X",
               "Copy" : "Command-C",
               "Paste" : "Command-V",
               "Select All" : "Command-A"}
else:
    window.geometry("500x295")
    window.minsize(370, 200)
    operating_system = NOT_SUPPORTED
    messagebox.showwarning(title="Binary-like Encryptor warning",
                           message=NO_OS_SUPPORT_WARNING)

# Input Label

input_label = Label(window, text="Input")
input_label.grid_configure(row=0, column=0, rowspan=1, columnspan=1,
                           sticky="W")

# Encrypt Button

def encrypt_button_function():
    input_contents = input_text.get("1.0", "end-1c")
    try:
        encryption = encryptor.encrypt(input_contents)
    except Exception:
        set_status("Encrypt Error: Nothing to encrypt")
    else:
        set_status("Encryption successful", "info")
        output_text.delete("1.0", END)
        output_text.insert(END, encryption)

encrypt_button = Button(window, text="Encrypt",
                                command=encrypt_button_function)
encrypt_button.grid_configure(row=0, column=1, rowspan=1, columnspan=1,
                              sticky="NESW")

# Decrypt Button

def decrypt_button_function():
    input_contents = input_text.get("1.0", END)
    decryption = encryptor.decrypt(input_contents)
    if decryption == "error":
        set_status("Decrypt Error: Encryption is invalid")
    else:
        set_status("Decryption successful", "info")
        output_text.delete("1.0", END)
        output_text.insert(END, decryption)

decrypt_button = Button(window, text="Decrypt",
                                command=decrypt_button_function)
decrypt_button.grid_configure(row=0, column=2, rowspan=1, columnspan=1,
                              sticky="NESW")

# Input Text and Scrollbar

input_text = Text(window, width=60, height=7, undo=True, borderwidth=1)
input_text.grid_configure(row=1, column=0, rowspan=1, columnspan=3,
                          sticky="NESW")
window.grid_rowconfigure(index=1, weight=1)
window.grid_columnconfigure(index=0, weight=1)

input_text.insert(END, """Welcome!

Input your text here.

To encrypt a message, click the Encrypt button.

To decrypt an encryption, click the Decrypt button.

Have fun!""")

input_text.edit_reset()

input_text_scrollbar = Scrollbar(window)
input_text_scrollbar.grid_configure(row=1, column=3, rowspan=1, columnspan=1,  
                                    sticky="NESW")

input_text_scrollbar.config(command=input_text.yview)
input_text.config(yscrollcommand=input_text_scrollbar.set)

# Output Label

output_label = Label(window, text="Output")
output_label.grid_configure(row=2, column=0, rowspan=1, columnspan=4,
                            sticky="W")

# Output Text and Scrollbar

output_text = Text(window, width=60, height=7, undo=True, borderwidth=1)
output_text.grid_configure(row=3, column=0, rowspan=1, columnspan=3,
                           sticky="NESW")
window.grid_rowconfigure(index=3, weight=1)

output_text.insert(END, """Welcome!

All the output of encrypting/decrypting goes here.

Have fun!""")

output_text.edit_reset()

output_text_scrollbar = Scrollbar(window)
output_text_scrollbar.grid_configure(row=3, column=3, rowspan=1, columnspan=1,
                                     sticky="NESW")

output_text_scrollbar.config(command=output_text.yview)
output_text.config(yscrollcommand=output_text_scrollbar.set)

# Status Label

status_label = Label(window, text="", background="white", foreground="red",
                     borderwidth=1, relief=SUNKEN)

if operating_system == WINDOWS:
    status_label.config(font="Calibri 12")
elif operating_system == OS_X:
    status_label.config(font="Times 14")

status_label.grid_configure(row=4, column=0, rowspan=1, columnspan=3,
                            sticky="W")

def set_status(message="", status_type="error"):
    if message == "":
        status_type = None

    if status_type == None:
        status_label.config(text="", foreground="black")
    else:
        current_time = datetime.datetime.now().time()
        current_time = current_time.isoformat()
        
        time_string = "[" + current_time + "]"
    
        status_message = time_string + " " + message
        status_label.config(text=status_message)

        del current_time

    if status_type == "error":
        status_label.config(foreground="red")
    elif status_type == "info":
        status_label.config(foreground="black")
        
# Menus

menu = Menu(window)

def binary_like_encryptor_docs(open_text="About"):
    # Docs Window Settings
    docs_window = Tk()
    docs_window.resizable(True, True)
    docs_window.title("Binary-like Encryptor Docs")
    docs_window.geometry("1100x200")
    docs_window.minsize(1100, 200)
    docs_window.configure(background="gray")

    # Docs Text Box
    docs_window_text = Text(docs_window, width=50, height=5, borderwidth=1,
                             wrap=WORD, state=DISABLED)
    docs_window_text.grid_configure(row=1, column=0, rowspan=1, columnspan=1,
                                     sticky="NESW")
    docs_window.grid_rowconfigure(index=1, weight=1)
    docs_window.grid_columnconfigure(index=0, weight=1)

    # Docs Text Scrollbar

    docs_window_yscrollbar = Scrollbar(docs_window)
    docs_window_yscrollbar.grid_configure(row=1, column=1, rowspan=1,
                                           columnspan=1, sticky="NESW")

    docs_window_yscrollbar.config(command=docs_window_text.yview)
    docs_window_text.config(yscrollcommand=docs_window_yscrollbar.set)

    # Docs Status Label
	
    docs_status_label = Label(docs_window, text="", background="white", 
                              foreground="red", borderwidth=1, relief=SUNKEN)

    if operating_system == WINDOWS:
        docs_status_label.config(font="Calibri 12")
    elif operating_system == OS_X:
        docs_status_label.config(font="Times 14")

    docs_status_label.grid_configure(row=2, column=0, rowspan=1, columnspan=1,
                                     sticky="W")

    def set_docs_status(message="", status_type="error"):
        if message == "":
            status_type = None

        if status_type == None:
            docs_status_label.config(text="", foreground="black")
        else:
            current_time = datetime.datetime.now().time()
            current_time = current_time.isoformat()
        
            time_string = "[" + current_time + "]"
    
            status_message = time_string + " " + message
            docs_status_label.config(text=status_message)

            del current_time

        if status_type == "error":
            docs_status_label.config(foreground="red")
        elif status_type == "info":
            docs_status_label.config(foreground="black")

    # Docs Menu
    docs_menu = Menu(docs_window)

    if operating_system == OS_X:
        # Docs Apple Menu
        docs_apple_menu = Menu(docs_menu, name="apple")
        docs_menu.add_cascade(menu=docs_apple_menu)

        docs_apple_menu.add_command(label="About Binary-like Encryptor",
                                    command=binary_like_encryptor_docs)
        docs_apple_menu.entryconfig("About Binary-like Encryptor",
                                    state=DISABLED)

        docs_apple_menu.add_separator()

    # Docs File Menu

    docs_file_menu = Menu(docs_menu, tearoff=0)
    docs_menu.add_cascade(label="File", menu=docs_file_menu)

    # Docs File Menu Layout

    docs_file_menu.add_command(label="Close Docs", command=docs_window.destroy)

    # Docs Edit Menu

    docs_edit_menu = Menu(docs_menu, tearoff=0)
    docs_menu.add_cascade(label="Edit", menu=docs_edit_menu)

    # Docs Edit Menu Layout

    docs_edit_menu.add_command(label="Undo", accelerator=AccDict["Undo"],
                               command=undo_command)
    docs_edit_menu.add_command(label="Redo", accelerator=AccDict["Redo"],
                               command=redo_command)

    docs_edit_menu.add_separator()

    docs_edit_menu.add_command(label="Cut", accelerator=AccDict["Cut"],
                               command=cut_command)
    docs_edit_menu.add_command(label="Copy", accelerator=AccDict["Copy"],
                               command=copy_command)
    docs_edit_menu.add_command(label="Paste", accelerator=AccDict["Paste"],
                               command=paste_command)
    docs_edit_menu.add_command(label="Select All",
                               accelerator=AccDict["Select All"],
                               command=select_all_command)
    docs_edit_menu.add_command(label="Delete Selected",
                               command=delete_command)
    docs_edit_menu.add_command(label="Delete All",
                               command=delete_all_command)

    docs_menu.entryconfig("Edit", state=DISABLED)

    if operating_system == OS_X:
        # Window Menu (OS X)

        docs_window_menu = Menu(docs_menu, name="window")
        docs_menu.add_cascade(menu=docs_window_menu, label="Window")
    
    # Docs Help Menu

    docs_help_menu = Menu(docs_menu, tearoff=0)
    docs_menu.add_cascade(label="Help ", menu=docs_help_menu)

    # Docs Help Menu Layout

    docs_help_menu.add_command(label="Binary-like Encryptor Docs",
                               command=help_menu_command)
    docs_menu.entryconfig("Help ", state=DISABLED)

    # Attatching Menu to Docs

    docs_window.config(menu=docs_menu)

    # Viewing files
    def change_text_file(text_name):
        text_contents = eval("text_strings." + text_name + "_TXT")
        docs_window_text.config(state=NORMAL)
        docs_window_text.delete("1.0", END)
        docs_window_text.insert("1.0", text_contents)
        docs_window_text.config(state=DISABLED)

    default_option = StringVar(docs_window)
    default_option.set(open_text)
    options = ["", "About", "Changelog", "Help"]

    docs_option_menu = OptionMenu(docs_window, default_option, *options,
                                  command=change_text_file)
    docs_option_menu.grid_configure(row=0, column=0, rowspan=1, columnspan=2)

    change_text_file(open_text)

    # Docs Size Grip

    Sizegrip(docs_window).grid_configure(row=2, column=1, rowspan=1,
                                          columnspan=1, sticky="NES")

if operating_system == OS_X:
    # Apple Menu (OS X only)
    apple_menu = Menu(menu, name="apple")
    menu.add_cascade(menu=apple_menu)
    
    apple_menu.add_command(label="About Binary-like Encryptor",
                           command=binary_like_encryptor_docs)
    apple_menu.add_separator()

# File Menu

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

# File Menu Layout

file_menu.add_command(label="Close Binary-like Encryptor",
                      command=window.destroy)

# Edit Menu

edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)

# Edit Menu Commands

def undo_command(give_error=True):
    widget = window.focus_get()
    if isinstance(widget, Text):
        try:
            widget.edit_undo()
        except Exception:
            if give_error:
                set_status("Undo Error: Nothing to undo")
                
                #clipboard_contents = window.clipboard_get()
                
                #cut_command(False)
                #paste_command(False)

                #window.clipboard_append(clipboard_contents)
        else:
            if give_error:
                set_status("Undo successful", "info")
    elif give_error:
        set_status("Undo Error: No text box selected")

def redo_command(give_error=True):
    widget = window.focus_get()
    if isinstance(widget, Text):
        try:
            widget.edit_redo()
        except Exception:
            if give_error:
                set_status("Redo Error: Nothing to redo")
        else:
            if give_error:
                set_status("Redo successful", "info")
    elif give_error:
        set_status("Redo Error: No text box selected")

def cut_command(give_error=True):
    widget = window.focus_get()
    if isinstance(widget, Text):
        copy_command(give_error)
        delete_command(give_error)
    elif give_error:
        set_status("Cut Error: No text box selected")

def copy_command(give_error=True):
    widget = window.focus_get()
    if isinstance(widget, Text):
        window.clipboard_clear()
        try:
            widget_selection = widget.selection_get()
            window.clipboard_append(widget_selection)
        except Exception:
            if give_error:
                set_status("Copy Error: Nothing selected")
        else:
            if give_error:
                set_status("Copy successful", "info")
    elif give_error:
        set_status("Copy Error: No text box selected")

def paste_command(give_error=True):
    widget = window.focus_get()
    if isinstance(widget, Text):
        widget.tk.call("tk_textPaste", widget._w)
    elif give_error:
        set_status("Paste Error: No text box selected")

def select_all_command(give_error=True):
    widget = window.focus_get()
    if isinstance(widget, Text):
        widget.tag_add("sel", "1.0", END)
    elif give_error:
        set_status("Select All Error: No text box selected")

def delete_command(give_error=True):
    widget = window.focus_get()
    if isinstance(widget, Text):
        try:
            widget.delete(SEL_FIRST, SEL_LAST)
        except Exception:
            if give_error:
                set_status("Delete Selected Error: No text selected")
        else:
            if give_error:
                set_status("Delete successful", "info")
    elif give_error:
        set_status("Delete Selected Error: No text box selected")

def delete_all_command(give_error=True):
    widget = window.focus_get()
    if isinstance(widget, Text):
        widget.delete("1.0", END)
    elif give_error:
        set_status("Delete All Error: No text box selected")

# Edit Menu Layout

edit_menu.add_command(label="Undo", accelerator=AccDict["Undo"],
                      command=undo_command)
edit_menu.add_command(label="Redo", accelerator=AccDict["Redo"],
                      command=redo_command)

edit_menu.add_separator()

edit_menu.add_command(label="Cut", accelerator=AccDict["Cut"],
                      command=cut_command)
edit_menu.add_command(label="Copy", accelerator=AccDict["Copy"],
                      command=copy_command)
edit_menu.add_command(label="Paste", accelerator=AccDict["Paste"],
                      command=paste_command)
edit_menu.add_command(label="Select All", accelerator=AccDict["Select All"],
                      command=select_all_command)
edit_menu.add_command(label="Delete Selected", command=delete_command)
edit_menu.add_command(label="Delete All", command=delete_all_command)

if operating_system == OS_X:
    # Window Menu (OS X)

    window_menu = Menu(menu, name="window")
    menu.add_cascade(menu=window_menu, label="Window")
    
# Help Menu

help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help ", menu=help_menu)

# Help Menu Commands

def help_menu_command():
    binary_like_encryptor_docs("Help")

# Help Menu Layout

help_menu.add_command(label="Binary-like Encryptor Docs",
                      command=help_menu_command)

# Size Grip

Sizegrip().grid_configure(row=4, column=3, sticky="SE")

# Attaching Menu to Window

window.config(menu=menu)

# EXPERIMENTAL: CONTEXTUAL MENU
"""
# Contextual Menu

contextual_menu = Menu(window)

# Contextual Menu Layout

contextual_menu.add_command(label="Undo", accelerator=AccDict["Undo"],
                            command=undo_command)
contextual_menu.add_command(label="Redo", accelerator=AccDict["Redo"],
                            command=redo_command)

contextual_menu.add_separator()

contextual_menu.add_command(label="Cut", accelerator=AccDict["Cut"],
                            command=cut_command)
contextual_menu.add_command(label="Copy", accelerator=AccDict["Copy"],
                            command=copy_command)
contextual_menu.add_command(label="Paste", accelerator=AccDict["Paste"],
                            command=paste_command)
contextual_menu.add_command(label="Select All",
                            accelerator=AccDict["Select All"],
                            command=select_all_command)
contextual_menu.add_command(label="Delete Selected", command=delete_command)
contextual_menu.add_command(label="Delete All", command=delete_all_command)

# Attaching Contextual Menu

if operating_system == WINDOWS:
    window.bind("<3>",
                lambda command: contextual_menu.post(command.x_root,
                                                     command.y_root))
elif operating_system == OS_X:
    window.bind("<2>",
                lambda command: contextual_menu.post(command.x_root,
                                                     command.y_root))
    window.bind("Control-1",
                lambda command: contextual_menu.post(command.x_root,
                                                     command.y_root)) 
"""
# End of the file
mainloop()
