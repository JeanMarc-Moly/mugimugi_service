PYTHON_ENV = ".python_env"
PYTHON_BIN = f"{PYTHON_ENV}/bin"
PYTHON_EXE = f"{PYTHON_BIN}/python"
ISORT = f"{PYTHON_BIN}/isort"
BLACK = f"{PYTHON_BIN}/black"

SRC = "mugimugi"
TEST = "test"


def task_prod_env():
    return dict(
        actions=[
            ["git", "config", "core.hooksPath", ".git-hooks"],
            ["conda", "install", "-n", "base", "-c", "conda-forge", "mamba"],
            [
                "mamba",
                "env",
                "create",
                "--file",
                "envs/base/environment.prod.yml",
                "--prefix",
                PYTHON_ENV,
            ],
        ],
        targets=[PYTHON_EXE],
        uptodate=[True],
    )


def task_dev_env():
    return dict(
        file_dep=[PYTHON_EXE],
        actions=[
            [
                "mamba",
                "env",
                "update",
                "--file",
                "envs/base/environment.dev.yml",
                "--prefix",
                PYTHON_ENV,
            ]
        ],
        targets=[BLACK, ISORT],
        uptodate=[True],
    )


def task_format():
    return dict(
        file_dep=[BLACK, ISORT],
        actions=[
            [ISORT, SRC],
            [BLACK, SRC],
            [ISORT, TEST],
            [BLACK, TEST],
            [BLACK, "dodo.py"],
        ],
        uptodate=[False],
    )


def task_test():
    return dict(
        file_dep=[PYTHON_EXE],
        actions=[[PYTHON_EXE, "-m", "unittest", "discover", "--start-directory", TEST]],
        uptodate=[False],
    )
