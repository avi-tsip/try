import json
import os
import pytest
from pathlib import Path, PurePath
from main import InterviewDemo

FILE_NAME = "updated_file.json"
json_file = {}

def setup_module(module):
    global json_file
    demo_data = InterviewDemo(Path.cwd())
    demo_data.refactor_json()
    print('generating demo file')
    with open(PurePath(Path.cwd(), FILE_NAME)) as f:
        try:
            json_file = json.load(f)
        except Exception:
            raise json.JSONDecodeError('Bad Input', 'data.json', 1)

def teardown_module(module):
    print("deleting artifact")
    os.unlink(PurePath(Path.cwd(), FILE_NAME))

# @pytest.fixture(scope="module")
# def prepare_test_data():
#     demo_data = InterviewDemo(Path.cwd())
#     demo_data.refactor_json()
#     with open(PurePath(Path.cwd(), FILE_NAME)) as f:
#         try:
#             json_file = json.load(f)
#         except Exception:
#             raise json.JSONDecodeError('Bad Input', 'data.json', 1)
#     yield json_file
#     print("deleting artifact")
#     os.unlink(PurePath(Path.cwd(), FILE_NAME))

def test_no_white_spaces():
    """
    This test is checking that string values in the json file do not have white spaces
    """
    json_string = json_file['value2']
    assert ' ' not in json_string, f"Expected string to have no whitespace but instead got: {json_string}"

def test_no_duplicates():
    """
    This test is checking that list has no duplicate values in the json file
    """
    json_list = json_file['value3']
    assert len(json_list) == len(set(json_list)), f"Expected list to not have duplicates but instead got: {json_list}"

def test_correct_year():
    """
    This test is checking that timestamp year is 2001
    """
    for key, value in json_file.items():
        if key in ('value1', 'value4'):
            assert value[0:4] == '2001', f"Expected year to be 2001 but instead got {value[0:4]}"

