from typing import Union, List
from .pinyin_dicts import PHONETIC_SYMBOLS, PINYIN_TO_KATAKANA
from pypinyin import pinyin


def replace_phonetic_symbols(pinyin_list: List[str]) -> List[str]:
    """Replace each Chinese character's Pinyin with its corresponding phonetic symbol."""
    return [
        "".join(PHONETIC_SYMBOLS.get(char, char) for char in word[0])
        for word in pinyin_list
    ]


def convert_to_katakana(text):
    pinyin_list = pinyin(text)
    phonetic_list = replace_phonetic_symbols(pinyin_list)
    return [PINYIN_TO_KATAKANA.get(p, "") for p in phonetic_list]


def to_katakana(text: Union[str, List[str]]) -> List[str]:
    """Convert Chinese text to Pinyin and then to Katakana."""
    if isinstance(text, list):
        return ["".join(convert_to_katakana(t)) for t in text]
    return convert_to_katakana(text)
