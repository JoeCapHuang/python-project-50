import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('filepath1, filepath2, expected_filepath',
                         [
                             ("tests/fixtures/file1.json",
                              "tests/fixtures/file2.json",
                              "tests/fixtures/expected_result"
                              ),
                          ]
                         )
def test_generate_diff(filepath1, filepath2, expected_filepath):
    with (
        open(expected_filepath) as expected_file,
    ):
        expected = expected_file.read()
        result = generate_diff(filepath1, filepath2)
        assert result == expected
