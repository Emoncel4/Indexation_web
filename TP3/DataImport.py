import json

def import_json_data(json_path):
    with open(json_path, encoding='utf-8') as f:
        df = json.load(f)
        return df
