def dict_vocabulary(path="Data/words1.txt"):
    """
    :param path: document txt with the vocabulary
    :return: a dictionary, keys = length of the word, value : list of words
    """
    print("Vocabulary...")
    dict_words = {}
    with open(path, "r") as fichier_lu:
        list_words = fichier_lu.read().splitlines()
    for word in list_words:
        key = str(word.__len__())
        if key not in dict_words:
            dict_words[key] = [word.lower()]
        else:
            dict_words[key].append(word.lower())

    for key, value in dict_words.items():
        dict_words[key] = set(dict_words[key])

    return dict_words