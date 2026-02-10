import os 
from markdown_to_html_node import markdown_to_html_node 
from extract_title import extract_title
import pathlib


def generate_page(from_path, template_path, dest_path):
    print(f"Beep Boop ...Generating Page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    markdown_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", markdown_html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            new_dest_path = pathlib.Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, new_dest_path)
        else: 
            generate_pages_recursive(from_path, template_path, dest_path)