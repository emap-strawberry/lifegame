import tkinter as tk

app = tk.Tk()
labelExample = tk.Label(
    app,
    text="ラベルのサンプル",
    bg="#ff5357",
    fg="#383347",
    font=("コーポレート・ロゴＭ", 40))
labelExample.pack()
app.mainloop()