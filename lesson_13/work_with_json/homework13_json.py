"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
Pезультат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

import json
import logging
from pathlib import Path

def json_validation(folder_name):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handler = logging.FileHandler('json__bondarenko.log')
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    base_dir = Path(__file__).parent
    while base_dir.name != "aqa_090125" and base_dir.parent != base_dir:
        base_dir = base_dir.parent
    directory = next(base_dir.rglob(folder_name), None)
    if not directory:
        print(f"Папка '{folder_name}' не знайдена в репозитории.")
        return

    for files in directory.iterdir():
        if files.is_file() and files.suffix == ".json":
            try:
                with open(files, 'r',  encoding='utf-8') as file:
                    json.load(file)
            except json.JSONDecodeError:
                logger.error(f"Файл {files} має невалідний синтаксис та не може бути розібранним.")

#json_validation('work_with_json')