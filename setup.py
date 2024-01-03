from setuptools import setup

setup(
    name='graphing',
    version='0.1',
    description='linux command line tool for graphing',
    url='http://github.com/NishanthMankali/graphing',
    author='Nishanth & Team',
    author_email='mankalinishanth.com',
    license=NONE,
    packages=['graphing'],
    scripts=['bin/script.py'],
    install_requires=[
        'matplotlib',
        'numpy',
        'sympy',
        'tkinter',
    ],
    zip_safe=False
)
