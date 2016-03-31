import nltk
import numpy
from nltk.cluster import KMeansClusterer, GAAClusterer, euclidean_distance
import nltk.corpus
import nltk.stem
from nltk import decorators
import random
from built_in_page import BuiltInPage as bip

CACHED_HEADERS = 'headers.txt'

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

def print_features_to_file(file_name=CACHED_HEADERS):
    headers = reduce(lambda h1, h2: h1+"\n"+h2, get_featureset())
    open(file_name, 'w').write(headers.encode('UTF-8'))


@decorators.memoize
def normalize_word(word):
    stemmer = nltk.stem.snowball.SnowballStemmer("english").stem
    return stemmer(word.lower())

def get_words(input):
    words = set()
    for header in input:
        for word in header.split():
            words.add(normalize_word(word))
    return list(words)

@decorators.memoize
def vectorspaced(header):
    stopwords = set(nltk.corpus.stopwords.words('english'))
    header_components = [normalize_word(header) for word in header.split()]
    return numpy.array([
        word in header_components and not word in stopwords
        for word in words], numpy.short)

if __name__ == '__main__':

    file_name = 'example.txt'

    f = open(file_name, 'r')
    headers = [line.decode('UTF-8').strip() for line in f.readlines()]
    words = get_words(headers)

    cluster = GAAClusterer(5)
    print([vectorspaced(h) for h in headers if h])
    # cluster.cluster([vectorspaced(h) for h in headers if h])

    # classified = [cluster.classify(vectorspaced(h)) for h in headers]
    # print(classified)

    # for cluster_id, header in sorted(zip(classified, headers)):
    #     print cluster_id, header

# Categories for headers
    # Job Description
    # Company Description
        #  Perks
    # Job Requirements
    # Job Preferences
    # Steps to Apply
