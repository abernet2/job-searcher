import nltk

locs = [('Omnicom', 'IN', 'New York'),
        ('DDB Needham', 'IN', 'New York'),
        ('Kaplan Thaler Group', 'IN', 'New York'),
        ('BBDO South', 'IN', 'Atlanta'),
        ('Georgia-Pacific', 'IN', 'Atlanta')]
query = [e1 for (e1, re1, e2) in locs if e2 == 'Atlanta']

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

if __name__ == '__main__':
    document = open('../headers.txt').read().decode('UTF-8')
    test = ie_preprocess(document)
    print(test)