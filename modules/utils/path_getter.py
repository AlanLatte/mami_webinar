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
