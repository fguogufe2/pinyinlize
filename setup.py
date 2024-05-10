from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "jieba", "pypinyin"
    ],
    entry_points={
        'console_scripts': [
            'pinyinlize=pinyinlize.pinpinlize:main'
        ]
    }
    auhtor='Fei Guo',
    author_email=fguogufe2@gmail.com
    description='A package for Chinese text processing'
    license='MIT'
    keywords='Chinese text processing'
)
