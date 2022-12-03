#  Determine if Two Strings Are Close
from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = self.get_dict_from_word(word1)
        d2 = self.get_dict_from_word(word2)
        keys_dicts = d1.keys() == d2.keys()
        values_dicts = sorted(d1.values()) == sorted(d2.values())
        return keys_dicts and values_dicts

    @staticmethod
    def get_dict_from_word(word: str) -> dict:
        word_dict = defaultdict(int)
        for char in word:
            word_dict[char] += 1
        return word_dict
