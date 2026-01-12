import json
from Extraction import extract_content_function, extract_title, extract_links, extract_description

def prioritize_link_with_product(links):
    return sorted(links, key=lambda link: "product" not in link)

def create_json_datafile_with_crawler(start_url, limit):

    visited = set()
    to_visit = [start_url]
    json_file = []

    while to_visit and len(json_file) < limit:
        url = to_visit.pop(0)
        if url in visited:
            continue

        visited.add(url)

        # Extraire le contenu
        soup_content = extract_content_function(url)
        link_list = extract_links(soup_content)

        # Ajouter les nouvelles pages à visiter
        for link in link_list:
            if link not in visited and link not in to_visit:
                to_visit.append(link)
        # Prioriser les liens contenant "product" pour la prochaine itération
        to_visit = prioritize_link_with_product(to_visit)

        # Créer l'entrée JSON pour cette page
        json_page_data = {
            "url": url,
            "title": extract_title(soup_content),
            "description": extract_description(soup_content),
            "links": link_list
        }

        json_file.append(json_page_data)

    # Sauvegarder dans un fichier JSON
    with open("crawler_data.json", "w", encoding="utf-8") as f:
        json.dump(json_file, f, indent=4)

    return json_file

create_json_datafile_with_crawler("https://web-scraping.dev/products",50)