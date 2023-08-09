from setuptools import setup, find_packages

setup(
    name='eventful-delegate',
    version='0.1.0',
    description='A custom event system with async capabilities mimicking C# delegates.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Your Name',
    author_email='youremail@example.com',
    url='https://github.com/yourusername/eventful-delegate',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='events delegate asyncio',
    python_requires='>=3.7, <4',
)
