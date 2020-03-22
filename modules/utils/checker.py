from modules.consts.common import INPUT_FOLDER, OUTPUT_FOLDER
from modules.utils.path_getter import get_abs_path
from modules.consts.common import INPUT_FOLDER, OUTPUT_FOLDER, ABS_PATH
import os


def make_folder(folder_name):
    os.mkdir(
        os.path.join(
            ABS_PATH, folder_name
        )
    )


def check_required_folders():
    if INPUT_FOLDER not in os.listdir(ABS_PATH):
        make_folder(folder_name=INPUT_FOLDER)
    if OUTPUT_FOLDER not in os.listdir(ABS_PATH):
        make_folder(folder_name=OUTPUT_FOLDER)