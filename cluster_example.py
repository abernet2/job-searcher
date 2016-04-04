import sys

import numpy
from nltk.cluster import KMeansClusterer, GAAClusterer, euclidean_distance
import nltk.corpus
from nltk import decorators
from nltk.corpus import wordnet as wn
import nltk.stem
import re

stemmer_func = nltk.stem.snowball.EnglishStemmer().stem
stopwords = set(nltk.corpus.stopwords.words('english'))

stopwords.union(set(['phew', 'lovely']))
LANGUAGES = set(['python', 'html/javascript', 'nosql', 'net', 'mvc'])
KEYWORDS = set(['about', 'h-1b'])

@decorators.memoize
def normalize_word(word):
    stem = stemmer_func(word.lower())
    if stem in LANGUAGES:
        stem = 'languag'
    return stem

def get_words(titles):
    words = set()
    for title in job_titles:
        for word in title.split():
            words.add(normalize_word(word))
    return list(words)

@decorators.memoize
def vectorspaced(title):
    title_components = [normalize_word(word) for word in title.split()]
    return numpy.array([
        word in title_components and not word in stopwords
        for word in words], numpy.short)

def clean(line):
    line = line.decode('UTF-8').strip().lower()
    line = re.sub(r'\s+', r' ', line)
    return re.sub(r'[.,]+', r'', line)

def find_min_sim(word1, word2):
    ssets1 = [sset for sset in wn.synsets(word1)]
    ssets2 = [sset for sset in wn.synsets(word2)]
    maxi = 0
    for s1 in ssets1:
        for s2 in ssets2:
            sim = s1.path_similarity(s2)
            if sim is not None and sim > maxi:
                maxi = sim
    return maxi

if __name__ == '__main__':


    filename = 'headers.txt'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as title_file:

        job_titles = set()
        for line in title_file.readlines():
            job_titles.add(clean(line))

        words = get_words(list(job_titles))

        # cluster = KMeansClusterer(5, euclidean_distance)
        cluster = GAAClusterer(30)
        cluster.cluster([vectorspaced(title) for title in job_titles if title])

        # NOTE: This is inefficient, cluster.classify should really just be
        # called when you are classifying previously unseen examples!
        classified_examples = [
                cluster.classify(vectorspaced(title)) for title in job_titles
            ]

        for cluster_id, title in sorted(zip(classified_examples, job_titles)):
            print cluster_id, title.encode('UTF-8')
        print(words)

        print(find_min_sim('requirements', 'qualifications'))