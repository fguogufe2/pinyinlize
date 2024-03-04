readMe.md

This is a simple and short script that converts short Chinese text(book, article or journal titles) to pinyin. It is written for the purpose of facilitating the generation of Chinese citations and bibiliograph in English academic settings. 

It first tokenizes the Chinese text using Jieba, then output the corresponding pinyin of the Chinese tokens via pypinyin's `lazy_pinyin` method.

 input: chinese text  
 output: pinyin strings

There are two possible outputs:  

One is the sentence style, which means only the first letter of the first word is capitalized. Another is the headline style, in which the first letters of all tokens are capitalized. The default is the sentence style. You can use `--head` to output in the headline style

    usage: 
        
        python pinyinlize.py <Chinese_text> [--headline]

    eg: 

    command: python pinyinlize.py "清代基層地方官人事嬗遞現象之量化分析"  

    output: "Qingdai jiceng difangguan renshi shandi xianxiang zhi lianghua fenxi"

    

