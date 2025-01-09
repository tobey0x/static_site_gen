from pathlib import Path
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
    html = markdown_to_html_node(markdown)
    
    template = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html.to_html()
    )

    if not dest_path.parent.exists():
        dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    if dest_path == Path(dest_path)/'':
        dest_file = dest_path / "index.html"
        dest_path = dest_file

    dest_path.write_text(template)


def main():
    project_root = Path.cwd()
    public_dir_in_dest = project_root / "public"
    static_dir_in_src = project_root / "static"
    
    
    if public_dir_in_dest.exists():
        shutil.rmtree(public_dir_in_dest)
        
    recursive_copy_directory(static_dir_in_src, public_dir_in_dest)
    
    from_path = project_root / "content/index.md"
    template_path = project_root / "template.html"
    dest_path = project_root / "public"
    
    generate_page(from_path, template_path, dest_path)

main()