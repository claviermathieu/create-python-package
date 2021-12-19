import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="dprm",
    version="0.0.1",
    author="Deloitte",
    author_email="mathieu.clavier@outlook.com",
    description="Package to modelize physical climate risk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Deloitte License",
        "Operating System :: OS Independent",
    ],  
    python_requires='>=3.7',
)