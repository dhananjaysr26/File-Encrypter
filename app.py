from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
      
root = Tk()
#app background color
app_bg="plum1"
gif_backcolor="black"
root.configure(bg=app_bg)
root.geometry("500x500+850+50")
root.title("Let's Encrypt")

#menu
def Exiting():
   messagebox.showinfo( "Lets Encrypt", "Thanks for Visiting! ")
   exit()
def about():
    messagebox.showinfo('About', 'This Simple File Encrypter Decrypter Application Based on the Cipher Encryption Technique.')

menubar = Menu(root, background='plum3', foreground='black', activebackground='white', activeforeground='black')  
file = Menu(menubar, tearoff=1, background='plum2', foreground='black')  
file.add_command(label="Encrypt")
file.add_command(label="Decrypt")       
file.add_separator()  
file.add_command(label="Exit", command=Exiting)  
menubar.add_cascade(label="File", menu=file)  

help = Menu(menubar, background='plum2',tearoff=0)  
help.add_command(label="About", command=about)  
menubar.add_cascade(label="Help", menu=help)  
    
root.config(menu=menubar)


img = ImageTk.PhotoImage(Image.open("img/logo.png"))
panel = Label(root, image = img,bg=app_bg)
panel.pack(side = "top")
#Button


###main Function
def show():
   A=1
   if A==1:
   	import main
   	
B1 = Button(root,height=3,	
width=7,text="Browse File",borderwidth=1,activebackground='purple1',bd='5',bg='gold',justify='center',    
command = show)
B1.pack(side='bottom')


mainloop()