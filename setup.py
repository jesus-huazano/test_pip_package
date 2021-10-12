from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Creacion y suscripcion a SNS'
LONG_DESCRIPTION = ''

# Setting up
setup(
    name="rankmisns",
    version=VERSION,
    author="Jesus Huazano (jesus.huazano)",
    author_email="<jesus.huazano@rankmi.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['SNS'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Rankmi Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)