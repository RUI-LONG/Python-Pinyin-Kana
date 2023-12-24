import unittest
from unittest.mock import patch
from pinyin_kana.pinyin_converter import to_katakana


class TestPronounceConverter(unittest.TestCase):
    def test_with_mocked_text(self):
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
        with patch(
            "pinyin_kana.pinyin_converter", return_value=expected_output
        ):
            result = to_katakana(input_text)
        self.assertEqual(result, expected_output)

    def test_with_mocked_list(self):
        input_text = ["測試", "中文轉日文發音"]
        expected_output = ["ツェシ", "ジョンウェンジュアンリウェンファイン"]
        with patch(
            "pinyin_kana.pinyin_converter", return_value=expected_output
        ):
            result = to_katakana(input_text)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
