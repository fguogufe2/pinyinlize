from setuptools import setup, find_packages

setup(
    name='pinyinlize',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "jieba >= 0.42.1", 
        "pypinyin >= 0.50.0"
    ],
    entry_points={
        'console_scripts': [
            'pinyinlize=pinyinlize.pinpinlize:main'
        ]
    },
    auhtor='Fei Guo',
    author_email= "fguogufe2@gmail.com",
    description='a package converts short Chinese-character strings(titles of books, articles or journals) to pinyin.',
    license='MIT',
    keywords='convert chinese text to pinyin'
)
