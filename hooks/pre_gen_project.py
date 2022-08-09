def check_project_slug(project_slug: str) -> None:
    if not hasattr(project_slug, "isidentifier"):
        raise TypeError("Project Slug must be a string")

    if not project_slug.isidentifier():
        raise ValueError(
            "Project slug is not a valid Python identifier, a "
            "valid identifier cannot start with a number, or "
            "contain any spaces."
        )

    if not project_slug == project_slug.lower():
        raise ValueError("Project slug should be all lowercase")


def check_vscode_settings(vscode_settings: str) -> None:
    if vscode_settings.lower() not in ["y", "n", "yes", "no"]:
        raise ValueError("Vscode Settings option must be ['y', 'n', 'yes', 'no']")


if __name__ == "__main__":
    check_project_slug("{{ cookiecutter.project_slug }}")
    check_vscode_settings("{{ cookiecutter.vscode_settings }}")
