import tkinter as tk
import tkinter.filedialog
import time

def browse_files(): 
    filename = tkinter.filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    label_file_explorer.configure(text="File Opened: "+filename) 
       
       
                                                                                                   
# Create the root window 
window = tk.Tk() 
   
# Set window title 
window.title('File Explorer') 
   
# Set window size 
window.geometry("500x500") 
   
#Set window background color 
window.config(background = "white") 
   
# Create a File Explorer label 
label_file_explorer = tk.Label(window,  
                            text = "File Explorer using Tkinter", 
                            width = 100, height = 4,  
                            fg = "blue") 
   
       
button_explore = tk.Button(window,  
                        text = "Browse Files", 
                        command = browse_files)  
   
button_exit = tk.Button(window,  
                     text = "Exit", 
                     command = exit)  
   
# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns 
label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.grid(column = 1, row = 2) 
   
button_exit.grid(column = 1,row = 3) 
   
# Let the window wait for any events 
window.mainloop() 