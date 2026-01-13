import json
import pandas as pd

def import_json_data(json_path):
    with open(json_path, encoding='utf-8') as f:
        df = json.load(f)
        return pd.DataFrame(df)

def import_jsonl_data(path):
    data = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error: {e} at line: {line}")
    return pd.DataFrame(data)

import re

def find_pattern_url(pattern, url):
    match = re.search(pattern, str(url))
    if match:
        return match.group(1)
    return None

def extract_product_id(df):
    df["product_id"] = df["url"].apply(lambda url: find_pattern_url(r"/product/(\d+)", url))
    return df


def extract_variant(df):
    df["variant"] = df["url"].apply(lambda url: find_pattern_url(r"variant=([a-z]+)", url))
    return df
