from Request import http_get
from Parsing import parsing_allowed, parse_html

def extract_content_function(url):
    if parsing_allowed(url):
        response = http_get(url)
        return parse_html(response)
    else :
        raise Exception("Parsing not allowed")
    
def extract_title(soup):
    if soup.title:
        return soup.title.get_text(strip=True)
    return None

def extract_description(soup):
    p = soup.find("p")
    if p:
        return p.get_text(strip=True)
    return None

def extract_links(soup):
    links = []
    for a in soup.find_all("a", href=True):
        href = a.get("href")
        if href:
            links.append(href.strip())
    return links