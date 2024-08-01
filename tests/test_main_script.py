import pytest
from pinyinlize.main_script import to_pinyin

def test_to_pinyin():
    result = to_pinyin("清代基層地方官人事嬗遞現象之量化分析", head=True)
    expected = "Qingdai jiceng difangguan renshi shandi xianxiang zhi lianghua fenxi"
    assert result == expected