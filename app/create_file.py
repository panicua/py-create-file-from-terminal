import argparse
import datetime
import os


def terminal_to_file() -> None:
    parser = argparse.ArgumentParser(
        description="The app creates folders/files, "
                    "writes inside of those files"
    )
    parser.add_argument("-d",
                        nargs="+",
                        default=[],
                        help="\"-d dir1 dir2\" "
                             "- creates directory \"dir1/dir2\".")
    parser.add_argument("-f",
                        type=str,
                        default=None,
                        help="\"-f file.txt\" "
                             "- creates \"file.txt\" in current directory.")

    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        raise argparse.ArgumentError

    d_arguments, f_argument = args.d, args.f

    if d_arguments:
        create_folder(d_arguments)
    if f_argument:
        create_file(d_arguments, f_argument)


def create_folder(list_args_dir: list) -> None:
    universal_path = os.path.join(*list_args_dir)
    try:
        os.makedirs(universal_path, exist_ok=True)
    except OSError as e:
        raise OSError(f"{e}. Path is invalid, check "
                      f"for unaccepted symbols: '{universal_path}'")


def create_file(list_args_dir: list, file_name: str) -> None:
    if list_args_dir:
        universal_path = os.path.join(*list_args_dir)
    else:
        universal_path = ""

    universal_path = os.path.join(universal_path, file_name)

    if not os.path.exists(universal_path):
        writing_to_file(universal_path, "w")
    else:
        writing_to_file(universal_path, "a")


def writing_to_file(path: str, mode: str, full_message: str = "") -> None:
    with open(path, mode) as file:
        while True:
            message = input("content line: ") + "\n"
            if message == "stop\n":
                full_message += "\n"
                break
            full_message += message
        file.write(datetime.date.strftime(datetime.datetime.now(),
                                          "%Y-%m-%d %H:%M:%S") + "\n")
        file.write(full_message)


terminal_to_file()
