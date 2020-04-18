collection_of_words = {}
text = input("Text: ")

sentence = text.split()
for a in sentence:
    frequency = collection_of_words.get(a, 0)
    collection_of_words[a] = frequency + 1

sentence = list(collection_of_words.keys())
sentence.sort()

max_length = max((len(a) for a in sentence))
for a in sentence:
    print("{:{}} : {}".format(a, max_length, collection_of_words[a]))
