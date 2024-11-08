## Badges

(Customize these badges with your own links, and check https://shields.io/ or https://badgen.net/ to see which other badges are available.)

| fair-software.eu recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/taimoorh13/life) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/taimoorh13/life)](https://github.com/taimoorh13/life) |
| (3/5) community registry           | [![RSD](https://img.shields.io/badge/rsd-life-00a3e3.svg)](https://github.com/taimoorh13/life/tree/main?tab=readme-ov-file) [![workflow pypi badge](https://img.shields.io/pypi/v/life.svg?colorB=blue)](https://pypi.python.org/project/life/) |
| (4/5) citation                     | **Taimoor Hanif, Life - Conway's game of life, Version 0.1.1, 2024, GitHub repository:**
| (5/5) checklist                    | [![workflow cii badge](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>/badge)](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>) |
| howfairis                          | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |To ensure high quality and consistency in the codebase, please follow these best practices.
| **GitHub Actions**                 | &nbsp; |
| Build                              | [![build](https://github.com/taimoorh13/life/actions/workflows/build.yml/badge.svg)](https://github.com/taimoorh13/life/actions/workflows/build.yml) |
## How to use life

A python implementation of Game of Life

The project setup is documented in [project_setup.md](project_setup.md). 

## Installation

To install life from GitHub repository, do:

```console
git clone git@github.com:taimoorh13/life.git
cd life
python -m pip install .
```

## Testing

- This has been tested on an input
- Navigate to *life.ipynb* to see the notebook with implementation of the module. *A copy is kept in same directory to avoid import issues*.
- *life.ipynb* also has information and comparisons of execution times and memory usage, by having **before** and **after** images. Input files used for testing is *./tests./data/1000x1000_0.1.txt* and also has correspong ouptut file as *1000x1000_output.txt*
- Notebook uses all the functions in the module, simply execute it reproduce the output.
- Output file is saved in the directory, to change it, put the path, right now it is as */docs/output.txt*, it can be changed by providing filepath of your choice
- An output is already there for the input file which is used.
- Repo also contains images of which are used in the notebook to make comparisons. These can be found in *./tests/Images/*

## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
