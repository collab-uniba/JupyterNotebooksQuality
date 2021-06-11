from pynblint.notebook import Notebook
from pathlib import Path
import pytest

if __name__ == '__main__':
    pytest.main()


@pytest.fixture(scope="module")
def notebooks():
    nb1 = Notebook(Path("../fixtures", "FullNotebook2.ipynb"))
    nb2 = Notebook(Path("../fixtures", "FullNotebook.ipynb"))
    nb3 = Notebook(Path("../fixtures", "JustMarkdown.ipynb"))
    nb4 = Notebook(Path("../fixtures", "DefectiveNotebook.ipynb"))
    return {
        "FullNotebook2.ipynb": nb1,
        "FullNotebook.ipynb": nb2,
        "JustMarkdown.ipynb": nb3,
        "DefectiveNotebook.ipynb": nb4
    }


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 3),
    ("FullNotebook.ipynb", 15)
])
def test_count_cells(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["notebookStats"]["numberOfCells"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 0),
    ("FullNotebook.ipynb", 5)
])
def test_count_md_cells(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["notebookStats"][
               "numberOfMDCells"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("JustMarkdown.ipynb", 0),
    ("FullNotebook.ipynb", 9)
])
def test_count_code_cells(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["notebookStats"][
               "numberOfCodeCells"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 0),
    ("FullNotebook.ipynb", 1)
])
def test_count_raw_cells(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["notebookStats"][
               "numberOfRawCells"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", False),
    ("FullNotebook.ipynb", True)
])
def test_has_linear_execution_order(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "linearExecutionOrder"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 1),
    ("FullNotebook.ipynb", 0)
])
def test_count_class_defs(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "numberOfClassDefinitions"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 0),
    ("FullNotebook.ipynb", 1)
])
def test_count_func_defs(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "numberOfFunctionDefinitions"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", False),
    ("FullNotebook.ipynb", True)
])
def test_are_imports_in_first_cell(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "allImportsInFirstCell"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 0),
    ("FullNotebook.ipynb", 8)
])
def test_count_md_lines(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "numberOfMarkdownLines"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 0),
    ("FullNotebook.ipynb", 1)
])
def test_count_md_titles(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "numberOfMarkdownTitles"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", None),
    ("FullNotebook.ipynb", 0.375)
])
def test_get_bottom_md_lines_ratio(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "bottomMarkdownLinesRatio"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 0),
    ("DefectiveNotebook.ipynb", 2)
])
def test_count_non_executed_cells(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "nonExecutedCells"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", 0),
    ("DefectiveNotebook.ipynb", 1)
])
def test_count_empty_cells(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "emptyCells"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", None),
    ("DefectiveNotebook.ipynb", 1)
])
def test_count_bottom_non_executed_cells(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "bottomNonExecutedCells"] == expected


@pytest.mark.parametrize("test_input,expected", [
    ("FullNotebook2.ipynb", None),
    ("DefectiveNotebook.ipynb", 1)
])
def test_count_bottom_empty_cells(test_input, expected, notebooks):
    assert notebooks[test_input].get_pynblint_results()["lintingResults"][
               "bottomEmptyCells"] == expected
