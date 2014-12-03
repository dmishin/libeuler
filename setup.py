from distutils.core import setup

with open('README.md') as readme:
    long_desc = readme.read()

setup(
    name='LibEuler',
    version='0.1',
    packages=['libeuler'],
    license='Free Domain',
    long_description=long_desc,
    url='https://github.com/dmishin/libeuler',
    author="Dmitry Shintyakov",
    author_email="shintyakov@gmail.com"
)

