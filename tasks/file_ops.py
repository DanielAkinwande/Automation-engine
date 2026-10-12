import os
import shutil

def rename_files(folder):
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)

        if os.path.isfile(old_path):
            new_name = f"renamed_{filename}"
            new_path = os.path.join(folder, new_name)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")


def move_files(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    for file in os.listdir(src):
        shutil.move(os.path.join(src, file), dst)
        print(f"Moved: {file}")