import os
import shutil
from copy_dir_content import copy_dir_content
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    source_dir = "static"
    dest_dir = "docs"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    copy_dir_content(source_dir, dest_dir)

    from_path = "content"
    template_path = "template.html"
    
    generate_pages_recursive(from_path, template_path, dest_dir, basepath)
    

if __name__ == "__main__":
    main()
