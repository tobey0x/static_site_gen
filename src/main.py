from pathlib import Path
import os
import shutil
from block_markdown import markdown_to_html_node


def recursive_copy_directory(src, dest):
    if not dest.exists():
        dest.mkdir()
    
    for file in src.iterdir():
        if file.is_file():
            shutil.copy(file, dest)
        else:
            recursive_copy_directory(file, dest / file.name)
        

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        markdown = f.read()
        
    with open(template_path) as f:
        template = f.read()
        
    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()
    
    template = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html
    )

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def main():
    project_root = Path.cwd()
    public_dir_in_dest = project_root / "public"
    static_dir_in_src = project_root / "static"
    
    
    if public_dir_in_dest.exists():
        shutil.rmtree(public_dir_in_dest)
        
    recursive_copy_directory(static_dir_in_src, public_dir_in_dest)
    
    from_path = project_root / "content"
    template_path = project_root / "template.html"
    dest_path = project_root / "public"
    
    generate_pages_recursive(from_path, template_path, dest_path)

main()