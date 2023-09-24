import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.font import Font
import keyword

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

def cut_text():
    text.event_generate("<<Cut>>")

def copy_text():
    text.event_generate("<<Copy>>")

def paste_text():
    text.event_generate("<<Paste>>")

def change_font():
    font = Font(family="Helvetica", size=12)
    text.config(font=font)

def highlight_syntax(event):
    for keyword in keywords:
        start = "1.0"
        while True:
            start = text.search(keyword, start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(keyword)}c"
            text.tag_add("keyword", start, end)
            start = end

root = tk.Tk()
root.title("PythonText - By Giovanni Carlino")
root.geometry("800x600")

# Creazione di un widget di testo avanzato con barra di scorrimento
text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text.pack(fill=tk.BOTH, expand=True)

# Creazione di un menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Apri", command=open_file)
file_menu.add_command(label="Salva", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Esci", command=root.quit)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Modifica", menu=edit_menu)
edit_menu.add_command(label="Taglia", command=cut_text)
edit_menu.add_command(label="Copia", command=copy_text)
edit_menu.add_command(label="Incolla", command=paste_text)

format_menu = tk.Menu(menu)
menu.add_cascade(label="Formato", menu=format_menu)
format_menu.add_command(label="Cambia Font", command=change_font)

# Evidenzia la sintassi delle parole chiave del linguaggio Python
keywords = keyword.kwlist
text.tag_configure("keyword", foreground="blue", font=("Helvetica", 12, "bold"))
text.bind("<KeyRelease>", highlight_syntax)

root.mainloop()
