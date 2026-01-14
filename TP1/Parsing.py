from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

#Crawler
USER_AGENT = "Crawler/1.0 (+emile.moncel@eleve-ensai.fr)"

def parsing_allowed(url):
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"  #Pour avoir un lien de la forme nom_de_domaine/robots.txt

    rp = RobotFileParser()
    rp.set_url(robots_url) #Modifie l'URL référençant le fichier robots.txt.
    rp.read()

    return rp.can_fetch(USER_AGENT, url) #Renvoie True si useragent est autorisé à accéder à url selon les règles contenues dans le fichier robots.txt analysé.


from bs4 import BeautifulSoup
#Parse une page html
def parse_html(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    return(soup)
