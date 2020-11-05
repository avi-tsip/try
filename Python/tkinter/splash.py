from tkinter import *

splash = Tk()
splash.overrideredirect(True)
splash.geometry('600x500')

splash_label = Label(splash, text='Splash Screen', font=('Helvetica', 18))
splash_label.pack(pady=20)



def main_window():
    splash.destroy()
    root = Tk()
    root.title('Avi Tsipshtein - My App')
    root.iconbitmap('coffee.ico')
    root.geometry('600x500')

    root_label = Label(root, text='Main App', font=('Helvetica', 18))
    root_label.pack(pady=20)
    

splash.after(3000, main_window)


mainloop()