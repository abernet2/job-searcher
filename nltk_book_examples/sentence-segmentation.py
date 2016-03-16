import nltk

sents = nltk.corpus.treebank_raw.sents()
tokens = []
boundaries = set()
offset = 0
for sent in sents:
    tokens.extend(sent)
    offset += len(sent)
    boundaries.add(offset - 1)

def punct_features(tokens, i):
    return {'next-word-capitalized': tokens[i+1][0].isupper(),
            'prev-word': tokens[i-1].lower(),
            'punct': tokens[i],
            'prev-word-is-one-char': len(tokens[i-1]) == 1}

def segment_sentences(words):
    start = 0
    sents = []
    for i, word in enumerate(words):
        if word in '.!?' and classifier.classify(punct_features(words, i)) == True:
            print(words[start:i+1])
            sents.append(words[start:i+1])
            start = i + 1
    if start < len(words):
        sents.append(words[start:])
    return sents
  
featuresets = [(punct_features(tokens, i), (i in boundaries))
                for i in range(1, len(tokens) - 1)
                if tokens[i] in '.?!']


size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
result = nltk.classify.accuracy(classifier, test_set)
test = punct_features('Centerfold in crackwhore magazine. A', 33)
print(test)

segs = segment_sentences('Centerfold in crackwhore magazine.The quick brown fox! Asdias. ')
print(segs)
# print(featuresets)
