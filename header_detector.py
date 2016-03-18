import nltk
import random
from built_in_page import BuiltInPage as bip

# def header_detector(header):

def header_features(header):
    sents = nltk.sent_tokenize(header)
    return {
        "ends_with_colon": header[-1] == ':',
        "single_sentence": len(sents) == 1
    }

def get_featureset():
    pages = bip.all()
    featureset = [page.extract_headers() for page in pages]
    featureset = reduce(lambda x,y: x.union(y), featureset)
    return list(featureset)

# Categories for headers
    # Job Description
    # Company Description
        #  Perks
    # Job Requirements
    # Job Preferences
    # Steps to Apply

print(get_featureset())
# print(header_features('asdasda. Ras al gul! Yippe:'))