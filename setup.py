import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='Yogesh Baghel',
    author_email='yogeshbaghel8130@gmail.com',
    url='',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)