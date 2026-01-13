from DataImport import import_jsonl_data, extract_product_id, extract_variant

data = import_jsonl_data("input/products.jsonl")
df_product = extract_product_id(data)
df_product = extract_variant(df_product)
print(df_product[["url", "product_id", "variant"]])

from Indexation import create_inverted_title_index, create_inverted_description_index

import json 

# inverted_title_index = create_inverted_title_index(df_product)
# with open("output/inverted_title_index.json", "w") as f:
#     json.dump(inverted_title_index, f, indent=2)

# inverted_description_index = create_inverted_description_index(df_product)
# with open("output/inverted_description_index.json", "w") as f:
#     json.dump(inverted_description_index, f, indent=2)

from Indexation import create_review_index

review_index = create_review_index(df_product)
with open("output/review_index.json", "w") as f:
    json.dump(review_index, f, indent=2)