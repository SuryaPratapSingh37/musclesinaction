import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()
    
setuptools.setup(
    name="musclesinaction",
    version="0.0.1",
    author="Muhammed Kocabas",
    description="Muscles in Action",
    packages=setuptools.find_packages(),
    install_reqs=required,
    python_requires='>=3.6',
)
