import random
import string
import tkinter as tk
from tkinter import messagebox
def pas_gen():
  try:
    len=int(len_entry.get())
    if len<=0:
      messagebox.showerror("Error,please enter length more than 0:")
      return
  except ValueError:
    messagebox.showerror("Error,Please Enter Valid Number:")
  characters=""
  if letters.get():
    characters+=string.ascii_letters
  if numbers.get():
    characters+=string.digits
  if symbols.get():
    characters+=string.punctuation
  if characters=="":
    messagebox.showerror("please select atleast one option:")
    return
  password=""
  for i in range(len):
    password+=random.choice(characters)
  result_var.set(password)
def pas_copy():
  password=result_var.get()
  if password:
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied","Password copied to clipboard")
  else:
    messagebox.showwarning("Warning","Generate password first")
root=tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
tk.Label(root,text="Password Length").pack()
len_entry=tk.Entry(root)
len_entry.pack()
letters=tk.BooleanVar()
numbers=tk.BooleanVar()
symbols=tk.BooleanVar()
tk.Checkbutton(root,text="Include Letters",variable=letters).pack()
tk.Checkbutton(root,text="Include Numbers",variable=numbers).pack()
tk.Checkbutton(root,text="Include Symbols",variable=symbols).pack()
tk.Button(root,text="Generate Password",command=pas_gen).pack(pady=10)
result_var=tk.StringVar()
tk.Entry(root,textvariable=result_var,width=30).pack()
tk.Button(root,text="copy to clipboard",command=pas_copy).pack(pady=5)
root.mainloop()
    
    
      
    