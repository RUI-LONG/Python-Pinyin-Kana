import unittest
from unittest.mock import patch
from pinyin_kana.utils import PronounceConverter


class TestPronounceConverter(unittest.TestCase):
    def test_convert_with_mocked_pinyin(self):
        input_text = "測試中文轉日文發音"
        expected_output = [
            "ツェ",
            "シ",
            "ジョン",
            "ウェン",
            "ジュアン",
            "リ",
            "ウェン",
            "ファ",
            "イン",
        ]
        with patch("pinyin_kana.utils", return_value=expected_output):
            result = PronounceConverter.convert(input_text)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
