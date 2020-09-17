import tkinter as tk
from tkinter import filedialog, Text
import os

win = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        reader = f.read()
        reader = reader.split(',')
        apps = [x for x in reader if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes=(('Executables', '*.exe'),('All Files', '*.*')))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()
    
def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(win, height=700, width=400, bg='#51d0de')
canvas.pack()

frame = tk.Frame(win, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(win, text="Open File", padx=10, pady=5, fg='white', bg='#263D42', command=addApp)
openFile.pack()
runApps = tk.Button(win, text="Run Apps", padx=10, pady=5, fg='white', bg='#263D42', command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app, bg='gray')
    label.pack()

win.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')