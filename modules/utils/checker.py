import os

from modules.consts.common import ABS_PATH, INPUT_FOLDER, OUTPUT_FOLDER


def make_folder(folder_name):
    os.mkdir(os.path.join(ABS_PATH, folder_name))


def check_required_folders():
    if INPUT_FOLDER not in os.listdir(ABS_PATH):
        make_folder(folder_name=INPUT_FOLDER)
    if OUTPUT_FOLDER not in os.listdir(ABS_PATH):
        make_folder(folder_name=OUTPUT_FOLDER)
