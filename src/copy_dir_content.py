import os
import shutil


def copy_dir_content(src: str, dst: str) -> None:
    if not os.path.exists(dst):
        os.mkdir(dst)

    items = os.listdir(src)
    print(f"Current list of dirs:\n {items}")
    for item in items:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Entering directory: {src_path}")
            copy_dir_content(src_path, dst_path)
