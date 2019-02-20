import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfocus",
    version="0.1",
    author="Nicholas Mancuso, Ruth Johnson",
    author_email="nick.mancuso@gmail.com, ruthjohnson@ucla.com",
    description="Fine-map transcriptome-wide association studies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bogdanlab/focus",
    packages=["pyfocus"],
    package_data={'pyfocus': ['data/ld_blocks/*.bed']},
    install_requires=[
          "numpy",
          "scipy",
          "pandas>=0.23.0",
          "pandas-plink",
      ],
    scripts=[
        "bin/focus",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
)
