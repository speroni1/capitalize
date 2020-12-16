from setuptools import setup

setup(
    name='capitalize',
    packages = ['capitalize', 'capitalize.test'],
    scripts = ['bin/cap_script.py'],
    package_data ={'capitalize':['data/cap_data.txt',
                                'data/sample_text_file.txt',
                                'data/sample_text_file_cap.txt'
                                ]},

    version = '0.1.0',
    author = 'James Roefs',
    url = 'none',
    license = 'LICENSE.txt',
    description = 'It capitalizes text files.',
    
)