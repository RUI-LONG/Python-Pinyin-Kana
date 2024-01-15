# Chinese Pronounce in Kana

## Overview

This library is designed to convert Chinese text into Japanese Katakana characters based on their pronunciation.

<h3>Demo</h3>

> 1. 凱文要不要吃香蕉

https://github.com/RUI-LONG/Python-Pinyin-Kana/assets/25581309/a974f9e7-61d8-43d2-9a46-a74e57411669

> 2. 你應該要被加薪

https://github.com/RUI-LONG/Python-Pinyin-Kana/assets/25581309/4637d939-4e9f-4de5-8230-6112d0c7007b

> 3. 哩喜嘞工三小

https://github.com/RUI-LONG/Python-Pinyin-Kana/assets/25581309/01e95025-5237-40a4-b041-3313794e1f45


### Installation

**Prerequisite**: pinyin-kana requires [Python 3.7 or higher](https://www.python.org/downloads/)

[PYPI](https://pypi.org/project/pinyin-kana/)

```
pip install pinyin-kana
```

## Usage

Here's a simple example of how to use the `PronounceConverter` class to convert Chinese text to Katakana:

```python
from pinyin_kana import to_katakana

result = to_katakana("你好")
print(" ".join(result))

print(
    f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=ja&q={'+'.join(result)}"
)
```
