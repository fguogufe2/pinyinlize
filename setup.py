from setuptools import setup, find_packages

setup(
    name='pinyinlize',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "jieba", 
        "pypinyin"
    ],
    entry_points={
        'console_scripts': [
            'pinyinlize=pinyinlize.pinyinlize:main'
        ]
    },
    auhtor='Fei Guo',
    author_email= "fguogufe2@gmail.com",
    description='a package converts short Chinese-character strings(titles of books, articles or journals) to pinyin.',
    license='MIT',
    keywords='convert chinese text to pinyin'
)
