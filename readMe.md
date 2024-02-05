readMe.md

This is a simple script that converts short Chinese text to pinyin.  

It first tokenizes the Chinese text using Jieba, then output the corresponding pinyin of the Chinese tokens via pypinyin's `lazy_pinyin` method.

 input: chinese text  
 output: pinyin text

There are two possible outcomes for the input:  

One is sentence style, which means that only the first letter of the first word is capitlized. Another is headline style of which the first letters of all tokens are capitalized. The default is sentence style. You can use "--head" to output in headline style

    usage: 
        `python pinyinlize.py "你好，世界" [--headline]`

    

