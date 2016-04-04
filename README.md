# job-searcher

Intended for educational purposes (mostly to play around with NLTK and learn some Python). This repo includes files that will parse the builtin job-board and cache relevant job posts. The final goal would be to extract information from each post, store that in a database and then one could access data on local market job posts.

Currently I've been working on extracting information from headers. I'm using NLTK's built-in classification methods to determine if a line of text is a header, then I store the following text in a dictionary with the header as the key and the text as the value. The header extractor works well enough, I also want to classify headers so I can store information by type.
