# train the model
tfidf = models.TfidfModel(doc_term_list)
corpus_tfidf = tfidf[doc_term_list]

# Creating the LDA model
ldamodel = LdaModel(corpus=corpus_tfidf, num_topics=6,id2word=dictionary, random_state=20)

# printing the topics
pprint(ldamodel.print_topics())
