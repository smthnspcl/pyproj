from setuptools import setup, find_packages

setup(
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    name="pyproj-smthnspcl",
    version="0.1",
    description="easily create new python projects",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    rl="https://github.com/smthnspcl/pyproj",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords="python project development",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyproj = pyproj.__main__:main'
        ]
    },
    install_requires=open("requirements.txt").readlines()
)
