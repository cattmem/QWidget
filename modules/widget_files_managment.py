import os
import py7zr

from database.connect import database as db


def export(id_: int, to_path: str) -> None:
    folder_path = f'widgets\\w_{id_}'
    with py7zr.SevenZipFile(to_path, mode='w') as zip_:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file = os.path.join(root, file)
                zip_.write(file, os.path.relpath(file, folder_path))


def import_(path: str) -> None:
    id_ = db.new_widget(os.path.splitext(os.path.basename(path))[0])
    output_folder = f'widgets\\w_{id_}'

    os.makedirs(output_folder, exist_ok=True)

    with py7zr.SevenZipFile(path, mode='r') as zip_:
        zip_.extractall(path=output_folder)