def remove_stopword_2(test_list,stopword_list):
    test_list = [word for word in test_list if word not in stopword_list]
    print(test_list)
