import config
import json
from notebooktoall.transform import transform_notebook


class Notebook:
    """
    This class stores the representations of a notebook
    on which pynblint functions are called
    """

    def __init__(self, notebook_path: str):
        # Importing the notebook as a Python dictionary
        with open(notebook_path) as f:
            self._nb_dict = json.load(f)

        # Importing the notebook as a Python script
        transform_notebook(ipynb_file=notebook_path, export_list=["py"])
        notebook_path = notebook_path.split("/")[-1]
        with open(notebook_path.replace(".ipynb", ".py")) as f:
            self._script = f.read()

    @property
    def nb_dict(self):
        return self._nb_dict

    @property
    def script(self):
        return self._script

    @nb_dict.setter
    def nb_dict(self, value):
        self._nb_dict = value

    @script.setter
    def script(self, value):
        self._script = value


class Repository:
    """
    This class stores data about a code repository
    """

    notebooks = []  # List of Notebook objects


class LocalRepository(Repository):
    """
    This class stores data about a local code repository
    """

    def __init__(self, path: str):
        # Decompresses the repo (if needed)
        # Then, crawls the repo's content searching for notebooks
        # When it finds a notebook, it appends it to the list of notebooks
        # e.g., notebooks.append(Notebook(path_where_the_nb_was_found))
        ...


class GitHubRepository(Repository):
    """
    This class stores data about a GitHub repository
    """

    def __init__(self, github_url: str):
        # Clones the repo
        # Crawls the repo's content searching for notebooks
        # When it finds a notebook, it appends it to the list of notebooks
        # e.g., notebooks.append(Notebook(path_where_the_nb_was_found))
        ...
