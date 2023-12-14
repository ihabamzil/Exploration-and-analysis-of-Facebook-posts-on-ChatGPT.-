# Creating the LDA model
ldamodel = LdaModel(corpus=doc_term_list, num_topics=6,id2word=dictionary, random_state=20)#passes : int, optional  Number of passes through the corpus during training.

# printing the topics
pprint(ldamodel.print_topics())

# Compute Coherence Score

#Topic Coherence measures score a single topic by measuring the degree of semantic similarity between high scoring words in the topic. These measurements help distinguish between topics that are semantically interpretable topics and topics that are artifacts of statistical inference.
coherence_model_lda = CoherenceModel(model=ldamodel, texts=doc_split, dictionary=dictionary, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)
#Coherence Score:  0.5604865194495483

# calculate topic coherence for each topic
coherence_model_lda = CoherenceModel(model=ldamodel, texts=doc_split, dictionary=dictionary, coherence='c_v', topn=10)
coherence_per_topic = coherence_model_lda.get_coherence_per_topic()

# print the coherence score for each topic
for topic_idx, coherence_score in enumerate(coherence_per_topic):
    print(f'Topic {topic_idx}: Coherence Score = {coherence_score:.3f}')

"""Topic 0: Coherence Score = 0.404
Topic 1: Coherence Score = 0.307
Topic 2: Coherence Score = 0.439
Topic 3: Coherence Score = 0.594
Topic 4: Coherence Score = 0.543
Topic 5: Coherence Score = 0.635"""
