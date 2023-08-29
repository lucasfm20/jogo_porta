import tkinter as tk

def button_click():
    label.config(text="Botão foi clicado!")

root = tk.Tk()
root.title("Minha Janela")

label = tk.Label(root, text="Olá, Tkinter!")
button = tk.Button(root, text="Clique em mim", command=button_click)
entry = tk.Entry(root)

label.pack()
button.pack()
entry.pack()

root.mainloop()
