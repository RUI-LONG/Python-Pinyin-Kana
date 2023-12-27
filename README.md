# Chinese Pronounce in Kana

## Overview

The `chinese-pronounce-in-kana` library is designed to convert Chinese text into Japanese Katakana characters based on their pronunciation. This can be particularly useful when you want to transcribe Chinese words into a Japanese phonetic script, making it easier for Japanese speakers to understand and pronounce Chinese words.

## Features

- Converts Chinese text to Pinyin using the `pypinyin` library.
- Replaces Chinese characters with their corresponding phonetic symbols.
- Converts the phonetic symbols into Japanese Katakana characters.

## Requirements

Before using this library, make sure you have the following prerequisites installed:

- Python
- `pypinyin` library (You can install it using `pip install pypinyin`)

## Usage

Here's a simple example of how to use the `PronounceConverter` class to convert Chinese text to Katakana:

```python
from pinyin_kana import PronounceConverter

converter = PronounceConverter()
result = converter.convert("你好")
print(" ".join(result))
```