import pytest
from pinyinlize import process_text, segment, pinyin_lize, to_pinyin, main


def test_main():
    result = to_pinyin("清代基層地方官人事嬗遞現象之量化分析", head=True)
    expected = "Qingdai jiceng difangguan renshi shandi xianxiang zhi lianghua fenxi"
    assert result == expected