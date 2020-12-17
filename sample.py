from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
    
app = tk.Tk()
app.title("Hello World")
app.mainloop()