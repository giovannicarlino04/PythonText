import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("PythonText - By Giovanni Carlino")

# Creazione di un widget di testo
text = tk.Text(root)
text.pack()

# Creazione di un menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Apri", command=open_file)
file_menu.add_command(label="Salva", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Esci", command=root.quit)

root.mainloop()
