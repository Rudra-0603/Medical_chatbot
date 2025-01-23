from setuptools import find_packages, setup

setup(
    name='generative_ai_project',  # Use underscores or dashes, no spaces
    version='0.0.0',
    author='Rudranil Ghosh',
    author_email='rboh.007@gmail.com',
    packages=find_packages(),
    install_requires=[
        "sentence-transformers==2.2.2",
        "langchain",
        "flask",
        "pypdf",
        "python-dotenv",
        "pinecone[grpc]",
        "langchain-pinecone",
        "langchain_community",
        "langchain_openai",
        "langchain_experimental",
    ],
)
