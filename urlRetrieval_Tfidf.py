#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:37:42 2018

@author: pankaj
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#df = pd.read_csv("urls.csv", header=0)

#urlList = df.URLS.tolist()

def sentence_similarity(sentence1, sentence2):
    """ compute the cosine similarity using Tfidf Vectorizer """
    # Tokenize and tag
    finalText = [sentence1 , sentence2]

    vectorizer = TfidfVectorizer()
    doc_vector = vectorizer.fit_transform(finalText)

    df = pd.DataFrame(doc_vector.toarray().transpose(), index=vectorizer.get_feature_names(), columns = ['userInput', 'URL'])

    txt1 = df['userInput'].values.reshape(1, -1)
    txt2 = df['URL'].values.reshape(1, -1)

    return cosine_similarity(txt1, txt2)


#sentence1="https://www.odyssey.com/dal/peoplesoft"
#sentence2="star technical document"
#sentence1 = pos_tag(word_tokenize(sentence1))
#" ".join(re.compile('\w+').findall(sentence1))

#sentence_similarity_query(sentence2)
