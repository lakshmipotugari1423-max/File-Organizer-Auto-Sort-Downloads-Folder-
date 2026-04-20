import os
from config import FILE_TYPES

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category

    return "Others"
