import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import simpledialog


def rename():
    directory = directory_entry.get()
    base_name = name_entry.get()

    if not directory or not  base_name:
        messagebox.showwarning("Aviso", "Informe a pasta e o nome base!")
        return

    try:
    # lista todos os arquivos com seus tempos de modificação

        files = [
            (name, os.path.getmtime(os.path.join(directory, name)))
            for name in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, name)) 
        ] 

        # ordena do mais novo ao mais antigo

        files.sort(key=lambda x: x[1], reverse=True)

        # Renomeia os arquivos
        for i, (name_file, _) in enumerate(files, start=1):
            old_path = os.path.join(directory, name_file)
            extension = os.path.splitext(name_file)[1]
            new_name = f"{base_name} {i}{extension}"
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)

        messagebox.showinfo("Sucesso", f"Arquivos renomeados com sucesso na pasta:\n{directory}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def selecionar_pasta():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

# Janela principal
root = tk.Tk()
root.title("Renomeador de Arquivos")
root.geometry("400x200")

# Widgets
tk.Label(root, text="Pasta:").pack(pady=5)
directory_entry = tk.Entry(root, width=50)
directory_entry.pack()
tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta).pack(pady=5)

tk.Label(root, text="Nome base:").pack(pady=5)
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Button(root, text="Renomear", command=rename).pack(pady=20)

root.mainloop()