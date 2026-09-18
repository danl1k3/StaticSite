import os
import shutil
from copy_dir_content import copy_dir_content

def main():
    source_dir = "static"
    dest_dir = "public"

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    copy_dir_content(source_dir, dest_dir)
    
if __name__ == "__main__":
    main()
