def bow_tf(df_column,vocabulary_=None):
    #Check Vocabualary
    if vocabulary_ == None:
        vocabulary_ = {v: k for k, v in enumerate(set(chain.from_iterable(df_column)))}
    else:
        vocabulary_ = vocabulary_
    # Term-Frequency
    bow =dict()
    values, row_indices, col_indices = [], [], []
    for n,sentence in enumerate(df_column):
        bag_vector = np.zeros(len(vocabulary_))
        for token in sentence:
            word_index = vocabulary_.get(token)
            bag_vector[word_index] += 1
        bow[n] = bag_vector
        for c, v in bow.items():
            values.append(v)
            row_indices.append(n)
            col_indices.append(c)
    return pd.DataFrame.from_dict(bow ,columns=vocabulary_, orient='index')


