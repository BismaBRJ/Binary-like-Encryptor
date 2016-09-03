import encryptor
from tkinter import *
from tkinter.ttk import *

# Window

window = Tk()
window.geometry("500x280")
window.resizable(False, False)
window.title("Binary-like Encryptor 0.1.1")

# Input Label

input_label = Label(window, text="Input")
input_label.grid_configure(row=0, column=0, rowspan=1, columnspan=1,
                           sticky="W")

# Encrypt Button

def encrypt_button_function():
    input_contents = input_text.get("1.0", "end-1c")
    encryption = encryptor.encrypt(input_contents)
    output_text.delete("1.0", END)
    output_text.insert(END, encryption)

encrypt_button = Button(window, text="Encrypt",
                                command=encrypt_button_function)
encrypt_button.grid_configure(row=0, column=1, rowspan=1, columnspan=1,
                              sticky="NESW")

# Decrypt Button

def decrypt_button_function():
    input_contents = input_text.get("1.0", "end-2c")
    decryption = encryptor.decrypt(input_contents)
    output_text.delete("1.0", END)
    output_text.insert(END, decryption)

decrypt_button = Button(window, text="Decrypt",
                                command=decrypt_button_function)
decrypt_button.grid_configure(row=0, column=2, rowspan=1, columnspan=1,
                              sticky="NESW")

# Input Text and Scrollbar

input_text = Text(window, width=60, height=7)
input_text.grid_configure(row=1, column=0, rowspan=1, columnspan=3)

input_text.insert(END, """Welcome!

Input your text here.

To encrypt a message, click the Encrypt button.

To decrypt an encryption, click the Decrypt button.

Have fun!""")

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

output_text = Text(window, width=60, height=7)
output_text.grid_configure(row=3, column=0, rowspan=1, columnspan=3)

output_text.insert(END, """Welcome!

All the output of encrypting/decrypting goes here.

Have fun!""")

output_text_scrollbar = Scrollbar(window)
output_text_scrollbar.grid_configure(row=3, column=3, rowspan=1, columnspan=1,
                                     sticky="NESW")

output_text_scrollbar.config(command=output_text.yview)
output_text.config(yscrollcommand=output_text_scrollbar.set)

# End of the file
window.mainloop()
