import re
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
from DataImport import import_json_data

STOPWORDS = stopwords.words("english")
SYNONYM_INDEX = import_json_data("input/origin_synonyms.json")

def tokenize(string):
    lower_string = str.lower(string)
    lower_string_without_alphanum = re.sub(r"[^\w\s]", "", lower_string, flags=re.UNICODE) #We keep only alphanumerical characters except spaces
    #List of stopwords from nltk
    token_list = lower_string_without_alphanum.split()
    clean_token_list = [token for token in token_list if token not in STOPWORDS]
    return clean_token_list

def replace_origin_synonyms(string,synonym_index):
    for value in synonym_index:
        for synonym in synonym_index[value]:
            if re.search(synonym+"(?:s|$)",string): #For all the fr not to be considered as France
                string = re.sub(synonym+"(?:s|$)",value,string)
    return string

def normalize_request(request):
    nrmlz_request = replace_origin_synonyms(request, synonym_index=SYNONYM_INDEX)
    return tokenize(nrmlz_request)