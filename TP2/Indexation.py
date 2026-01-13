import re

def tokenize(string):
    lower_string = str.lower(string)
    lower_string_without_alphanum = re.sub(r"[^\w\s]", "", lower_string, flags=re.UNICODE) #We keep only alphanumerical characters except spaces
    #List of stopwords found on internet
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    token_list = lower_string_without_alphanum.split()
    clean_token_list = [token for token in token_list if token not in stopwords]
    return clean_token_list

from collections import defaultdict

def create_inverted_title_index(data):
    #Tokenisation
    data["title_token"] = data["title"].apply(tokenize)

    inverted_index = defaultdict(dict) #Creating a dictionnary to store data

    for index, row in data.iterrows(): #We want to go from rows to column so we have to iter on rows
        url = row["url"]
        tokens = row["title_token"]
        for position, token in enumerate(tokens): #To store the position of the and values of the tokens in the token list
            if token not in inverted_index:
                inverted_index[token] = {} #If not a key we create the key corresponding in the dictionnary
            if url not in inverted_index[token]:
                inverted_index[token][url] = [] #Create a value of each url that contains the token which is a list where we store the position of the token
            inverted_index[token][url].append(position)

    return inverted_index

def create_inverted_description_index(data):
    #Tokenisation
    data["description_token"] = data["description"].apply(tokenize)

    inverted_index = defaultdict(dict) #Creating a dictionnary to store data

    for index, row in data.iterrows(): #We want to go from rows to column so we have to iter on rows
        url = row["url"]
        tokens = row["description_token"]
        for position, token in enumerate(tokens): #To store the position of the and values of the tokens in the token list
            if token not in inverted_index:
                inverted_index[token] = {} #If not a key we create the key corresponding in the dictionnary
            if url not in inverted_index[token]:
                inverted_index[token][url] = [] #Create a value of each url that contains the token which is a list where we store the position of the token
            inverted_index[token][url].append(position)

    return inverted_index

from ReviewHandler import calculate_mean_review, calculate_number_review, find_last_review

def create_review_index(data):

    review_index = defaultdict(dict)

    for index, row in data.iterrows():
        url = row["url"]
        review=row["product_reviews"]
        review_index[url]={
            "total_reviews":calculate_number_review(review),
            "mean_mark":calculate_mean_review(review),
            "last_rating":find_last_review(review)
        }
    return review_index
