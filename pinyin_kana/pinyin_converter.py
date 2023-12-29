from typing import Union, List
from .pinyin_dicts import PHONETIC_SYMBOLS, PINYIN_TO_KATAKANA
from pypinyin import pinyin


def replace_phonetic_symbols(pinyin_list: List[str]) -> List[str]:
    """
    Replace each Chinese character's Pinyin with its corresponding phonetic symbol.

    Parameters:
    - pinyin_list (List[str]): A list of strings representing Pinyin transcriptions for Chinese characters.

    Returns:
    - List[str]: A list of strings where Pinyin transcriptions are replaced with phonetic symbols.
    """
    return [
        "".join(PHONETIC_SYMBOLS.get(char, char) for char in word[0])
        for word in pinyin_list
    ]


def convert_to_katakana(text, ignore_non_kana=False):
    """
    Convert a given text to Katakana using Pinyin-to-Katakana mapping.

    Parameters:
    - text (str): The input text to be converted to Katakana.
    - ignore_non_kana (bool): If True, non-kana characters will be ignored during conversion.
                              If False, non-kana characters will be retained as is in the output.

    Returns:
    - list of str: A list of Katakana representations of the input text.
    """
    pinyin_list = pinyin(text)
    phonetic_list = replace_phonetic_symbols(pinyin_list)
    if ignore_non_kana:
        return [PINYIN_TO_KATAKANA.get(p, "") for p in phonetic_list]
    return [PINYIN_TO_KATAKANA.get(p, p) for p in phonetic_list]


def to_katakana(text: Union[str, List[str]]) -> List[str]:
    """
    Convert Chinese text to Pinyin and then to Katakana.

    Parameters:
    - text (Union[str, List[str]]): Either a single string or a list of strings representing Chinese text.
                                   If a list is provided, each string in the list will be converted.

    Returns:
    - List[str]: A list of strings representing the converted text in Katakana.
    """
    if isinstance(text, list):
        return ["".join(convert_to_katakana(t)) for t in text]
    return convert_to_katakana(text)
