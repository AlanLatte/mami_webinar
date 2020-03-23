import os


def get_abs_path() -> str:
    os.chdir(
        os.path.abspath(
            os.path.join(
                os.path.join(
                    os.path.join(__file__, os.pardir),
                    os.pardir
                ),
                os.pardir
            )
        )
    )
    return os.getcwd()

def get_google_api_key_path(google_api_dir_path):
    """
    get_google_api_key_path() accepts 1 main parameters:
        abs_path to dir with api.json file

        Only 1 json file should be in the directory
    """
    files = os.listdir(INPUT_DIR_PATH)
    api_keys = filter(lambda x: x.endswith('.json'), files)
    if len(api_keys) > 1:
        print(__doc__).sys.exit()
    api_key_file_path = os.path.join(google_api_dir_path, api_keys[0])
    return api_key_file_path
