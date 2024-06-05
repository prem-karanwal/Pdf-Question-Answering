import os
from fastapi import UploadFile

UP_DIR = "./uploaded_files"

if not os.path.exists(UP_DIR):
    os.makedirs(UP_DIR)

def save_file(file: UploadFile):
    file_path = os.path.join(UP_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path
