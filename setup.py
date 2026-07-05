from setuptools import setup, find_packages

setup(
    name="mcqgenrater",
    version="0.0.1",
    author="darapaneni naveen",
    author_email="naveendarapaneni@gmail.com",
    install_requires=[
        "openai",  
        "langchain",
        "streamlit",
        "python-dotenv",
        "pypdf2"
    ],
    packages=find_packages()
)