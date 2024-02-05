readMe.md

This is simply script that converts short Chinese text to pinyin.  

It first tokenize the Chinese text using Jieba, then output the corresponding pinyin of the Chinese tokens via pypinyin's `lazy_pinyin` methods.

 input: chinese text
 output: pinyin text

There are two ways for the the output:

One is sentence style, which means that only the first letter of the first word is capitlized. Another is headline style of which the first letters of all tokens are capitalized. 

    usage: 
        `python pinyinlize.py "你好，世界"`

    the default output is in sentence style, you can use "--head" to output in word style

