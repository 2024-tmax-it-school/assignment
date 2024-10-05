import json
import os
from io import TextIOWrapper

"""
파일을 오픈하는 메소드

mode에 따라서, 파일을 읽기 또는 쓰기 모드로 오픈한다.
"""
def file_open(mode : str) -> TextIOWrapper:
    if os.path.exists('user_info.json'):
        return open('user_info.json', mode)
    else:
        with open('user_info.json', 'w') as f:
            f.write('{}')
        return open('user_info.json', mode)
    
"""
파이썬 딕셔너리를 JSON 파일로 저장하는 메소드
"""
def dict_to_json_file(data : dict):
    with file_open('w') as f:
        json.dump(data, f, ensure_ascii=False)

"""
파이썬 딕셔너리를 JSON 데이터로 변환하는 메소드
"""
def dict_to_json_data(data : dict) -> str:
    return json.dumps(data, ensure_ascii=False)

"""
JSON 파일을 파이썬 딕셔너리로 읽어오는 메소드
"""
def json_file_to_dict() -> dict:
    with file_open('r') as f:
        return json.load(f)

"""
JSON 데이터를 파이썬 딕셔너리로 변환하는 메소드
"""
def json_data_to_dict(data : str) -> dict:
    return json.loads(data)