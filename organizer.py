import os
import shutil
from config import FILE_TYPES
from utils import get_category

def organize_folder(path):
    if not os.path.exists(path):
        print("Invalid path!")
        return

    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            continue

        category = get_category(file)

        target_folder = os.path.join(path, category)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        move_file(file_path, target_folder)

    print("Folder organized successfully!")

def move_file(file_path, target_folder):
    filename = os.path.basename(file_path)
    target_path = os.path.join(target_folder, filename)

    count = 1
    while os.path.exists(target_path):
        name, ext = os.path.splitext(filename)
        target_path = os.path.join(target_folder, f"{name}_{count}{ext}")
        count += 1

    shutil.move(file_path, target_path)
