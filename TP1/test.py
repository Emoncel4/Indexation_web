from Request import http_get
from Parsing import html_parser

page = http_get("https://web-scraping.dev/products")
#print(page)
parse = html_parser(page)
print(parse)