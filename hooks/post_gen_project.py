import os
import shutil


def delete_file_or_directory(file_path: str):
    file_path = file_path.strip()
    if file_path and os.path.exists(file_path):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.unlink(file_path)


def check_negative_choice(choice: str) -> bool:
    return choice.lower() in ["n", "no"]


def main():
    if check_negative_choice("{{ cookiecutter.vscode_settings }}"):
        delete_file_or_directory(".vscode")
    if check_negative_choice("{{ cookiecutter.poetry_env_in_project }}"):
        delete_file_or_directory("poetry.toml")


if __name__ == "__main__":
    main()
