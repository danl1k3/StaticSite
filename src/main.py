import os
import shutil
from copy_dir_content import copy_dir_content
from generate_page import generate_page

def main():
    source_dir = "static"
    dest_dir = "public"

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    copy_dir_content(source_dir, dest_dir)

    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    
    generate_page(from_path, template_path, dest_path)
    

if __name__ == "__main__":
    main()
