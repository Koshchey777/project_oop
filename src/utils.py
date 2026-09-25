import json
import os


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as f:
        read_data = json.load(f)
        return read_data
