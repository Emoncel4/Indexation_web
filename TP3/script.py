from DataImport import import_json_data

title_index = import_json_data("input/title_index.json")

description_index = import_json_data("input/description_index.json")

origin_index = import_json_data("input/origin_index.json")

brand_index = import_json_data("input/brand_index.json")

reviews_index = import_json_data("input/reviews_index.json")


from Tokenization import normalize_request
test = "I want to have some spanish chocolate from the Alps %!"

test = normalize_request(test)