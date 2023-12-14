# la matrice terme-document
# Création du vectoriseur
vectorizer = CountVectorizer()
doc_term_matrix = vectorizer.fit_transform(data['posts'])

# Creating a list of documents
list_of_docs = data['posts'].tolist()
doc_split = [doc.split() for doc in list_of_docs]

# Creating the dictionary id2word from our cleaned word list doc_split
dictionary = corpora.Dictionary(doc_split) 
# Creating the corpus
doc_term_list = [dictionary.doc2bow(doc) for doc in doc_split]

# Creating the LSi model
lsimodel = LsiModel(corpus=doc_term_list, num_topics=6, id2word=dictionary)
pprint(lsimodel.print_topics())

