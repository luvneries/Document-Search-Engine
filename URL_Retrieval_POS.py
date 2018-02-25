#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 22:00:56 2018

@author: pankaj
"""

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import re


df = pd.read_csv("urls.csv", header=0)

urlList = df.URLS.tolist()

def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'

    if tag.startswith('V'):
        return 'v'

    if tag.startswith('J'):
        return 'a'

    if tag.startswith('R'):
        return 'r'

    return None

def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None

def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    score, count = 0.0, 0.001

    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        # print [synset.path_similarity(ss) for ss in synsets2]
        try:
            best_score = max([synset.path_similarity(ss) for ss in synsets2])
        except:
            best_score = 0.0
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1

    # Average the values
    score /= count
    return score


def symmetric_sentence_similarity(sentence1, sentence2):
    """ compute the symmetric sentence similarity using Wordnet """
    #print (sentence1,sentence2)
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2


def sentence_similarity_query(userInput):
    userInput = " ".join(re.compile('\w+').findall(userInput.lower()))
    print(userInput)
    score_list=[]
    for url in urlList:
        print(url)
        url = " ".join(re.compile('\w+').findall(url.lower()))
        score_list.append(symmetric_sentence_similarity(sentence1,url))
        print(score_list)
    best_match = urlList[score_list.index(min(score_list))]
    return best_match


#sentence1="https://www.odyssey.com/dal/peoplesoft"
sentence2="I want a superdatascience features"
#sentence1 = pos_tag(word_tokenize(sentence1))
#" ".join(re.compile('\w+').findall(sentence1))

sentence_similarity_query(sentence2)      