import os
import shutil


def remove_vscode_settings():
    vscode_settings_path = ".vscode"
    if os.path.exists(vscode_settings_path):
        shutil.rmtree(vscode_settings_path)


def main():
    if "{{ cookiecutter.vscode_settings }}".lower() in ["n", "no"]:
        remove_vscode_settings()


if __name__ == "__main__":
    main()
