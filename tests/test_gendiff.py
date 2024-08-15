import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('filepath1, filepath2, expected_filepath, format_name',
                         [
                             ("tests/fixtures/file1.json",
                              "tests/fixtures/file2.json",
                              "tests/fixtures/stylish_result",
                              "stylish"
                              ),
                             ("tests/fixtures/file1.yaml",
                              "tests/fixtures/file2.yaml",
                              "tests/fixtures/stylish_result",
                              "stylish"
                              ),
                             ("tests/fixtures/file1.json",
                              "tests/fixtures/file2.yaml",
                              "tests/fixtures/plain_result",
                              "plain"
                              ),
                          ]
                         )
def test_generate_diff(filepath1, filepath2, expected_filepath, format_name):
    with (
        open(expected_filepath) as expected_file,
    ):
        expected = expected_file.read()
        result = generate_diff(filepath1, filepath2, format_name)
        assert result == expected
