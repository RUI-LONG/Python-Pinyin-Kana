from pypinyin import pinyin
from typing import Text, List
from functools import wraps

from .pinyin_dicts import phonetic_symbol, pinyin_to_katakana


class PronounceConverter:
    @staticmethod
    def _replace_phonetic_symbols(pinyin_list: List) -> List:
        """Replace each Chinese character with its corresponding phonetic symbol."""
        return [
            "".join(phonetic_symbol.get(char, char) for char in word[0])
            for word in pinyin_list
        ]

    @classmethod
    def convert(cls, text: Text) -> List:
        """Convert Chinese text to Pinyin and then to Katakana."""
        pinyin_list = pinyin(text)
        phonetic_list = cls._replace_phonetic_symbols(pinyin_list)
        return [pinyin_to_katakana.get(l, "") for l in phonetic_list]
