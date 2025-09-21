import os
from datetime import datetime

# pasta que será usada 
directory = r"C:\Users\Edith Carollaine\OneDrive\Documentos\pasta teste"

base_name = "meu arquivo"

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


print("Arquivos renomeados com sucesso!")