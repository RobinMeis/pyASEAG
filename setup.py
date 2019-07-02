import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pyASEAG',
     version='0.1',
     author="Robin Meis",
     author_email="blog@smartnoob.de",
     description="A Python3 Library and interactive Shell to access FormelASEAGs race data",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
     entry_points={
        'console_scripts': [
            'ASEAG = pyASEAG.__main__:main'
        ]
    },
 )
