import os
import shutil


def copy_static(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)

    os.mkdir(dest)

    copy_recursive(source, dest)


def copy_recursive(source, dest):
    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        dest_path = os.path.join(dest, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            os.mkdir(dest_path)
            copy_recursive(from_path, dest_path)