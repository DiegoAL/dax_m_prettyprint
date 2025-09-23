import tkinter as tk
from tkinter import filedialog

def selectPath():
    path = filedialog.askopenfilename(
        title="Selecione o arquivo",
        filetypes=(("Arquivo de Texto","*txt"), ("Todos os arquivos", "*.*"))
    )

    print(path)


mainwindow = tk.Tk()
mainwindow.title("Dax/M Prettyprint")
mainwindow.geometry("300x250")

tk.Label(mainwindow, text="teste").grid(row=1,column=1)
tk.Button(mainwindow, text="text" ,command=selectPath).grid(row=2,column=1)



# Mantem a janela aberta até que o evento de close ocorra
mainwindow.mainloop()