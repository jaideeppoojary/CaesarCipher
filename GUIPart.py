import re
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import pyperclip

from CaesarCipher import autoCipherDecript, cipherEncryptDecrypt

def retrieve_input():
    text = plain_text.get("1.0",'end-1c')
    result_label.config(text=text)
    pyperclip.copy(text)
    messagebox.showinfo("Result", "Result Copied to clip board")
    
def manual_button_action():
    skip_count = simpledialog.askinteger("Input","Enter skip count value", parent=mainscreen) 
    encriptedString = plain_text.get("1.0",'end-1c')
    result = cipherEncryptDecrypt(encriptedString, skip_count )
    print(result)

    cipher_text.config(text=result)
    pyperclip.copy(result)
    messagebox.showinfo("Result", "Result Copied to clip board")
    


def auto_button_action():
    hint_word = simpledialog.askstring("Input","Enter flag (hint word)")
    encriptedString = plain_text.get("1.0",'end-1c')
    result = autoCipherDecript(encriptedString, hint_word )

    cipher_text.config(text=result)
    pyperclip.copy(result)
    messagebox.showinfo("Result", "Result Copied to clip board")

def main_screen():
    global mainscreen
    mainscreen = Tk()   # create a GUI window 
    mainscreen.configure(bg='#F7CCAC')
    mainscreen.geometry("900x500") # set the configuration of GUI window 
    mainscreen.title(" Caesar Cipher") # set the title of GUI window

    Top_title = Label(mainscreen, text = "Caesar Cipher", font=("Arial", 18), bg='#826F66',width=100,height=2)


    global plain_text
    plain_text_label = Label(mainscreen, text = "Enter Message ", font=("Arial", 18), bg='#F7CCAC')
    plain_text = Text(mainscreen, height = 5, width = 52)

    global result_label
    result_label = Label(mainscreen, text = "", font=("Arial", 24), bg='#F7CCAC')

    manual_or_encrypt = Button(mainscreen, text = "Manual Encrypt/Decrypt", command = manual_button_action,width=30)
    auto_decript = Button(mainscreen, text = "Auto Decript", command = auto_button_action, width= 30)

    global cipher_text
    cipher_text_label = Label(mainscreen, text = "Cipher Text ", font=("Arial", 18), bg='#F7CCAC')
    cipher_text = Label(mainscreen, text = "", font=("Arial", 18), bg='#C69B7B',width=100)


    Top_title.pack()
    plain_text_label.pack(pady=20)
    plain_text.pack()
    manual_or_encrypt.pack(pady = 20)
    auto_decript.pack(pady = 20)

    cipher_text_label.pack(pady=15)
    cipher_text.pack()
    result_label.pack(pady=20)


    mainscreen.mainloop() # start the GUI

main_screen() 