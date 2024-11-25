import os
import shutil

import py7zr

from modules import loger as lg

from database.connect import database as db


def export(id_: int, to_path: str) -> None:
    folder_path = f'widgets/w_{id_}'
    with py7zr.SevenZipFile(to_path, mode='w') as zip_:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file = os.path.join(root, file)
                zip_.write(file, os.path.relpath(file, folder_path))
    lg.info(f'export succes ({folder_path} --> {to_path})')


def import_(path: str) -> None:
    id_ = db.new_widget(os.path.splitext(os.path.basename(path))[0])
    output_folder = f'widgets/w_{id_}'

    os.makedirs(output_folder, exist_ok=True)

    with py7zr.SevenZipFile(path, mode='r') as zip_:
        zip_.extractall(path=output_folder)

    lg.info(f'import succes ({path} --> {output_folder})')


def import_from_folder(path: str) -> None:
    for file_name in ['main.py', 'config.py', 'preview.png']:
        file = os.path.join(path, file_name)
        if not os.path.exists(file):
            lg.warn(f'cant import: file {file_name} dont exists')
            return
    
    id_ = db.new_widget(os.path.splitext(os.path.basename(path))[0])
    output_folder = f'widgets/w_{id_}'

    shutil.copytree(path, output_folder)