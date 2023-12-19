"""
Program Made by :
    Nanda Pranesh.S - 21pc19
    Varun.s         - 21pc25

Note:
    The program doesnt't work without it's functions counterpart
"""

import functions as imp
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet


imp.initialize()


    
def finish_button():
    txt = textbox.get('1.0',tk.END)
    imp.encrypt_and_store(txt, username)
    messagebox.showinfo('Info',"Data Saved in File! You may close the program safely now")
    
def Data_Locker():
    window = tk.Toplevel()
    window.title("Your Data Locker")
    window.iconbitmap(r"iconlocked.ico")
    window.resizable(0,0)
    tk.Label(window,text = "Your Data Locker",font = ('Consolas',24)).grid(row = 1,column = 0,columnspan = 2)
    
    global textbox
    textbox = tk.Text(window,height = 10,width = 55,relief = 'ridge',bd=5)
    textbox.grid(row = 2,columnspan = 2)
    
    file = open(username+".dat","rb")
    raw = file.read()
    if raw != b'':
        key = imp.load_key()
        f = Fernet(key)
        decrypted = f.decrypt(raw)
        textbox.insert("1.0",decrypted.decode())
       
    tk.Button(window,text = "Finish and Save",command = finish_button,font = ('Consolas',12,'bold')).grid(row = 3,columnspan = 2)
    
def submit_login():
    global username
    username = Username.get()
    userpass = Userpass.get()
    if imp.username_check(username):
        
        if imp.hash_check(username, userpass) == "Login Success":
            Data_Locker()
        else:
            messagebox.showinfo('Info',"Login Failed!"+" "+imp.hash_check(username, userpass))
    else:
        messagebox.showinfo('Info',"Login Failed! User doesn't Exist!")
    
def submit_register():
    preuser = username_pre.get()
    prepass = userpass_pre.get()
    chk = 0
    if prepass.lower() == prepass:
        chk+=1
    a = 0
    n = 0
    for i in prepass:
        if i.isalpha():
            a+=1
        if i.isdigit():
            n+=1
    if n==0:
        chk+=1
    if len(prepass) < 8:
        chk+=1
        
    chk1 = imp.username_check(preuser)
    if chk1 != True:
        
        if (chk == 0):
            if (preuser == "") or (" " in preuser):
                messagebox.showwarning('Info',"Username cannot be empty or can't contain spaces!")
            elif (prepass == ""):
                messagebox.showwarning('Info',"Password cannot be Empty!")
            else:
                imp.hash_store(preuser,imp.hash_gen(prepass))
                imp.new_user_file(preuser)
                messagebox.showinfo('Info','Account Registered Successfully!')
        else:
            messagebox.showwarning('Info',"Account wasn't Created! Password too weak!")
    else:
        messagebox.showwarning('Info',"Account wasn't Created! Username Already Exists!")

    
    
def Login_func():
    win = tk.Toplevel()
    win.title("Login")
    win.iconbitmap(r"iconlocked.ico")
    win.resizable(0,0)
    window = tk.Frame(win, width = 50,height = 50)
    window.pack()
    tk.Label(window,text = "Login",font = ('Consolas',24)).grid(row = 1,column = 0,columnspan = 2)
    
    tk.Label(window,text = "Username:",font = ('Consolas',12,'bold')).grid(row = 2,column = 0)
    global Username
    Username = tk.StringVar()
    tk.Entry(window,textvariable = Username).grid(row = 2,column = 1)
    
    tk.Label(window,text = "Password:",font = ('Consolas',12,'bold')).grid(row = 3,column = 0)
    global Userpass
    Userpass = tk.StringVar()
    tk.Entry(window,textvariable = Userpass,show="*").grid(row = 3,column = 1)
    
    tk.Button(window,text = "Proceed",command = submit_login,font = ('Consolas',12,'bold')).grid(row = 4,column = 0,columnspan = 2)

def Register_func():
    window = tk.Toplevel()
    window.title("Register Account")
    window.iconbitmap(r"iconlocked.ico")
    window.resizable(0,0)
    tk.Label(window,text = "Register",font = ('Consolas',24)).grid(row = 1,column = 0,columnspan = 2)
    
    tk.Label(window,text = "Set Username:",font = ('Consolas',12,'bold')).grid(row = 2,column = 0)
    global username_pre
    username_pre = tk.StringVar()
    tk.Entry(window,textvariable = username_pre).grid(row = 2,column = 1)
    
    tk.Label(window,text = "Set Password:",font = ('Consolas',12,'bold')).grid(row = 3,column = 0)
    global userpass_pre
    userpass_pre = tk.StringVar()
    tk.Entry(window,textvariable = userpass_pre).grid(row = 3,column = 1)
        
    
    tk.Label(window,text="Please Ensure your password contains atleast",anchor = "w").grid(row = 6,column = 0, columnspan= 2,sticky = "w")
    tk.Label(window,text=" - 8 Characters",anchor = "w").grid(row = 7,column = 0, columnspan= 2,sticky = "w")
    tk.Label(window,text=" - One Uppercase Letter",anchor = "w").grid(row = 8,column = 0, columnspan= 2,sticky = "w")
    tk.Label(window,text=" - One Digit",anchor = "w").grid(row = 9,column = 0, columnspan= 2,sticky = "w")
    
    tk.Button(window,text = "Proceed",command = submit_register,font = ('Consolas',12,'bold')).grid(row = 5,column = 0,columnspan = 2)

def credit():
    top = tk.Toplevel()
    top.title("Creators")
    top.iconbitmap(r"iconlocked.ico")
    tk.Label(top,text = "Encryptor v.1.17",font = ('Consolas',20,'bold')).grid(row = 0,column = 0)
    tk.Label(top,text = "Creators",font = ('Consolas',16)).grid(row = 1,column = 0)
    tk.Label(top,text = "Nanda Pranesh S",font = ('Consolas',14)).grid(row = 2,column = 0)
    tk.Label(top,text = "Varun S",font = ('Consolas',14)).grid(row = 3,column = 0)
    
    
root = tk.Tk()
root.title("Encryptor v1.17")
root.iconbitmap(r"iconlocked.ico")
root.resizable(100,100)
 
top = tk.Frame(root)
top.grid(row = 0,column = 0)
#img = tk.PhotoImage(file = r"icon.png").subsample(4,4)
tk.Button(top,command = credit).grid(row = 0,column = 0)
tk.Label(top,text = "Encryptor v.1.17",font = ('Consolas',26)).grid(row = 0,column = 1)
tk.Button(root,text = "Login",command = Login_func,font = ('Consolas',18,'bold'), padx = 20).grid(row = 1,column = 0)
tk.Button(root,text = "Register",command = Register_func,font = ('Consolas',18,'bold')).grid(row = 2,column = 0)

root.mainloop()


