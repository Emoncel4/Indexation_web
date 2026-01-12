from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
import json
import time

#Crawler
USER_AGENT = "Crawler/1.0 (+emile.moncel@eleve-ensai.fr)"

#Delai
CRAWL_DELAY = 1.0

# Dernier accès
LAST_REQUEST_TIME = {}

def apply_politeness(url):
    domain = urlparse(url).netloc
    now = time.time()

    #Si on a déjà requete le nom de domaine d'un site on attend une seconde avant de le requêter à nouveau
    if domain in LAST_REQUEST_TIME: 
        elapsed = now - LAST_REQUEST_TIME[domain]
        if elapsed < CRAWL_DELAY:
            time.sleep(CRAWL_DELAY - elapsed)

    LAST_REQUEST_TIME[domain] = time.time()

#Requete get avec gestion des erreurs 
def http_get(url):
    apply_politeness(url)

    request = Request(
        url,
        method="GET",
        headers={"User-Agent": USER_AGENT}
    )

    try:
        with urlopen(request) as response:
            return response.read().decode("utf-8")

    except HTTPError as e:
        print(f"HTTP error {e.code} for {url}")
    except URLError as e:
        print(f"URL error for {url}: {e.reason}")

    return None

#Requete post (voir si utile)
def http_post(url, data):
    apply_politeness(url)

    data_bytes = json.dumps(data).encode("utf-8")

    request = Request(
        url,
        data=data_bytes,
        method="POST",
        headers={
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json"
        }
    )

    try:
        with urlopen(request) as response:
            return response.read().decode("utf-8")

    except HTTPError as e:
        print(f"HTTP error {e.code} for {url}")
    except URLError as e:
        print(f"URL error for {url}: {e.reason}")

    return None
