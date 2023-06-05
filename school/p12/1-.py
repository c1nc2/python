#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:27:21 2023

@author: office
"""

from mytestlib import test
from L12_1 import search_linear
vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab 1 """
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

test(find_unknown_words (vocab, book_words) == ["from", "to"])
test(find_unknown_words ([], book_words) == book_words)
test(find_unknown_words (vocab, ["the", "boy", "fell"]) == [])