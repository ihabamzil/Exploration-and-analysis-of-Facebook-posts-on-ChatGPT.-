# Creating the LDA model
ldamodel = LdaModel(corpus=doc_term_list, num_topics=6,id2word=dictionary, random_state=20)#passes : int, optional  Number of passes through the corpus during training.

# printing the topics
pprint(ldamodel.print_topics())
