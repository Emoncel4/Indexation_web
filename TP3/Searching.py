from DataImport import import_json_data
from Tokenization import normalize_request

TITLE_INDEX = import_json_data("input/title_index.json")

DESCRIPTION_INDEX = import_json_data("input/description_index.json")

ORIGIN_INDEX = import_json_data("input/origin_index.json")

BRAND_INDEX = import_json_data("input/brand_index.json")

from collections import defaultdict

import re 

def find_token(token, page):
    token_localisation = defaultdict(dict)
    
    if token in TITLE_INDEX:
        for url in TITLE_INDEX[token]:
            if re.search(re.escape(page) + "$", url):
                token_localisation["title"] = TITLE_INDEX[token][url]
                break

    if token in DESCRIPTION_INDEX:
        for url in DESCRIPTION_INDEX[token]:
            if re.search(re.escape(page) + "$", url):
                token_localisation["description"] = DESCRIPTION_INDEX[token][url]
                break
    
    if token in ORIGIN_INDEX:
        for url in ORIGIN_INDEX[token]:
            if re.search(re.escape(page) + "$", url):
                token_localisation["origin"] = ORIGIN_INDEX[token][url]
                break
    
    if token in BRAND_INDEX:
        for url in BRAND_INDEX[token]:
            if re.search(re.escape(page) + "$", url):
                token_localisation["brand"] = BRAND_INDEX[token][url]
                break

    if token_localisation == {}:
        return None
    else:
        return token_localisation

def find_all_token(request, page):
    rq = normalize_request(request)
    list_localisation = []
    for token in rq:
        search_result = find_token(token,page)
        if search_result is None :
            return None
        else:
            list_localisation.append(search_result)

    return list_localisation

test = find_token("Box of Chocolate","https://web-scraping.dev/product/1")
print(test)