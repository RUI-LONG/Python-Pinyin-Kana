# 用日文發音轉中文

[EN README](./README.md)
## 概述

這個library是將中文文本根據其發音轉換為日語片假名字符。

<h3>Demo</h3>

> 1. 凱文要不要吃香蕉

https://github.com/RUI-LONG/Python-Pinyin-Kana/assets/25581309/a974f9e7-61d8-43d2-9a46-a74e57411669

> 2. 你應該要被加薪

https://github.com/RUI-LONG/Python-Pinyin-Kana/assets/25581309/4637d939-4e9f-4de5-8230-6112d0c7007b

> 3. 哩喜嘞工三小

https://github.com/RUI-LONG/Python-Pinyin-Kana/assets/25581309/01e95025-5237-40a4-b041-3313794e1f45

### 安裝

**前提條件**：pinyin-kana 需要 [Python 3.7 或更高版本](https://www.python.org/downloads/)

[PYPI](https://pypi.org/project/pinyin-kana/)
```
pip install pinyin-kana
```


## 用法

以下是一個使用 `PronounceConverter` 類將中文文本轉換為片假名的簡單範例：

```python
from pinyin_kana import to_katakana

result = to_katakana("你好")
print(" ".join(result))

print(
    f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=ja&q={'+'.join(result)}"
)
```




