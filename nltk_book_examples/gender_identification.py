import nltk
from nltk.corpus import names
import random

class NameGenderIdentifier:
    def __init__(self):
        feature_sets = [(self.gender_features(n), gender) for (n, gender) in labeled_names()]
        train_set, self.test_set, self.devtest = feature_sets[1500:], feature_sets[:500], feature_sets[500:1500]
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def classify(self, name):
        return self.classifier.classify(self.gender_features(name))

    # returns a feature set dict
    def gender_features(self, word):
        features = {
            'suffix': word[-1],
            'first_letter': word[0],
            'double_suffic': word[-2:]
        }
        return features

    def find_errors(self):
        errors = []
        for(name, tag) in labeled_names()[500:1500]:
            guess = self.classify(name)
            if guess != tag: errors.append((tag, guess, name))
        return errors

# get labeled names
def labeled_names():
    labeled_names = [(name, 'male') for name in names.words('male.txt')]
    labeled_names += [(name, 'female') for name in names.words('female.txt')]
    random.shuffle(labeled_names)
    return labeled_names


c = NameGenderIdentifier()
print(c.classify('leon'))
print(nltk.classify.accuracy(c.classifier, c.devtest))