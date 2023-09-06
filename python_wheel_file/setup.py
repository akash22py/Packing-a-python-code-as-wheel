import setuptools

setuptools.setup(
    name= 'my_package',
    version= "0.0.1",
    author= "Akash Gupta",
    author_email= "akimcruz123@gmail.com",
    description= "Package to perform calculation",
    packages= setuptools.find_packages(),
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires= '>=3.7',
)