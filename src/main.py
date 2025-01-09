from textnode import TextNode
from pathlib import Path
import os
import shutil

def recursive_copy_directory(src, dest):
    if not dest.exists():
        dest.mkdir()
    
    for file in src.iterdir():
        if file.is_file():
            shutil.copy(file, dest)
        else:
            recursive_copy_directory(file, dest / file.name)
        
    


def main():
    project_root = Path.cwd()
    public_dir_in_dest = project_root / "public"
    static_dir_in_src = project_root / "static"
    
    
    if public_dir_in_dest.exists():
        shutil.rmtree(public_dir_in_dest)
        
    recursive_copy_directory(static_dir_in_src, public_dir_in_dest)

main()