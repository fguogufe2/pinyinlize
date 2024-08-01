import jieba
from pypinyin import lazy_pinyin
import argparse
import logging

""" convert chinese text to pinyin
 input: chinese text
 output: pinyin text

    usage: python pinyinlize.py "你好，世界" 
    the default output is in sentence style, you can use "--head" to output in word style

"""

# preliminary test shows that it works well for chinese names, journal title, and publishers.

logging.getLogger("jieba").setLevel(logging.WARNING)

def process_text(text): 
    # remove \n, \r, \t
    text = text.replace("\n", "")
    text = text.replace("\r", "")
    text = text.replace("\t", "")
    text = text.strip()
    text = text.replace(" ", "")
    return text

def segment(text):
    # use jieba to segment chinese text
    word_list = jieba.cut(text, use_paddle=True, cut_all=False)
    return word_list

def pinyin_lize(word_list, sentStyle=True):
    # convert word list to pinyin list
    # sentStyle: output pinyin in sentence style, capitalize the first letter of the sentence
    # wordStyle: output pinyin in word style, capitalize the first letter of each word
    pinyin_list = []
    for word in word_list:
        pinyin_list.append("".join(lazy_pinyin(word, v_to_u=True, strict=False)))
    
    if sentStyle:
        pinyin_string = ' '.join(pinyin_list)
        final_result = pinyin_string.capitalize()
    else:
        pinyin_list = [pinyin.capitalize() for pinyin in pinyin_list]
        final_result = ' '.join(pinyin_list)
    
    return final_result


# this is for use in a python script
# run import pinyinlize.to_pinyin
def to_pinyin(text, head=True):
    post_text = process_text(text)
    word_list = segment(post_text)
    pinyin_text = pinyin_lize(word_list, sentStyle=head)
    print(pinyin_text)
    return pinyin_text


def main():

    parser = argparse.ArgumentParser(description='Convert Chinese text to pinyin')
    parser.add_argument('text', type=str, help='Chinese text')
    parser.add_argument('--head', action="store_false", help='output pinyin in word style')

    args = parser.parse_args()
    post_text = process_text(args.text)
    word_list = segment(post_text)
    pinyin_text = pinyin_lize(word_list, sentStyle=args.head)
    print(pinyin_text)

if __name__ == "__main__":
    main()

