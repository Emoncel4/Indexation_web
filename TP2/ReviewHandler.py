def calculate_mean_review(reviews):
    sum = 0
    if len(reviews) != 0:
        for review in reviews :
            sum = sum + float(review['rating'])
        return sum / len(reviews)
    else : 
        return 0
        
def calculate_number_review(reviews):
    return len(reviews)


def find_last_review(reviews):
    if len(reviews) != 0:
        last_review = max(reviews, key=lambda x: x['date'])
        return last_review['rating']
    else : 
        return 0
    