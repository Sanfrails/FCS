import time as t
import tkinter as tk
from tkinter import ttk, filedialog
from FCS import *

dotted_line = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
def clean_log():
        logbox.delete(0,tk.END)
        logbox.insert(tk.END ,f' / Log {counter} / -- Tagged [{len(toTag)}] -- Errors [{len(issues)}]')
        logbox.insert(tk.END, f' Target Folder: {folder_path}\n')
        logbox.insert(tk.END, dotted_line)
def clear_func():
    logbox.delete(0,tk.END)
    section.set('\tSection')
    tag_color.set('\tTag Color')
    global folder_path, counter, tag_dic, toTag, issues
    folder_path = None
    counter = 0
    toTag = []
    issues = []
    tag_dic = {' Red Tag':'Red', ' Orange Tag':'Orange', ' Green Tag':'Green', ' Purple Tag':'Purple'}
    logbox.insert(tk.END ,' / Log 0 / -- Tagged [0] -- Errors [0]')
    logbox.insert(tk.END, ' Target Folder: None')
    logbox.insert(tk.END, dotted_line)
def folder_pick(event=None):
    global folder_path
    folder_path = filedialog.askdirectory()
def run_scan():
    if section_choice.get() == '\tSection' or folder_path == None or tag_color.get()=='\tTag Color':
        logbox.insert(tk.END, ' Error: Please configure scan settings!')
        logbox.insert(tk.END, dotted_line)
    else:
        # Button State
        scan.configure(state='disabled', text='Scanning...')
        scan.update()
        try:
            # Running Logic
            global issues, toTag 
            issues, toTag = run_process(folder_path, section_choice.get(), tag_dic[tag_color.get()])
            # Logbox insertions
            global counter
            counter += 1
            logbox.insert(tk.END ,f' / Log {counter} / -- Tagged [{len(toTag)}] -- Errors [{len(issues)}]')
            logbox.insert(tk.END, f' Target Folder: {folder_path}\n')      
            for x in issues:
                logbox.insert(tk.END, '')
                logbox.insert(tk.END, ' ' + x)
            logbox.insert(tk.END, dotted_line)   
        except Exception as e:
            logbox.insert(tk.END, f' Error: Process failed - {e}')
            logbox.insert(tk.END, f' Please check target and section')
            logbox.insert(tk.END, dotted_line)
        finally:
            # Button State
            t.sleep(1)
            scan.configure(state='normal', text='Scan')
def c(event):
    event.widget.selection_clear()
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Setup
root = tk.Tk()
root.focus_force()
root.title("Formatting Control System")
center_window(root, 600,450) 
style = ttk.Style()
style.theme_use('default')
Menu_bar = tk.Menu(root)
file_menu = tk.Menu(Menu_bar, tearoff=0)
file_menu.add_command(label='Exit', command=root.destroy)
Menu_bar.add_cascade(label='File', menu=file_menu)
root.config(menu=Menu_bar, bg='#3E3D3D')
root.bind("<Command-w>", lambda e: root.destroy())

# Side Panel
side_panel = tk.Frame(root, bg="#1E1E1E", width=250, height=350)
side_panel.pack(side='left', fill='y')
side_panel.pack_propagate(False)

# Side Panel Title
label_frame = tk.Frame(side_panel, bg='#141414', width=250, height=50)
label_frame.pack()
label_frame.pack_propagate(False)
panel_label = tk.Label(label_frame, text='Options Panel', bg="#141414", fg='#ffffff', font=("Times New Roman", 15))
panel_label.pack(side='top', pady=(10,0)) 

# Section Choice
section_choice = tk.StringVar()
style.map('Custom.TCombobox', fieldbackground = [('readonly', '#3d3c3b')], foreground=[('readonly', 'white')], background=[('readonly', '#3d3c3b')], arrowcolor = [('readonly', 'white')])
section = ttk.Combobox(side_panel, width=20, height=10, values=[" Photography Section", " Editing Section"], state='readonly', style='Custom.TCombobox', textvariable=section_choice)
section.set('\tSection')
section.bind('<<ComboboxSelected>>', c)
section.pack(side='top', pady=(40,0))

# Target Choice
style.configure('Target.TButton', foreground='white', padding=(55,0))
style.map('Target.TButton', background = [('active', "#474746"), ("!pressed", "#3d3c3b"), ("pressed", "#474746")])
target = ttk.Button(side_panel, text='Target', style='Target.TButton', takefocus=0, command=folder_pick)
target.pack(side='top', pady=(40,0))

# Tag Color Choice
tag_choice = tk.StringVar()
tag_color = ttk.Combobox(side_panel, width=20, height=10, values=[" Red Tag", " Orange Tag", ' Green Tag', ' Purple Tag'], state='readonly', style='Custom.TCombobox', textvariable=tag_choice)
tag_color.set('Tag Color')
tag_color.bind('<<ComboboxSelected>>', c)
tag_color.pack(side='top', pady=(40,0))

# Reset Button
style.configure('Clear.TButton', foreground='white', padding=(2,0))
style.map('Clear.TButton', background = [('active', "#474746"), ("!pressed", "#3d3c3b"), ("pressed", "#474746")])
clear = ttk.Button(side_panel, text='↺', takefocus=0, style='Clear.TButton', width=2, command=clear_func)
clear.pack(side='bottom',anchor='e', pady=(0,10), padx=(0,5))

# Start Scan
style.configure('Scan.TButton', foreground='white', padding=(55,0))
style.map('Scan.TButton', background = [('active', "#474746"), ("!pressed", "#3d3c3b"), ("pressed", "#474746")])
scan = ttk.Button(side_panel, text='Scan', style='Scan.TButton', takefocus=0, command=run_scan)
scan.pack(side='top', pady=(80,0))

# Deco Lines
deco_line1 = tk.Frame(side_panel, width=225, height=4, bg="#2A2A2A")
deco_line1.pack(side='top', pady=(15,0), padx=(4,0))
deco_line2 = tk.Frame(side_panel, width=215, height=3, bg="#2A2A2A")
deco_line2.pack(side='top', pady=(4,0), padx=(4,0))

# Clean Log
style.configure('Clean.TButton', foreground='white', padding=(2,0))
style.map('Clean.TButton', background = [('active', "#474746"), ("!pressed", "#3d3c3b"), ("pressed", "#474746")])
clean = ttk.Button(side_panel, text='⌫', style='Clean.TButton', takefocus=0, width=2, command=clean_log)
clean.pack(side='bottom',anchor='e', pady=(0,10), padx=(0,5))

# Log Panel
log_panel = tk.Frame(root, width=290, height=440)
log_panel.pack(side='right', expand=True, fill='both', pady=(5,0), padx=(5,0))
log_panel.pack_propagate(False)

# List Box Log
logbox = tk.Listbox(log_panel, activestyle='none', bg="#2C2C2C", fg="#ffffff", selectbackground="#1D1D1D",selectforeground='#ffffff')
logbox.pack(side='left', expand=True, fill='both')

clear_func()
root.mainloop()