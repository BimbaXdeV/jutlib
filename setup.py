from setuptools import setup


__version = '0.1.0'

with open('README.md', encoding='utf-8') as file:
    __long_description = file.read()


if __name__ == '__main__':
    setup(
        name='jutlib',
        version='0.1.0',

        author='BimbaXdeV',
        author_email='kirillkirill497@gmail.com',

        description='A small Python parser for installing anime episodes on user device from service jut.su',
        long_description=__long_description,
        long_description_content_type='text/markdown',

        requires_python='>=3.9',
        license='MIT License',
        keywords=['jutsu', 'downloader', 'anime', 'jut'],
        classifierds=['Programming Language :: Python :: 3',
                      'Programming Language :: Python :: 3.9',
                      'Programming Language :: Python :: 3.10',
                      'Intended Audience :: Developers',
                      'Natural Language :: English',
                      'Operating System :: OS Independent'],

        url='https://github.com/BimbaXdeV/jutlib/',
        download_url='https://github.com/BimbaXdeV/jutlib/archive/refs/heads/master.zip',

        packages=['jutsu'],
        install_requires=['beautifulsoup4', 'bs4', 'certifi', 'charset-normalizer', 'colorama', 'idna',
            'lxml', 'requests', 'soupsieve', 'tqdm', 'urllib3']
    )

# install_requires = [
#     'beautifulsoup4==4.12.3',
#     'bs4==0.0.2',
#     'certifi==2024.8.30',
#     'charset-normalizer==3.4.0',
#     'colorama==0.4.6',
#     'idna==3.10',
#     'lxml==5.3.0',
#     'requests==2.32.3',
#     'soupsieve==2.6',
#     'tqdm==4.66.5',
#     'urllib3==2.2.3'
# ]

