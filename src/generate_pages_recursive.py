from generate_page import generate_page
import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        full_path_from = os.path.join(dir_path_content, entry)
        full_path_where = os.path.join(dest_dir_path, entry)
        if os.path.isdir(full_path_from):
            generate_pages_recursive(full_path_from, template_path, full_path_where, basepath)
        else:
            full_path_where = full_path_where.replace('.md', ".html")
            generate_page(full_path_from, template_path, full_path_where, basepath)

