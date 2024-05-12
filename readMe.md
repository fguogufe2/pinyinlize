readMe.md

**1 Description**: 
This is a simple and short command-line tool that converts short Chinese-character strings(titles of books, articles or journals) to pinyin. It's purpose is to facilitate generating Chinese citations or bibiliograph in the English setting. 

**2 Internal Steps** 

It first tokenizes the Chinese strings using **Jieba**, and then output the corresponding pinyin via `pypinyin`'s `lazy_pinyin`.

 - input: Chinese characters (it accepts both traditional and simplified Chinese)
 - output: pinyin strings

There are two possible outputs:  

- 1. the sentence style, which means only the first letter of the first word is capitalized. 
- 2. the headline style, in which the first letters of all tokens are capitalized. The default is the sentence style. You can use `--head` to output in the headline style


**3 usage:** 
        
    pinyinlize <Chinese_text> [--head]

    eg: 

    pinyinlize "清代基層地方官人事嬗遞現象之量化分析"  

    output: "Qingdai jiceng difangguan renshi shandi xianxiang zhi lianghua fenxi"

    
**4 Installation** 

`pip install pinyinlize`

**5 future plans**
To include a API call to Crossref and an option to output DOI or bibtex for the article or book input.
