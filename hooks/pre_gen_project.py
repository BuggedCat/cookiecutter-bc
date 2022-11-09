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


def check_yes_or_no_option(option: str) -> None:
    if option.lower() not in ["y", "n", "yes", "no"]:
        raise ValueError("Vscode Settings option must be ['y', 'n', 'yes', 'no']")


if __name__ == "__main__":
    check_project_slug("{{ cookiecutter.project_slug }}")
    check_yes_or_no_option("{{ cookiecutter.vscode_settings }}")
    check_yes_or_no_option("{{ cookiecutter.poetry_env_in_project }}")
