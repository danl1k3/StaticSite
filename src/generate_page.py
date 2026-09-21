from markdown_to_html_node import markdown_to_html_node 
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown
    with open(from_path) as md_file:
        md = md_file.read()

    # Read template
    with open(template_path) as template_file:
        template = template_file.read()
    
    # Get the html string and title
    html_str = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    
    # Change the templates
    generated_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_str)
    generated_page = generated_page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
        
    dirs = os.path.dirname(dest_path)
    if not os.path.exists(dirs):  
        os.makedirs(dirs)

    with open(dest_path, "w") as f:
        f.write(generated_page)


