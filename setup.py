from setuptools import setup, find_packages

setup(
    name='emoji_visualizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'emoji',
    ],
    description='A Python library to visualize all emojis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aditya26062003/emoji_visualizer',
    author='Aditya Singh',
    author_email='adityarathore2606@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
