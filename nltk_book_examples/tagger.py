import nltk

text = word_tokenize("And now for something completely different")
nltk.pos_tag(text)

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print(text.similar('woman'))