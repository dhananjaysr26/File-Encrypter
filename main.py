from tkinter import filedialog as fd
from easygui import *
def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    msgbox("File Encrypted Successfully!","Encryption")
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    msgbox("File Decrypted Successfully!","Decryption")
 

filetypes =(
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
filename = fd.askopenfilename(
        title='Open a file',
        filetypes=filetypes)

if filename== ():
    exit()

key= integerbox("Enter Key ","Lets Encrypt",100,1,10000)
if key==None:
    exit()
buttons = ["Encrypt", "Decrypt"]
option=indexbox("What Do Want to DO?", "Lets Encrypt", buttons)
if option==0:
    Encrypt(filename,key)
if option==1:
    Decrypt(filename,key)
