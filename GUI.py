import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import time as t

def c(event):
    event.widget.selection_clear()
def f():
    global folder_path
    folder_path = filedialog.askdirectory()
def p():
    print(section_choice.get())

# Setup
root = tk.Tk()
root.focus_force()
root.title("Formatting Control System")
root.geometry("550x450+600-1100") 
style = ttk.Style()
style.theme_use('default')

# Side Panel
side_panel = tk.Frame(root, bg="#1E1E1E", width=250, height=350)
side_panel.pack(side='left', fill='y')
side_panel.pack_propagate(False)

# Side Panel Title
label_frame = tk.Frame(side_panel, bg='#141414', width=250, height=50)
label_frame.pack()
label_frame.pack_propagate(False)
panel_label = tk.Label(label_frame, text='Options Panel', bg="#141414", font=("Futura", 15, "italic"))
panel_label.pack(side='top', pady=(13,0)) 

# Section Choice
section_choice = tk.StringVar()
style.map('Custom.TCombobox', fieldbackground = [('readonly', '#3d3c3b')], foreground=[('readonly', 'white')], background=[('readonly', '#3d3c3b')], arrowcolor = [('readonly', 'white')])
section = ttk.Combobox(side_panel, width=20, height=10, values=["Photography Section", "Editing Section"], state='readonly', style='Custom.TCombobox', textvariable=section_choice)
section.set('\tSection')
section.bind('<<ComboboxSelected>>', c)
section.pack(side='top', pady=(50,0))

# Target Choice
style.configure('Custom.TButton', foreground='white', padding=(55,0))
style.map('Custom.TButton', background = [('active', "#474746"), ("!pressed", "#3d3c3b"), ("pressed", "#474746")])
target = ttk.Button(side_panel, text='Target', style='Custom.TButton', command=f, takefocus=0)
target.pack(side='top', pady=(50,0))

# path = tk.Button(side_panel, text='Print Path', command=p)
# path.pack(side='top', pady=(70,0))

# Log Panel
log_panel = tk.Frame(root, bg='#141414', width=290, height=440)
log_panel.pack(side='right', expand=True, fill='both', pady=(5,0), padx=(5,0))
log_panel.pack_propagate(False)

# List Box Log
logbox = tk.Listbox(log_panel, activestyle='none')
logbox.configure(selectbackground='#141414')
logbox.pack(side='left', expand=True, fill='both')
logbox.insert(0 ,' / Log / -- Test no. 0 -- Errors 0')

root.mainloop()