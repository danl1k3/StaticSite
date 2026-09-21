import os
import shutil
from copy_dir_content import copy_dir_content
from generate_pages_recursive import generate_pages_recursive

def main():
    source_dir = "static"
    dest_dir = "public"

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    copy_dir_content(source_dir, dest_dir)

    from_path = "content"
    template_path = "template.html"
    dest_path = "public"
    
    generate_pages_recursive(from_path, template_path, dest_path)
    

if __name__ == "__main__":
    main()
