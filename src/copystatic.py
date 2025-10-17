import os, shutil

def copy_content(source, destination):
    if not os.path.exists(source):
        raise ValueError(f"Source {source} n'existe pas")
    
    if not os.path.exists(destination):
        os.mkdir(destination)
    
    entries = os.listdir(source)
    
    for entry in entries:
        source_path = os.path.join(source, entry)
        dest_path = os.path.join(destination, entry)
        print(f"Copié: {source_path} → {dest_path}")
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_content(source_path, dest_path)