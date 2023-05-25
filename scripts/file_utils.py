import os


def project_dir():
    """
    Returns path to the project root
    Returns
    -------
    Path
        Return path to the project root
    """
    return os.path.dirname(os.path.dirname(__file__))